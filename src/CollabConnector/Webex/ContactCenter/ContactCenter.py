import sys
import requests
import json
import time
import urllib

requests.packages.urllib3.disable_warnings()


class Connect:
    class Token:
        import time
        import threading

        access_token = None
        refresh_token = None
        refresh_interval = 0
        client_id = None
        client_secret = None

        def __init__(self,
                     access_token: str = None,
                     refresh_token: str = None,
                     client_id: str = None,
                     client_secret: str = None,
                     auth_file: str = None
                     ):
            if auth_file:
                with open("webex_key.json") as auth_file:
                    webex_key = json.loads(auth_file.read())
                    client_id = webex_key['client_id'] if "client_id" in webex_key.keys() and webex_key['client_id'] else None
                    client_secret = webex_key['client_secret'] if "client_secret" in webex_key.keys() and webex_key['client_secret'] else None
                    access_token = webex_key['access_token']
                    refresh_token = webex_key['refresh_token'] if "refresh_token" in webex_key.keys() and webex_key['refresh_token'] else None
            self.access_token = access_token
            if refresh_token and client_id and client_secret:
                import threading
                import time

                self.refresh_token = refresh_token
                self.client_id = client_id
                self.client_secret = client_secret

                thread = threading.Thread(target=self.token_refresh, args=())
                thread.daemon = True
                thread.start()

        def info(self) -> dict:
            return {
                "access_token": self.access_token,
                "refresh_token": self.refresh_token,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "expires_in": self.refresh_interval
            }

        # refresh token
        def token_refresh(self) -> None:
            while True:
                time.sleep(1)
                self.refresh_interval -= 1
                if self.refresh_interval <= 0:
                    refresh_data = {
                        "grant_type": "refresh_token",
                        "client_id": self.client_id,
                        "client_secret": self.client_secret,
                        "refresh_token": self.refresh_token
                    }
                    try:
                        new_token = self.get_token(refresh_data)
                    except Exception as err:
                        raise Exception(f"Not able to perform Webex Token Refresh: {err}")
                    else:
                        self.access_token = new_token['access_token']
                        self.refresh_token = new_token['refresh_token']
                        self.refresh_interval = int(new_token['expires_in']) - 1000

        # basic REST POST
        def get_token(self, data: dict) -> dict:
            headers = {"Accept": "application/json",
                       "Content-Type": "application/json",
                       "Authorization": f"Bearer {self.access_token}"}

            while True:  # loop for throttling
                try:
                    response = requests.post("https://webexapis.com/v1/access_token",
                                             headers=headers,
                                             data=json.dumps(data),
                                             verify=False)

                except Exception as err:
                    raise Exception(f"Error sending Webex REST Token Refresh - {err}")

                else:
                    if response.status_code == 426:  # handle throttling
                        time.sleep(int(response.headers['Retry-After']) + 1)
                    elif response.status_code == 200 and response.json():
                        return json.loads(response.text)
                    else:
                        raise Exception(f"Not able to perform Webex Token Refresh: REST response not valid.")

    token = None
    org_id = None
    debug = False

    # store token then fetch users orgId and save
    def __init__(self,
                 access_token: str = None,
                 org_id: str = None,
                 refresh_token: str = None,
                 client_id: str = None,
                 client_secret: str = None,
                 auth_file: str = None,
                 debug: bool = False
                 ):
        self.debug = debug
        if access_token is None and auth_file is None:
            raise Exception("Must pass API token for Admin API")
        else:
            self.token = self.Token(access_token, refresh_token, client_id, client_secret, auth_file)

            try:
                self.org_id = self.get("/v1/subscriptions")['meta']['orgId']

            except Exception as err:
                Exception ("Error retrieving Org ID from token. If token valid?")

            if org_id:
                self.org_id = org_id

    # get next page for large requests
    @staticmethod
    def find_next_page(call_response):
        return True

    #  set headers
    def headers(self, payload: bool = False, debug: bool = False):
        if payload:
            return {
                "Accept": "application/json",
                "Content-Type":  "application/json",
                "Authorization": f"Bearer {self.token.access_token}"
            }
        else:
            return {
                "Accept": "application/json",
                "Authorization": f"Bearer {self.token.access_token}"
            }

    # basic REST GET
    def get(self, uri, data={}, page_size=50, page=0, debug: bool = False):
        if uri.find("organization//") > -1:  # add org ID for ease of use
            uri = uri.replace("//", f"/{self.org_id}/")
        elif uri.find("/v1/") > -1 and self.org_id is not None:
            data['orgId'] = self.org_id

        if uri.find("{orgid}") > -1: # remove {orgid} syntax from documentation to make it easy
            uri = uri.replace("/{orgid}/", f"/{self.org_id}/")

        if len(data) > 0:
            data = f"&{urllib.parse.urlencode(data)}"
        else:
            data = ""

        return_data = {'data': [], 'meta': {}}
        api_url = f"https://api.wxcc-us1.cisco.com/{uri.strip('/')}?pageSize={page_size}&page={page}{data}"
        while True:  # loop for throttling
            try:
                response = requests.get(f"https://api.wxcc-us1.cisco.com/{uri.strip('/')}?pageSize={page_size}&page={page}{data}",
                                        headers=self.headers(),
                                        verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex CC REST GET - {uri} {err}")

            else:
                if self.debug or debug:
                    print("GET", uri, response.status_code, response.headers)
                if response.status_code == 200 and response.json():
                    try:
                        response_data = json.loads(response.text)
                    except Exception as err:
                        raise Exception(f"Return Data not in correct format - {response.text}")

                    else:
                        if isinstance(return_data, str):
                            raise Exception(f"Return Data not in correct format - {response.text}")

                        if isinstance(response_data, list):  # reformat v2 API to match v1 cor consistent return
                            response_data = {'data': response_data,
                                             'meta': {'orgId': self.org_id,
                                                      'urlexpiration': None,
                                                      'library_added': True}
                                             }
                        else:
                            return_data['meta']['library_added'] = False

                        if isinstance(response_data, dict):
                            if 'meta' not in response_data.keys():
                                return { "data": [response_data],
                                               'meta': {
                                                           'orgId': self.org_id,
                                                            'urlexpiration': None,
                                                            'library_added': True
                                                       }
                                         }
                            if  "links" not in response_data['meta'].keys() or response_data['meta']['page'] == response_data['meta']['totalPages']:
                                return_data = {'data': return_data['data'] if return_data else response_data['data'],
                                               'meta': {
                                                           'orgId': response_data['meta']['orgId'] if "orgId" in response_data['meta'].keys() else self.org_id,
                                                            'urlexpiration': None,
                                                            'library_added': True
                                                       }
                                               }
                                return return_data
                            else:
                                page += 1
                                return_data['data'].extend( response_data['data'] if 'data' in response_data.keys() else response_data )

                elif response.status_code >= 200 and response.status_code < 300:
                    if response.headers.get('content-type') == 'application/json' and response.json():
                        return response.json()
                    else:
                        return True
                elif response.status_code == 429 or response.status_code == 429:  # handle throttling Wait and don't return to continue loop
                    print(f"{uri}{data} - API Request throttled: {response.headers['Retry-After']}", file=sys.stderr)
                    time.sleep(int(response.headers['Retry-After']) + 1)

                elif response.status_code == 401:
                    raise Exception("Webex Admin token invalid.  Generate new token.")

                else:
                    raise Exception(f"Error sending CC GET to Webex - {uri}{data} {response}{response.text}")

    def delete(self, uri, debug: bool = False) -> dict:
        if uri.find("organization//") > -1:  # add org ID for ease of use
            uri = uri.replace("//", f"/{self.org_id}/")

        while True:  # loop for throttling
            try:
                response = requests.delete(f"https://api.wxcc-us1.cisco.com/{uri.strip('/')}",
                                           headers=self.headers(),
                                           verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex CC REST DELETE - {uri} {err}")

            else:
                if self.debug or debug:
                    print("DELETE", uri, response.status_code, response.headers)
                if response.status_code == 429:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    if response.headers.get('content-type') == 'application/json' and response.json():
                        return response.json()
                    else:
                        return {"success": True}
                else:
                    raise Exception(f"Error sending CC DELETE to Webex - {uri} {response}{response.text}")

    def post(self, uri, data, debug: bool = False) -> dict:
        if uri.find("organization//") > -1:  # add org ID for ease of use
            uri = uri.replace("//", f"/{self.org_id}/")

        while True:  # loop for throttling
            try:
                response = requests.post(f"https://api.wxcc-us1.cisco.com/{uri.strip('/')}",
                                         headers=self.headers(payload =True),
                                         data=json.dumps(data),
                                         verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex CC REST POST - {uri} {err}")

            else:
                if self.debug or debug:
                    print("POST", uri, response.status_code, response.headers)
                if response.status_code == 429:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    if response.headers.get('content-type') == 'application/json' and response.json():
                        return response.json()
                    else:
                        return {"success": True}
                else:
                    raise Exception(f"Error sending POST to Webex - {uri} {response}{response.text}")

    def put(self, uri, data, debug: bool = False) -> dict:
        if uri.find("organization//") > -1:  # add org ID for ease of use
            uri = uri.replace("//", f"/{self.org_id}/")

        while True:  # loop for throttling
            try:
                response = requests.put(f"https://api.wxcc-us1.cisco.com/{uri.strip('/')}",
                                        headers=self.headers(payload =True),
                                        data=json.dumps(data),
                                        verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex CC REST PUT - {uri} {err}")

            else:
                if self.debug or debug:
                    print("PUT", uri, response.status_code, response.headers)
                if response.status_code == 429:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    if response.headers.get('content-type') == 'application/json' and response.json():
                        return response.json()
                    else:
                        return {"success": True}
                else:
                    raise Exception(f"Error sending PUT to Webex - {uri} {response}{response.text}")

    def patch(self, uri, data, debug: bool = False) -> dict:
        if uri.find("organization//") > -1:  # add org ID for ease of use
            uri = uri.replace("//", f"/{self.org_id}/")

        while True:  # loop for throttling
            try:
                response = requests.patch(f"https://api.wxcc-us1.cisco.com/{uri.strip('/')}",
                                          headers=self.headers(payload =True),
                                          data=json.dumps(data),
                                          verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex CC REST PATCH - {uri} {err}")

            else:
                if self.debug or debug:
                    print("PATCH", uri, response.status_code, response.headers)
                if response.status_code == 429:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    if response.headers.get('content-type') == 'application/json' and response.json():
                        return response.json()
                    else:
                        return {"success": True}
                else:
                    raise Exception(f"Error sending PATCH to Webex - {uri} {response}{response.text}")

    def search(self, graphql_query: str, debug: bool = False, ms_offset: int = 86400000) -> dict:
        #  if to/from is not defined in query, ie: samplerequests, yjrm replace with 1 day from now
        current_time = int(time.time() * 1000)
        graphql_query = graphql_query.replace("{from}", str(current_time - ms_offset)).replace("{to}", str(current_time))
        while True:  # loop for throttling
            try:
                response = requests.post(f"https://api.wxcc-us1.cisco.com/search",
                                         headers=self.headers(payload =True),
                                         data=json.dumps({"query": graphql_query}),
                                         verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex CC Search API REST POST: {err}")

            else:
                if self.debug or debug:
                    print("POST", uri, response.status_code, response.headers)
                if response.status_code == 429:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return {}
                else:
                    raise Exception(f"Error sending Search API POST to Webex: {response}{response.text}")
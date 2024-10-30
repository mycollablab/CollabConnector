import sys
from collections import OrderedDict
import requests
import requests.packages.urllib3
import json
import time
import urllib.parse
import base64
import codecs
from typing import Self

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
    org = None
    tenant_id = None
    active_org = None
    profile = None
    id = None
    service_url = "https://webexapis.com"
    type = "wbx"
    guest_info = {}
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
        self.debug = False
        if access_token is None and auth_file is None:
            raise Exception("Must pass API token for Admin API")
        else:
            self.token = self.Token(access_token, refresh_token, client_id, client_secret, auth_file)

            try:
                self.profile = self.get("/v1/people/me?callingData=true")
                self.id = self.profile['id']
                self.org = self.profile['orgId']
                self.active_org = self.org

            except Exception as err:
                if client_id is None:
                    raise Exception(f"Error with Token or getting Org")
                else:
                    print("User profile not found. Assuming Service App!", file=sys.stderr)

            if org_id:
                self.org = org_id
            if self.org:
                self.tenant_id = codecs.decode(base64.b64decode(f"{self.org}==============")).split("/")[-1]

    #  set headers
    def headers(self, send: bool = False):
        if send:
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

    # parses out paging from response headers
    @staticmethod
    def find_next_page(call_response):
        if 'Link' in call_response.headers:
            return call_response.headers['Link'].split(";")[0].strip("<>")
        else:
            return False

    # create guest user
    def guest(self, subject: str, display_name: str = "") -> Self:
        guest_info = {
            "displayName": display_name,
            "subject": subject
        }
        guest_auth = self.post("/v1/guests/token", guest_info)
        guest_account = Connect(guest_auth['accessToken'])
        guest_account.guest_info = guest_info

        return guest_account

    # basic REST GET
    def get(self, uri, data=None, limit=50000, debug=False) -> dict:
        # URL encode parameters for appending to URI if provided
        if data:
            data = f"?{urllib.parse.urlencode(data)}"
        else:
            data = ""

        uri = f"{self.service_url}/{uri.strip('/')}{data}"
        return_values = {'items': []}
        # Loop while true to handled paged results and throttling
        while True:
            try:
                # send request to Webex
                response = requests.get(uri, headers=self.headers(), verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST GET - {uri} {err}")

            else:
                if self.debug or debug:
                    print("GET", uri, response.status_code, response.headers)
                if 200 <= response.status_code <= 300 and response.json():
                    # create or add to return dict
                    response_data = response.json()
                    if isinstance(response_data, dict) and len(response_data) == 1:
                        key = list(response_data.keys())[0]
                        response_data['items'] = response_data[key]
                    if not isinstance(response_data, dict) or not isinstance(response_data, list):
                        return response_data
                    if 'items' in response_data:
                        return_values['items'].extend(response_data['items'])
                    else:
                        return response_data

                    # check for additional and loop until max (limit minimum is 50)
                    if len(return_values['items']) >= limit or self.find_next_page(response) is False:
                        key_list = []
                        for item in return_values['items']:
                            for key in item:
                                if key not in key_list:
                                    key_list.append(key)
                        full_return = []
                        for item in return_values['items']:
                            full_return.append(OrderedDict())
                            for key in key_list:
                                if key not in item.keys():
                                    full_return[-1][key] = None
                                else:
                                    full_return[-1][key] = item[key]
                        return full_return
                    else:
                        uri = self.find_next_page(response)
                elif 200 <= response.status_code < 300:
                    return True
                elif response.status_code == 429:  # handle throttling
                    print(f"Request to {uri} throttled.  Doing it again in a bit.", file=sys.stderr)
                    time.sleep(int(response.headers['Retry-After']) + 1)

                elif response.status_code == 401:  # handle auth issues
                    raise Exception("Webex Admin token invalid.  Generate new token")
                else:  # catch generic failures
                    print(f"Error sending GET to Webex - {uri}{data} {response}{response.text}", file=sys.stderr)
                    raise Exception(f"Error sending GET to Webex - {uri}{data} {response}{response.text}")

    # basic REST HEAD
    def head(self, uri: str, full: bool = False, debug: bool = False) -> dict:
        uri = uri.replace(self.service_url, "")
        uri = f"{self.service_url}/{uri.strip('/')}"
        # Loop while true to handled paged results and throttling
        while True:
            try:
                # send request to Webex
                response = requests.head(uri, headers=self.headers(), verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST GET - {uri} {err}")

            else:
                if self.debug or debug:
                    print("GET", uri, response.status_code, response.headers)
                if 200 <= response.status_code < 300:
                    return dict(response.headers)

                elif response.status_code == 429:  # handle throttling
                    print(f"Request to {uri} throttled.  Doing it again in a bit.", file=sys.stderr)
                    time.sleep(int(response.headers['Retry-After']) + 1)

                elif response.status_code == 401:  # handle auth issues
                    raise Exception("Webex Admin token invalid.  Generate new token")
                else:  # catch generic failures
                    print(f"Error sending HEAD to Webex - {uri} {response}", file=sys.stderr)
                    raise Exception(f"Error sending HEAD to Webex - {uri} {response}")

    # basic REST GET for bytes content
    def get_content(self, uri: str, debug: bool = False) -> bytes:
        uri = f"{self.service_url}/{uri.strip('/')}"
        # Loop while true to handled paged results and throttling
        while True:
            try:
                # send request to Webex
                response = requests.get(uri, headers=self.headers(), verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST GET - {uri} {err}")

            else:
                if self.debug or debug:
                    print("GET", uri, response.status_code, response.headers)
                if 200 <= response.status_code <= 300 and response.json():
                    # test for non-json responces ie: images
                    if response.headers['Content-type'].split("/")[0] not in ["video", "audio", "image"]:
                        return response.content
                    else:
                        raise Exception(f"Non-bytes response for {uri} Try regular get.")

                elif response.status_code == 429:  # handle throttling
                    print(f"Request to {uri} throttled.  Doing it again in a bit.", file=sys.stderr)
                    time.sleep(int(response.headers['Retry-After']) + 1)

                elif response.status_code == 401:  # handle auth issues
                    raise Exception("Webex Admin token invalid.  Generate new token")
                else:  # catch generic failures
                    print(f"Error sending GET to Webex - {uri} {response}", file=sys.stderr)
                    raise Exception(f"Error sending GET to Webex - {uri} {response}")

    # basic REST DELETE
    def delete(self, uri, debug=False):
        while True:  # loop for throttling
            try:
                response = requests.delete(f"{self.service_url}/{uri.strip('/')}", headers=self.headers(), verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST DELETE - {uri} {err}")

            else:
                if self.debug or debug:
                    print("DELETE", uri, response.status_code, response.headers)
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return True
                else:
                    raise Exception(f"Error sending DELETE to Webex - {uri} {response}{response.text}")

    # basic REST POST
    def post(self, uri, data, debug=False):
        while True:  # loop for throttling
            try:
                response = requests.post(f"{self.service_url}/{uri.strip('/')}",
                                         headers=self.headers(True),
                                         data=json.dumps(data),
                                         verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST POST - {uri} {err}")

            else:
                if self.debug or debug:
                    print("POST", uri, response.status_code, response.headers)
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return True
                else:
                    raise Exception(f"Error sending POST to Webex - {uri} {response}{response.text}")

    # basic REST PUT
    def put(self, uri, data, debug=False):
        while True:  # loop for throttling\
            try:
                response = requests.put(f"{self.service_url}/{uri.strip('/')}",
                                        headers=self.headers(True),
                                        data=json.dumps(data),
                                        verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST PUT - {uri} {err}")

            else:
                if self.debug or debug:
                    print("PUT", uri, response.status_code, response.headers)
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return True
                else:
                    raise Exception(f"Error sending PUT to Webex - {uri} {response}{response.text}")

    # basic REST patch
    def patch(self, uri, data, debug=False):
        while True:  # loop for throttling
            try:
                response = requests.patch(f"{self.service_url}/{uri.strip('/')}",
                                          headers=self.headers(True),
                                          data=json.dumps(data),
                                          verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST PATCH - {uri} {err}")

            else:
                if self.debug or debug:
                    print("PATCH", uri, response.status_code, response.headers)
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return True
                else:
                    raise Exception(f"Error sending PATCH to Webex - {uri} {response}{response.text}")

import requests
import json
from .OutputStyle import TextStyle
import time
import urllib

requests.packages.urllib3.disable_warnings()


class Connect:
    access_token = None
    org_id = None
    profile = None
    id = None
    service_url = "https://webexapis.com"
    type = "wbx"

    # store token then fetch users orgId and save
    def __init__(self, access_token=None, type="wbx"):
        if not access_token:
            TextStyle.error("Must pass API token for Admin API")
        else:
            self.access_token = access_token

            try:
                self.profile = self.get("/v1/people/me?callingData=true")
                self.od = self.profile['id']
                self.org = self.profile['orgId']

            except Exception as err:
                raise Exception(f"Error with Token or getting Org")

    # parses out paging from response headers
    @staticmethod
    def find_next_page(call_response):
        if 'Link' in call_response.headers:
            return call_response.headers['Link'].split(";")[0].strip("<>")
        else:
            return False

    # basic REST GET
    def get(self, uri, data=None, limit=50000):
        # URL encode parameters for appending to URI if provided
        if data:
            data = f"?{urllib.urlencode(data)}"
        else:
            data = ""

        headers = {"Accept": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}  # set auth header

        uri = f"{self.service_url}/{uri.strip('/')}{data}"
        return_values = {'items': []}
        # Loop while true to handled paged results and throttling
        while True:
            try:
                # send request to Webex
                response = requests.get(uri, headers=headers, verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST GET - {uri} {err}")

            else:
                if 200 <= response.status_code <= 300 and (response.headers['Content-Type'].find("json") > -1):
                    # create or add to return dict
                    response_data = response.json()
                    if 'items' in response_data:
                        return_values['items'].extend(response_data['items'])
                    else:
                        return response_data

                    # check for additional and loop until max (limit minimum is 50)
                    if len(return_values['items']) >= limit or self.find_next_page(response) is False:
                        return return_values
                    else:
                        uri = self.find_next_page(response)
                elif 200 <= response.status_code < 300:
                    return True
                elif response.status_code == 429:  # handle throttling
                    TextStyle.warning(f"Request to {uri} throttled.  Doing it again in a bit.")
                    time.sleep(int(response.headers['Retry-After']) + 1)

                elif response.status_code == 401:  # handle auth issues
                    TextStyle.error("Webex Admin token invalid.  Generate new token")
                    return False
                else:  # catch generic failures
                    TextStyle.error(f"Error sending GET to Webex - {uri}{data} {response}{response.text}")
                    return False

    # basic REST DELETE
    def delete(self, uri):
        headers = {"Accept": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}

        while True:  # loop for throttling
            try:
                response = requests.delete(f"{self.service_url}/{uri.strip('/')}", headers=headers, verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST DELETE - {uri} {err}")

            else:
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and (response.headers['Content-Type'].find("json") > -1):
                    return json.loads(response.text)
                else:
                    TextStyle.error(f"Error sending DELETE to Webex - {uri} {response}{response.text}")
                    return False

    # basic REST POST
    def post(self, uri, data):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}

        while True:  # loop for throttling
            try:
                response = requests.post(f"{self.service_url}/{uri.strip('/')}",
                                         headers=headers,
                                         data=json.dumps(data),
                                         verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST POST - {uri} {err}")

            else:
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and (response.headers['Content-Type'].find("json") > -1):
                    return json.loads(response.text)
                else:
                    TextStyle.error(f"Error sending POST to Webex - {uri} {response}{response.text}")
                    return False

    # basic REST PUT
    def put(self, uri, data):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}

        while True:  # loop for throttling\
            try:
                response = requests.put(f"{self.service_url}/{uri.strip('/')}",
                                        headers=headers,
                                        data=json.dumps(data),
                                        verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST PUT - {uri} {err}")

            else:
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and (response.headers['Content-Type'].find("json") > -1):
                    return json.loads(response.text)
                else:
                    TextStyle.error(f"Error sending PUT to Webex - {uri} {response}{response.text}")
                    return False

    # basic REST patch
    def patch(self, uri, data):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}

        while True:  # loop for throttling
            try:
                response = requests.patch(f"{self.service_url}/{uri.strip('/')}",
                                          headers=headers,
                                          data=json.dumps(data),
                                          verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST PATCH - {uri} {err}")

            else:
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and (response.headers['Content-Type'].find("json") > -1):
                    return json.loads(response.text)
                else:
                    TextStyle.error(f"Error sending PATCH to Webex - {uri} {response}{response.text}")
                    return False

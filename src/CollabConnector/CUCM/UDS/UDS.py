import requests
from requests.auth import HTTPBasicAuth
import sys
import json
import urllib

requests.packages.urllib3.disable_warnings()


class Connect:
    def __init__(self, ipaddr, username, passwd):
        self.ipaddr = ipaddr
        self.username = username
        self.auth = HTTPBasicAuth(username, passwd)

    # standard REST interface
    def get(self, target_uri=None, params={}):
        if target_uri.find("cucm-uds/") > -1:
            target_uri = "".join(target_uri.split("cucm-uds/")[1:])

        target_uri = f"https://{self.ipaddr}:8443/cucm-uds/{target_uri}"

        if len(params) > 0:
            target_uri += f"?{urllib.parse.urlencode(params)}"

        try:
            # send API request
            response = requests.request("GET",
                                        target_uri,
                                        headers={'Accept': 'application/json',
                                                 'Content-Type': 'application/json'},
                                        auth=self.auth,
                                        verify=False)

        except Exception as err:
            print(f"Error requesting UDS API: GET:{target_uri} - {err}", file=sys.stderr)
            return False

        else:
            if 200 <= response.status_code <= 300:
                # Attempt to parse json to dict
                try:
                    result = json.loads(response.text)
                except:
                    print(f"UDS response parsing error: {target_uri} - {response.text}", file=sys.stderr)
                    return False
                else:
                    return result
            elif 400 <= response.status_code <= 600:
                print(f"UDS response parsing error: {target_uri} - {response.text}", file=sys.stderr)
                return False
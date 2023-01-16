import requests
from requests.auth import HTTPBasicAuth
import sys
import json
import urllib
import socket

requests.packages.urllib3.disable_warnings()


class Connect:
    def __init__(self, ipaddr, username, passwd):
        self.ipaddr = ipaddr
        self.username = username
        self.auth = HTTPBasicAuth(username, passwd)
        if self.open_port(ipaddr, 443) is False:
            raise Exception (f"EXP Connection Error: {ipaddr}:443 not reachable or open. Is this Expressway?")
        try:
            self.version = self.get("/sysinfo")['SoftwareVersion'].replace('X', '')
        except Exception as err:
            raise Exception (f"EXP Connection Error: API request not valid. Improper credentials?: {err}")

    @staticmethod
    def open_port(ip, port, return_object=[]):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            s.connect((ip, int(port)))
            s.close()
            return_object.append(str(port))
            return port
        except Exception as e:
            s.close()
            return False

    # standard REST interface
    def rest(self, method, target_uri=None, params={}):
        if target_uri.find("api/provisioning") > -1:
            target_uri = "".join(target_uri.split("api/provisioning")[1:])

        target_uri = f"https://{self.ipaddr}/api/provisioning{target_uri}"

        if len(params) > 0 and (method == "get" or method == "delete"):
            target_uri += f"?{urllib.parse.urlencode(params)}"

        try:
            # send API request
            response = requests.request(method,
                                        target_uri,
                                        headers={'Accept': 'application/json',
                                                 'Content-Type': 'application/json'},
                                        auth=self.auth,
                                        verify=False,
                                        data=json.dumps(params))

        except Exception as err:
            print(f"Error requesting Expressway API: GET:{target_uri} - {err}", file=sys.stderr)
            return False

        else:
            if 200 <= response.status_code <= 300:
                # Attempt to parse json to dict
                try:
                    result = json.loads(response.text)
                except Exception as err:
                    print(f"EXP response parsing error: {err} - {target_uri} - {response.text}", file=sys.stderr)
                    return False
                else:
                    return result
            elif 400 <= response.status_code <= 600:
                print(f"EXP response parsing error: {target_uri} - {response}", file=sys.stderr)
                return False

    def get(self, target_uri, params={}):
        return self.rest("get", target_uri, params)

    def post(self, target_uri, params={}):
        return self.rest("get", target_uri, params)

    def put(self, target_uri, params={}):
        return self.rest("get", target_uri, params)

    def delete(self, target_uri, params={}):
        return self.rest("get", target_uri, params)

    def patch(self, target_uri, params={}):
        return self.rest("get", target_uri, params)

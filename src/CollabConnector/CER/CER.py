import requests
from requests.auth import HTTPBasicAuth
import sys
import xmltodict
import hashlib
import urllib

requests.packages.urllib3.disable_warnings()

REQUIRED_LIBS = {}


class Connect:

    # initialize object set system type and build DB connectors as needed
    def __init__(self,
                 ipaddr=None,
                 username=None,
                 passwd=None):

        # if type= cucm then set username/password for AXL connection
        if ipaddr is  None or passwd is None or username is None:
            print(f'Usage: CollabConnector.CUCM("ipaddr", "admin", "password", wsdl="./AXLAPI.wsdl")',
                  file=sys.stderr)
        else:
            self.system_type = "CER"
            self.ipaddr = ipaddr
            self.username = username
            self.auth = HTTPBasicAuth(username, passwd)
            self.hash_pass = hashlib.sha256(passwd.encode()).hexdigest()

            print("Connected.")

    # REST Wrapper for CER
    def cer_api(self, target_uri, method='GET', data={}):
        if target_uri.find("cerappservices/export/") > -1:
            target_uri = target_uri
        else:
            if target_uri.find('/') == 0:
                target_uri = target_uri[1:]
            target_uri = f"https://{self.ipaddr}:8443/cerappservices/export/{target_uri}"

        if len(data) > 0:
            target_uri += f"?{urllib.parse.urlencode(data)}"

        target_uri += f"/{self.username}/{self.hash_pass}"

        # create result array
        try:
            response = requests.request(method, target_uri, verify=False, timeout=(5, 30))
        except Exception as err:
            print(f"\tError with REST call - {err}")
            return False

        if str(response.status_code) == 200:
            try:
                cer_array = xmltodict.parse(response.text, dict_constructor=dict)
            except Exception as err:
                print("Error parsing XML.  Expect String back", file=sys.stderr)
                return response.text
            else:
                return cer_array

        else:
            print("\tError:" + str(response) + "\n\n" + response.text, file=sys.stderr)
            return False

    # wrapper for api Gets
    def get(self, target_endpoint, params={}):
        return self.cer_api(target_endpoint, data=params)

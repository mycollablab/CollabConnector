import requests
from requests import Session
from requests.auth import HTTPBasicAuth
import sys
import os
from zeep.transports import Transport
from zeep import Client, Settings

requests.packages.urllib3.disable_warnings()


class Connect:
    def __init__(self, ipaddr, username, passwd, version="14.0", wsdl=None):
        # if type= cucm then set username/password for AXL connection
        if ipaddr is None or passwd is None or username is None:
            print(f'Usage: CollabConnector.AXL("ipaddr", "admin", "password", version="12.0", wsdl="./AXL/AXLAPI.wsdl")',
                  file=sys.stderr)
        else:
            self.username = username

            if wsdl:
                wsdl = wsdl
            elif version and int(version.split(".")[0]) < 10:
                wsdl = os.path.join(os.path.dirname(__file__), 'schema', '10.0', 'AXLAPI.wsdl')
            elif version:
                wsdl = os.path.join(os.path.dirname(__file__), 'schema', version, 'AXLAPI.wsdl')

            # create a SOAP client session
            session = Session()

            # avoid certificate verification by default and setup session
            session.verify = False
            session.auth = HTTPBasicAuth(username, passwd)
            transport = Transport(session=session, timeout=10)
            settings = Settings(strict=False, xml_huge_tree=True)

            # If WSDL file specified then create AXL SOAP connector
            if wsdl is not None:
                # Create the Zeep client with the specified settings
                client_axl = Client(wsdl, settings=settings, transport=transport)  # ,plugins = plugin )
                # Create the Zeep service binding to AXL at the specified CUCM
                try:
                    self.client = client_axl.create_service(
                        '{http://www.cisco.com/AXLAPIService/}AXLAPIBinding',
                        f'https://{ipaddr}:8443/axl/')

                except Exception as err:
                    print(f"SOAP/AXL Error could not create service: {err}", file=sys.stderr)
                    self.client = False
import requests
from requests import Session
from requests.auth import HTTPBasicAuth
import sys
import os
from zeep.transports import Transport
from zeep import Client, Settings

requests.packages.urllib3.disable_warnings()


class Connect:
    def __init__(self, ipaddr, username, passwd):
        # if type= cucm then set username/password for AXL connection
        if ipaddr is None or passwd is None or username is None:
            print(f'Usage: CollabConnector.Risport("ipaddr", "admin", "password")',
                  file=sys.stderr)
        else:
            self.username = username
            # set risport WSDL file from URL
            risport_wsdl = f'https://{ipaddr}:8443/realtimeservice2/services/RISService70?wsdl'

            # create a SOAP client session
            session = Session()

            # avoid certificate verification by default and setup session
            session.verify = False
            session.auth = HTTPBasicAuth(username, passwd)
            transport = Transport(session=session, timeout=10)
            settings = Settings(strict=False, xml_huge_tree=True)

            # Create client and soap service
            client_risport = Client(risport_wsdl, settings=settings,
                                    transport=transport)  # , plugins = plugin )
            self.client = client_risport.create_service(
                '{http://schemas.cisco.com/ast/soap}RisBinding',
                f'https://{ipaddr}:8443/realtimeservice2/services/RISService70')
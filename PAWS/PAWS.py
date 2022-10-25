# https://d1nmyq4gcgsfi5.cloudfront.net/site/paws/documents/api-reference/#getclusternodes

import sys
import requests
from zeep.transports import Transport
from zeep import Client, Settings
from zeep.helpers import serialize_object

requests.packages.urllib3.disable_warnings()


class Connect():
    ipaddr = None
    os_creds = None
    soap_cluster_node_service = None

    def __init__(self, ipaddr=None, username=None, passwd=None,):
        print("Connecting to CM Platform Administration...")
        if ipaddr is None:
            print("Must declare connection info: ", file=sys.stderr)
            print("Collab.CMServiceManager(ipaddr='x.x.x.x', app_creds=('appAdmin', 'SECRET')",
                  file=sys.stderr)
        else:
            self.ipaddr = ipaddr
            if username is None or passwd is None:
                print("Must declare connection info: ", file=sys.stderr)
                print("Collab.CMServiceManager(ipaddr='x.x.x.x', app_creds=('appAdmin', 'SECRET')",
                      file=sys.stderr)
            else:
                self.os_creds = requests.auth.HTTPBasicAuth(username, passwd)
                self.create_cluster_node_service()
                # self.create_drs_service()

        print("... Done")

    def create_drs_service(self):
        paws_wsdl = f'https://{self.ipaddr}/platform-services/services/DataExportService?wsdl'

        # create a SOAP client session
        session = requests.Session()

        # avoid certificate verification by default and setup session
        session.verify = False
        session.auth = self.os_creds
        transport = Transport(session=session, timeout=10)
        settings = Settings(strict=False, xml_huge_tree=True)

        # Create client and soap service
        client_paws = Client(paws_wsdl, settings=settings,
                             transport=transport)  # , plugins = plugin )
        try:
            self.soap_drs_service = client_paws.create_service(
                '{http://services.api.platform.vos.cisco.com}DataExportServiceHttpBinding',
                paws_wsdl)
        except Exception as err:
            print(f"Error creating PAWS SOAP Connector: {err}", file=sys.stderr)
            return False

        paws_wsdl = f'https://{self.ipaddr}/platform-services/services/DataExportStatusService?wsdl'

        # create a SOAP client session
        session = requests.Session()

        # avoid certificate verification by default and setup session
        session.verify = False
        session.auth = self.os_creds
        transport = Transport(session=session, timeout=10)
        settings = Settings(strict=False, xml_huge_tree=True)

        # Create client and soap service
        client_paws = Client(paws_wsdl, settings=settings,
                             transport=transport)  # , plugins = plugin )
        try:
            self.soap_drs_status = client_paws.create_service(
                '{http://services.api.platform.vos.cisco.com}DataExportStatusServiceHttpBinding',
                paws_wsdl)
        except Exception as err:
            print(f"Error creating PAWS SOAP Connector: {err}", file=sys.stderr)
            return False

        else:
            return True

    def create_cluster_node_service(self):
        paws_wsdl = f'https://{self.ipaddr}/platform-services/services/ClusterNodesService?wsdl'

        # create a SOAP client session
        session = requests.Session()

        # avoid certificate verification by default and setup session
        session.verify = False
        session.auth = self.os_creds
        transport = Transport(session=session, timeout=10)
        settings = Settings(strict=False, xml_huge_tree=True)

        # Create client and soap service
        client_paws = Client(paws_wsdl, settings=settings,
                             transport=transport)  # , plugins = plugin )
        try:
            self.soap_cluster_node_service = client_paws.create_service(
                '{http://services.api.platform.vos.cisco.com}ClusterNodesServiceSoap11Binding',
                paws_wsdl)
        except Exception as err:
            print(f"Error creating PAWS SOAP Connector: {err}", file=sys.stderr)
            return False

        else:
            return True

    def discover_cluster(self):
        try:
            result = self.soap_cluster_node_service.getClusterStatus()['clusterNodeStatus']

        except Exception as err:
            print(f"Error with cluster discovery: {err}", file=sys.stderr)
            return False

        else:
            return serialize_object(result, dict)

    def replication_status(self):
        try:
            result = self.soap_cluster_node_service.isClusterReplicationOK()

        except Exception as err:
            print(f"Error with cluster discovery: {err}", file=sys.stderr)
            return False

        else:
            return serialize_object(result, dict)

    def drs_initiate(self, sftp_server=None, sftp_port=22, sftp_username=None, sftp_passwd=None, sftp_directory=None):
        try:
            result = self.soap_drs_service.dataExport([sftp_server,
                                                      sftp_port,
                                                      sftp_username,
                                                      sftp_passwd,
                                                      sftp_directory])

        except Exception as err:
            print(f"Error initiating DRS backup: {err}", file=sys.stderr)
            return False

        else:
            return serialize_object(result, dict)

    def drs_status(self):
        try:
            result = self.soap_drs_status.dataExportStatus()

        except Exception as err:
            print(f"Error getting DRS status: {err}", file=sys.stderr)
            return False

        else:
            return serialize_object(result, dict)

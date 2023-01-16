import sys
import requests
from zeep.transports import Transport
from zeep import Client, Settings
from zeep.helpers import serialize_object
import re

requests.packages.urllib3.disable_warnings()


class Connect:
    app_creds = None
    version = None
    nodes = {}
    service_list = []

    def __init__(self, ipaddr=None, username=None, passwd=None, nodes=None):
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
                self.app_creds = requests.auth.HTTPBasicAuth(username, passwd)
                if nodes is None:
                    nodes = [ipaddr]
                for node in nodes:
                    self.discover_node(node)

    # discover platform components for nodes and available services and store
    def discover_node(self, ipaddr):
        # set WSDL file from URL
        controlcenter_wsdl = f'https://{ipaddr}:8443/controlcenterservice2/services/ControlCenterServices?wsdl'

        # create a SOAP client session
        session = requests.Session()

        # avoid certificate verification by default and setup session
        session.verify = False
        session.auth = self.app_creds
        transport = Transport(session=session, timeout=10)
        settings = Settings(strict=False, xml_huge_tree=True)

        # Create client and soap service
        client_controlcenter = Client(controlcenter_wsdl, settings=settings,
                                      transport=transport)  # , plugins = plugin )
        try:
            soap_controlcenter = client_controlcenter.create_service(
                '{http://schemas.cisco.com/ast/soap}ControlCenterServicesBinding',
                controlcenter_wsdl)
        except Exception as err:
            print(f"Error creating SOAP Connector: {err}", file=sys.stderr)

        else:
            try:
                server_list = soap_controlcenter.getProductInformationList(ServiceInfo="")

            except Exception as err:
                print(f"Error getting server list and info: {err}", file=sys.stderr)
                return False

            else:
                self.version = server_list['ActiveServerVersion']
                if ipaddr not in list(self.nodes.keys()):
                    self.nodes[ipaddr] = { 'name': server_list['PrimaryNode'], 'soap': soap_controlcenter }

                if self.service_list == []:
                    [self.service_list.append(i['ServiceName']) for i in server_list['Services']['item']]

                return True

    # convert list return into a dict based on the service name
    @staticmethod
    def list_to_dict(return_list):
        results = {}
        for service in return_list['ServiceInfoList']['item']:
            try:
                results[service['ServiceName']] = serialize_object(service, dict)
            except:
                results[service['ServiceName']] = service

        return results

    # check requested service against actual services and try to resolve
    def verify_service_name(self, service):
        if service in self.service_list:
            return service

        else:
            for i in self.service_list:
                if re.sub("[^a-z]","",service.lower().replace("cisco","")) == re.sub("[^a-z]","",i.lower().replace("cisco","")):
                    return i

        print('Cannot find service in list', file=sys.stderr)
        return False

    # return service status of all services
    def status(self, service_list=None, nodes=None):
        # if nodes not specified then assume all nodes in cluster
        if nodes is None:
            nodes = self.nodes

        elif isinstance(nodes, str):
            nodes = [nodes]

        if service_list is not None:
            if isinstance(service_list, list):
                # loop through the requested service list and try and correct naming
                x = 0
                while x < len(service_list):
                    service = self.verify_service_name(service_list[x])
                    if service is not False:
                        service_list[x] = self.verify_service_name(service_list[x])
                    else:
                        print(f"Unknown Service {service_list[x]}", file=sys.stderr)
                        service_list.pop(x)
                    x += 1
            else:
                service_list = [self.verify_service_name(service_list)]

        else:
            service_list = ""

        results = {}
        for node in nodes:
            try:
                service_status = self.nodes[node]['soap'].soapGetServiceStatus(ServiceStatus=service_list)

            except Exception as err:
                print(f"Error getting service status: {err}", file=sys.stderr)

            else:
                results[node] = self.list_to_dict(service_status)

        return results

    # actions based on service list n node list
    def service(self, action, service_list, nodes=None):
        activate = False
        if isinstance(service_list, str):
            service_list = [service_list]

        # if none list is blank then assume all nodes
        if nodes is None:
            nodes = self.nodes
        elif isinstance(nodes, str):
            nodes = [nodes]

        if action.lower() == "status":
            return self.get_service_status(service_list, nodes)
        elif action.lower() == "start":
            action = "Start"
        elif action.lower() == "restart":
            action = "Restart"
        elif action.lower() == "stop":
            action = "Stop"
        elif action.lower() == "deactivate":
            activate = True
            action = "UnDeploy"
        elif action.lower() == "activate":
            activate = True
            action = "Deploy"
        else:
            print(f"\tUnknown action command - {action}", file=sys.stderr)
            return False

        # loop through service list and try and confirm/correct naming
        x = 0
        while x < len(service_list):
            service = self.verify_service_name(service_list[x])
            if service is not False:
                service_list[x] = self.verify_service_name(service_list[x])
            else:
                print(f"Unknown Service: {service_list[x]}", file=sys.stderr)
                service_list.pop(x)
            x += 1

        # if no valid services then skip fetching
        if len(service_list) == 0:
            print(f"No valid services to check.", file=sys.stderr)
            return False
        else:
            results = {}
            # loop services on nodes
            for node in nodes:
                print(f"\t{action}ing {service_list} on {node}...")
                try:
                    if activate:
                        result = self.nodes[node]['soap'].soapDoServiceDeployment(
                            DeploymentServiceRequest={'NodeName': node, 'DeployType': action,
                                                      'ServiceList': service_list})
                    else:
                        result = self.nodes[node]['soap'].soapDoControlServices(
                            ControlServiceRequest={'NodeName': node, 'ControlType': action, 'ServiceList': service_list})

                except Exception as err:
                    print(f"\tError {action}ing {service_list}: {err}", file=sys.stderr)

                else:
                    # reformat and append results
                    results[node] = self.list_to_dict(result)

            return results

    def start(self, service_list, nodes=None):
        return self.service("start", service_list, nodes)

    def stop(self, service_list, nodes=None):
        return self.service("stop", service_list, nodes)

    def restart(self, service_list, nodes=None):
        return self.service("restart", service_list, nodes)

    def activate(self, service_list, nodes=None):
        return self.service("activate", service_list, nodes)

    def deactivate(self, service_list, nodes=None):
        return self.service("deactivate", service_list, nodes)

    def find_tftp(self):
        print("Finding TFTP servers...")
        tftp_servers = self.status("Cisco Tftp")

        server_list = []
        for server in tftp_servers:
            if tftp_servers[server]['Cisco Tftp']['ReasonCodeString'].find("Service Not Activated") < 0:
                server_list.append(server)

        return server_list

    def find_moh(self):
        print("Finding Media Streaming servers...")
        moh_servers = self.status("Cisco IP Voice Media Streaming App")

        server_list = []
        for server in moh_servers:
            if moh_servers[server]['Cisco IP Voice Media Streaming App']['ReasonCodeString'].find("Service Not Activated") < 0:
                server_list.append(server)

        return server_list

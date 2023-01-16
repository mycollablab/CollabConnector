import requests
from requests.auth import HTTPBasicAuth
import sys
import xmltodict
import urllib

requests.packages.urllib3.disable_warnings()


class Connect:
    ip_addr = None
    username = None
    passwd = None
    cluster = None
    status_service = {
                "0": 'Service Down',
                "1": 'Service Up',
                "2": 'Service Not Activated',
                "3": 'Service Stopping',
                "4": 'Service Starting',
                "5": 'Service Commanded Out of Service',
                "255": 'Service Does Not Exist'
              }
    status_device = {
                    "1": "Registered"
    }

    def __init__(self, ip_addr=None, username=None, passwd=None):
        if not ( ip_addr and username and passwd):
            raise "AST init: Must provide ip_addr, username, passwd"
        else:
            self.ip_addr = ip_addr
            self.username = username
            self.auth = HTTPBasicAuth(username, passwd)
            self.cluster = self.cluster_discovery()

    # standard REST interface
    def rest_get(self, target_uri, params=None):
        if params is not None:
            params = f"&{urllib.parse.urlencode(params)}"
        else:
            params = ""

        try:
            # send API request
            response = requests.request("GET", f"https://{self.ip_addr}/ast/Astisapi.dll?{target_uri}{params}", auth=self.auth,
                                        headers={}, verify=False)

        except Exception as err:
            print(f"Error requesting API: GET- {target_uri} - {err}", file=sys.stderr)
            return False

        else:
            if 200 <= response.status_code == 300:
                # Attempt to parse XML to dict
                try:
                    result = xmltodict.parse(response.text, dict_constructor=dict)
                except:
                    result = response.text

                return result
            else:
                print(f"AST GET Error: {target_uri} - {response.status_code}", file=sys.stderr)
                return False

    def cluster_discovery(self):
        try:
            cluster = self.rest_get(f"QueryService")['QueryServiceReply']['Cluster']
        except Exception as err:
            print(f"AST ERROR: Discover_cluster: {err}", file=sys.stderr)
            return None
        else:
            return_cluster = {'cluster_name': cluster['@Name'], 'nodes': [], 'service_nodes': {}}
            for srv in cluster['ServiceType']:
                return_cluster['service_nodes'][srv['@Name'].lower().split("_")[1]] = []
                if isinstance(srv['Service'], list):
                    for srv_num in srv['Service']:
                        return_cluster['service_nodes'][srv['@Name'].lower().split("_")[1]].append(srv_num['@Name'])
                else:
                    return_cluster['service_nodes'][srv['@Name'].lower().split("_")[1]].append(srv['Service']['@Name'])

            for node in return_cluster['service_nodes']['db']:
                return_cluster['nodes'].append(node)

            return return_cluster

    def query_service(self):
        try:
            ast_response = self.rest_get(f"QueryService")['QueryServiceReply']['Cluster']['ServiceType']
        except Exception as err:
            print(f"AST ERROR: get_ris_collector_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_device_status(self, devices):
        if type(devices) == list:
            devices = ",".join(devices)
        return self.rest_get(f"OpenDeviceSearch?Type=&NodeName=&SubSystemType=&Status=1&DownloadStatus=&MaxDevices=200&Model=&SearchType=Name&Protocol=Any&SearchPattern={devices}")['DeviceReply']['ReplyNode']

    def get_precanned_info(self, request=None):
        if request is None:
            print("Must supply list of items to request", file=sys.stderr)
            return False
        if type(request) == list:
            request = f"Items={';'.join(request)}"
        try:
            ast_response = self.rest_get(f"GetPreCannedInfo&{request}")['PreCannedReplies']
        except Exception as err:
            print(f"AST ERROR: get_precanned_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_ris_collector_info(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getRisCollectorInfoRequest")['PreCannedReplies']['getRisCollectorInfoReply']
        except Exception as err:
            print(f"AST ERROR: get_ris_collector_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_service_info(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getServiceInfoRequest")['PreCannedReplies']['getServiceInfoReply']
        except Exception as err:
            print(f"AST ERROR: get_service_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_cpu_and_memory(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getCpuAndMemoryRequest")['PreCannedReplies']['getCpuAndMemoryReply']
        except Exception as err:
            print(f"AST ERROR: get_cpu_and_memory", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_partition_info(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getPartitionInfoRequest")['PreCannedReplies']['getPartitionInfoReply']
        except Exception as err:
            print(f"AST ERROR: get_partition_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_call_activity(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getCallActivityRequest")['PreCannedReplies']['getCallActivityReply']
        except Exception as err:
            print(f"AST ERROR: get_call_activity", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_gateway_activity(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getGatewayActivityRequest")['PreCannedReplies']['getGatewayActivityReply']
        except Exception as err:
            print(f"AST ERROR: get_gateway_activity", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_trunk_activity(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getTrunkActivityRequest")['PreCannedReplies']['getTrunkActivityReply']
        except Exception as err:
            print(f"AST ERROR: get_trunk_activity", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_sdl_queue_info(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getSdlqueueInfoRequest")['PreCannedReplies']['getSdlqueueInfoReply']
        except Exception as err:
            print(f"AST ERROR: get_sdl_queue_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_cti_manager_info(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getCtiManagerInfoRequest")['PreCannedReplies']['getCtiManagerInfoReply']
        except Exception as err:
            print(f"AST ERROR: get_cti_manager_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_tftp_info(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getTftpInfoRequest")['PreCannedReplies']['getTftpInfoReply']
        except Exception as err:
            print(f"AST ERROR: get_tftp_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_registered_device(self, params={}):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getRegisteredDeviceRequest", params)['PreCannedReplies']
        except Exception as err:
            print(f"AST ERROR: get_registered_device", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_heartbeat_info(self):
        try:
            ast_response = self.rest_get("GetPreCannedInfo&Items=getHeartbeatInfoRequest")['PreCannedReplies']['getHeartbeatInfoReply']
        except Exception as err:
            print(f"AST ERROR: get_heartbeat_info", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_db_change_notify(self):
        try:
            ast_response = self.rest_get('GetPreCannedInfo&Items=getDbChngNotifyRequest')['PreCannedReplies']['getDbSummaryReply']
        except Exception as err:
            print(f"AST ERROR: get_db_change_notify", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_alert_summary(self):
        try:
            ast_response = self.rest_get("GetAlertSummaryList")['GetAlertSummaryListReply']['AlertSummaryList']
        except Exception as err:
            print(f"AST ERROR: get_alert_summary", file=sys.stderr)
            return False
        else:
            return ast_response

    def list_alert_action(self):
        try:
            ast_response = self.rest_get("ListAlertAction")['ListAlertActionReply']['AlertActionList']
        except Exception as err:
            print(f"AST ERROR: list_alert_action", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_email_config(self):
        try:
            ast_response = self.rest_get("GetEmailConfig")['GetEmailConfigReply']['EmailConfig']
        except Exception as err:
            print(f"AST ERROR: get_email_config", file=sys.stderr)
            return False
        else:
            return ast_response

    def get_alert_suspend(self):
        try:
            ast_response = self.rest_get("GetAlertSuspend")['GetAlertSuspendReply']['NodeList']
        except Exception as err:
            print(f"AST ERROR: get_alert_suspend", file=sys.stderr)
            return False
        else:
            return ast_response

    def perfmon_list(self):
        try:
            ast_response = self.rest_get("PerfmonListObject")['PerfmonListObjectReply']['Cluster']
        except Exception as err:
            print(f"AST ERROR: perfmon_list", file=sys.stderr)
            return False
        else:
            return ast_response




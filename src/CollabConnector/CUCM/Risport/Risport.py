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
            self.risport = self.client

    # risport query for device registration
    def query(self, device_list: str|list = None, return_format="dict"):
        if self.risport is False:
            print("risport client not available.", file=sys.stderr)
            return False
        # If no list given then get all devices to list
        if type(device_list) == str:
            device_list = [device_list]

        i = 0
        risport_response = {}
        while i < len(device_list):
            # Build and execute the risport request object
            state_info = ''

            # Build Search Criteria
            risport_search_criteria = {
                'MaxReturnedDevices': '1000',
                'DeviceClass': 'Any',
                'Model': '255',
                'Status': 'Any',
                'NodeName': '',
                'SelectBy': 'Name',
                'Protocol': 'Any',
                'DownloadStatus': 'Any',
                'SelectItems': {
                    'item': device_list
                }
            }
            # One or more specific devices can be retrieved by replacing * with
            # the device name in multiple items
            # device_count = 0
            # while device_count < 1000 and (device_count + i) < len(device_list):
            #     if isinstance(device_list[device_count + i], dict):
            #         risport_response[device_list[device_count + i]['device']] = {'description': '', 'protocol': '',
            #                                                                      'type': '', 'firmware': '', 'Node': '',
            #                                                                      'IPAddress': '', 'dirn': '',
            #                                                                      'status': 'Never'}
            #         risport_search_criteria['SelectItems']['item'].append(
            #             {'Item': device_list[device_count + i]['device']})
            #
            #     elif isinstance(device_list[device_count + i], str):
            #         risport_response[device_list[device_count + i]] = {'description': '', 'protocol': '', 'type': '',
            #                                                            'firmware': '', 'Node': '', 'IPAddress': '',
            #                                                            'dirn': '', 'status': 'Never'}
            #         risport_search_criteria['SelectItems']['item'].append({'Item': device_list[device_count + i]})
            #
            #     device_count = device_count + 1
            #
            # i += device_count

            # Get reg statuses
            try:
                resp = self.risport.selectCmDevice(state_info, risport_search_criteria)
            except Exception as err:
                print(f'Zeep error: selectCmDevice: {err}', file=sys.stderr)
                return False

            # format results for easy parsing
            for node in resp['SelectCmDeviceResult']['CmNodes']['item']:
                if node['ReturnCode'] != 'Ok':
                    continue

                for device in node['CmDevices']['item']:
                    risport_response[device['Name']] = {}
                    risport_response[device['Name']]['name'] = device['Name']
                    risport_response[device['Name']]['node'] = node['Name']
                    ipaddresses = device['IPAddress']
                    risport_response[device['Name']]['description'] = device['Description'] if device[
                                                                                                   'Description'] is not None else ''
                    risport_response[device['Name']]['protocol'] = device['Protocol'] if device[
                                                                                             'Protocol'] is not None else ''
                    risport_response[device['Name']]['type'] = device['DeviceClass'] if device[
                                                                                            'DeviceClass'] is not None else ''
                    risport_response[device['Name']]['firmware'] = device['ActiveLoadID'] if device[
                                                                                                 'ActiveLoadID'] is not None else ''
                    risport_response[device['Name']]['IPAddress'] = ipaddresses['item'][0]['IP'] if ipaddresses else ''

                    if device['LinesStatus'] is None:
                        risport_response[device['Name']]['dirn'] = "unknown"
                        risport_response[device['Name']]['status'] = device['Status']

                    else:
                        for x in range(0, len(device['LinesStatus']['item'])):
                            if x == 0:
                                risport_response[device['Name']]['dirn'] = device['LinesStatus']['item'][x][
                                    'DirectoryNumber']
                                risport_response[device['Name']]['status'] = device['LinesStatus']['item'][x]['Status']
                                break

        # if default dict format then return dict
        if return_format == "dict":
            return risport_response

        # else if return format is list then loop through to convert dict based on device name to list of results
        elif return_format == "list":
            risport_list = []
            for item in risport_response:
                if "name" in risport_response[item]:
                    risport_list.append(risport_response[item])

            return risport_list

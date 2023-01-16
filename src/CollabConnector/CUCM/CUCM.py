import requests
from requests import Session
from requests.auth import HTTPBasicAuth
import sys
import xmltodict
import re
import os
import json
import urllib
from .AST import *
from .Serviceability import *
from .DIME import *
from .Logs import Logs
from .CDR import CDR
from . import AXL
from . import Risport
from . import UDS
import socket

requests.packages.urllib3.disable_warnings()


class Connect:
    # initialize object set system type and build DB connectors as needed
    def __init__(self, ipaddr=None, username=None, passwd=None, version=None, wsdl=None):
        self.system_type = "cucm"
        self.ipaddr = ipaddr
        self.axl = False
        self.risport = False
        self.auth = HTTPBasicAuth(username, passwd)

        if self.open_port(ipaddr, 8443) is False:
            raise Exception (f"Connection Error: {ipaddr}:8443 not reachable or open. Is this CUCM?")
        if self.query("SELECT COUNT(*) FROM processnode") is False:
            raise Exception (f"Connection Error: AXL request not valid. Improper credentials?")

        self.uds = UDS.Connect(ipaddr, username, passwd)
        try:
            self.version = self.uds.get("version")['@version']
        except Exception as err:
            print(f"Could not determine CUCM version via UDS: {err}")
            self.version = False

        risport = Risport.Connect(ipaddr, username, passwd)
        self.risport = risport.client

        axl = AXL.Connect(ipaddr, username, passwd, '.'.join(self.version.split('.')[0:2]))
        self.axl = axl.client
        self.add = AXL.Add(self.axl)
        self.do = AXL.Do(self.axl)
        self.get = AXL.Get(self.axl)
        self.list = AXL.List(self.axl)
        self.remove = AXL.Remove(self.axl)
        self.update = AXL.Update(self.axl)

        self.ast = AST.Connect(ipaddr, username, passwd)
        self.cluster = self.ast.cluster
        if self.cluster:
            self.serviceability = Serviceability.Connect(ipaddr, username, passwd, self.cluster['nodes'])
        else:
            self.serviceability = Serviceability.Connect(ipaddr, username, passwd)
        self.dime = DIME.Connect(ipaddr, username, passwd)
        # self.logs = Logs(ipaddr, username, passwd)
        self.cdr = CDR(ipaddr, username, passwd)

        print("Connected.")

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

    # Function to query SQL via AXL API to CUCM
    def query(self, sql_statement):
        result_dict = []
        row_info = ["", None, None]
        newsql_statement = sql_statement
        while row_info[1] is None or int(row_info[1]) > len(result_dict):
            if re.search("select", sql_statement.lower()):
                execute_sql = "executeSQLQuery"
            else:
                execute_sql = "executeSQLUpdate"

            if row_info[1] is not None and int(row_info[1]) > 0:
                newsql_statement = re.sub("[sS][eE][lL][eE][cC][tT] ",
                                          f"SELECT SKIP {len(result_dict)} LIMIT {row_info[2]} ", sql_statement)

            payload = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
                            <soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ns=\"http://www.cisco.com/AXL/API/10.5\">
                              <soapenv:Header/>
                              <soapenv:Body>
                                <ns:{execute_sql}>
                                  <sql>
                                    {newsql_statement}
                                  </sql>
                                </ns:{execute_sql}>  
                              </soapenv:Body>
                            </soapenv:Envelope>"""
            try:
                # send API request
                response = requests.request("POST", f'https://{self.ipaddr}:8443/axl/',
                                            headers={'Content-Type': 'text/xml'},
                                            auth=self.auth,
                                            data=payload,
                                            verify=False)
            except Exception as err:
                print(f"Error with AXL DB request: {err}", file=sys.stderr)
                return False
            else:
                # If request was good then return response values
                if response.status_code == 200:
                    # normalize output to always show array of rows
                    if re.search('ns:executeSQLUpdateResponse', response.text):
                        result_dict.extend([xmltodict.parse(response.text)['soapenv:Envelope']['soapenv:Body'][
                                                'ns:executeSQLUpdateResponse']['return']])
                        break

                    elif xmltodict.parse(response.text)['soapenv:Envelope']['soapenv:Body']['ns:executeSQLQueryResponse'][
                        'return'] is not None:
                        if type(xmltodict.parse(response.text, dict_constructor=dict)['soapenv:Envelope']['soapenv:Body'][
                                    'ns:executeSQLQueryResponse']['return']['row']) is not list:
                            result_dict.extend([xmltodict.parse(response.text, dict_constructor=dict)['soapenv:Envelope'][
                                                    'soapenv:Body']['ns:executeSQLQueryResponse']['return']['row']])
                        else:
                            result_dict.extend(
                                xmltodict.parse(response.text, dict_constructor=dict)['soapenv:Envelope']['soapenv:Body'][
                                    'ns:executeSQLQueryResponse']['return']['row'])

                        if row_info[1] is None or int(row_info[1]) <= len(result_dict):
                            break
                    else:
                        return []

                elif re.search("Query request too large. Total rows matched: ", response.text):
                    row_info = re.sub("[^\d:]", '',
                                      xmltodict.parse(response.text, dict_constructor=dict)['soapenv:Envelope'][
                                          'soapenv:Body']['soapenv:Fault']['faultstring']).split(":")
                    print(f"Multiple queries needed for {row_info[1]} rows.")

                else:
                    print(f'Requests Error: {response}', file=sys.stderr)
                    print(f'\t{sql_statement}', file=sys.stderr)
                    print(f'\t{response.text}', file=sys.stderr)
                    return False

        return result_dict

    # risport query for device registration
    def registration_status(self, device_list=None, return_format="dict"):
        if self.risport is False:
            print("risport client not available.", file=sys.stderr)
            return False
        # If no list given then get all devices to list
        if device_list is None:
            device_list = self.query(f"SELECT name AS device FROM device WHERE tkclass = 1")
        elif type(device_list) == str:
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
                    'item': []
                }
            }
            # One or more specific devices can be retrieved by replacing * with
            # the device name in multiple items
            device_count = 0
            while device_count < 1000 and (device_count + i) < len(device_list):
                if isinstance(device_list[device_count + i], dict):
                    risport_response[device_list[device_count + i]['device']] = {'description': '', 'protocol': '',
                                                                                 'type': '', 'firmware': '', 'Node': '',
                                                                                 'IPAddress': '', 'dirn': '',
                                                                                 'status': 'Never'}
                    risport_search_criteria['SelectItems']['item'].append(
                        {'Item': device_list[device_count + i]['device']})

                elif isinstance(device_list[device_count + i], str):
                    risport_response[device_list[device_count + i]] = {'description': '', 'protocol': '', 'type': '',
                                                                       'firmware': '', 'Node': '', 'IPAddress': '',
                                                                       'dirn': '', 'status': 'Never'}
                    risport_search_criteria['SelectItems']['item'].append({'Item': device_list[device_count + i]})

                device_count = device_count + 1

            i += device_count

            # Get reg statuses
            try:
                resp = self.risport.selectCmDevice(state_info, risport_search_criteria)
            except Fault as err:
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

    def update_pt(self, uuid, partition):
        try:
            dn_return = self.update.Line(uuid=uuid, newRoutePartitionName=partition)

        except Exception as err:
            print(f"Error during DN Update: ", err)
            return False

        else:
            return dn_return

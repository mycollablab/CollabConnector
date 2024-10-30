import requests
from requests import Session
from requests.auth import HTTPBasicAuth
import sys
import os
import lxml
from zeep.transports import Transport
from zeep import Client, Settings
from zeep.helpers import serialize_object

requests.packages.urllib3.disable_warnings()


class Connect:
    def __init__(self, ipaddr, username, passwd, version="14.0", wsdl=None):
        # if type= cucm then set username/password for AXL connection
        if ipaddr is None or passwd is None or username is None:
            raise Exception(
                f'Usage: CollabConnector.AXL("ipaddr", "admin", "password", version="12.0", wsdl="./AXL/AXLAPI.wsdl")')
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
                self.axl_client = Client(wsdl, settings=settings, transport=transport)  # ,plugins = plugin )
                # Create the Zeep service binding to AXL at the specified CUCM
                try:
                    self.axl_service = self.axl_client.create_service(
                        '{http://www.cisco.com/AXLAPIService/}AXLAPIBinding',
                        f'https://{ipaddr}:8443/axl/')

                except Exception as err:
                    print(f"SOAP/AXL Error could not create service: {err}", file=sys.stderr)
                    self.axl_service = False

    def elements_to_dict(self, input):
        if input is None or isinstance(input, (str, int, float, complex, bool, tuple)):
            return input

        if isinstance(input, dict):
            for key, value in input.items():
                input[key] = self.elements_to_dict(value)
            return input

        elif isinstance(input, list):
            return_list = []
            for position in input:
                return_list.append(self.elements_to_dict(position))
            return return_list

        elif isinstance(input, lxml.etree._Element):
            element = {}  # {t.tag : map(etree_to_dict, t.iterchildren())}
            element.update(('@' + k, v) for k, v in input.attrib.iteritems())
            element[input.tag] = input.text
            return element

        else:
            return str(input)

    def getSipProfile(self, **args):
        try:
            resp = self.axl_service.getSipProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSipProfile`: ", str(err), file=sys.stderr)
            return []

    def listSipProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSipProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSipProfile`: ", str(err), file=sys.stderr)
            return []

    def getSipProfileOptions(self, **args):
        try:
            resp = self.axl_service.getSipProfileOptions(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSipProfileOptions`: ", str(err), file=sys.stderr)
            return []

    def getSipTrunkSecurityProfile(self, **args):
        try:
            resp = self.axl_service.getSipTrunkSecurityProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSipTrunkSecurityProfile`: ", str(err), file=sys.stderr)
            return []

    def listSipTrunkSecurityProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSipTrunkSecurityProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSipTrunkSecurityProfile`: ", str(err), file=sys.stderr)
            return []

    def getTimePeriod(self, **args):
        try:
            resp = self.axl_service.getTimePeriod(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getTimePeriod`: ", str(err), file=sys.stderr)
            return []

    def listTimePeriod(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listTimePeriod(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listTimePeriod`: ", str(err), file=sys.stderr)
            return []

    def getTimeSchedule(self, **args):
        try:
            resp = self.axl_service.getTimeSchedule(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getTimeSchedule`: ", str(err), file=sys.stderr)
            return []

    def listTimeSchedule(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listTimeSchedule(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listTimeSchedule`: ", str(err), file=sys.stderr)
            return []

    def getTodAccess(self, **args):
        try:
            resp = self.axl_service.getTodAccess(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getTodAccess`: ", str(err), file=sys.stderr)
            return []

    def listTodAccess(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listTodAccess(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listTodAccess`: ", str(err), file=sys.stderr)
            return []

    def getVoiceMailPilot(self, **args):
        try:
            resp = self.axl_service.getVoiceMailPilot(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getVoiceMailPilot`: ", str(err), file=sys.stderr)
            return []

    def listVoiceMailPilot(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listVoiceMailPilot(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listVoiceMailPilot`: ", str(err), file=sys.stderr)
            return []

    def getProcessNode(self, **args):
        try:
            resp = self.axl_service.getProcessNode(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getProcessNode`: ", str(err), file=sys.stderr)
            return []

    def listProcessNode(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listProcessNode(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listProcessNode`: ", str(err), file=sys.stderr)
            return []

    def getCallerFilterList(self, **args):
        try:
            resp = self.axl_service.getCallerFilterList(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCallerFilterList`: ", str(err), file=sys.stderr)
            return []

    def listCallerFilterList(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCallerFilterList(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCallerFilterList`: ", str(err), file=sys.stderr)
            return []

    def getRoutePartition(self, **args):
        try:
            resp = self.axl_service.getRoutePartition(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRoutePartition`: ", str(err), file=sys.stderr)
            return []

    def listRoutePartition(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRoutePartition(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRoutePartition`: ", str(err), file=sys.stderr)
            return []

    def getCss(self, **args):
        try:
            resp = self.axl_service.getCss(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCss`: ", str(err), file=sys.stderr)
            return []

    def listCss(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCss(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCss`: ", str(err), file=sys.stderr)
            return []

    def getCallManager(self, **args):
        try:
            resp = self.axl_service.getCallManager(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCallManager`: ", str(err), file=sys.stderr)
            return []

    def listCallManager(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCallManager(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCallManager`: ", str(err), file=sys.stderr)
            return []

    def getExpresswayCConfiguration(self, **args):
        try:
            resp = self.axl_service.getExpresswayCConfiguration(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getExpresswayCConfiguration`: ", str(err), file=sys.stderr)
            return []

    def listExpresswayCConfiguration(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listExpresswayCConfiguration(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listExpresswayCConfiguration`: ", str(err), file=sys.stderr)
            return []

    def getMedia(self, **args):
        try:
            resp = self.axl_service.getMedia(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMedia`: ", str(err), file=sys.stderr)
            return []

    def listMedia(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMedia(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMedia`: ", str(err), file=sys.stderr)
            return []

    def getRegion(self, **args):
        try:
            resp = self.axl_service.getRegion(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRegion`: ", str(err), file=sys.stderr)
            return []

    def listRegion(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRegion(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRegion`: ", str(err), file=sys.stderr)
            return []

    def getAarGroup(self, **args):
        try:
            resp = self.axl_service.getAarGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getAarGroup`: ", str(err), file=sys.stderr)
            return []

    def listAarGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listAarGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listAarGroup`: ", str(err), file=sys.stderr)
            return []

    def getPhysicalLocation(self, **args):
        try:
            resp = self.axl_service.getPhysicalLocation(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPhysicalLocation`: ", str(err), file=sys.stderr)
            return []

    def listPhysicalLocation(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listPhysicalLocation(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listPhysicalLocation`: ", str(err), file=sys.stderr)
            return []

    def getCustomer(self, **args):
        try:
            resp = self.axl_service.getCustomer(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCustomer`: ", str(err), file=sys.stderr)
            return []

    def listCustomer(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCustomer(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCustomer`: ", str(err), file=sys.stderr)
            return []

    def getRouteGroup(self, **args):
        try:
            resp = self.axl_service.getRouteGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRouteGroup`: ", str(err), file=sys.stderr)
            return []

    def listRouteGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRouteGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRouteGroup`: ", str(err), file=sys.stderr)
            return []

    def getDevicePool(self, **args):
        try:
            resp = self.axl_service.getDevicePool(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDevicePool`: ", str(err), file=sys.stderr)
            return []

    def listDevicePool(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDevicePool(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDevicePool`: ", str(err), file=sys.stderr)
            return []

    def getDeviceMobilityGroup(self, **args):
        try:
            resp = self.axl_service.getDeviceMobilityGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDeviceMobilityGroup`: ", str(err), file=sys.stderr)
            return []

    def listDeviceMobilityGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDeviceMobilityGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDeviceMobilityGroup`: ", str(err), file=sys.stderr)
            return []

    def getLocation(self, **args):
        try:
            resp = self.axl_service.getLocation(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLocation`: ", str(err), file=sys.stderr)
            return []

    def listLocation(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLocation(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLocation`: ", str(err), file=sys.stderr)
            return []

    def getSoftKeyTemplate(self, **args):
        try:
            resp = self.axl_service.getSoftKeyTemplate(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSoftKeyTemplate`: ", str(err), file=sys.stderr)
            return []

    def listSoftKeyTemplate(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSoftKeyTemplate(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSoftKeyTemplate`: ", str(err), file=sys.stderr)
            return []

    def getTranscoder(self, **args):
        try:
            resp = self.axl_service.getTranscoder(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getTranscoder`: ", str(err), file=sys.stderr)
            return []

    def listTranscoder(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listTranscoder(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listTranscoder`: ", str(err), file=sys.stderr)
            return []

    def getCommonDeviceConfig(self, **args):
        try:
            resp = self.axl_service.getCommonDeviceConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCommonDeviceConfig`: ", str(err), file=sys.stderr)
            return []

    def listCommonDeviceConfig(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCommonDeviceConfig(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCommonDeviceConfig`: ", str(err), file=sys.stderr)
            return []

    def getDeviceMobility(self, **args):
        try:
            resp = self.axl_service.getDeviceMobility(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDeviceMobility`: ", str(err), file=sys.stderr)
            return []

    def listDeviceMobility(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDeviceMobility(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDeviceMobility`: ", str(err), file=sys.stderr)
            return []

    def getCmcInfo(self, **args):
        try:
            resp = self.axl_service.getCmcInfo(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCmcInfo`: ", str(err), file=sys.stderr)
            return []

    def listCmcInfo(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCmcInfo(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCmcInfo`: ", str(err), file=sys.stderr)
            return []

    def getCredentialPolicy(self, **args):
        try:
            resp = self.axl_service.getCredentialPolicy(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCredentialPolicy`: ", str(err), file=sys.stderr)
            return []

    def listCredentialPolicy(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCredentialPolicy(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCredentialPolicy`: ", str(err), file=sys.stderr)
            return []

    def getFacInfo(self, **args):
        try:
            resp = self.axl_service.getFacInfo(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getFacInfo`: ", str(err), file=sys.stderr)
            return []

    def listFacInfo(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listFacInfo(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listFacInfo`: ", str(err), file=sys.stderr)
            return []

    def getHuntList(self, **args):
        try:
            resp = self.axl_service.getHuntList(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getHuntList`: ", str(err), file=sys.stderr)
            return []

    def listHuntList(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listHuntList(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listHuntList`: ", str(err), file=sys.stderr)
            return []

    def getIvrUserLocale(self, **args):
        try:
            resp = self.axl_service.getIvrUserLocale(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getIvrUserLocale`: ", str(err), file=sys.stderr)
            return []

    def listIvrUserLocale(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listIvrUserLocale(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listIvrUserLocale`: ", str(err), file=sys.stderr)
            return []

    def getLineGroup(self, **args):
        try:
            resp = self.axl_service.getLineGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLineGroup`: ", str(err), file=sys.stderr)
            return []

    def listLineGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLineGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLineGroup`: ", str(err), file=sys.stderr)
            return []

    def getRecordingProfile(self, **args):
        try:
            resp = self.axl_service.getRecordingProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRecordingProfile`: ", str(err), file=sys.stderr)
            return []

    def listRecordingProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRecordingProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRecordingProfile`: ", str(err), file=sys.stderr)
            return []

    def getRouteFilter(self, **args):
        try:
            resp = self.axl_service.getRouteFilter(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRouteFilter`: ", str(err), file=sys.stderr)
            return []

    def listRouteFilter(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRouteFilter(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRouteFilter`: ", str(err), file=sys.stderr)
            return []

    def getCallManagerGroup(self, **args):
        try:
            resp = self.axl_service.getCallManagerGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCallManagerGroup`: ", str(err), file=sys.stderr)
            return []

    def listCallManagerGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCallManagerGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCallManagerGroup`: ", str(err), file=sys.stderr)
            return []

    def getUserGroup(self, **args):
        try:
            resp = self.axl_service.getUserGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getUserGroup`: ", str(err), file=sys.stderr)
            return []

    def listUserGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUserGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUserGroup`: ", str(err), file=sys.stderr)
            return []

    def getDialPlan(self, **args):
        try:
            resp = self.axl_service.getDialPlan(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDialPlan`: ", str(err), file=sys.stderr)
            return []

    def listDialPlan(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDialPlan(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDialPlan`: ", str(err), file=sys.stderr)
            return []

    def getDialPlanTag(self, **args):
        try:
            resp = self.axl_service.getDialPlanTag(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDialPlanTag`: ", str(err), file=sys.stderr)
            return []

    def listDialPlanTag(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDialPlanTag(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDialPlanTag`: ", str(err), file=sys.stderr)
            return []

    def getDdi(self, **args):
        try:
            resp = self.axl_service.getDdi(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDdi`: ", str(err), file=sys.stderr)
            return []

    def listDdi(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDdi(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDdi`: ", str(err), file=sys.stderr)
            return []

    def getMobileSmartClientProfile(self, **args):
        try:
            resp = self.axl_service.getMobileSmartClientProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMobileSmartClientProfile`: ", str(err), file=sys.stderr)
            return []

    def listMobileSmartClientProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMobileSmartClientProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMobileSmartClientProfile`: ", str(err), file=sys.stderr)
            return []

    def getProcessNodeService(self, **args):
        try:
            resp = self.axl_service.getProcessNodeService(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getProcessNodeService`: ", str(err), file=sys.stderr)
            return []

    def listProcessNodeService(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listProcessNodeService(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listProcessNodeService`: ", str(err), file=sys.stderr)
            return []

    def getMohAudioSource(self, **args):
        try:
            resp = self.axl_service.getMohAudioSource(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMohAudioSource`: ", str(err), file=sys.stderr)
            return []

    def listMohAudioSource(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMohAudioSource(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMohAudioSource`: ", str(err), file=sys.stderr)
            return []

    def getDhcpServer(self, **args):
        try:
            resp = self.axl_service.getDhcpServer(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDhcpServer`: ", str(err), file=sys.stderr)
            return []

    def listDhcpServer(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDhcpServer(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDhcpServer`: ", str(err), file=sys.stderr)
            return []

    def getDhcpSubnet(self, **args):
        try:
            resp = self.axl_service.getDhcpSubnet(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDhcpSubnet`: ", str(err), file=sys.stderr)
            return []

    def listDhcpSubnet(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDhcpSubnet(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDhcpSubnet`: ", str(err), file=sys.stderr)
            return []

    def getCallPark(self, **args):
        try:
            resp = self.axl_service.getCallPark(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCallPark`: ", str(err), file=sys.stderr)
            return []

    def listCallPark(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCallPark(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCallPark`: ", str(err), file=sys.stderr)
            return []

    def getDirectedCallPark(self, **args):
        try:
            resp = self.axl_service.getDirectedCallPark(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDirectedCallPark`: ", str(err), file=sys.stderr)
            return []

    def listDirectedCallPark(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDirectedCallPark(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDirectedCallPark`: ", str(err), file=sys.stderr)
            return []

    def getMeetMe(self, **args):
        try:
            resp = self.axl_service.getMeetMe(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMeetMe`: ", str(err), file=sys.stderr)
            return []

    def listMeetMe(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMeetMe(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMeetMe`: ", str(err), file=sys.stderr)
            return []

    def getConferenceNow(self, **args):
        try:
            resp = self.axl_service.getConferenceNow(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getConferenceNow`: ", str(err), file=sys.stderr)
            return []

    def listConferenceNow(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listConferenceNow(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listConferenceNow`: ", str(err), file=sys.stderr)
            return []

    def getMobileVoiceAccess(self, **args):
        try:
            resp = self.axl_service.getMobileVoiceAccess(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMobileVoiceAccess`: ", str(err), file=sys.stderr)
            return []

    def getRouteList(self, **args):
        try:
            resp = self.axl_service.getRouteList(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRouteList`: ", str(err), file=sys.stderr)
            return []

    def listRouteList(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRouteList(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRouteList`: ", str(err), file=sys.stderr)
            return []

    def getUser(self, **args):
        try:
            resp = self.axl_service.getUser(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getUser`: ", str(err), file=sys.stderr)
            return []

    def listUser(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUser(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUser`: ", str(err), file=sys.stderr)
            return []

    def getAppUser(self, **args):
        try:
            resp = self.axl_service.getAppUser(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getAppUser`: ", str(err), file=sys.stderr)
            return []

    def listAppUser(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listAppUser(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listAppUser`: ", str(err), file=sys.stderr)
            return []

    def getSipRealm(self, **args):
        try:
            resp = self.axl_service.getSipRealm(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSipRealm`: ", str(err), file=sys.stderr)
            return []

    def listSipRealm(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSipRealm(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSipRealm`: ", str(err), file=sys.stderr)
            return []

    def getPhoneNtp(self, **args):
        try:
            resp = self.axl_service.getPhoneNtp(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPhoneNtp`: ", str(err), file=sys.stderr)
            return []

    def listPhoneNtp(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listPhoneNtp(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listPhoneNtp`: ", str(err), file=sys.stderr)
            return []

    def getDateTimeGroup(self, **args):
        try:
            resp = self.axl_service.getDateTimeGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDateTimeGroup`: ", str(err), file=sys.stderr)
            return []

    def listDateTimeGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDateTimeGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDateTimeGroup`: ", str(err), file=sys.stderr)
            return []

    def getPresenceGroup(self, **args):
        try:
            resp = self.axl_service.getPresenceGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPresenceGroup`: ", str(err), file=sys.stderr)
            return []

    def listPresenceGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listPresenceGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listPresenceGroup`: ", str(err), file=sys.stderr)
            return []

    def getGeoLocation(self, **args):
        try:
            resp = self.axl_service.getGeoLocation(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGeoLocation`: ", str(err), file=sys.stderr)
            return []

    def listGeoLocation(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listGeoLocation(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listGeoLocation`: ", str(err), file=sys.stderr)
            return []

    def getSrst(self, **args):
        try:
            resp = self.axl_service.getSrst(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSrst`: ", str(err), file=sys.stderr)
            return []

    def listSrst(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSrst(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSrst`: ", str(err), file=sys.stderr)
            return []

    def getMlppDomain(self, **args):
        try:
            resp = self.axl_service.getMlppDomain(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMlppDomain`: ", str(err), file=sys.stderr)
            return []

    def listMlppDomain(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMlppDomain(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMlppDomain`: ", str(err), file=sys.stderr)
            return []

    def getCumaServerSecurityProfile(self, **args):
        try:
            resp = self.axl_service.getCumaServerSecurityProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCumaServerSecurityProfile`: ", str(err), file=sys.stderr)
            return []

    def listCumaServerSecurityProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCumaServerSecurityProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCumaServerSecurityProfile`: ", str(err), file=sys.stderr)
            return []

    def getApplicationServer(self, **args):
        try:
            resp = self.axl_service.getApplicationServer(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getApplicationServer`: ", str(err), file=sys.stderr)
            return []

    def listApplicationServer(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listApplicationServer(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listApplicationServer`: ", str(err), file=sys.stderr)
            return []

    def getApplicationUserCapfProfile(self, **args):
        try:
            resp = self.axl_service.getApplicationUserCapfProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getApplicationUserCapfProfile`: ", str(err), file=sys.stderr)
            return []

    def listApplicationUserCapfProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listApplicationUserCapfProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listApplicationUserCapfProfile`: ", str(err), file=sys.stderr)
            return []

    def getEndUserCapfProfile(self, **args):
        try:
            resp = self.axl_service.getEndUserCapfProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getEndUserCapfProfile`: ", str(err), file=sys.stderr)
            return []

    def listEndUserCapfProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listEndUserCapfProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listEndUserCapfProfile`: ", str(err), file=sys.stderr)
            return []

    def getServiceParameter(self, **args):
        try:
            resp = self.axl_service.getServiceParameter(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getServiceParameter`: ", str(err), file=sys.stderr)
            return []

    def listServiceParameter(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listServiceParameter(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listServiceParameter`: ", str(err), file=sys.stderr)
            return []

    def getGeoLocationFilter(self, **args):
        try:
            resp = self.axl_service.getGeoLocationFilter(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGeoLocationFilter`: ", str(err), file=sys.stderr)
            return []

    def listGeoLocationFilter(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listGeoLocationFilter(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listGeoLocationFilter`: ", str(err), file=sys.stderr)
            return []

    def getVoiceMailProfile(self, **args):
        try:
            resp = self.axl_service.getVoiceMailProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getVoiceMailProfile`: ", str(err), file=sys.stderr)
            return []

    def listVoiceMailProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listVoiceMailProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listVoiceMailProfile`: ", str(err), file=sys.stderr)
            return []

    def getVoiceMailPort(self, **args):
        try:
            resp = self.axl_service.getVoiceMailPort(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getVoiceMailPort`: ", str(err), file=sys.stderr)
            return []

    def listVoiceMailPort(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listVoiceMailPort(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listVoiceMailPort`: ", str(err), file=sys.stderr)
            return []

    def getGatekeeper(self, **args):
        try:
            resp = self.axl_service.getGatekeeper(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGatekeeper`: ", str(err), file=sys.stderr)
            return []

    def listGatekeeper(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listGatekeeper(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listGatekeeper`: ", str(err), file=sys.stderr)
            return []

    def getPhoneButtonTemplate(self, **args):
        try:
            resp = self.axl_service.getPhoneButtonTemplate(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPhoneButtonTemplate`: ", str(err), file=sys.stderr)
            return []

    def listPhoneButtonTemplate(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listPhoneButtonTemplate(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listPhoneButtonTemplate`: ", str(err), file=sys.stderr)
            return []

    def getCommonPhoneConfig(self, **args):
        try:
            resp = self.axl_service.getCommonPhoneConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCommonPhoneConfig`: ", str(err), file=sys.stderr)
            return []

    def listCommonPhoneConfig(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCommonPhoneConfig(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCommonPhoneConfig`: ", str(err), file=sys.stderr)
            return []

    def getMessageWaiting(self, **args):
        try:
            resp = self.axl_service.getMessageWaiting(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMessageWaiting`: ", str(err), file=sys.stderr)
            return []

    def listMessageWaiting(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMessageWaiting(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMessageWaiting`: ", str(err), file=sys.stderr)
            return []

    def getIpPhoneServices(self, **args):
        try:
            resp = self.axl_service.getIpPhoneServices(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getIpPhoneServices`: ", str(err), file=sys.stderr)
            return []

    def listIpPhoneServices(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listIpPhoneServices(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listIpPhoneServices`: ", str(err), file=sys.stderr)
            return []

    def getCtiRoutePoint(self, **args):
        try:
            resp = self.axl_service.getCtiRoutePoint(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCtiRoutePoint`: ", str(err), file=sys.stderr)
            return []

    def listCtiRoutePoint(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCtiRoutePoint(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCtiRoutePoint`: ", str(err), file=sys.stderr)
            return []

    def getTransPattern(self, **args):
        try:
            resp = self.axl_service.getTransPattern(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getTransPattern`: ", str(err), file=sys.stderr)
            return []

    def listTransPattern(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listTransPattern(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listTransPattern`: ", str(err), file=sys.stderr)
            return []

    def getTransPatternOptions(self, **args):
        try:
            resp = self.axl_service.getTransPatternOptions(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getTransPatternOptions`: ", str(err), file=sys.stderr)
            return []

    def getCallingPartyTransformationPattern(self, **args):
        try:
            resp = self.axl_service.getCallingPartyTransformationPattern(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCallingPartyTransformationPattern`: ", str(err), file=sys.stderr)
            return []

    def listCallingPartyTransformationPattern(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCallingPartyTransformationPattern(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCallingPartyTransformationPattern`: ", str(err), file=sys.stderr)
            return []

    def getSipRoutePattern(self, **args):
        try:
            resp = self.axl_service.getSipRoutePattern(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSipRoutePattern`: ", str(err), file=sys.stderr)
            return []

    def listSipRoutePattern(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSipRoutePattern(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSipRoutePattern`: ", str(err), file=sys.stderr)
            return []

    def getHuntPilot(self, **args):
        try:
            resp = self.axl_service.getHuntPilot(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getHuntPilot`: ", str(err), file=sys.stderr)
            return []

    def listHuntPilot(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listHuntPilot(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listHuntPilot`: ", str(err), file=sys.stderr)
            return []

    def getRoutePattern(self, **args):
        try:
            resp = self.axl_service.getRoutePattern(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRoutePattern`: ", str(err), file=sys.stderr)
            return []

    def listRoutePattern(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRoutePattern(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRoutePattern`: ", str(err), file=sys.stderr)
            return []

    def getApplicationDialRules(self, **args):
        try:
            resp = self.axl_service.getApplicationDialRules(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getApplicationDialRules`: ", str(err), file=sys.stderr)
            return []

    def listApplicationDialRules(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listApplicationDialRules(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listApplicationDialRules`: ", str(err), file=sys.stderr)
            return []

    def getDirectoryLookupDialRules(self, **args):
        try:
            resp = self.axl_service.getDirectoryLookupDialRules(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDirectoryLookupDialRules`: ", str(err), file=sys.stderr)
            return []

    def listDirectoryLookupDialRules(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDirectoryLookupDialRules(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDirectoryLookupDialRules`: ", str(err), file=sys.stderr)
            return []

    def getPhoneSecurityProfile(self, **args):
        try:
            resp = self.axl_service.getPhoneSecurityProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPhoneSecurityProfile`: ", str(err), file=sys.stderr)
            return []

    def listPhoneSecurityProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listPhoneSecurityProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listPhoneSecurityProfile`: ", str(err), file=sys.stderr)
            return []

    def getSipDialRules(self, **args):
        try:
            resp = self.axl_service.getSipDialRules(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSipDialRules`: ", str(err), file=sys.stderr)
            return []

    def listSipDialRules(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSipDialRules(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSipDialRules`: ", str(err), file=sys.stderr)
            return []

    def getConferenceBridge(self, **args):
        try:
            resp = self.axl_service.getConferenceBridge(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getConferenceBridge`: ", str(err), file=sys.stderr)
            return []

    def listConferenceBridge(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listConferenceBridge(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listConferenceBridge`: ", str(err), file=sys.stderr)
            return []

    def getAnnunciator(self, **args):
        try:
            resp = self.axl_service.getAnnunciator(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getAnnunciator`: ", str(err), file=sys.stderr)
            return []

    def listAnnunciator(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listAnnunciator(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listAnnunciator`: ", str(err), file=sys.stderr)
            return []

    def getInteractiveVoice(self, **args):
        try:
            resp = self.axl_service.getInteractiveVoice(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getInteractiveVoice`: ", str(err), file=sys.stderr)
            return []

    def listInteractiveVoice(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listInteractiveVoice(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listInteractiveVoice`: ", str(err), file=sys.stderr)
            return []

    def getMtp(self, **args):
        try:
            resp = self.axl_service.getMtp(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMtp`: ", str(err), file=sys.stderr)
            return []

    def listMtp(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMtp(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMtp`: ", str(err), file=sys.stderr)
            return []

    def getFixedMohAudioSource(self, **args):
        try:
            resp = self.axl_service.getFixedMohAudioSource(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getFixedMohAudioSource`: ", str(err), file=sys.stderr)
            return []

    def getRemoteDestinationProfile(self, **args):
        try:
            resp = self.axl_service.getRemoteDestinationProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRemoteDestinationProfile`: ", str(err), file=sys.stderr)
            return []

    def listRemoteDestinationProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRemoteDestinationProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRemoteDestinationProfile`: ", str(err), file=sys.stderr)
            return []

    def getLine(self, **args):
        try:
            resp = self.axl_service.getLine(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLine`: ", str(err), file=sys.stderr)
            return []

    def listLine(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLine(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLine`: ", str(err), file=sys.stderr)
            return []

    def getLineOptions(self, **args):
        try:
            resp = self.axl_service.getLineOptions(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLineOptions`: ", str(err), file=sys.stderr)
            return []

    def getDefaultDeviceProfile(self, **args):
        try:
            resp = self.axl_service.getDefaultDeviceProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDefaultDeviceProfile`: ", str(err), file=sys.stderr)
            return []

    def listDefaultDeviceProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDefaultDeviceProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDefaultDeviceProfile`: ", str(err), file=sys.stderr)
            return []

    def getH323Phone(self, **args):
        try:
            resp = self.axl_service.getH323Phone(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getH323Phone`: ", str(err), file=sys.stderr)
            return []

    def listH323Phone(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listH323Phone(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listH323Phone`: ", str(err), file=sys.stderr)
            return []

    def getMohServer(self, **args):
        try:
            resp = self.axl_service.getMohServer(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMohServer`: ", str(err), file=sys.stderr)
            return []

    def listMohServer(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMohServer(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMohServer`: ", str(err), file=sys.stderr)
            return []

    def getH323Trunk(self, **args):
        try:
            resp = self.axl_service.getH323Trunk(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getH323Trunk`: ", str(err), file=sys.stderr)
            return []

    def listH323Trunk(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listH323Trunk(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listH323Trunk`: ", str(err), file=sys.stderr)
            return []

    def getPhone(self, **args):
        try:
            resp = self.axl_service.getPhone(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPhone`: ", str(err), file=sys.stderr)
            return []

    def listPhone(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listPhone(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listPhone`: ", str(err), file=sys.stderr)
            return []

    def getPhoneOptions(self, **args):
        try:
            resp = self.axl_service.getPhoneOptions(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPhoneOptions`: ", str(err), file=sys.stderr)
            return []

    def getH323Gateway(self, **args):
        try:
            resp = self.axl_service.getH323Gateway(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getH323Gateway`: ", str(err), file=sys.stderr)
            return []

    def listH323Gateway(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listH323Gateway(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listH323Gateway`: ", str(err), file=sys.stderr)
            return []

    def getDeviceProfile(self, **args):
        try:
            resp = self.axl_service.getDeviceProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDeviceProfile`: ", str(err), file=sys.stderr)
            return []

    def listDeviceProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDeviceProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDeviceProfile`: ", str(err), file=sys.stderr)
            return []

    def getDeviceProfileOptions(self, **args):
        try:
            resp = self.axl_service.getDeviceProfileOptions(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDeviceProfileOptions`: ", str(err), file=sys.stderr)
            return []

    def getRemoteDestination(self, **args):
        try:
            resp = self.axl_service.getRemoteDestination(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRemoteDestination`: ", str(err), file=sys.stderr)
            return []

    def listRemoteDestination(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRemoteDestination(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRemoteDestination`: ", str(err), file=sys.stderr)
            return []

    def getVg224(self, **args):
        try:
            resp = self.axl_service.getVg224(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getVg224`: ", str(err), file=sys.stderr)
            return []

    def getGateway(self, **args):
        try:
            resp = self.axl_service.getGateway(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGateway`: ", str(err), file=sys.stderr)
            return []

    def listGateway(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listGateway(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listGateway`: ", str(err), file=sys.stderr)
            return []

    def getGatewayEndpointAnalogAccess(self, **args):
        try:
            resp = self.axl_service.getGatewayEndpointAnalogAccess(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGatewayEndpointAnalogAccess`: ", str(err), file=sys.stderr)
            return []

    def getGatewayEndpointDigitalAccessPri(self, **args):
        try:
            resp = self.axl_service.getGatewayEndpointDigitalAccessPri(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGatewayEndpointDigitalAccessPri`: ", str(err), file=sys.stderr)
            return []

    def getGatewayEndpointDigitalAccessBri(self, **args):
        try:
            resp = self.axl_service.getGatewayEndpointDigitalAccessBri(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGatewayEndpointDigitalAccessBri`: ", str(err), file=sys.stderr)
            return []

    def getGatewayEndpointDigitalAccessT1(self, **args):
        try:
            resp = self.axl_service.getGatewayEndpointDigitalAccessT1(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGatewayEndpointDigitalAccessT1`: ", str(err), file=sys.stderr)
            return []

    def getCiscoCatalyst600024PortFXSGateway(self, **args):
        try:
            resp = self.axl_service.getCiscoCatalyst600024PortFXSGateway(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCiscoCatalyst600024PortFXSGateway`: ", str(err), file=sys.stderr)
            return []

    def listCiscoCatalyst600024PortFXSGateway(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCiscoCatalyst600024PortFXSGateway(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCiscoCatalyst600024PortFXSGateway`: ", str(err), file=sys.stderr)
            return []

    def getCiscoCatalyst6000E1VoIPGateway(self, **args):
        try:
            resp = self.axl_service.getCiscoCatalyst6000E1VoIPGateway(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCiscoCatalyst6000E1VoIPGateway`: ", str(err), file=sys.stderr)
            return []

    def listCiscoCatalyst6000E1VoIPGateway(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCiscoCatalyst6000E1VoIPGateway(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCiscoCatalyst6000E1VoIPGateway`: ", str(err), file=sys.stderr)
            return []

    def getCiscoCatalyst6000T1VoIPGatewayPri(self, **args):
        try:
            resp = self.axl_service.getCiscoCatalyst6000T1VoIPGatewayPri(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCiscoCatalyst6000T1VoIPGatewayPri`: ", str(err), file=sys.stderr)
            return []

    def listCiscoCatalyst6000T1VoIPGatewayPri(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCiscoCatalyst6000T1VoIPGatewayPri(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCiscoCatalyst6000T1VoIPGatewayPri`: ", str(err), file=sys.stderr)
            return []

    def getCiscoCatalyst6000T1VoIPGatewayT1(self, **args):
        try:
            resp = self.axl_service.getCiscoCatalyst6000T1VoIPGatewayT1(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCiscoCatalyst6000T1VoIPGatewayT1`: ", str(err), file=sys.stderr)
            return []

    def listCiscoCatalyst6000T1VoIPGatewayT1(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCiscoCatalyst6000T1VoIPGatewayT1(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCiscoCatalyst6000T1VoIPGatewayT1`: ", str(err), file=sys.stderr)
            return []

    def getCallPickupGroup(self, **args):
        try:
            resp = self.axl_service.getCallPickupGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCallPickupGroup`: ", str(err), file=sys.stderr)
            return []

    def listCallPickupGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCallPickupGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCallPickupGroup`: ", str(err), file=sys.stderr)
            return []

    def listRoutePlan(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRoutePlan(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRoutePlan`: ", str(err), file=sys.stderr)
            return []

    def getGeoLocationPolicy(self, **args):
        try:
            resp = self.axl_service.getGeoLocationPolicy(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGeoLocationPolicy`: ", str(err), file=sys.stderr)
            return []

    def listGeoLocationPolicy(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listGeoLocationPolicy(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listGeoLocationPolicy`: ", str(err), file=sys.stderr)
            return []

    def getSipTrunk(self, **args):
        try:
            resp = self.axl_service.getSipTrunk(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSipTrunk`: ", str(err), file=sys.stderr)
            return []

    def listSipTrunk(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSipTrunk(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSipTrunk`: ", str(err), file=sys.stderr)
            return []

    def getCalledPartyTransformationPattern(self, **args):
        try:
            resp = self.axl_service.getCalledPartyTransformationPattern(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCalledPartyTransformationPattern`: ", str(err), file=sys.stderr)
            return []

    def listCalledPartyTransformationPattern(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCalledPartyTransformationPattern(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCalledPartyTransformationPattern`: ", str(err), file=sys.stderr)
            return []

    def getExternalCallControlProfile(self, **args):
        try:
            resp = self.axl_service.getExternalCallControlProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getExternalCallControlProfile`: ", str(err), file=sys.stderr)
            return []

    def listExternalCallControlProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listExternalCallControlProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listExternalCallControlProfile`: ", str(err), file=sys.stderr)
            return []

    def getSafSecurityProfile(self, **args):
        try:
            resp = self.axl_service.getSafSecurityProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSafSecurityProfile`: ", str(err), file=sys.stderr)
            return []

    def listSafSecurityProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSafSecurityProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSafSecurityProfile`: ", str(err), file=sys.stderr)
            return []

    def getSafForwarder(self, **args):
        try:
            resp = self.axl_service.getSafForwarder(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSafForwarder`: ", str(err), file=sys.stderr)
            return []

    def listSafForwarder(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSafForwarder(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSafForwarder`: ", str(err), file=sys.stderr)
            return []

    def getCcdHostedDN(self, **args):
        try:
            resp = self.axl_service.getCcdHostedDN(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCcdHostedDN`: ", str(err), file=sys.stderr)
            return []

    def listCcdHostedDN(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCcdHostedDN(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCcdHostedDN`: ", str(err), file=sys.stderr)
            return []

    def getCcdHostedDNGroup(self, **args):
        try:
            resp = self.axl_service.getCcdHostedDNGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCcdHostedDNGroup`: ", str(err), file=sys.stderr)
            return []

    def listCcdHostedDNGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCcdHostedDNGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCcdHostedDNGroup`: ", str(err), file=sys.stderr)
            return []

    def getCcdRequestingService(self, **args):
        try:
            resp = self.axl_service.getCcdRequestingService(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCcdRequestingService`: ", str(err), file=sys.stderr)
            return []

    def getInterClusterServiceProfile(self, **args):
        try:
            resp = self.axl_service.getInterClusterServiceProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getInterClusterServiceProfile`: ", str(err), file=sys.stderr)
            return []

    def getRemoteCluster(self, **args):
        try:
            resp = self.axl_service.getRemoteCluster(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRemoteCluster`: ", str(err), file=sys.stderr)
            return []

    def listRemoteCluster(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRemoteCluster(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRemoteCluster`: ", str(err), file=sys.stderr)
            return []

    def getCcdAdvertisingService(self, **args):
        try:
            resp = self.axl_service.getCcdAdvertisingService(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCcdAdvertisingService`: ", str(err), file=sys.stderr)
            return []

    def listCcdAdvertisingService(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCcdAdvertisingService(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCcdAdvertisingService`: ", str(err), file=sys.stderr)
            return []

    def getLdapDirectory(self, **args):
        try:
            resp = self.axl_service.getLdapDirectory(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLdapDirectory`: ", str(err), file=sys.stderr)
            return []

    def listLdapDirectory(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLdapDirectory(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLdapDirectory`: ", str(err), file=sys.stderr)
            return []

    def getEmccFeatureConfig(self, **args):
        try:
            resp = self.axl_service.getEmccFeatureConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getEmccFeatureConfig`: ", str(err), file=sys.stderr)
            return []

    def getSafCcdPurgeBlockLearnedRoutes(self, **args):
        try:
            resp = self.axl_service.getSafCcdPurgeBlockLearnedRoutes(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSafCcdPurgeBlockLearnedRoutes`: ", str(err), file=sys.stderr)
            return []

    def listSafCcdPurgeBlockLearnedRoutes(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSafCcdPurgeBlockLearnedRoutes(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSafCcdPurgeBlockLearnedRoutes`: ", str(err), file=sys.stderr)
            return []

    def getVpnGateway(self, **args):
        try:
            resp = self.axl_service.getVpnGateway(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getVpnGateway`: ", str(err), file=sys.stderr)
            return []

    def listVpnGateway(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listVpnGateway(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listVpnGateway`: ", str(err), file=sys.stderr)
            return []

    def getVpnGroup(self, **args):
        try:
            resp = self.axl_service.getVpnGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getVpnGroup`: ", str(err), file=sys.stderr)
            return []

    def listVpnGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listVpnGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listVpnGroup`: ", str(err), file=sys.stderr)
            return []

    def getVpnProfile(self, **args):
        try:
            resp = self.axl_service.getVpnProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getVpnProfile`: ", str(err), file=sys.stderr)
            return []

    def listVpnProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listVpnProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listVpnProfile`: ", str(err), file=sys.stderr)
            return []

    def getImeServer(self, **args):
        try:
            resp = self.axl_service.getImeServer(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeServer`: ", str(err), file=sys.stderr)
            return []

    def listImeServer(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeServer(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeServer`: ", str(err), file=sys.stderr)
            return []

    def getImeRouteFilterGroup(self, **args):
        try:
            resp = self.axl_service.getImeRouteFilterGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeRouteFilterGroup`: ", str(err), file=sys.stderr)
            return []

    def listImeRouteFilterGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeRouteFilterGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeRouteFilterGroup`: ", str(err), file=sys.stderr)
            return []

    def getImeRouteFilterElement(self, **args):
        try:
            resp = self.axl_service.getImeRouteFilterElement(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeRouteFilterElement`: ", str(err), file=sys.stderr)
            return []

    def listImeRouteFilterElement(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeRouteFilterElement(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeRouteFilterElement`: ", str(err), file=sys.stderr)
            return []

    def getImeClient(self, **args):
        try:
            resp = self.axl_service.getImeClient(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeClient`: ", str(err), file=sys.stderr)
            return []

    def listImeClient(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeClient(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeClient`: ", str(err), file=sys.stderr)
            return []

    def getImeEnrolledPattern(self, **args):
        try:
            resp = self.axl_service.getImeEnrolledPattern(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeEnrolledPattern`: ", str(err), file=sys.stderr)
            return []

    def listImeEnrolledPattern(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeEnrolledPattern(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeEnrolledPattern`: ", str(err), file=sys.stderr)
            return []

    def getImeEnrolledPatternGroup(self, **args):
        try:
            resp = self.axl_service.getImeEnrolledPatternGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeEnrolledPatternGroup`: ", str(err), file=sys.stderr)
            return []

    def listImeEnrolledPatternGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeEnrolledPatternGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeEnrolledPatternGroup`: ", str(err), file=sys.stderr)
            return []

    def getImeExclusionNumber(self, **args):
        try:
            resp = self.axl_service.getImeExclusionNumber(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeExclusionNumber`: ", str(err), file=sys.stderr)
            return []

    def listImeExclusionNumber(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeExclusionNumber(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeExclusionNumber`: ", str(err), file=sys.stderr)
            return []

    def getImeExclusionNumberGroup(self, **args):
        try:
            resp = self.axl_service.getImeExclusionNumberGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeExclusionNumberGroup`: ", str(err), file=sys.stderr)
            return []

    def listImeExclusionNumberGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeExclusionNumberGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeExclusionNumberGroup`: ", str(err), file=sys.stderr)
            return []

    def getImeFirewall(self, **args):
        try:
            resp = self.axl_service.getImeFirewall(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeFirewall`: ", str(err), file=sys.stderr)
            return []

    def listImeFirewall(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeFirewall(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeFirewall`: ", str(err), file=sys.stderr)
            return []

    def getImeE164Transformation(self, **args):
        try:
            resp = self.axl_service.getImeE164Transformation(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeE164Transformation`: ", str(err), file=sys.stderr)
            return []

    def listImeE164Transformation(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImeE164Transformation(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImeE164Transformation`: ", str(err), file=sys.stderr)
            return []

    def getTransformationProfile(self, **args):
        try:
            resp = self.axl_service.getTransformationProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getTransformationProfile`: ", str(err), file=sys.stderr)
            return []

    def listTransformationProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listTransformationProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listTransformationProfile`: ", str(err), file=sys.stderr)
            return []

    def getFallbackProfile(self, **args):
        try:
            resp = self.axl_service.getFallbackProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getFallbackProfile`: ", str(err), file=sys.stderr)
            return []

    def listFallbackProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listFallbackProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listFallbackProfile`: ", str(err), file=sys.stderr)
            return []

    def getLdapFilter(self, **args):
        try:
            resp = self.axl_service.getLdapFilter(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLdapFilter`: ", str(err), file=sys.stderr)
            return []

    def listLdapFilter(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLdapFilter(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLdapFilter`: ", str(err), file=sys.stderr)
            return []

    def getTvsCertificate(self, **args):
        try:
            resp = self.axl_service.getTvsCertificate(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getTvsCertificate`: ", str(err), file=sys.stderr)
            return []

    def listTvsCertificate(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listTvsCertificate(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listTvsCertificate`: ", str(err), file=sys.stderr)
            return []

    def getFeatureControlPolicy(self, **args):
        try:
            resp = self.axl_service.getFeatureControlPolicy(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getFeatureControlPolicy`: ", str(err), file=sys.stderr)
            return []

    def listFeatureControlPolicy(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listFeatureControlPolicy(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listFeatureControlPolicy`: ", str(err), file=sys.stderr)
            return []

    def getMobilityProfile(self, **args):
        try:
            resp = self.axl_service.getMobilityProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMobilityProfile`: ", str(err), file=sys.stderr)
            return []

    def listMobilityProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMobilityProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMobilityProfile`: ", str(err), file=sys.stderr)
            return []

    def getEnterpriseFeatureAccessConfiguration(self, **args):
        try:
            resp = self.axl_service.getEnterpriseFeatureAccessConfiguration(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getEnterpriseFeatureAccessConfiguration`: ", str(err), file=sys.stderr)
            return []

    def listEnterpriseFeatureAccessConfiguration(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listEnterpriseFeatureAccessConfiguration(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listEnterpriseFeatureAccessConfiguration`: ", str(err), file=sys.stderr)
            return []

    def getHandoffConfiguration(self, **args):
        try:
            resp = self.axl_service.getHandoffConfiguration(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getHandoffConfiguration`: ", str(err), file=sys.stderr)
            return []

    def listCalledPartyTracing(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCalledPartyTracing(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCalledPartyTracing`: ", str(err), file=sys.stderr)
            return []

    def getSIPNormalizationScript(self, **args):
        try:
            resp = self.axl_service.getSIPNormalizationScript(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSIPNormalizationScript`: ", str(err), file=sys.stderr)
            return []

    def listSIPNormalizationScript(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSIPNormalizationScript(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSIPNormalizationScript`: ", str(err), file=sys.stderr)
            return []

    def getCustomUserField(self, **args):
        try:
            resp = self.axl_service.getCustomUserField(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCustomUserField`: ", str(err), file=sys.stderr)
            return []

    def listCustomUserField(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCustomUserField(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCustomUserField`: ", str(err), file=sys.stderr)
            return []

    def getGatewaySccpEndpoints(self, **args):
        try:
            resp = self.axl_service.getGatewaySccpEndpoints(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getGatewaySccpEndpoints`: ", str(err), file=sys.stderr)
            return []

    def listBillingServer(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listBillingServer(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listBillingServer`: ", str(err), file=sys.stderr)
            return []

    def getLbmGroup(self, **args):
        try:
            resp = self.axl_service.getLbmGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLbmGroup`: ", str(err), file=sys.stderr)
            return []

    def listLbmGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLbmGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLbmGroup`: ", str(err), file=sys.stderr)
            return []

    def getAnnouncement(self, **args):
        try:
            resp = self.axl_service.getAnnouncement(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getAnnouncement`: ", str(err), file=sys.stderr)
            return []

    def listAnnouncement(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listAnnouncement(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listAnnouncement`: ", str(err), file=sys.stderr)
            return []

    def getServiceProfile(self, **args):
        try:
            resp = self.axl_service.getServiceProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getServiceProfile`: ", str(err), file=sys.stderr)
            return []

    def listServiceProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listServiceProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listServiceProfile`: ", str(err), file=sys.stderr)
            return []

    def getLdapSyncCustomField(self, **args):
        try:
            resp = self.axl_service.getLdapSyncCustomField(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLdapSyncCustomField`: ", str(err), file=sys.stderr)
            return []

    def getAudioCodecPreferenceList(self, **args):
        try:
            resp = self.axl_service.getAudioCodecPreferenceList(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getAudioCodecPreferenceList`: ", str(err), file=sys.stderr)
            return []

    def listAudioCodecPreferenceList(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listAudioCodecPreferenceList(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listAudioCodecPreferenceList`: ", str(err), file=sys.stderr)
            return []

    def getUcService(self, **args):
        try:
            resp = self.axl_service.getUcService(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getUcService`: ", str(err), file=sys.stderr)
            return []

    def listUcService(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUcService(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUcService`: ", str(err), file=sys.stderr)
            return []

    def getLbmHubGroup(self, **args):
        try:
            resp = self.axl_service.getLbmHubGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLbmHubGroup`: ", str(err), file=sys.stderr)
            return []

    def listLbmHubGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLbmHubGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLbmHubGroup`: ", str(err), file=sys.stderr)
            return []

    def getImportedDirectoryUriCatalogs(self, **args):
        try:
            resp = self.axl_service.getImportedDirectoryUriCatalogs(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImportedDirectoryUriCatalogs`: ", str(err), file=sys.stderr)
            return []

    def listImportedDirectoryUriCatalogs(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listImportedDirectoryUriCatalogs(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listImportedDirectoryUriCatalogs`: ", str(err), file=sys.stderr)
            return []

    def getVohServer(self, **args):
        try:
            resp = self.axl_service.getVohServer(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getVohServer`: ", str(err), file=sys.stderr)
            return []

    def listVohServer(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listVohServer(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listVohServer`: ", str(err), file=sys.stderr)
            return []

    def getSdpTransparencyProfile(self, **args):
        try:
            resp = self.axl_service.getSdpTransparencyProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSdpTransparencyProfile`: ", str(err), file=sys.stderr)
            return []

    def listSdpTransparencyProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listSdpTransparencyProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listSdpTransparencyProfile`: ", str(err), file=sys.stderr)
            return []

    def getFeatureGroupTemplate(self, **args):
        try:
            resp = self.axl_service.getFeatureGroupTemplate(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getFeatureGroupTemplate`: ", str(err), file=sys.stderr)
            return []

    def listFeatureGroupTemplate(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listFeatureGroupTemplate(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listFeatureGroupTemplate`: ", str(err), file=sys.stderr)
            return []

    def getDirNumberAliasLookupandSync(self, **args):
        try:
            resp = self.axl_service.getDirNumberAliasLookupandSync(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDirNumberAliasLookupandSync`: ", str(err), file=sys.stderr)
            return []

    def listDirNumberAliasLookupandSync(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDirNumberAliasLookupandSync(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDirNumberAliasLookupandSync`: ", str(err), file=sys.stderr)
            return []

    def getLocalRouteGroup(self, **args):
        try:
            resp = self.axl_service.getLocalRouteGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLocalRouteGroup`: ", str(err), file=sys.stderr)
            return []

    def listLocalRouteGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLocalRouteGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLocalRouteGroup`: ", str(err), file=sys.stderr)
            return []

    def getAdvertisedPatterns(self, **args):
        try:
            resp = self.axl_service.getAdvertisedPatterns(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getAdvertisedPatterns`: ", str(err), file=sys.stderr)
            return []

    def listAdvertisedPatterns(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listAdvertisedPatterns(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listAdvertisedPatterns`: ", str(err), file=sys.stderr)
            return []

    def getBlockedLearnedPatterns(self, **args):
        try:
            resp = self.axl_service.getBlockedLearnedPatterns(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getBlockedLearnedPatterns`: ", str(err), file=sys.stderr)
            return []

    def listBlockedLearnedPatterns(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listBlockedLearnedPatterns(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listBlockedLearnedPatterns`: ", str(err), file=sys.stderr)
            return []

    def getCCAProfiles(self, **args):
        try:
            resp = self.axl_service.getCCAProfiles(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCCAProfiles`: ", str(err), file=sys.stderr)
            return []

    def listCCAProfiles(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCCAProfiles(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCCAProfiles`: ", str(err), file=sys.stderr)
            return []

    def getUniversalDeviceTemplate(self, **args):
        try:
            resp = self.axl_service.getUniversalDeviceTemplate(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getUniversalDeviceTemplate`: ", str(err), file=sys.stderr)
            return []

    def listUniversalDeviceTemplate(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUniversalDeviceTemplate(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUniversalDeviceTemplate`: ", str(err), file=sys.stderr)
            return []

    def getUserProfileProvision(self, **args):
        try:
            resp = self.axl_service.getUserProfileProvision(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getUserProfileProvision`: ", str(err), file=sys.stderr)
            return []

    def listUserProfileProvision(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUserProfileProvision(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUserProfileProvision`: ", str(err), file=sys.stderr)
            return []

    def getPresenceRedundancyGroup(self, **args):
        try:
            resp = self.axl_service.getPresenceRedundancyGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPresenceRedundancyGroup`: ", str(err), file=sys.stderr)
            return []

    def listPresenceRedundancyGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listPresenceRedundancyGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listPresenceRedundancyGroup`: ", str(err), file=sys.stderr)
            return []

    def listAssignedPresenceServers(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listAssignedPresenceServers(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listAssignedPresenceServers`: ", str(err), file=sys.stderr)
            return []

    def listUnassignedPresenceServers(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUnassignedPresenceServers(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUnassignedPresenceServers`: ", str(err), file=sys.stderr)
            return []

    def listAssignedPresenceUsers(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listAssignedPresenceUsers(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listAssignedPresenceUsers`: ", str(err), file=sys.stderr)
            return []

    def listUnassignedPresenceUsers(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUnassignedPresenceUsers(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUnassignedPresenceUsers`: ", str(err), file=sys.stderr)
            return []

    def getWifiHotspot(self, **args):
        try:
            resp = self.axl_service.getWifiHotspot(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getWifiHotspot`: ", str(err), file=sys.stderr)
            return []

    def listWifiHotspot(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listWifiHotspot(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listWifiHotspot`: ", str(err), file=sys.stderr)
            return []

    def getWlanProfileGroup(self, **args):
        try:
            resp = self.axl_service.getWlanProfileGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getWlanProfileGroup`: ", str(err), file=sys.stderr)
            return []

    def listWlanProfileGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listWlanProfileGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listWlanProfileGroup`: ", str(err), file=sys.stderr)
            return []

    def getWLANProfile(self, **args):
        try:
            resp = self.axl_service.getWLANProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getWLANProfile`: ", str(err), file=sys.stderr)
            return []

    def listWLANProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listWLANProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listWLANProfile`: ", str(err), file=sys.stderr)
            return []

    def getUniversalLineTemplate(self, **args):
        try:
            resp = self.axl_service.getUniversalLineTemplate(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getUniversalLineTemplate`: ", str(err), file=sys.stderr)
            return []

    def listUniversalLineTemplate(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUniversalLineTemplate(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUniversalLineTemplate`: ", str(err), file=sys.stderr)
            return []

    def getNetworkAccessProfile(self, **args):
        try:
            resp = self.axl_service.getNetworkAccessProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getNetworkAccessProfile`: ", str(err), file=sys.stderr)
            return []

    def listNetworkAccessProfile(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listNetworkAccessProfile(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listNetworkAccessProfile`: ", str(err), file=sys.stderr)
            return []

    def getLicensedUser(self, **args):
        try:
            resp = self.axl_service.getLicensedUser(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLicensedUser`: ", str(err), file=sys.stderr)
            return []

    def listLicensedUser(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLicensedUser(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLicensedUser`: ", str(err), file=sys.stderr)
            return []

    def getHttpProfile(self, **args):
        try:
            resp = self.axl_service.getHttpProfile(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getHttpProfile`: ", str(err), file=sys.stderr)
            return []

    def getElinGroup(self, **args):
        try:
            resp = self.axl_service.getElinGroup(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getElinGroup`: ", str(err), file=sys.stderr)
            return []

    def listElinGroup(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listElinGroup(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listElinGroup`: ", str(err), file=sys.stderr)
            return []

    def getSecureConfig(self, **args):
        try:
            resp = self.axl_service.getSecureConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSecureConfig`: ", str(err), file=sys.stderr)
            return []

    def listUnassignedDevice(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listUnassignedDevice(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listUnassignedDevice`: ", str(err), file=sys.stderr)
            return []

    def getRegistrationDynamic(self, **args):
        try:
            resp = self.axl_service.getRegistrationDynamic(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getRegistrationDynamic`: ", str(err), file=sys.stderr)
            return []

    def listRegistrationDynamic(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listRegistrationDynamic(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listRegistrationDynamic`: ", str(err), file=sys.stderr)
            return []

    def getInfrastructureDevice(self, **args):
        try:
            resp = self.axl_service.getInfrastructureDevice(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getInfrastructureDevice`: ", str(err), file=sys.stderr)
            return []

    def listInfrastructureDevice(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listInfrastructureDevice(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listInfrastructureDevice`: ", str(err), file=sys.stderr)
            return []

    def getLdapSearch(self, **args):
        try:
            resp = self.axl_service.getLdapSearch(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLdapSearch`: ", str(err), file=sys.stderr)
            return []

    def listLdapSearch(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLdapSearch(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLdapSearch`: ", str(err), file=sys.stderr)
            return []

    def getWirelessAccessPointControllers(self, **args):
        try:
            resp = self.axl_service.getWirelessAccessPointControllers(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getWirelessAccessPointControllers`: ", str(err), file=sys.stderr)
            return []

    def listWirelessAccessPointControllers(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listWirelessAccessPointControllers(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listWirelessAccessPointControllers`: ", str(err), file=sys.stderr)
            return []

    def listPhoneActivationCode(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listPhoneActivationCode(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listPhoneActivationCode`: ", str(err), file=sys.stderr)
            return []

    def getDeviceDefaults(self, **args):
        try:
            resp = self.axl_service.getDeviceDefaults(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getDeviceDefaults`: ", str(err), file=sys.stderr)
            return []

    def listDeviceDefaults(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listDeviceDefaults(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listDeviceDefaults`: ", str(err), file=sys.stderr)
            return []

    def getMraServiceDomain(self, **args):
        try:
            resp = self.axl_service.getMraServiceDomain(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMraServiceDomain`: ", str(err), file=sys.stderr)
            return []

    def listMraServiceDomain(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listMraServiceDomain(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listMraServiceDomain`: ", str(err), file=sys.stderr)
            return []

    def listCiscoCloudOnboarding(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listCiscoCloudOnboarding(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listCiscoCloudOnboarding`: ", str(err), file=sys.stderr)
            return []

    def executeSQLQuery(self, **args):
        try:
            resp = self.axl_service.executeSQLQuery(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `executeSQLQuery`: ", str(err), file=sys.stderr)
            return []

    def executeSQLQueryInactive(self, **args):
        try:
            resp = self.axl_service.executeSQLQueryInactive(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `executeSQLQueryInactive`: ", str(err), file=sys.stderr)
            return []

    def executeSQLUpdate(self, **args):
        try:
            resp = self.axl_service.executeSQLUpdate(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `executeSQLUpdate`: ", str(err), file=sys.stderr)
            return []

    def doAuthenticateUser(self, **args):
        try:
            resp = self.axl_service.doAuthenticateUser(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `doAuthenticateUser`: ", str(err), file=sys.stderr)
            return []

    def getOSVersion(self, **args):
        try:
            resp = self.axl_service.getOSVersion(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getOSVersion`: ", str(err), file=sys.stderr)
            return []

    def getMobility(self, **args):
        try:
            resp = self.axl_service.getMobility(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getMobility`: ", str(err), file=sys.stderr)
            return []

    def getEnterprisePhoneConfig(self, **args):
        try:
            resp = self.axl_service.getEnterprisePhoneConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getEnterprisePhoneConfig`: ", str(err), file=sys.stderr)
            return []

    def getLdapSystem(self, **args):
        try:
            resp = self.axl_service.getLdapSystem(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLdapSystem`: ", str(err), file=sys.stderr)
            return []

    def getLdapAuthentication(self, **args):
        try:
            resp = self.axl_service.getLdapAuthentication(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getLdapAuthentication`: ", str(err), file=sys.stderr)
            return []

    def getCCMVersion(self, **args):
        try:
            resp = self.axl_service.getCCMVersion(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCCMVersion`: ", str(err), file=sys.stderr)
            return []

    def getFallbackFeatureConfig(self, **args):
        try:
            resp = self.axl_service.getFallbackFeatureConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getFallbackFeatureConfig`: ", str(err), file=sys.stderr)
            return []

    def getImeLearnedRoutes(self, **args):
        try:
            resp = self.axl_service.getImeLearnedRoutes(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeLearnedRoutes`: ", str(err), file=sys.stderr)
            return []

    def getImeFeatureConfig(self, **args):
        try:
            resp = self.axl_service.getImeFeatureConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getImeFeatureConfig`: ", str(err), file=sys.stderr)
            return []

    def getAppServerInfo(self, **args):
        try:
            resp = self.axl_service.getAppServerInfo(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getAppServerInfo`: ", str(err), file=sys.stderr)
            return []

    def getSoftKeySet(self, **args):
        try:
            resp = self.axl_service.getSoftKeySet(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSoftKeySet`: ", str(err), file=sys.stderr)
            return []

    def getSyslogConfiguration(self, **args):
        try:
            resp = self.axl_service.getSyslogConfiguration(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSyslogConfiguration`: ", str(err), file=sys.stderr)
            return []

    def listLdapSyncCustomField(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listLdapSyncCustomField(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listLdapSyncCustomField`: ", str(err), file=sys.stderr)
            return []

    def getIlsConfig(self, **args):
        try:
            resp = self.axl_service.getIlsConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getIlsConfig`: ", str(err), file=sys.stderr)
            return []

    def getSNMPCommunityString(self, **args):
        try:
            resp = self.axl_service.getSNMPCommunityString(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSNMPCommunityString`: ", str(err), file=sys.stderr)
            return []

    def getSNMPUser(self, **args):
        try:
            resp = self.axl_service.getSNMPUser(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSNMPUser`: ", str(err), file=sys.stderr)
            return []

    def getSNMPMIB2List(self, **args):
        try:
            resp = self.axl_service.getSNMPMIB2List(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSNMPMIB2List`: ", str(err), file=sys.stderr)
            return []

    def getBillingServer(self, **args):
        try:
            resp = self.axl_service.getBillingServer(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getBillingServer`: ", str(err), file=sys.stderr)
            return []

    def getCcdFeatureConfig(self, **args):
        try:
            resp = self.axl_service.getCcdFeatureConfig(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCcdFeatureConfig`: ", str(err), file=sys.stderr)
            return []

    def getPageLayoutPreferences(self, **args):
        try:
            resp = self.axl_service.getPageLayoutPreferences(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getPageLayoutPreferences`: ", str(err), file=sys.stderr)
            return []

    def getCredentialPolicyDefault(self, **args):
        try:
            resp = self.axl_service.getCredentialPolicyDefault(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getCredentialPolicyDefault`: ", str(err), file=sys.stderr)
            return []

    def listChange(self, searchCriteria={}, returnedTags=[]):
        try:
            resp = self.axl_service.listChange(searchCriteria=searchCriteria, returnedTags=returnedTags)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `listChange`: ", str(err), file=sys.stderr)
            return []

    def getSmartLicenseStatus(self, **args):
        try:
            resp = self.axl_service.getSmartLicenseStatus(**args)
            if resp['return']:
                soap_result = self.elements_to_dict(serialize_object(resp['return'], dict))

                while isinstance(soap_result, dict) and len(soap_result) == 1:
                    soap_result = soap_result[list(soap_result.keys())[0]]

                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return [True]

        except Exception as err:
            print(f"AXL error `getSmartLicenseStatus`: ", str(err), file=sys.stderr)
            return []

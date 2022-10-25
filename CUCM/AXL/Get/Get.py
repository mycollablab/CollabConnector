from zeep.helpers import serialize_object
from zeep.exceptions import Fault
import sys


class Get:
    def __init__(self, soap_client):
        self.client = soap_client

    def SipProfile(self, **args):
        """
        axl.get.GetSipProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSipProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sipProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSipProfile: ", str(err), file=sys.stderr)
            return False
        

    def SipProfileOptions(self, **args):
        """
        axl.get.GetSipProfileOptions parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSipProfileOptions(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sipProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSipProfileOptions: ", str(err), file=sys.stderr)
            return False
        

    def SipTrunkSecurityProfile(self, **args):
        """
        axl.get.GetSipTrunkSecurityProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSipTrunkSecurityProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sipTrunkSecurityProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSipTrunkSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def TimePeriod(self, **args):
        """
        axl.get.GetTimePeriod parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getTimePeriod(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['timePeriod']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getTimePeriod: ", str(err), file=sys.stderr)
            return False
        

    def TimeSchedule(self, **args):
        """
        axl.get.GetTimeSchedule parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getTimeSchedule(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['timeSchedule']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getTimeSchedule: ", str(err), file=sys.stderr)
            return False
        

    def TodAccess(self, **args):
        """
        axl.get.GetTodAccess parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getTodAccess(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['todAccess']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getTodAccess: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailPilot(self, **args):
        """
        axl.get.GetVoiceMailPilot parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getVoiceMailPilot(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['voiceMailPilot']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getVoiceMailPilot: ", str(err), file=sys.stderr)
            return False
        

    def ProcessNode(self, **args):
        """
        axl.get.GetProcessNode parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getProcessNode(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['processNode']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getProcessNode: ", str(err), file=sys.stderr)
            return False
        

    def CallerFilterList(self, **args):
        """
        axl.get.GetCallerFilterList parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCallerFilterList(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['callerFilterList']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCallerFilterList: ", str(err), file=sys.stderr)
            return False
        

    def RoutePartition(self, **args):
        """
        axl.get.GetRoutePartition parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRoutePartition(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['routePartition']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRoutePartition: ", str(err), file=sys.stderr)
            return False
        

    def Css(self, **args):
        """
        axl.get.GetCss parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCss(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['css']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCss: ", str(err), file=sys.stderr)
            return False
        

    def CallManager(self, **args):
        """
        axl.get.GetCallManager parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCallManager(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['callManager']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCallManager: ", str(err), file=sys.stderr)
            return False
        

    def ExpresswayCConfiguration(self, **args):
        """
        axl.get.GetExpresswayCConfiguration parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getExpresswayCConfiguration(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['expresswayCConfiguration']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getExpresswayCConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def Media(self, **args):
        """
        axl.get.GetMedia parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMedia(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mediaResourceGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMedia: ", str(err), file=sys.stderr)
            return False
        

    def Media(self, **args):
        """
        axl.get.GetMedia parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMedia(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mediaResourceList']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMedia: ", str(err), file=sys.stderr)
            return False
        

    def Region(self, **args):
        """
        axl.get.GetRegion parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRegion(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['region']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRegion: ", str(err), file=sys.stderr)
            return False
        

    def AarGroup(self, **args):
        """
        axl.get.GetAarGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getAarGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['aarGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getAarGroup: ", str(err), file=sys.stderr)
            return False
        

    def PhysicalLocation(self, **args):
        """
        axl.get.GetPhysicalLocation parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPhysicalLocation(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['physicalLocation']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPhysicalLocation: ", str(err), file=sys.stderr)
            return False
        

    def Customer(self, **args):
        """
        axl.get.GetCustomer parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCustomer(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['customer']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCustomer: ", str(err), file=sys.stderr)
            return False
        

    def RouteGroup(self, **args):
        """
        axl.get.GetRouteGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRouteGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['routeGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRouteGroup: ", str(err), file=sys.stderr)
            return False
        

    def DevicePool(self, **args):
        """
        axl.get.GetDevicePool parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDevicePool(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['devicePool']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDevicePool: ", str(err), file=sys.stderr)
            return False
        

    def DeviceMobilityGroup(self, **args):
        """
        axl.get.GetDeviceMobilityGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDeviceMobilityGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['deviceMobilityGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDeviceMobilityGroup: ", str(err), file=sys.stderr)
            return False
        

    def Location(self, **args):
        """
        axl.get.GetLocation parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLocation(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['location']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLocation: ", str(err), file=sys.stderr)
            return False
        

    def SoftKeyTemplate(self, **args):
        """
        axl.get.GetSoftKeyTemplate parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSoftKeyTemplate(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['softKeyTemplate']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSoftKeyTemplate: ", str(err), file=sys.stderr)
            return False
        

    def Transcoder(self, **args):
        """
        axl.get.GetTranscoder parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getTranscoder(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['transcoder']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getTranscoder: ", str(err), file=sys.stderr)
            return False
        

    def CommonDeviceConfig(self, **args):
        """
        axl.get.GetCommonDeviceConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCommonDeviceConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['commonDeviceConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCommonDeviceConfig: ", str(err), file=sys.stderr)
            return False
        

    def resourcePriorityNamespace(self, **args):
        """
        axl.get.Get parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.get(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['resourcePriorityNamespace']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error get: ", str(err), file=sys.stderr)
            return False
        

    def resourcePriorityNamespaceList(self, **args):
        """
        axl.get.Get parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.get(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['resourcePriorityNamespaceList']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error get: ", str(err), file=sys.stderr)
            return False
        

    def DeviceMobility(self, **args):
        """
        axl.get.GetDeviceMobility parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDeviceMobility(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['deviceMobility']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDeviceMobility: ", str(err), file=sys.stderr)
            return False
        

    def CmcInfo(self, **args):
        """
        axl.get.GetCmcInfo parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCmcInfo(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['cmcInfo']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCmcInfo: ", str(err), file=sys.stderr)
            return False
        

    def CredentialPolicy(self, **args):
        """
        axl.get.GetCredentialPolicy parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCredentialPolicy(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['credentialPolicy']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCredentialPolicy: ", str(err), file=sys.stderr)
            return False
        

    def FacInfo(self, **args):
        """
        axl.get.GetFacInfo parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getFacInfo(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['facInfo']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getFacInfo: ", str(err), file=sys.stderr)
            return False
        

    def HuntList(self, **args):
        """
        axl.get.GetHuntList parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getHuntList(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['huntList']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getHuntList: ", str(err), file=sys.stderr)
            return False
        

    def IvrUserLocale(self, **args):
        """
        axl.get.GetIvrUserLocale parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getIvrUserLocale(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ivrUserLocale']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getIvrUserLocale: ", str(err), file=sys.stderr)
            return False
        

    def LineGroup(self, **args):
        """
        axl.get.GetLineGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLineGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['lineGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLineGroup: ", str(err), file=sys.stderr)
            return False
        

    def RecordingProfile(self, **args):
        """
        axl.get.GetRecordingProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRecordingProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['recordingProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRecordingProfile: ", str(err), file=sys.stderr)
            return False
        

    def RouteFilter(self, **args):
        """
        axl.get.GetRouteFilter parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRouteFilter(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['routeFilter']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRouteFilter: ", str(err), file=sys.stderr)
            return False
        

    def CallManagerGroup(self, **args):
        """
        axl.get.GetCallManagerGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCallManagerGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['callManagerGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCallManagerGroup: ", str(err), file=sys.stderr)
            return False
        

    def UserGroup(self, **args):
        """
        axl.get.GetUserGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getUserGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['userGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getUserGroup: ", str(err), file=sys.stderr)
            return False
        

    def DialPlan(self, **args):
        """
        axl.get.GetDialPlan parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDialPlan(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['dialPlan']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDialPlan: ", str(err), file=sys.stderr)
            return False
        

    def DialPlanTag(self, **args):
        """
        axl.get.GetDialPlanTag parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDialPlanTag(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['dialPlanTag']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDialPlanTag: ", str(err), file=sys.stderr)
            return False
        

    def Ddi(self, **args):
        """
        axl.get.GetDdi parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDdi(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ddi']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDdi: ", str(err), file=sys.stderr)
            return False
        

    def MobileSmartClientProfile(self, **args):
        """
        axl.get.GetMobileSmartClientProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMobileSmartClientProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mobileSmartClientProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMobileSmartClientProfile: ", str(err), file=sys.stderr)
            return False
        

    def ProcessNodeService(self, **args):
        """
        axl.get.GetProcessNodeService parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getProcessNodeService(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['processNodeService']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getProcessNodeService: ", str(err), file=sys.stderr)
            return False
        

    def MohAudioSource(self, **args):
        """
        axl.get.GetMohAudioSource parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMohAudioSource(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mohAudioSource']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMohAudioSource: ", str(err), file=sys.stderr)
            return False
        

    def DhcpServer(self, **args):
        """
        axl.get.GetDhcpServer parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDhcpServer(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['dhcpServer']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDhcpServer: ", str(err), file=sys.stderr)
            return False
        

    def DhcpSubnet(self, **args):
        """
        axl.get.GetDhcpSubnet parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDhcpSubnet(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['dhcpSubnet']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDhcpSubnet: ", str(err), file=sys.stderr)
            return False
        

    def CallPark(self, **args):
        """
        axl.get.GetCallPark parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCallPark(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['callPark']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCallPark: ", str(err), file=sys.stderr)
            return False
        

    def DirectedCallPark(self, **args):
        """
        axl.get.GetDirectedCallPark parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDirectedCallPark(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['directedCallPark']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDirectedCallPark: ", str(err), file=sys.stderr)
            return False
        

    def MeetMe(self, **args):
        """
        axl.get.GetMeetMe parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMeetMe(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['meetMe']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMeetMe: ", str(err), file=sys.stderr)
            return False
        

    def ConferenceNow(self, **args):
        """
        axl.get.GetConferenceNow parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getConferenceNow(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['conferenceNow']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getConferenceNow: ", str(err), file=sys.stderr)
            return False
        

    def MobileVoiceAccess(self, **args):
        """
        axl.get.GetMobileVoiceAccess parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMobileVoiceAccess(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mobileVoiceAccess']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMobileVoiceAccess: ", str(err), file=sys.stderr)
            return False
        

    def RouteList(self, **args):
        """
        axl.get.GetRouteList parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRouteList(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['routeList']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRouteList: ", str(err), file=sys.stderr)
            return False
        

    def User(self, **args):
        """
        axl.get.GetUser parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getUser(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['user']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getUser: ", str(err), file=sys.stderr)
            return False
        

    def AppUser(self, **args):
        """
        axl.get.GetAppUser parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getAppUser(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['appUser']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getAppUser: ", str(err), file=sys.stderr)
            return False
        

    def SipRealm(self, **args):
        """
        axl.get.GetSipRealm parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSipRealm(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sipRealm']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSipRealm: ", str(err), file=sys.stderr)
            return False
        

    def PhoneNtp(self, **args):
        """
        axl.get.GetPhoneNtp parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPhoneNtp(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['phoneNtp']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPhoneNtp: ", str(err), file=sys.stderr)
            return False
        

    def DateTimeGroup(self, **args):
        """
        axl.get.GetDateTimeGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDateTimeGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['dateTimeGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDateTimeGroup: ", str(err), file=sys.stderr)
            return False
        

    def PresenceGroup(self, **args):
        """
        axl.get.GetPresenceGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPresenceGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['presenceGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPresenceGroup: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocation(self, **args):
        """
        axl.get.GetGeoLocation parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGeoLocation(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['geoLocation']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGeoLocation: ", str(err), file=sys.stderr)
            return False
        

    def Srst(self, **args):
        """
        axl.get.GetSrst parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSrst(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['srst']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSrst: ", str(err), file=sys.stderr)
            return False
        

    def MlppDomain(self, **args):
        """
        axl.get.GetMlppDomain parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMlppDomain(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mlppDomain']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMlppDomain: ", str(err), file=sys.stderr)
            return False
        

    def CumaServerSecurityProfile(self, **args):
        """
        axl.get.GetCumaServerSecurityProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCumaServerSecurityProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['cumaServerSecurityProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCumaServerSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationServer(self, **args):
        """
        axl.get.GetApplicationServer parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getApplicationServer(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['applicationServer']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getApplicationServer: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationUserCapfProfile(self, **args):
        """
        axl.get.GetApplicationUserCapfProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getApplicationUserCapfProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['applicationUserCapfProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getApplicationUserCapfProfile: ", str(err), file=sys.stderr)
            return False
        

    def EndUserCapfProfile(self, **args):
        """
        axl.get.GetEndUserCapfProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getEndUserCapfProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['endUserCapfProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getEndUserCapfProfile: ", str(err), file=sys.stderr)
            return False
        

    def ServiceParameter(self, **args):
        """
        axl.get.GetServiceParameter parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getServiceParameter(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['serviceParameter']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getServiceParameter: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocationFilter(self, **args):
        """
        axl.get.GetGeoLocationFilter parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGeoLocationFilter(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['geoLocationFilter']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGeoLocationFilter: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailProfile(self, **args):
        """
        axl.get.GetVoiceMailProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getVoiceMailProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['voiceMailProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getVoiceMailProfile: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailPort(self, **args):
        """
        axl.get.GetVoiceMailPort parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getVoiceMailPort(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['voiceMailPort']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getVoiceMailPort: ", str(err), file=sys.stderr)
            return False
        

    def Gatekeeper(self, **args):
        """
        axl.get.GetGatekeeper parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGatekeeper(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['gatekeeper']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGatekeeper: ", str(err), file=sys.stderr)
            return False
        

    def PhoneButtonTemplate(self, **args):
        """
        axl.get.GetPhoneButtonTemplate parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPhoneButtonTemplate(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['phoneButtonTemplate']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPhoneButtonTemplate: ", str(err), file=sys.stderr)
            return False
        

    def CommonPhoneConfig(self, **args):
        """
        axl.get.GetCommonPhoneConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCommonPhoneConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['commonPhoneConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCommonPhoneConfig: ", str(err), file=sys.stderr)
            return False
        

    def MessageWaiting(self, **args):
        """
        axl.get.GetMessageWaiting parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMessageWaiting(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['messageWaiting']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMessageWaiting: ", str(err), file=sys.stderr)
            return False
        

    def IpPhoneServices(self, **args):
        """
        axl.get.GetIpPhoneServices parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getIpPhoneServices(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ipPhoneServices']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getIpPhoneServices: ", str(err), file=sys.stderr)
            return False
        

    def CtiRoutePoint(self, **args):
        """
        axl.get.GetCtiRoutePoint parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCtiRoutePoint(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ctiRoutePoint']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCtiRoutePoint: ", str(err), file=sys.stderr)
            return False
        

    def TransPattern(self, **args):
        """
        axl.get.GetTransPattern parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getTransPattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['transPattern']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getTransPattern: ", str(err), file=sys.stderr)
            return False
        

    def TransPatternOptions(self, **args):
        """
        axl.get.GetTransPatternOptions parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getTransPatternOptions(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['transPattern']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getTransPatternOptions: ", str(err), file=sys.stderr)
            return False
        

    def CallingPartyTransformationPattern(self, **args):
        """
        axl.get.GetCallingPartyTransformationPattern parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCallingPartyTransformationPattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['callingPartyTransformationPattern']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCallingPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
        

    def SipRoutePattern(self, **args):
        """
        axl.get.GetSipRoutePattern parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSipRoutePattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sipRoutePattern']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSipRoutePattern: ", str(err), file=sys.stderr)
            return False
        

    def HuntPilot(self, **args):
        """
        axl.get.GetHuntPilot parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getHuntPilot(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['huntPilot']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getHuntPilot: ", str(err), file=sys.stderr)
            return False
        

    def RoutePattern(self, **args):
        """
        axl.get.GetRoutePattern parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRoutePattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['routePattern']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRoutePattern: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationDialRules(self, **args):
        """
        axl.get.GetApplicationDialRules parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getApplicationDialRules(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['applicationDialRules']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getApplicationDialRules: ", str(err), file=sys.stderr)
            return False
        

    def DirectoryLookupDialRules(self, **args):
        """
        axl.get.GetDirectoryLookupDialRules parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDirectoryLookupDialRules(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['directoryLookupDialRules']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDirectoryLookupDialRules: ", str(err), file=sys.stderr)
            return False
        

    def PhoneSecurityProfile(self, **args):
        """
        axl.get.GetPhoneSecurityProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPhoneSecurityProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['phoneSecurityProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPhoneSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def SipDialRules(self, **args):
        """
        axl.get.GetSipDialRules parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSipDialRules(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sipDialRules']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSipDialRules: ", str(err), file=sys.stderr)
            return False
        

    def ConferenceBridge(self, **args):
        """
        axl.get.GetConferenceBridge parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getConferenceBridge(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['conferenceBridge']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getConferenceBridge: ", str(err), file=sys.stderr)
            return False
        

    def Annunciator(self, **args):
        """
        axl.get.GetAnnunciator parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getAnnunciator(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['annunciator']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getAnnunciator: ", str(err), file=sys.stderr)
            return False
        

    def InteractiveVoice(self, **args):
        """
        axl.get.GetInteractiveVoice parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getInteractiveVoice(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['interactiveVoiceResponse']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getInteractiveVoice: ", str(err), file=sys.stderr)
            return False
        

    def Mtp(self, **args):
        """
        axl.get.GetMtp parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMtp(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mtp']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMtp: ", str(err), file=sys.stderr)
            return False
        

    def FixedMohAudioSource(self, **args):
        """
        axl.get.GetFixedMohAudioSource parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getFixedMohAudioSource(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['fixedMohAudioSource']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getFixedMohAudioSource: ", str(err), file=sys.stderr)
            return False
        

    def RemoteDestinationProfile(self, **args):
        """
        axl.get.GetRemoteDestinationProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRemoteDestinationProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['remoteDestinationProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRemoteDestinationProfile: ", str(err), file=sys.stderr)
            return False
        

    def Line(self, **args):
        """
        axl.get.GetLine parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLine(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['line']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLine: ", str(err), file=sys.stderr)
            return False
        

    def LineOptions(self, **args):
        """
        axl.get.GetLineOptions parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLineOptions(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['line']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLineOptions: ", str(err), file=sys.stderr)
            return False
        

    def DefaultDeviceProfile(self, **args):
        """
        axl.get.GetDefaultDeviceProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDefaultDeviceProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['defaultDeviceProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDefaultDeviceProfile: ", str(err), file=sys.stderr)
            return False
        

    def H323Phone(self, **args):
        """
        axl.get.GetH323Phone parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getH323Phone(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['h323Phone']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getH323Phone: ", str(err), file=sys.stderr)
            return False
        

    def MohServer(self, **args):
        """
        axl.get.GetMohServer parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMohServer(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mohServer']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMohServer: ", str(err), file=sys.stderr)
            return False
        

    def H323Trunk(self, **args):
        """
        axl.get.GetH323Trunk parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getH323Trunk(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['h323Trunk']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getH323Trunk: ", str(err), file=sys.stderr)
            return False
        

    def Phone(self, **args):
        """
        axl.get.GetPhone parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPhone(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['phone']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPhone: ", str(err), file=sys.stderr)
            return False
        

    def PhoneOptions(self, **args):
        """
        axl.get.GetPhoneOptions parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPhoneOptions(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['phone']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPhoneOptions: ", str(err), file=sys.stderr)
            return False
        

    def H323Gateway(self, **args):
        """
        axl.get.GetH323Gateway parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getH323Gateway(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['h323Gateway']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getH323Gateway: ", str(err), file=sys.stderr)
            return False
        

    def DeviceProfile(self, **args):
        """
        axl.get.GetDeviceProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDeviceProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['deviceProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDeviceProfile: ", str(err), file=sys.stderr)
            return False
        

    def DeviceProfileOptions(self, **args):
        """
        axl.get.GetDeviceProfileOptions parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDeviceProfileOptions(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['deviceProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDeviceProfileOptions: ", str(err), file=sys.stderr)
            return False
        

    def RemoteDestination(self, **args):
        """
        axl.get.GetRemoteDestination parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRemoteDestination(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['remoteDestination']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRemoteDestination: ", str(err), file=sys.stderr)
            return False
        

    def Vg224(self, **args):
        """
        axl.get.GetVg224 parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getVg224(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['vg224']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getVg224: ", str(err), file=sys.stderr)
            return False
        

    def Gateway(self, **args):
        """
        axl.get.GetGateway parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGateway(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['gateway']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGateway: ", str(err), file=sys.stderr)
            return False
        

    def GatewayEndpointAnalogAccess(self, **args):
        """
        axl.get.GetGatewayEndpointAnalogAccess parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGatewayEndpointAnalogAccess(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['gatewayEndpointAnalogAccess']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGatewayEndpointAnalogAccess: ", str(err), file=sys.stderr)
            return False
        

    def GatewayEndpointDigitalAccessPri(self, **args):
        """
        axl.get.GetGatewayEndpointDigitalAccessPri parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGatewayEndpointDigitalAccessPri(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['gatewayEndpointDigitalAccessPri']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGatewayEndpointDigitalAccessPri: ", str(err), file=sys.stderr)
            return False
        

    def GatewayEndpointDigitalAccessBri(self, **args):
        """
        axl.get.GetGatewayEndpointDigitalAccessBri parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGatewayEndpointDigitalAccessBri(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['gatewayEndpointDigitalAccessBri']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGatewayEndpointDigitalAccessBri: ", str(err), file=sys.stderr)
            return False
        

    def GatewayEndpointDigitalAccessT1(self, **args):
        """
        axl.get.GetGatewayEndpointDigitalAccessT1 parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGatewayEndpointDigitalAccessT1(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['gatewayEndpointDigitalAccessT1']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGatewayEndpointDigitalAccessT1: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst600024PortFXSGateway(self, **args):
        """
        axl.get.GetCiscoCatalyst600024PortFXSGateway parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCiscoCatalyst600024PortFXSGateway(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ciscoCatalyst600024PortFXSGateway']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCiscoCatalyst600024PortFXSGateway: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000E1VoIPGateway(self, **args):
        """
        axl.get.GetCiscoCatalyst6000E1VoIPGateway parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCiscoCatalyst6000E1VoIPGateway(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ciscoCatalyst6000E1VoIPGateway']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCiscoCatalyst6000E1VoIPGateway: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000T1VoIPGatewayPri(self, **args):
        """
        axl.get.GetCiscoCatalyst6000T1VoIPGatewayPri parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCiscoCatalyst6000T1VoIPGatewayPri(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ciscoCatalyst6000T1VoIPGatewayPri']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCiscoCatalyst6000T1VoIPGatewayPri: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000T1VoIPGatewayT1(self, **args):
        """
        axl.get.GetCiscoCatalyst6000T1VoIPGatewayT1 parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCiscoCatalyst6000T1VoIPGatewayT1(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ciscoCatalyst6000T1VoIPGatewayT1']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCiscoCatalyst6000T1VoIPGatewayT1: ", str(err), file=sys.stderr)
            return False
        

    def CallPickupGroup(self, **args):
        """
        axl.get.GetCallPickupGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCallPickupGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['callPickupGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCallPickupGroup: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocationPolicy(self, **args):
        """
        axl.get.GetGeoLocationPolicy parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGeoLocationPolicy(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['geoLocationPolicy']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGeoLocationPolicy: ", str(err), file=sys.stderr)
            return False
        

    def SipTrunk(self, **args):
        """
        axl.get.GetSipTrunk parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSipTrunk(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sipTrunk']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSipTrunk: ", str(err), file=sys.stderr)
            return False
        

    def CalledPartyTransformationPattern(self, **args):
        """
        axl.get.GetCalledPartyTransformationPattern parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCalledPartyTransformationPattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['calledPartyTransformationPattern']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCalledPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
        

    def ExternalCallControlProfile(self, **args):
        """
        axl.get.GetExternalCallControlProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getExternalCallControlProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['externalCallControlProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getExternalCallControlProfile: ", str(err), file=sys.stderr)
            return False
        

    def SafSecurityProfile(self, **args):
        """
        axl.get.GetSafSecurityProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSafSecurityProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['safSecurityProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSafSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def SafForwarder(self, **args):
        """
        axl.get.GetSafForwarder parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSafForwarder(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['safForwarder']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSafForwarder: ", str(err), file=sys.stderr)
            return False
        

    def CcdHostedDN(self, **args):
        """
        axl.get.GetCcdHostedDN parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCcdHostedDN(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ccdHostedDN']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCcdHostedDN: ", str(err), file=sys.stderr)
            return False
        

    def CcdHostedDNGroup(self, **args):
        """
        axl.get.GetCcdHostedDNGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCcdHostedDNGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ccdHostedDNGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCcdHostedDNGroup: ", str(err), file=sys.stderr)
            return False
        

    def CcdRequestingService(self, **args):
        """
        axl.get.GetCcdRequestingService parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCcdRequestingService(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ccdRequestingService']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCcdRequestingService: ", str(err), file=sys.stderr)
            return False
        

    def InterClusterServiceProfile(self, **args):
        """
        axl.get.GetInterClusterServiceProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getInterClusterServiceProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['interClusterServiceProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getInterClusterServiceProfile: ", str(err), file=sys.stderr)
            return False
        

    def RemoteCluster(self, **args):
        """
        axl.get.GetRemoteCluster parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRemoteCluster(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['remoteCluster']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRemoteCluster: ", str(err), file=sys.stderr)
            return False
        

    def CcdAdvertisingService(self, **args):
        """
        axl.get.GetCcdAdvertisingService parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCcdAdvertisingService(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ccdAdvertisingService']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCcdAdvertisingService: ", str(err), file=sys.stderr)
            return False
        

    def LdapDirectory(self, **args):
        """
        axl.get.GetLdapDirectory parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLdapDirectory(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ldapDirectory']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLdapDirectory: ", str(err), file=sys.stderr)
            return False
        

    def EmccFeatureConfig(self, **args):
        """
        axl.get.GetEmccFeatureConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getEmccFeatureConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['emccFeatureConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getEmccFeatureConfig: ", str(err), file=sys.stderr)
            return False
        

    def SafCcdPurgeBlockLearnedRoutes(self, **args):
        """
        axl.get.GetSafCcdPurgeBlockLearnedRoutes parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSafCcdPurgeBlockLearnedRoutes(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['safCcdPurgeBlockLearnedRoutes']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSafCcdPurgeBlockLearnedRoutes: ", str(err), file=sys.stderr)
            return False
        

    def VpnGateway(self, **args):
        """
        axl.get.GetVpnGateway parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getVpnGateway(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['vpnGateway']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getVpnGateway: ", str(err), file=sys.stderr)
            return False
        

    def VpnGroup(self, **args):
        """
        axl.get.GetVpnGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getVpnGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['vpnGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getVpnGroup: ", str(err), file=sys.stderr)
            return False
        

    def VpnProfile(self, **args):
        """
        axl.get.GetVpnProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getVpnProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['vpnProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getVpnProfile: ", str(err), file=sys.stderr)
            return False
        

    def ImeServer(self, **args):
        """
        axl.get.GetImeServer parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeServer(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeServer']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeServer: ", str(err), file=sys.stderr)
            return False
        

    def ImeRouteFilterGroup(self, **args):
        """
        axl.get.GetImeRouteFilterGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeRouteFilterGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeRouteFilterGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeRouteFilterGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeRouteFilterElement(self, **args):
        """
        axl.get.GetImeRouteFilterElement parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeRouteFilterElement(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeRouteFilterElement']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeRouteFilterElement: ", str(err), file=sys.stderr)
            return False
        

    def ImeClient(self, **args):
        """
        axl.get.GetImeClient parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeClient(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeClient']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeClient: ", str(err), file=sys.stderr)
            return False
        

    def ImeEnrolledPattern(self, **args):
        """
        axl.get.GetImeEnrolledPattern parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeEnrolledPattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeEnrolledPattern']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeEnrolledPattern: ", str(err), file=sys.stderr)
            return False
        

    def ImeEnrolledPatternGroup(self, **args):
        """
        axl.get.GetImeEnrolledPatternGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeEnrolledPatternGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeEnrolledPatternGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeEnrolledPatternGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeExclusionNumber(self, **args):
        """
        axl.get.GetImeExclusionNumber parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeExclusionNumber(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeExclusionNumber']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeExclusionNumber: ", str(err), file=sys.stderr)
            return False
        

    def ImeExclusionNumberGroup(self, **args):
        """
        axl.get.GetImeExclusionNumberGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeExclusionNumberGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeExclusionNumberGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeExclusionNumberGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeFirewall(self, **args):
        """
        axl.get.GetImeFirewall parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeFirewall(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeFirewall']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeFirewall: ", str(err), file=sys.stderr)
            return False
        

    def ImeE164Transformation(self, **args):
        """
        axl.get.GetImeE164Transformation parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeE164Transformation(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeE164Transformation']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeE164Transformation: ", str(err), file=sys.stderr)
            return False
        

    def TransformationProfile(self, **args):
        """
        axl.get.GetTransformationProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getTransformationProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['transformationProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getTransformationProfile: ", str(err), file=sys.stderr)
            return False
        

    def FallbackProfile(self, **args):
        """
        axl.get.GetFallbackProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getFallbackProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['fallbackProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getFallbackProfile: ", str(err), file=sys.stderr)
            return False
        

    def LdapFilter(self, **args):
        """
        axl.get.GetLdapFilter parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLdapFilter(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ldapFilter']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLdapFilter: ", str(err), file=sys.stderr)
            return False
        

    def TvsCertificate(self, **args):
        """
        axl.get.GetTvsCertificate parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getTvsCertificate(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['tvsCertificate']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getTvsCertificate: ", str(err), file=sys.stderr)
            return False
        

    def FeatureControlPolicy(self, **args):
        """
        axl.get.GetFeatureControlPolicy parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getFeatureControlPolicy(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['featureControlPolicy']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getFeatureControlPolicy: ", str(err), file=sys.stderr)
            return False
        

    def MobilityProfile(self, **args):
        """
        axl.get.GetMobilityProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMobilityProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mobilityProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMobilityProfile: ", str(err), file=sys.stderr)
            return False
        

    def EnterpriseFeatureAccessConfiguration(self, **args):
        """
        axl.get.GetEnterpriseFeatureAccessConfiguration parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getEnterpriseFeatureAccessConfiguration(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['enterpriseFeatureAccessConfiguration']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getEnterpriseFeatureAccessConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def HandoffConfiguration(self, **args):
        """
        axl.get.GetHandoffConfiguration parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getHandoffConfiguration(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['handoffConfiguration']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getHandoffConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def SIPNormalizationScript(self, **args):
        """
        axl.get.GetSIPNormalizationScript parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSIPNormalizationScript(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sIPNormalizationScript']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSIPNormalizationScript: ", str(err), file=sys.stderr)
            return False
        

    def CustomUserField(self, **args):
        """
        axl.get.GetCustomUserField parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCustomUserField(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['customUserField']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCustomUserField: ", str(err), file=sys.stderr)
            return False
        

    def GatewaySccpEndpoints(self, **args):
        """
        axl.get.GetGatewaySccpEndpoints parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getGatewaySccpEndpoints(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['gatewaySccpEndpoints']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getGatewaySccpEndpoints: ", str(err), file=sys.stderr)
            return False
        

    def LbmGroup(self, **args):
        """
        axl.get.GetLbmGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLbmGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['lbmGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLbmGroup: ", str(err), file=sys.stderr)
            return False
        

    def Announcement(self, **args):
        """
        axl.get.GetAnnouncement parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getAnnouncement(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['announcement']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getAnnouncement: ", str(err), file=sys.stderr)
            return False
        

    def ServiceProfile(self, **args):
        """
        axl.get.GetServiceProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getServiceProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['serviceProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getServiceProfile: ", str(err), file=sys.stderr)
            return False
        

    def LdapSyncCustomField(self, **args):
        """
        axl.get.GetLdapSyncCustomField parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLdapSyncCustomField(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ldapSyncCustomField']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLdapSyncCustomField: ", str(err), file=sys.stderr)
            return False
        

    def AudioCodecPreferenceList(self, **args):
        """
        axl.get.GetAudioCodecPreferenceList parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getAudioCodecPreferenceList(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['audioCodecPreferenceList']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getAudioCodecPreferenceList: ", str(err), file=sys.stderr)
            return False
        

    def UcService(self, **args):
        """
        axl.get.GetUcService parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getUcService(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ucService']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getUcService: ", str(err), file=sys.stderr)
            return False
        

    def LbmHubGroup(self, **args):
        """
        axl.get.GetLbmHubGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLbmHubGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['lbmHubGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLbmHubGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImportedDirectoryUriCatalogs(self, **args):
        """
        axl.get.GetImportedDirectoryUriCatalogs parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImportedDirectoryUriCatalogs(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['importedDirectoryUriCatalogs']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImportedDirectoryUriCatalogs: ", str(err), file=sys.stderr)
            return False
        

    def VohServer(self, **args):
        """
        axl.get.GetVohServer parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getVohServer(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['vohServer']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getVohServer: ", str(err), file=sys.stderr)
            return False
        

    def SdpTransparencyProfile(self, **args):
        """
        axl.get.GetSdpTransparencyProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSdpTransparencyProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['sdpTransparencyProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSdpTransparencyProfile: ", str(err), file=sys.stderr)
            return False
        

    def FeatureGroupTemplate(self, **args):
        """
        axl.get.GetFeatureGroupTemplate parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getFeatureGroupTemplate(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['featureGroupTemplate']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getFeatureGroupTemplate: ", str(err), file=sys.stderr)
            return False
        

    def DirNumberAliasLookupandSync(self, **args):
        """
        axl.get.GetDirNumberAliasLookupandSync parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDirNumberAliasLookupandSync(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['dirNumberAliasLookupandSync']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDirNumberAliasLookupandSync: ", str(err), file=sys.stderr)
            return False
        

    def LocalRouteGroup(self, **args):
        """
        axl.get.GetLocalRouteGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLocalRouteGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['localRouteGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLocalRouteGroup: ", str(err), file=sys.stderr)
            return False
        

    def AdvertisedPatterns(self, **args):
        """
        axl.get.GetAdvertisedPatterns parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getAdvertisedPatterns(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['advertisedPatterns']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getAdvertisedPatterns: ", str(err), file=sys.stderr)
            return False
        

    def BlockedLearnedPatterns(self, **args):
        """
        axl.get.GetBlockedLearnedPatterns parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getBlockedLearnedPatterns(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['blockedLearnedPatterns']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getBlockedLearnedPatterns: ", str(err), file=sys.stderr)
            return False
        

    def CCAProfiles(self, **args):
        """
        axl.get.GetCCAProfiles parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCCAProfiles(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['cCAProfiles']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCCAProfiles: ", str(err), file=sys.stderr)
            return False
        

    def UniversalDeviceTemplate(self, **args):
        """
        axl.get.GetUniversalDeviceTemplate parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getUniversalDeviceTemplate(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['universalDeviceTemplate']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getUniversalDeviceTemplate: ", str(err), file=sys.stderr)
            return False
        

    def UserProfileProvision(self, **args):
        """
        axl.get.GetUserProfileProvision parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getUserProfileProvision(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['userProfileProvision']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getUserProfileProvision: ", str(err), file=sys.stderr)
            return False
        

    def PresenceRedundancyGroup(self, **args):
        """
        axl.get.GetPresenceRedundancyGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPresenceRedundancyGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['presenceRedundancyGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPresenceRedundancyGroup: ", str(err), file=sys.stderr)
            return False
        

    def WifiHotspot(self, **args):
        """
        axl.get.GetWifiHotspot parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getWifiHotspot(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['wifiHotspot']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getWifiHotspot: ", str(err), file=sys.stderr)
            return False
        

    def WlanProfileGroup(self, **args):
        """
        axl.get.GetWlanProfileGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getWlanProfileGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['wlanProfileGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getWlanProfileGroup: ", str(err), file=sys.stderr)
            return False
        

    def WLANProfile(self, **args):
        """
        axl.get.GetWLANProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getWLANProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['wLANProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getWLANProfile: ", str(err), file=sys.stderr)
            return False
        

    def UniversalLineTemplate(self, **args):
        """
        axl.get.GetUniversalLineTemplate parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getUniversalLineTemplate(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['universalLineTemplate']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getUniversalLineTemplate: ", str(err), file=sys.stderr)
            return False
        

    def NetworkAccessProfile(self, **args):
        """
        axl.get.GetNetworkAccessProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getNetworkAccessProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['networkAccessProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getNetworkAccessProfile: ", str(err), file=sys.stderr)
            return False
        

    def LicensedUser(self, **args):
        """
        axl.get.GetLicensedUser parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLicensedUser(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['licensedUser']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLicensedUser: ", str(err), file=sys.stderr)
            return False
        

    def HttpProfile(self, **args):
        """
        axl.get.GetHttpProfile parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getHttpProfile(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['httpProfile']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getHttpProfile: ", str(err), file=sys.stderr)
            return False
        

    def ElinGroup(self, **args):
        """
        axl.get.GetElinGroup parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getElinGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['elinGroup']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getElinGroup: ", str(err), file=sys.stderr)
            return False
        

    def SecureConfig(self, **args):
        """
        axl.get.GetSecureConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSecureConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['secureConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSecureConfig: ", str(err), file=sys.stderr)
            return False
        

    def RegistrationDynamic(self, **args):
        """
        axl.get.GetRegistrationDynamic parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getRegistrationDynamic(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['registrationDynamic']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getRegistrationDynamic: ", str(err), file=sys.stderr)
            return False
        

    def InfrastructureDevice(self, **args):
        """
        axl.get.GetInfrastructureDevice parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getInfrastructureDevice(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['infrastructureDevice']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getInfrastructureDevice: ", str(err), file=sys.stderr)
            return False
        

    def LdapSearch(self, **args):
        """
        axl.get.GetLdapSearch parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLdapSearch(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ldapSearch']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLdapSearch: ", str(err), file=sys.stderr)
            return False
        

    def WirelessAccessPointControllers(self, **args):
        """
        axl.get.GetWirelessAccessPointControllers parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getWirelessAccessPointControllers(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['wirelessAccessPointControllers']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getWirelessAccessPointControllers: ", str(err), file=sys.stderr)
            return False
        

    def DeviceDefaults(self, **args):
        """
        axl.get.GetDeviceDefaults parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getDeviceDefaults(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['deviceDefaults']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getDeviceDefaults: ", str(err), file=sys.stderr)
            return False
        

    def MraServiceDomain(self, **args):
        """
        axl.get.GetMraServiceDomain parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMraServiceDomain(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mraServiceDomain']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMraServiceDomain: ", str(err), file=sys.stderr)
            return False
        

    def OSVersion(self, **args):
        """
        axl.get.GetOSVersion parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getOSVersion(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['os']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getOSVersion: ", str(err), file=sys.stderr)
            return False
        

    def Mobility(self, **args):
        """
        axl.get.GetMobility parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getMobility(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['mobility']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getMobility: ", str(err), file=sys.stderr)
            return False
        

    def EnterprisePhoneConfig(self, **args):
        """
        axl.get.GetEnterprisePhoneConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getEnterprisePhoneConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['enterprisePhoneConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getEnterprisePhoneConfig: ", str(err), file=sys.stderr)
            return False
        

    def LdapSystem(self, **args):
        """
        axl.get.GetLdapSystem parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLdapSystem(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ldapSystem']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLdapSystem: ", str(err), file=sys.stderr)
            return False
        

    def LdapAuthentication(self, **args):
        """
        axl.get.GetLdapAuthentication parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getLdapAuthentication(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ldapAuthentication']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getLdapAuthentication: ", str(err), file=sys.stderr)
            return False
        

    def CCMVersion(self, **args):
        """
        axl.get.GetCCMVersion parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCCMVersion(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['componentVersion']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCCMVersion: ", str(err), file=sys.stderr)
            return False
        

    def FallbackFeatureConfig(self, **args):
        """
        axl.get.GetFallbackFeatureConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getFallbackFeatureConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['fallbackFeatureConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getFallbackFeatureConfig: ", str(err), file=sys.stderr)
            return False
        

    def ImeLearnedRoutes(self, **args):
        """
        axl.get.GetImeLearnedRoutes parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeLearnedRoutes(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeLearnedRoutes']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeLearnedRoutes: ", str(err), file=sys.stderr)
            return False
        

    def ImeFeatureConfig(self, **args):
        """
        axl.get.GetImeFeatureConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getImeFeatureConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['imeFeatureConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getImeFeatureConfig: ", str(err), file=sys.stderr)
            return False
        

    def AppServerInfo(self, **args):
        """
        axl.get.GetAppServerInfo parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getAppServerInfo(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['appServerInfo']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getAppServerInfo: ", str(err), file=sys.stderr)
            return False
        

    def SoftKeySet(self, **args):
        """
        axl.get.GetSoftKeySet parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSoftKeySet(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['softKeySet']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSoftKeySet: ", str(err), file=sys.stderr)
            return False
        

    def SyslogConfiguration(self, **args):
        """
        axl.get.GetSyslogConfiguration parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSyslogConfiguration(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['syslogConfiguration']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSyslogConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def IlsConfig(self, **args):
        """
        axl.get.GetIlsConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getIlsConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ilsConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getIlsConfig: ", str(err), file=sys.stderr)
            return False
        

    def SNMPCommunityString(self, **args):
        """
        axl.get.GetSNMPCommunityString parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSNMPCommunityString(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['SNMPCommunityString']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSNMPCommunityString: ", str(err), file=sys.stderr)
            return False
        

    def SNMPUser(self, **args):
        """
        axl.get.GetSNMPUser parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSNMPUser(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['SNMPUser']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSNMPUser: ", str(err), file=sys.stderr)
            return False
        

    def SNMPMIB2List(self, **args):
        """
        axl.get.GetSNMPMIB2List parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSNMPMIB2List(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['SNMPMIB2List']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSNMPMIB2List: ", str(err), file=sys.stderr)
            return False
        

    def BillingServer(self, **args):
        """
        axl.get.GetBillingServer parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getBillingServer(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['billingServer']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getBillingServer: ", str(err), file=sys.stderr)
            return False
        

    def CcdFeatureConfig(self, **args):
        """
        axl.get.GetCcdFeatureConfig parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCcdFeatureConfig(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ccdFeatureConfig']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCcdFeatureConfig: ", str(err), file=sys.stderr)
            return False
        

    def PageLayoutPreferences(self, **args):
        """
        axl.get.GetPageLayoutPreferences parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getPageLayoutPreferences(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['pageLayoutPreferences']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getPageLayoutPreferences: ", str(err), file=sys.stderr)
            return False
        

    def CredentialPolicyDefault(self, **args):
        """
        axl.get.GetCredentialPolicyDefault parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getCredentialPolicyDefault(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['credentialPolicyDefault']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getCredentialPolicyDefault: ", str(err), file=sys.stderr)
            return False
        

    def SmartLicenseStatus(self, **args):
        """
        axl.get.GetSmartLicenseStatus parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSmartLicenseStatus(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['SmartLicensing']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSmartLicenseStatus: ", str(err), file=sys.stderr)
            return False
        

    def SmartLicenseStatus(self, **args):
        """
        axl.get.GetSmartLicenseStatus parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSmartLicenseStatus(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['Registration']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSmartLicenseStatus: ", str(err), file=sys.stderr)
            return False
        

    def SmartLicenseStatus(self, **args):
        """
        axl.get.GetSmartLicenseStatus parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSmartLicenseStatus(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['Authorization']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSmartLicenseStatus: ", str(err), file=sys.stderr)
            return False
        

    def SmartLicenseStatus(self, **args):
        """
        axl.get.GetSmartLicenseStatus parameters
        :param name: name
        :param uuid: uuid 
        :return: result dictionary
        """
        try:
            resp = self.client.getSmartLicenseStatus(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['LicenseStatus']
                if soap_result is None:
                    return []
                elif isinstance(soap_result, dict):
                    return [soap_result]
                elif isinstance(soap_result, list):
                    return soap_result
                else:
                    return [soap_result]
            return True

        except Fault as err:
            print(f"AXL error getSmartLicenseStatus: ", str(err), file=sys.stderr)
            return False
        

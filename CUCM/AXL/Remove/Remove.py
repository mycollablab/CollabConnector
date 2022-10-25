from zeep.helpers import serialize_object
from zeep.exceptions import Fault
import sys


class Remove:
    def __init__(self, soap_client):
        self.client = soap_client

    def VoiceMailPilot(self, **args):
        """
        VoiceMailPilot parameters
        :param uuid: uuid
        :param dirn: dirn
:param cssName: cssName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeVoiceMailPilot(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeVoiceMailPilot: ", str(err), file=sys.stderr)
            return False
    

    def DhcpSubnet(self, **args):
        """
        DhcpSubnet parameters
        :param uuid: uuid
        :param dhcpServerName: dhcpServerName
:param subnetIpAddress: subnetIpAddress
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeDhcpSubnet(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeDhcpSubnet: ", str(err), file=sys.stderr)
            return False
    

    def CallPark(self, **args):
        """
        CallPark parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeCallPark(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeCallPark: ", str(err), file=sys.stderr)
            return False
    

    def DirectedCallPark(self, **args):
        """
        DirectedCallPark parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeDirectedCallPark(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeDirectedCallPark: ", str(err), file=sys.stderr)
            return False
    

    def MeetMe(self, **args):
        """
        MeetMe parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeMeetMe(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeMeetMe: ", str(err), file=sys.stderr)
            return False
    

    def ConferenceNow(self, **args):
        """
        ConferenceNow parameters
        :param uuid: uuid
        :param conferenceNowNumber: conferenceNowNumber
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeConferenceNow(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeConferenceNow: ", str(err), file=sys.stderr)
            return False
    

    def PhoneNtp(self, **args):
        """
        PhoneNtp parameters
        :param uuid: uuid
        :param ipAddress: ipAddress
:param ipv6Address: ipv6Address
:return: result list of dictionaries
        """
        try:
            resp = self.client.removePhoneNtp(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removePhoneNtp: ", str(err), file=sys.stderr)
            return False
    

    def MessageWaiting(self, **args):
        """
        MessageWaiting parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeMessageWaiting(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeMessageWaiting: ", str(err), file=sys.stderr)
            return False
    

    def TransPattern(self, **args):
        """
        TransPattern parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:param dialPlanName: dialPlanName
:param routeFilterName: routeFilterName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeTransPattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeTransPattern: ", str(err), file=sys.stderr)
            return False
    

    def CallingPartyTransformationPattern(self, **args):
        """
        CallingPartyTransformationPattern parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:param dialPlanName: dialPlanName
:param routeFilterName: routeFilterName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeCallingPartyTransformationPattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeCallingPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
    

    def SipRoutePattern(self, **args):
        """
        SipRoutePattern parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeSipRoutePattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeSipRoutePattern: ", str(err), file=sys.stderr)
            return False
    

    def HuntPilot(self, **args):
        """
        HuntPilot parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeHuntPilot(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeHuntPilot: ", str(err), file=sys.stderr)
            return False
    

    def RoutePattern(self, **args):
        """
        RoutePattern parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:param dialPlanName: dialPlanName
:param routeFilterName: routeFilterName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeRoutePattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeRoutePattern: ", str(err), file=sys.stderr)
            return False
    

    def Line(self, **args):
        """
        Line parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeLine(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeLine: ", str(err), file=sys.stderr)
            return False
    

    def CallPickupGroup(self, **args):
        """
        CallPickupGroup parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeCallPickupGroup(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeCallPickupGroup: ", str(err), file=sys.stderr)
            return False
    

    def CalledPartyTransformationPattern(self, **args):
        """
        CalledPartyTransformationPattern parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:param dialPlanName: dialPlanName
:param routeFilterName: routeFilterName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeCalledPartyTransformationPattern(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeCalledPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
    

    def SafCcdPurgeBlockLearnedRoutes(self, **args):
        """
        SafCcdPurgeBlockLearnedRoutes parameters
        :param uuid: uuid
        :param learnedPattern: learnedPattern
:param learnedPatternPrefix: learnedPatternPrefix
:param callControlIdentity: callControlIdentity
:param ipAddress: ipAddress
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeSafCcdPurgeBlockLearnedRoutes(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeSafCcdPurgeBlockLearnedRoutes: ", str(err), file=sys.stderr)
            return False
    

    def EnterpriseFeatureAccessConfiguration(self, **args):
        """
        EnterpriseFeatureAccessConfiguration parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeEnterpriseFeatureAccessConfiguration(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeEnterpriseFeatureAccessConfiguration: ", str(err), file=sys.stderr)
            return False
    

    def HandoffConfiguration(self, **args):
        """
        HandoffConfiguration parameters
        :param uuid: uuid
        :param pattern: pattern
:param routePartitionName: routePartitionName
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeHandoffConfiguration(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeHandoffConfiguration: ", str(err), file=sys.stderr)
            return False
    

    def LdapSyncCustomField(self, **args):
        """
        LdapSyncCustomField parameters
        :param uuid: uuid
        :param ldapConfigurationName: ldapConfigurationName
:param customUserField: customUserField
:return: result list of dictionaries
        """
        try:
            resp = self.client.removeLdapSyncCustomField(**args)
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['return']
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
            print(f"AXL error removeLdapSyncCustomField: ", str(err), file=sys.stderr)
            return False
    

from zeep.helpers import serialize_object
from zeep.exceptions import Fault
import sys


class List:
    def __init__(self, soap_client):
        self.client = soap_client

    def SipProfile(self, name=''):
        """
        list_sip_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listSipProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'defaultTelephonyEventPayloadType': '', 'redirectByApplication': '', 'ringing180': '', 'timerInvite': '', 'timerRegisterDelta': '', 'timerRegister': '', 'timerT1': '', 'timerT2': '', 'retryInvite': '', 'retryNotInvite': '', 'startMediaPort': '', 'stopMediaPort': '', 'callpickupListUri': '', 'callpickupGroupUri': '', 'meetmeServiceUrl': '', 'userInfo': '', 'dtmfDbLevel': '', 'callHoldRingback': '', 'anonymousCallBlock': '', 'callerIdBlock': '', 'dndControl': '', 'telnetLevel': '', 'timerKeepAlive': '', 'timerSubscribe': '', 'timerSubscribeDelta': '', 'maxRedirects': '', 'timerOffHookToFirstDigit': '', 'callForwardUri': '', 'abbreviatedDialUri': '', 'confJointEnable': '', 'rfc2543Hold': '', 'semiAttendedTransfer': '', 'enableVad': '', 'stutterMsgWaiting': '', 'callStats': '', 't38Invite': '', 'faxInvite': '', 'rerouteIncomingRequest': '', 'resourcePriorityNamespaceListName': '', 'enableAnatForEarlyOfferCalls': '', 'rsvpOverSip': '', 'fallbackToLocalRsvp': '', 'sipRe11XxEnabled': '', 'gClear': '', 'sendRecvSDPInMidCallInvite': '', 'enableOutboundOptionsPing': '', 'optionsPingIntervalWhenStatusOK': '', 'optionsPingIntervalWhenStatusNotOK': '', 'deliverConferenceBridgeIdentifier': '', 'sipOptionsRetryCount': '', 'sipOptionsRetryTimer': '', 'sipBandwidthModifier': '', 'enableUriOutdialSupport': '', 'userAgentServerHeaderInfo': '', 'allowPresentationSharingUsingBfcp': '', 'scriptParameters': '', 'isScriptTraceEnabled': '', 'sipNormalizationScript': '', 'allowiXApplicationMedia': '', 'dialStringInterpretation': '', 'acceptAudioCodecPreferences': '', 'mlppUserAuthorization': '', 'isAssuredSipServiceEnabled': '', 'resourcePriorityNamespace': '', 'useCallerIdCallerNameinUriOutgoingRequest': '', 'callingLineIdentification': '', 'rejectAnonymousIncomingCall': '', 'callpickupUri': '', 'rejectAnonymousOutgoingCall': '', 'videoCallTrafficClass': '', 'sdpTransparency': '', 'allowMultipleCodecs': '', 'sipSessionRefreshMethod': '', 'earlyOfferSuppVoiceCall': '', 'cucmVersionInSipHeader': '', 'confidentialAccessLevelHeaders': '', 'destRouteString': '', 'inactiveSDPRequired': '', 'allowRRAndRSBandwidthModifier': ''}
            )
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
            print(f"AXL error listSipProfile: ", str(err), file=sys.stderr)
            return False
        

    def SipTrunkSecurityProfile(self, name=''):
        """
        list_sip_trunk_security_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listSipTrunkSecurityProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'securityMode': '', 'incomingTransport': '', 'outgoingTransport': '', 'digestAuthentication': '', 'noncePolicyTime': '', 'x509SubjectName': '', 'incomingPort': '', 'applLevelAuthentication': '', 'acceptPresenceSubscription': '', 'acceptOutOfDialogRefer': '', 'acceptUnsolicitedNotification': '', 'allowReplaceHeader': '', 'transmitSecurityStatus': '', 'sipV150OutboundSdpOfferFiltering': '', 'allowChargingHeader': ''}
            )
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
            print(f"AXL error listSipTrunkSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def TimePeriod(self, name=''):
        """
        list_time_period parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listTimePeriod(
                {'name': '%'+name}, returnedTags={'name': '', 'startTime': '', 'endTime': '', 'startDay': '', 'endDay': '', 'monthOfYear': '', 'dayOfMonth': '', 'description': '', 'isPublished': '', 'todOwnerIdName': '', 'dayOfMonthEnd': '', 'monthOfYearEnd': ''}
            )
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
            print(f"AXL error listTimePeriod: ", str(err), file=sys.stderr)
            return False
        

    def TimeSchedule(self, name=''):
        """
        list_time_schedule parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listTimeSchedule(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'isPublished': '', 'timeScheduleCategory': '', 'todOwnerIdName': '', 'timePeriodName': ''}
            )
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
            print(f"AXL error listTimeSchedule: ", str(err), file=sys.stderr)
            return False
        

    def TodAccess(self, name=''):
        """
        list_tod_access parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param ownerIdName: ownerIdName
        """
        try:
            resp = self.client.listTodAccess(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'ownerIdName': ''}
            )
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
            print(f"AXL error listTodAccess: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailPilot(self, name=''):
        """
        list_voice_mail_pilot parameters
        :param uuid: uuid
        :param dirn: dirn
		:param description: description
		:param cssName: cssName
        """
        try:
            resp = self.client.listVoiceMailPilot(
                {'name': '%'+name}, returnedTags={'dirn': '', 'description': '', 'cssName': '', 'isDefault': ''}
            )
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
            print(f"AXL error listVoiceMailPilot: ", str(err), file=sys.stderr)
            return False
        

    def ProcessNode(self, name=''):
        """
        list_process_node parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param processNodeRole: processNodeRole
        """
        try:
            resp = self.client.listProcessNode(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'mac': '', 'ipv6Name': '', 'nodeUsage': '', 'lbmHubGroup': '', 'processNodeRole': '', 'processNodeName': '', 'service': '', 'traceLevel': '', 'userCategories': '', 'enable': '', 'numFiles': '', 'maxFileSize': '', 'isActive': '', 'lbmAssignedServices': ''}
            )
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
            print(f"AXL error listProcessNode: ", str(err), file=sys.stderr)
            return False
        

    def CallerFilterList(self, name=''):
        """
        list_caller_filter_list parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listCallerFilterList(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'isAllowedType': '', 'endUserIdName': '', 'DnMask': '', 'callerFilterMask': ''}
            )
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
            print(f"AXL error listCallerFilterList: ", str(err), file=sys.stderr)
            return False
        

    def RoutePartition(self, name=''):
        """
        list_route_partition parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listRoutePartition(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'dialPlanWizardGenId': '', 'timeScheduleIdName': '', 'useOriginatingDeviceTimeZone': '', 'timeZone': '', 'partitionUsage': ''}
            )
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
            print(f"AXL error listRoutePartition: ", str(err), file=sys.stderr)
            return False
        

    def Css(self, name=''):
        """
        list_css parameters
        :param uuid: uuid
        :param description: description
		:param partitionUsage: partitionUsage
		:param name: name
        """
        try:
            resp = self.client.listCss(
                {'name': '%'+name}, returnedTags={'description': '', 'clause': '', 'dialPlanWizardGenId': '', 'partitionUsage': '', 'name': ''}
            )
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
            print(f"AXL error listCss: ", str(err), file=sys.stderr)
            return False
        

    def CallManager(self, name=''):
        """
        list_call_manager parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listCallManager(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'autoRegistration': '', 'processNodeName': '', 'lbmGroup': '', 'tftpDefault': '', 'callManagerName': '', 'priority': ''}
            )
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
            print(f"AXL error listCallManager: ", str(err), file=sys.stderr)
            return False
        

    def ExpresswayCConfiguration(self, name=''):
        """
        list_expressway_c_configuration parameters
        :param uuid: uuid
        :param HostNameOrIP: HostNameOrIP
		:param description: description
        """
        try:
            resp = self.client.listExpresswayCConfiguration(
                {'name': '%'+name}, returnedTags={'HostNameOrIP': '', 'description': '', 'X509SubjectNameorSubjectAlternateName': ''}
            )
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
            print(f"AXL error listExpresswayCConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def MediaResourceGroup(self, name=''):
        """
        list_media_resource_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listMediaResourceGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'multicast': '', 'deviceName': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['None']
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
            print(f"AXL error listMediaResourceGroup: ", str(err), file=sys.stderr)
            return False
        

    def MediaResourceList(self, name=''):
        """
        list_media_resource_list parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listMediaResourceList(
                {'name': '%'+name}, returnedTags={'name': '', 'clause': '', 'mediaResourceGroupName': '', 'order': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['None']
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
            print(f"AXL error listMediaResourceList: ", str(err), file=sys.stderr)
            return False
        

    def Region(self, name=''):
        """
        list_region parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listRegion(
                {'name': '%'+name}, returnedTags={'name': '', 'defaultCodec': '', 'bandwidth': '', 'videoBandwidth': '', 'regionAName': '', 'regionBName': '', 'codecPreference': '', 'regionName': '', 'lossyNetwork': '', 'immersiveVideoBandwidth': ''}
            )
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
            print(f"AXL error listRegion: ", str(err), file=sys.stderr)
            return False
        

    def AarGroup(self, name=''):
        """
        list_aar_group parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listAarGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'prefixDigit': '', 'aarGroupFromName': '', 'aarGroupToName': ''}
            )
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
            print(f"AXL error listAarGroup: ", str(err), file=sys.stderr)
            return False
        

    def PhysicalLocation(self, name=''):
        """
        list_physical_location parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listPhysicalLocation(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listPhysicalLocation: ", str(err), file=sys.stderr)
            return False
        

    def Customer(self, name=''):
        """
        list_customer parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listCustomer(
                {'name': '%'+name}, returnedTags={'name': '', 'createTime': '', 'lastAuditTime': ''}
            )
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
            print(f"AXL error listCustomer: ", str(err), file=sys.stderr)
            return False
        

    def RouteGroup(self, name=''):
        """
        list_route_group parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listRouteGroup(
                {'name': '%'+name}, returnedTags={'dialPlanWizardGenld': '', 'distributionAlgorithm': '', 'name': '', 'deviceSelectionOrder': '', 'dialPlanWizardGenId': '', 'deviceName': '', 'port': ''}
            )
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
            print(f"AXL error listRouteGroup: ", str(err), file=sys.stderr)
            return False
        

    def DevicePool(self, name=''):
        """
        list_device_pool parameters
        :param uuid: uuid
        :param name: name
		:param callManagerGroupName: callManagerGroupName
		:param regionName: regionName
        """
        try:
            resp = self.client.listDevicePool(
                {'name': '%'+name}, returnedTags={'name': '', 'autoSearchSpaceName': '', 'dateTimeSettingName': '', 'callManagerGroupName': '', 'mediaResourceListName': '', 'regionName': '', 'networkLocale': '', 'srstName': '', 'connectionMonitorDuration': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'locationName': '', 'mobilityCssName': '', 'physicalLocationName': '', 'deviceMobilityGroupName': '', 'revertPriority': '', 'singleButtonBarge': '', 'joinAcrossLines': '', 'cgpnTransformationCssName': '', 'cdpnTransformationCssName': '', 'localRouteGroupName': '', 'geoLocationName': '', 'geoLocationFilterName': '', 'callingPartyNationalPrefix': '', 'callingPartyInternationalPrefix': '', 'callingPartyUnknownPrefix': '', 'callingPartySubscriberPrefix': '', 'adjunctCallingSearchSpace': '', 'callingPartyNationalStripDigits': '', 'callingPartyInternationalStripDigits': '', 'callingPartyUnknownStripDigits': '', 'callingPartySubscriberStripDigits': '', 'callingPartyNationalTransformationCssName': '', 'callingPartyInternationalTransformationCssName': '', 'callingPartyUnknownTransformationCssName': '', 'callingPartySubscriberTransformationCssName': '', 'calledPartyNationalPrefix': '', 'calledPartyInternationalPrefix': '', 'calledPartyUnknownPrefix': '', 'calledPartySubscriberPrefix': '', 'calledPartyNationalStripDigits': '', 'calledPartyInternationalStripDigits': '', 'calledPartyUnknownStripDigits': '', 'calledPartySubscriberStripDigits': '', 'calledPartyNationalTransformationCssName': '', 'calledPartyInternationalTransformationCssName': '', 'calledPartyUnknownTransformationCssName': '', 'calledPartySubscriberTransformationCssName': '', 'imeEnrolledPatternGroupName': '', 'localRouteGroup': '', 'mraServiceDomain': '', 'devicePoolName': ''}
            )
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
            print(f"AXL error listDevicePool: ", str(err), file=sys.stderr)
            return False
        

    def DeviceMobilityGroup(self, name=''):
        """
        list_device_mobility_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listDeviceMobilityGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listDeviceMobilityGroup: ", str(err), file=sys.stderr)
            return False
        

    def Location(self, name=''):
        """
        list_location parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listLocation(
                {'name': '%'+name}, returnedTags={'name': '', 'id': '', 'withinAudioBandwidth': '', 'withinVideoBandwidth': '', 'withinImmersiveKbits': '', 'locationName': '', 'rsvpSetting': '', 'weight': '', 'audioBandwidth': '', 'videoBandwidth': '', 'immersiveBandwidth': ''}
            )
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
            print(f"AXL error listLocation: ", str(err), file=sys.stderr)
            return False
        

    def SoftKeyTemplate(self, name=''):
        """
        list_soft_key_template parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listSoftKeyTemplate(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'baseSoftkeyTemplateName': ''}
            )
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
            print(f"AXL error listSoftKeyTemplate: ", str(err), file=sys.stderr)
            return False
        

    def Transcoder(self, name=''):
        """
        list_transcoder parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listTranscoder(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'subUnit': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'loadInformation': '', 'isTrustedRelayPoint': '', 'maximumCapacity': ''}
            )
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
            print(f"AXL error listTranscoder: ", str(err), file=sys.stderr)
            return False
        

    def CommonDeviceConfig(self, name=''):
        """
        list_common_device_config parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listCommonDeviceConfig(
                {'name': '%'+name}, returnedTags={'name': '', 'softkeyTemplateName': '', 'userLocale': '', 'networkHoldMohAudioSourceId': '', 'userHoldMohAudioSourceId': '', 'mlppIndicationStatus': '', 'useTrustedRelayPoint': '', 'preemption': '', 'ipAddressingMode': '', 'ipAddressingModePreferenceControl': '', 'allowAutoConfigurationForPhones': '', 'useImeForOutboundCalls': '', 'confidentialAccess': '', 'allowDuplicateAddressDetection': '', 'acceptRedirectMessages': '', 'replyMulticastEchoRequest': ''}
            )
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
            print(f"AXL error listCommonDeviceConfig: ", str(err), file=sys.stderr)
            return False
        

    def ResourcePriorityNamespace(self, name=''):
        """
        list_resource_priority_namespace parameters
        :param uuid: uuid
        :param namespace: namespace
		:param description: description
        """
        try:
            resp = self.client.listResourcePriorityNamespace(
                {'name': '%'+name}, returnedTags={'namespace': '', 'description': '', 'name': '', 'resourcePriorityNamespaceName': '', 'index': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['None']
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
            print(f"AXL error listResourcePriorityNamespace: ", str(err), file=sys.stderr)
            return False
        

    def ResourcePriorityNamespaceList(self, name=''):
        """
        list_resource_priority_namespace_list parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listResourcePriorityNamespaceList(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'resourcePriorityNamespaceName': '', 'index': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['None']
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
            print(f"AXL error listResourcePriorityNamespaceList: ", str(err), file=sys.stderr)
            return False
        

    def DeviceMobility(self, name=''):
        """
        list_device_mobility parameters
        :param uuid: uuid
        :param name: name
		:param subNet: subNet
		:param subNetMaskSz: subNetMaskSz
        """
        try:
            resp = self.client.listDeviceMobility(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'subNetDetails': ''}
            )
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
            print(f"AXL error listDeviceMobility: ", str(err), file=sys.stderr)
            return False
        

    def CmcInfo(self, name=''):
        """
        list_cmc_info parameters
        :param uuid: uuid
        :param code: code
        """
        try:
            resp = self.client.listCmcInfo(
                {'name': '%'+name}, returnedTags={'code': '', 'description': ''}
            )
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
            print(f"AXL error listCmcInfo: ", str(err), file=sys.stderr)
            return False
        

    def CredentialPolicy(self, name=''):
        """
        list_credential_policy parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listCredentialPolicy(
                {'name': '%'+name}, returnedTags={'name': '', 'failedLogon': '', 'resetFailedLogonAttempts': '', 'lockoutDuration': '', 'credChangeDuration': '', 'credExpiresAfter': '', 'minCredLength': '', 'prevCredStoredNum': '', 'inactiveDaysAllowed': '', 'expiryWarningDays': '', 'trivialCredCheck': '', 'minCharsToChange': '', 'credentialUser': '', 'credentialType': '', 'credPolicyName': '', 'credentials': '', 'confirmCredentials': '', 'credUserCantChange': '', 'credUserMustChange': '', 'credDoesNotExpire': ''}
            )
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
            print(f"AXL error listCredentialPolicy: ", str(err), file=sys.stderr)
            return False
        

    def FacInfo(self, name=''):
        """
        list_fac_info parameters
        :param uuid: uuid
        :param name: name
		:param code: code
		:param authorizationLevel: authorizationLevel
        """
        try:
            resp = self.client.listFacInfo(
                {'name': '%'+name}, returnedTags={'name': '', 'code': '', 'authorizationLevel': ''}
            )
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
            print(f"AXL error listFacInfo: ", str(err), file=sys.stderr)
            return False
        

    def HuntList(self, name=''):
        """
        list_hunt_list parameters
        :param uuid: uuid
        :param description: description
		:param name: name
        """
        try:
            resp = self.client.listHuntList(
                {'name': '%'+name}, returnedTags={'description': '', 'callManagerGroupName': '', 'routeListEnabled': '', 'voiceMailUsage': '', 'name': '', 'lineGroupName': '', 'selectionOrder': ''}
            )
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
            print(f"AXL error listHuntList: ", str(err), file=sys.stderr)
            return False
        

    def IvrUserLocale(self, name=''):
        """
        list_ivr_user_locale parameters
        :param uuid: uuid
        :param userLocale: userLocale
        """
        try:
            resp = self.client.listIvrUserLocale(
                {'name': '%'+name}, returnedTags={'userLocale': '', 'orderIndex': ''}
            )
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
            print(f"AXL error listIvrUserLocale: ", str(err), file=sys.stderr)
            return False
        

    def LineGroup(self, name=''):
        """
        list_line_group parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listLineGroup(
                {'name': '%'+name}, returnedTags={'distributionAlgorithm': '', 'rnaReversionTimeOut': '', 'huntAlgorithmNoAnswer': '', 'huntAlgorithmBusy': '', 'huntAlgorithmNotAvailable': '', 'name': '', 'autoLogOffHunt': '', 'lineSelectionOrder': '', 'directoryNumber': ''}
            )
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
            print(f"AXL error listLineGroup: ", str(err), file=sys.stderr)
            return False
        

    def RecordingProfile(self, name=''):
        """
        list_recording_profile parameters
        :param uuid: uuid
        :param name: name
		:param recordingCssName: recordingCssName
		:param recorderDestination: recorderDestination
        """
        try:
            resp = self.client.listRecordingProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'recordingCssName': '', 'recorderDestination': ''}
            )
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
            print(f"AXL error listRecordingProfile: ", str(err), file=sys.stderr)
            return False
        

    def RouteFilter(self, name=''):
        """
        list_route_filter parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listRouteFilter(
                {'name': '%'+name}, returnedTags={'name': '', 'clause': '', 'dialPlanName': '', 'dialPlanWizardGenId': '', 'dialPlanTagName': '', 'digits': '', 'operator': '', 'priority': ''}
            )
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
            print(f"AXL error listRouteFilter: ", str(err), file=sys.stderr)
            return False
        

    def CallManagerGroup(self, name=''):
        """
        list_call_manager_group parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listCallManagerGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'tftpDefault': ''}
            )
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
            print(f"AXL error listCallManagerGroup: ", str(err), file=sys.stderr)
            return False
        

    def UserGroup(self, name=''):
        """
        list_user_group parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listUserGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'userId': '', 'roleName': ''}
            )
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
            print(f"AXL error listUserGroup: ", str(err), file=sys.stderr)
            return False
        

    def DialPlan(self, name=''):
        """
        list_dial_plan parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listDialPlan(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'dialPlanName': '', 'operator': '', 'suppressFromRouteFilter': ''}
            )
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
            print(f"AXL error listDialPlan: ", str(err), file=sys.stderr)
            return False
        

    def DialPlanTag(self, name=''):
        """
        list_dial_plan_tag parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listDialPlanTag(
                {'name': '%'+name}, returnedTags={'name': '', 'dialPlanName': '', 'operator': '', 'suppressFromRouteFilter': ''}
            )
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
            print(f"AXL error listDialPlanTag: ", str(err), file=sys.stderr)
            return False
        

    def Ddi(self, name=''):
        """
        list_ddi parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listDdi(
                {'name': '%'+name}, returnedTags={'name': '', 'clause': '', 'dialPlanName': '', 'digitAnalysisId': ''}
            )
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
            print(f"AXL error listDdi: ", str(err), file=sys.stderr)
            return False
        

    def MobileSmartClientProfile(self, name=''):
        """
        list_mobile_smart_client_profile parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listMobileSmartClientProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'mobileSmartClient': '', 'enableSnrUri': '', 'enableCFAUri': '', 'handOffUri': ''}
            )
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
            print(f"AXL error listMobileSmartClientProfile: ", str(err), file=sys.stderr)
            return False
        

    def ProcessNodeService(self, name=''):
        """
        list_process_node_service parameters
        :param uuid: uuid
        :param processNodeName: processNodeName
        """
        try:
            resp = self.client.listProcessNodeService(
                {'name': '%'+name}, returnedTags={'processNodeName': '', 'service': '', 'traceLevel': '', 'userCategories': '', 'enable': '', 'numFiles': '', 'maxFileSize': '', 'isActive': ''}
            )
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
            print(f"AXL error listProcessNodeService: ", str(err), file=sys.stderr)
            return False
        

    def MohAudioSource(self, name=''):
        """
        list_moh_audio_source parameters
        :param uuid: uuid
        :param sourceId: sourceId
		:param name: name
        """
        try:
            resp = self.client.listMohAudioSource(
                {'name': '%'+name}, returnedTags={'sourceId': '', 'name': '', 'sourceFile': '', 'multicast': '', 'mohFileStatus': '', 'initialAnnouncement': '', 'periodicAnnouncement': '', 'periodicAnnouncementInterval': '', 'localeAnnouncement': '', 'initialAnnouncementPlayed': ''}
            )
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
            print(f"AXL error listMohAudioSource: ", str(err), file=sys.stderr)
            return False
        

    def DhcpServer(self, name=''):
        """
        list_dhcp_server parameters
        :param uuid: uuid
        :param processNodeName: processNodeName
		:param primaryDnsIpAddress: primaryDnsIpAddress
		:param secondaryDnsIpAddress: secondaryDnsIpAddress
		:param domainName: domainName
        """
        try:
            resp = self.client.listDhcpServer(
                {'name': '%'+name}, returnedTags={'processNodeName': '', 'primaryDnsIpAddress': '', 'secondaryDnsIpAddress': '', 'primaryTftpServerIpAddress': '', 'secondaryTftpServerIpAddress': '', 'bootstrapServerIpAddress': '', 'domainName': '', 'tftpServerName': '', 'arpCacheTimeout': '', 'ipAddressLeaseTime': '', 'renewalTime': '', 'rebindingTime': ''}
            )
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
            print(f"AXL error listDhcpServer: ", str(err), file=sys.stderr)
            return False
        

    def DhcpSubnet(self, name=''):
        """
        list_dhcp_subnet parameters
        :param uuid: uuid
        :param dhcpServerName: dhcpServerName
		:param subnetIpAddress: subnetIpAddress
		:param primaryStartIpAddress: primaryStartIpAddress
		:param primaryEndIpAddress: primaryEndIpAddress
		:param secondaryStartIpAddress: secondaryStartIpAddress
		:param secondaryEndIpAddress: secondaryEndIpAddress
        """
        try:
            resp = self.client.listDhcpSubnet(
                {'name': '%'+name}, returnedTags={'subnetIpAddress': '', 'primaryStartIpAddress': '', 'primaryEndIpAddress': '', 'secondaryStartIpAddress': '', 'secondaryEndIpAddress': '', 'primaryRouterIpAddress': '', 'secondaryRouterIpAddress': '', 'subnetMask': '', 'domainName': '', 'primaryDnsIpAddress': '', 'secondaryDnsIpAddress': '', 'tftpServerName': '', 'primaryTftpServerIpAddress': '', 'secondaryTftpServerIpAddress': '', 'bootstrapServerIpAddress': '', 'arpCacheTimeout': '', 'ipAddressLeaseTime': '', 'renewalTime': '', 'rebindingTime': ''}
            )
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
            print(f"AXL error listDhcpSubnet: ", str(err), file=sys.stderr)
            return False
        

    def CallPark(self, name=''):
        """
        list_call_park parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
		:param callManagerName: callManagerName
        """
        try:
            resp = self.client.listCallPark(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'callManagerName': ''}
            )
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
            print(f"AXL error listCallPark: ", str(err), file=sys.stderr)
            return False
        

    def DirectedCallPark(self, name=''):
        """
        list_directed_call_park parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
		:param reversionPattern: reversionPattern
        """
        try:
            resp = self.client.listDirectedCallPark(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'retrievalPrefix': '', 'reversionPattern': '', 'revertCssName': ''}
            )
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
            print(f"AXL error listDirectedCallPark: ", str(err), file=sys.stderr)
            return False
        

    def MeetMe(self, name=''):
        """
        list_meet_me parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
        """
        try:
            resp = self.client.listMeetMe(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'minimumSecurityLevel': ''}
            )
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
            print(f"AXL error listMeetMe: ", str(err), file=sys.stderr)
            return False
        

    def ConferenceNow(self, name=''):
        """
        list_conference_now parameters
        :param uuid: uuid
        :param conferenceNowNumber: conferenceNowNumber
		:param routePartitionName: routePartitionName
        """
        try:
            resp = self.client.listConferenceNow(
                {'name': '%'+name}, returnedTags={'conferenceNowNumber': '', 'routePartitionName': '', 'description': '', 'maxWaitTimeForHost': '', 'MohAudioSourceId': ''}
            )
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
            print(f"AXL error listConferenceNow: ", str(err), file=sys.stderr)
            return False
        

    def RouteList(self, name=''):
        """
        list_route_list parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listRouteList(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'callManagerGroupName': '', 'routeListEnabled': '', 'runOnEveryNode': '', 'routeGroupName': '', 'selectionOrder': '', 'calledPartyTransformationMask': '', 'callingPartyTransformationMask': '', 'dialPlanWizardGenId': '', 'digitDiscardInstructionName': '', 'callingPartyPrefixDigits': '', 'prefixDigitsOut': '', 'useFullyQualifiedCallingPartyNumber': '', 'callingPartyNumberingPlan': '', 'callingPartyNumberType': '', 'calledPartyNumberingPlan': '', 'calledPartyNumberType': ''}
            )
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
            print(f"AXL error listRouteList: ", str(err), file=sys.stderr)
            return False
        

    def User(self, name=''):
        """
        list_user parameters
        :param uuid: uuid
        :param firstName: firstName
		:param lastName: lastName
		:param userid: userid
		:param department: department
		:param customerName: customerName
        """
        try:
            resp = self.client.listUser(
                {'name': '%'+name}, returnedTags={'name': '', 'firstName': '', 'middleName': '', 'lastName': '', 'emMaxLoginTime': '', 'userid': '', 'mailid': '', 'department': '', 'manager': '', 'userLocale': '', 'primaryExtension': '', 'associatedPc': '', 'enableCti': '', 'subscribeCallingSearchSpaceName': '', 'enableMobility': '', 'enableMobileVoiceAccess': '', 'maxDeskPickupWaitTime': '', 'remoteDestinationLimit': '', 'status': '', 'enableEmcc': '', 'patternPrecedence': '', 'numericUserId': '', 'mlppPassword': '', 'homeCluster': '', 'imAndPresenceEnable': '', 'serviceProfile': '', 'directoryUri': '', 'telephoneNumber': '', 'title': '', 'mobileNumber': '', 'homeNumber': '', 'pagerNumber': '', 'calendarPresence': '', 'userIdentity': '', 'customerName': '', 'userId': '', 'password': '', 'pin': '', 'productType': '', 'dnCssName': '', 'phoneCssName': '', 'e164Mask': '', 'extension': '', 'routePartitionName': '', 'voiceMailProfileName': '', 'enableExtensionMobility': '', 'DirectoryURI': '', 'DirectoryNumberURIPartition': '', 'description': '', 'allowProvision': '', 'limitProvision': '', 'allowPhoneReassign': '', 'defaultUserProfile': '', 'allowProvisionEMMaxLoginTime': '', 'roleName': ''}
            )
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
            print(f"AXL error listUser: ", str(err), file=sys.stderr)
            return False
        

    def AppUser(self, name=''):
        """
        list_app_user parameters
        :param uuid: uuid
        :param userid: userid
        """
        try:
            resp = self.client.listAppUser(
                {'name': '%'+name}, returnedTags={'userid': '', 'presenceGroupName': '', 'acceptPresenceSubscription': '', 'acceptOutOfDialogRefer': '', 'acceptUnsolicitedNotification': '', 'allowReplaceHeader': '', 'isStandard': ''}
            )
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
            print(f"AXL error listAppUser: ", str(err), file=sys.stderr)
            return False
        

    def SipRealm(self, name=''):
        """
        list_sip_realm parameters
        :param uuid: uuid
        :param realm: realm
		:param userid: userid
        """
        try:
            resp = self.client.listSipRealm(
                {'name': '%'+name}, returnedTags={'realm': '', 'userid': '', 'digestCredentials': ''}
            )
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
            print(f"AXL error listSipRealm: ", str(err), file=sys.stderr)
            return False
        

    def PhoneNtp(self, name=''):
        """
        list_phone_ntp parameters
        :param uuid: uuid
        :param ipAddress: ipAddress
		:param ipv6Address: ipv6Address
		:param description: description
        """
        try:
            resp = self.client.listPhoneNtp(
                {'name': '%'+name}, returnedTags={'ipAddress': '', 'ipv6Address': '', 'description': '', 'mode': ''}
            )
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
            print(f"AXL error listPhoneNtp: ", str(err), file=sys.stderr)
            return False
        

    def DateTimeGroup(self, name=''):
        """
        list_date_time_group parameters
        :param uuid: uuid
        :param name: name
		:param timeZone: timeZone
        """
        try:
            resp = self.client.listDateTimeGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'timeZone': '', 'dateformat': '', 'phoneNtpName': '', 'selectionOrder': ''}
            )
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
            print(f"AXL error listDateTimeGroup: ", str(err), file=sys.stderr)
            return False
        

    def PresenceGroup(self, name=''):
        """
        list_presence_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listPresenceGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'presenceGroupName': '', 'subscriptionPermission': ''}
            )
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
            print(f"AXL error listPresenceGroup: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocation(self, name=''):
        """
        list_geo_location parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listGeoLocation(
                {'name': '%'+name}, returnedTags={'name': '', 'country': '', 'description': '', 'nationalSubDivision': '', 'district': '', 'communityName': '', 'cityDivision': '', 'neighbourhood': '', 'street': '', 'leadingStreetDirection': '', 'trailingStreetSuffix': '', 'streetSuffix': '', 'houseNumber': '', 'houseNumberSuffix': '', 'landmark': '', 'location': '', 'floor': '', 'occupantName': '', 'postalCode': '', 'useCountry': '', 'useNationalSubDivision': '', 'useDistrict': '', 'useCommunityName': '', 'useCityDivision': '', 'useNeighbourhood': '', 'useStreet': '', 'useLeadingStreetDirection': '', 'useTrailingStreetSuffix': '', 'useStreetSuffix': '', 'useHouseNumber': '', 'useHouseNumberSuffix': '', 'useLandmark': '', 'useLocation': '', 'useFloor': '', 'useOccupantName': '', 'usePostalCode': ''}
            )
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
            print(f"AXL error listGeoLocation: ", str(err), file=sys.stderr)
            return False
        

    def Srst(self, name=''):
        """
        list_srst parameters
        :param uuid: uuid
        :param name: name
		:param ipAddress: ipAddress
        """
        try:
            resp = self.client.listSrst(
                {'name': '%'+name}, returnedTags={'name': '', 'port': '', 'ipAddress': '', 'ipv6Address': '', 'SipNetwork': '', 'SipPort': '', 'srstCertificatePort': '', 'isSecure': ''}
            )
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
            print(f"AXL error listSrst: ", str(err), file=sys.stderr)
            return False
        

    def MlppDomain(self, name=''):
        """
        list_mlpp_domain parameters
        :param uuid: uuid
        :param domainName: domainName
        """
        try:
            resp = self.client.listMlppDomain(
                {'name': '%'+name}, returnedTags={'domainName': '', 'domainId': ''}
            )
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
            print(f"AXL error listMlppDomain: ", str(err), file=sys.stderr)
            return False
        

    def CumaServerSecurityProfile(self, name=''):
        """
        list_cuma_server_security_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listCumaServerSecurityProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'securityMode': '', 'transportType': '', 'x509SubjectName': '', 'serverIpHostName': ''}
            )
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
            print(f"AXL error listCumaServerSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationServer(self, name=''):
        """
        list_application_server parameters
        :param uuid: uuid
        :param name: name
		:param ipAddress: ipAddress
        """
        try:
            resp = self.client.listApplicationServer(
                {'name': '%'+name}, returnedTags={'appServerType': '', 'name': '', 'ipAddress': '', 'url': '', 'endUserUrl': '', 'processNodeName': ''}
            )
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
            print(f"AXL error listApplicationServer: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationUserCapfProfile(self, name=''):
        """
        list_application_user_capf_profile parameters
        :param uuid: uuid
        :param applicationUser: applicationUser
		:param instanceId: instanceId
        """
        try:
            resp = self.client.listApplicationUserCapfProfile(
                {'name': '%'+name}, returnedTags={'applicationUser': '', 'instanceId': '', 'certificateOperation': '', 'authenticationMode': '', 'authenticationString': '', 'keySize': '', 'keyOrder': '', 'ecKeySize': '', 'operationCompletion': '', 'certificationOperationStatus': ''}
            )
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
            print(f"AXL error listApplicationUserCapfProfile: ", str(err), file=sys.stderr)
            return False
        

    def EndUserCapfProfile(self, name=''):
        """
        list_end_user_capf_profile parameters
        :param uuid: uuid
        :param endUserId: endUserId
		:param instanceId: instanceId
        """
        try:
            resp = self.client.listEndUserCapfProfile(
                {'name': '%'+name}, returnedTags={'endUserId': '', 'instanceId': '', 'certificationOperation': '', 'authenticationMode': '', 'authenticationString': '', 'keySize': '', 'keyOrder': '', 'ecKeySize': '', 'operationCompletion': '', 'certificationOperationStatus': ''}
            )
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
            print(f"AXL error listEndUserCapfProfile: ", str(err), file=sys.stderr)
            return False
        

    def ServiceParameter(self, name=''):
        """
        list_service_parameter parameters
        :param uuid: uuid
        :param processNodeName: processNodeName
		:param service: service
        """
        try:
            resp = self.client.listServiceParameter(
                {'name': '%'+name}, returnedTags={'processNodeName': '', 'name': '', 'service': '', 'value': '', 'valueType': ''}
            )
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
            print(f"AXL error listServiceParameter: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocationFilter(self, name=''):
        """
        list_geo_location_filter parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listGeoLocationFilter(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'useCountry': '', 'useNationalSubDivision': '', 'useDistrict': '', 'useCommunityName': '', 'useCityDivision': '', 'useNeighbourhood': '', 'useStreet': '', 'useLeadingStreetDirection': '', 'useTrailingStreetSuffix': '', 'useStreetSuffix': '', 'useHouseNumber': '', 'useHouseNumberSuffix': '', 'useLandmark': '', 'useLocation': '', 'useFloor': '', 'useOccupantName': '', 'usePostalCode': ''}
            )
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
            print(f"AXL error listGeoLocationFilter: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailProfile(self, name=''):
        """
        list_voice_mail_profile parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listVoiceMailProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'isDefault': '', 'voiceMailboxMask': ''}
            )
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
            print(f"AXL error listVoiceMailProfile: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailPort(self, name=''):
        """
        list_voice_mail_port parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
		:param securityProfileName: securityProfileName
		:param dnPattern: dnPattern
        """
        try:
            resp = self.client.listVoiceMailPort(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'locationName': '', 'preemption': '', 'useTrustedRelayPoint': '', 'securityProfileName': '', 'geoLocationName': '', 'automatedAlternateRoutingCssName': '', 'dnPattern': '', 'callerIdDisplay': '', 'callerIdDisplayAscii': '', 'externalMask': ''}
            )
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
            print(f"AXL error listVoiceMailPort: ", str(err), file=sys.stderr)
            return False
        

    def Gatekeeper(self, name=''):
        """
        list_gatekeeper parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listGatekeeper(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'rrqTimeToLive': '', 'retryTimeout': '', 'enableDevice': ''}
            )
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
            print(f"AXL error listGatekeeper: ", str(err), file=sys.stderr)
            return False
        

    def PhoneButtonTemplate(self, name=''):
        """
        list_phone_button_template parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listPhoneButtonTemplate(
                {'name': '%'+name}, returnedTags={'name': '', 'isUserModifiable': ''}
            )
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
            print(f"AXL error listPhoneButtonTemplate: ", str(err), file=sys.stderr)
            return False
        

    def CommonPhoneConfig(self, name=''):
        """
        list_common_phone_config parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listCommonPhoneConfig(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'dndOption': '', 'dndAlertingType': '', 'backgroundImage': '', 'phonePersonalization': '', 'phoneServiceDisplay': '', 'sshUserId': '', 'alwaysUsePrimeLine': '', 'alwaysUsePrimeLineForVoiceMessage': '', 'vpnGroupName': '', 'vpnProfileName': '', 'featureControlPolicy': ''}
            )
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
            print(f"AXL error listCommonPhoneConfig: ", str(err), file=sys.stderr)
            return False
        

    def MessageWaiting(self, name=''):
        """
        list_message_waiting parameters
        :param uuid: uuid
        :param pattern: pattern
		:param routePartitionName: routePartitionName
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
        """
        try:
            resp = self.client.listMessageWaiting(
                {'name': '%'+name}, returnedTags={'pattern': '', 'routePartitionName': '', 'description': '', 'messageWaitingIndicator': '', 'callingSearchSpaceName': ''}
            )
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
            print(f"AXL error listMessageWaiting: ", str(err), file=sys.stderr)
            return False
        

    def IpPhoneServices(self, name=''):
        """
        list_ip_phone_services parameters
        :param uuid: uuid
        :param serviceName: serviceName
		:param serviceDescription: serviceDescription
        """
        try:
            resp = self.client.listIpPhoneServices(
                {'name': '%'+name}, returnedTags={'serviceName': '', 'asciiServiceName': '', 'serviceDescription': '', 'serviceUrl': '', 'secureServiceUrl': '', 'serviceCategory': '', 'serviceType': '', 'serviceVendor': '', 'serviceVersion': '', 'enabled': '', 'enterpriseSubscription': '', 'name': '', 'displayName': '', 'default': '', 'description': '', 'paramRequired': '', 'paramPassword': ''}
            )
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
            print(f"AXL error listIpPhoneServices: ", str(err), file=sys.stderr)
            return False
        

    def CtiRoutePoint(self, name=''):
        """
        list_cti_route_point parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listCtiRoutePoint(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'locationName': '', 'mediaResourceListName': '', 'networkHoldMohAudioSourceId': '', 'userHoldMohAudioSourceId': '', 'useTrustedRelayPoint': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'userLocale': ''}
            )
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
            print(f"AXL error listCtiRoutePoint: ", str(err), file=sys.stderr)
            return False
        

    def TransPattern(self, name=''):
        """
        list_trans_pattern parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
		:param isEmergencyServiceNumber: isEmergencyServiceNumber
        """
        try:
            resp = self.client.listTransPattern(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'blockEnable': '', 'calledPartyTransformationMask': '', 'callingPartyTransformationMask': '', 'useCallingPartyPhoneMask': '', 'callingPartyPrefixDigits': '', 'dialPlanName': '', 'digitDiscardInstructionName': '', 'patternUrgency': '', 'prefixDigitsOut': '', 'routeFilterName': '', 'callingLinePresentationBit': '', 'callingNamePresentationBit': '', 'connectedLinePresentationBit': '', 'connectedNamePresentationBit': '', 'patternPrecedence': '', 'provideOutsideDialtone': '', 'callingPartyNumberingPlan': '', 'callingPartyNumberType': '', 'calledPartyNumberingPlan': '', 'calledPartyNumberType': '', 'callingSearchSpaceName': '', 'resourcePriorityNamespaceName': '', 'routeNextHopByCgpn': '', 'routeClass': '', 'callInterceptProfileName': '', 'releaseClause': '', 'useOriginatorCss': '', 'dontWaitForIDTOnSubsequentHops': '', 'isEmergencyServiceNumber': ''}
            )
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
            print(f"AXL error listTransPattern: ", str(err), file=sys.stderr)
            return False
        

    def CallingPartyTransformationPattern(self, name=''):
        """
        list_calling_party_transformation_pattern parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
		:param dialPlanName: dialPlanName
		:param routeFilterName: routeFilterName
        """
        try:
            resp = self.client.listCallingPartyTransformationPattern(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'callingPartyTransformationMask': '', 'useCallingPartyPhoneMask': '', 'dialPlanName': '', 'digitDiscardInstructionName': '', 'patternUrgency': '', 'callingPartyPrefixDigits': '', 'routeFilterName': '', 'callingLinePresentationBit': '', 'callingPartyNumberingPlan': '', 'callingPartyNumberType': '', 'mlppPreemptionDisabled': ''}
            )
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
            print(f"AXL error listCallingPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
        

    def SipRoutePattern(self, name=''):
        """
        list_sip_route_pattern parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
		:param dnOrPatternIpv6: dnOrPatternIpv6
        """
        try:
            resp = self.client.listSipRoutePattern(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'blockEnable': '', 'callingPartyTransformationMask': '', 'useCallingPartyPhoneMask': '', 'callingPartyPrefixDigits': '', 'callingLinePresentationBit': '', 'callingNamePresentationBit': '', 'connectedLinePresentationBit': '', 'connectedNamePresentationBit': '', 'sipTrunkName': '', 'dnOrPatternIpv6': '', 'routeOnUserPart': '', 'useCallerCss': '', 'domainRoutingCssName': ''}
            )
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
            print(f"AXL error listSipRoutePattern: ", str(err), file=sys.stderr)
            return False
        

    def HuntPilot(self, name=''):
        """
        list_hunt_pilot parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
        """
        try:
            resp = self.client.listHuntPilot(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'blockEnable': '', 'calledPartyTransformationMask': '', 'callingPartyTransformationMask': '', 'useCallingPartyPhoneMask': '', 'callingPartyPrefixDigits': '', 'dialPlanName': '', 'digitDiscardInstructionName': '', 'patternUrgency': '', 'prefixDigitsOut': '', 'routeFilterName': '', 'callingLinePresentationBit': '', 'callingNamePresentationBit': '', 'connectedLinePresentationBit': '', 'connectedNamePresentationBit': '', 'patternPrecedence': '', 'provideOutsideDialtone': '', 'callingPartyNumberingPlan': '', 'callingPartyNumberType': '', 'calledPartyNumberingPlan': '', 'calledPartyNumberType': '', 'huntListName': '', 'parkMonForwardNoRetrieve': '', 'alertingName': '', 'asciiAlertingName': '', 'aarNeighborhoodName': '', 'forwardHuntNoAnswer': '', 'forwardHuntBusy': '', 'callPickupGroupName': '', 'maxHuntduration': '', 'releaseClause': '', 'displayConnectedNumber': '', 'queueCalls': ''}
            )
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
            print(f"AXL error listHuntPilot: ", str(err), file=sys.stderr)
            return False
        

    def RoutePattern(self, name=''):
        """
        list_route_pattern parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
		:param isEmergencyServiceNumber: isEmergencyServiceNumber
        """
        try:
            resp = self.client.listRoutePattern(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'blockEnable': '', 'calledPartyTransformationMask': '', 'callingPartyTransformationMask': '', 'useCallingPartyPhoneMask': '', 'callingPartyPrefixDigits': '', 'dialPlanName': '', 'dialPlanWizardGenId': '', 'digitDiscardInstructionName': '', 'networkLocation': '', 'patternUrgency': '', 'prefixDigitsOut': '', 'routeFilterName': '', 'callingLinePresentationBit': '', 'callingNamePresentationBit': '', 'connectedLinePresentationBit': '', 'connectedNamePresentationBit': '', 'supportOverlapSending': '', 'patternPrecedence': '', 'releaseClause': '', 'allowDeviceOverride': '', 'provideOutsideDialtone': '', 'callingPartyNumberingPlan': '', 'callingPartyNumberType': '', 'calledPartyNumberingPlan': '', 'calledPartyNumberType': '', 'authorizationCodeRequired': '', 'authorizationLevelRequired': '', 'clientCodeRequired': '', 'withTag': '', 'withValueClause': '', 'resourcePriorityNamespaceName': '', 'routeClass': '', 'externalCallControl': '', 'isEmergencyServiceNumber': ''}
            )
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
            print(f"AXL error listRoutePattern: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationDialRules(self, name=''):
        """
        list_application_dial_rules parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param numberBeginWith: numberBeginWith
        """
        try:
            resp = self.client.listApplicationDialRules(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'numberBeginWith': '', 'numberOfDigits': '', 'digitsToBeRemoved': '', 'prefixPattern': '', 'priority': ''}
            )
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
            print(f"AXL error listApplicationDialRules: ", str(err), file=sys.stderr)
            return False
        

    def DirectoryLookupDialRules(self, name=''):
        """
        list_directory_lookup_dial_rules parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param numberBeginWith: numberBeginWith
        """
        try:
            resp = self.client.listDirectoryLookupDialRules(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'numberBeginWith': '', 'numberOfDigits': '', 'digitsToBeRemoved': '', 'prefixPattern': '', 'priority': ''}
            )
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
            print(f"AXL error listDirectoryLookupDialRules: ", str(err), file=sys.stderr)
            return False
        

    def PhoneSecurityProfile(self, name=''):
        """
        list_phone_security_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listPhoneSecurityProfile(
                {'name': '%'+name}, returnedTags={'phoneType': '', 'protocol': '', 'name': '', 'description': '', 'deviceSecurityMode': '', 'authenticationMode': '', 'keySize': '', 'keyOrder': '', 'ecKeySize': '', 'tftpEncryptedConfig': '', 'EnableOAuthAuthentication': '', 'nonceValidityTime': '', 'transportType': '', 'sipPhonePort': '', 'enableDigestAuthentication': '', 'excludeDigestCredentials': ''}
            )
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
            print(f"AXL error listPhoneSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def SipDialRules(self, name=''):
        """
        list_sip_dial_rules parameters
        :param uuid: uuid
        :param dialPattern: dialPattern
		:param name: name
        """
        try:
            resp = self.client.listSipDialRules(
                {'name': '%'+name}, returnedTags={'dialPattern': '', 'name': '', 'description': ''}
            )
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
            print(f"AXL error listSipDialRules: ", str(err), file=sys.stderr)
            return False
        

    def ConferenceBridge(self, name=''):
        """
        list_conference_bridge parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listConferenceBridge(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'locationName': '', 'subUnit': '', 'loadInformation': '', 'maximumCapacity': '', 'useTrustedRelayPoint': '', 'securityProfileName': '', 'destinationAddress': '', 'mcuConferenceBridgeSipPort': '', 'sipProfile': '', 'srtpAllowed': '', 'normalizationScript': '', 'enableTrace': '', 'userName': '', 'password': '', 'httpPort': '', 'useHttps': '', 'conferenceBridgePrefix': '', 'allowCFBControlOfCallSecurityIcon': '', 'overrideSIPTrunkAddress': '', 'sipTrunkName': ''}
            )
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
            print(f"AXL error listConferenceBridge: ", str(err), file=sys.stderr)
            return False
        

    def Annunciator(self, name=''):
        """
        list_annunciator parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listAnnunciator(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'devicePoolName': '', 'locationName': '', 'useTrustedRelayPoint': '', 'serverName': ''}
            )
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
            print(f"AXL error listAnnunciator: ", str(err), file=sys.stderr)
            return False
        

    def InteractiveVoiceResponse(self, name=''):
        """
        list_interactive_voice_response parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listInteractiveVoiceResponse(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'devicePoolName': '', 'locationName': '', 'useTrustedRelayPoint': '', 'serverName': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['None']
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
            print(f"AXL error listInteractiveVoiceResponse: ", str(err), file=sys.stderr)
            return False
        

    def Mtp(self, name=''):
        """
        list_mtp parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listMtp(
                {'name': '%'+name}, returnedTags={'mtpType': '', 'name': '', 'description': '', 'devicePoolName': '', 'trustedRelayPoint': ''}
            )
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
            print(f"AXL error listMtp: ", str(err), file=sys.stderr)
            return False
        

    def RemoteDestinationProfile(self, name=''):
        """
        list_remote_destination_profile parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listRemoteDestinationProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'networkHoldMohAudioSourceId': '', 'userHoldMohAudioSourceId': '', 'callInfoPrivacyStatus': '', 'userId': '', 'ignorePresentationIndicators': '', 'rerouteCallingSearchSpaceName': '', 'cgpnTransformationCssName': '', 'automatedAlternateRoutingCssName': '', 'useDevicePoolCgpnTransformCss': '', 'userLocale': '', 'networkLocale': '', 'primaryPhoneName': '', 'dndOption': '', 'dndStatus': '', 'mobileSmartClientProfileName': ''}
            )
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
            print(f"AXL error listRemoteDestinationProfile: ", str(err), file=sys.stderr)
            return False
        

    def Line(self, name=''):
        """
        list_line parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param usage: usage
		:param routePartitionName: routePartitionName
        """
        try:
            resp = self.client.listLine(
                {'name': '%'+name}, returnedTags={'distributionAlgorithm': '', 'rnaReversionTimeOut': '', 'huntAlgorithmNoAnswer': '', 'huntAlgorithmBusy': '', 'huntAlgorithmNotAvailable': '', 'name': '', 'autoLogOffHunt': '', 'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'aarNeighborhoodName': '', 'aarDestinationMask': '', 'aarKeepCallHistory': '', 'aarVoiceMailEnabled': '', 'callPickupGroupName': '', 'autoAnswer': '', 'networkHoldMohAudioSourceId': '', 'userHoldMohAudioSourceId': '', 'callingIdPresentationWhenDiverted': '', 'alertingName': '', 'asciiAlertingName': '', 'presenceGroupName': '', 'shareLineAppearanceCssName': '', 'voiceMailProfileName': '', 'patternPrecedence': '', 'releaseClause': '', 'hrDuration': '', 'hrInterval': '', 'cfaCssPolicy': '', 'defaultActivatedDeviceName': '', 'parkMonForwardNoRetrieveDn': '', 'parkMonForwardNoRetrieveIntDn': '', 'parkMonForwardNoRetrieveVmEnabled': '', 'parkMonForwardNoRetrieveIntVmEnabled': '', 'parkMonForwardNoRetrieveCssName': '', 'parkMonForwardNoRetrieveIntCssName': '', 'parkMonReversionTimer': '', 'partyEntranceTone': '', 'allowCtiControlFlag': '', 'rejectAnonymousCall': '', 'confidentialAccess': '', 'externalCallControlProfile': '', 'enterpriseAltNum': '', 'e164AltNum': '', 'pstnFailover': '', 'lineSelectionOrder': '', 'directoryNumber': '', 'index': '', 'laapAssociate': '', 'laapProductType': '', 'laapDeviceName': '', 'laapDirectory': '', 'laapPartition': '', 'laapDescription': ''}
            )
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
            print(f"AXL error listLine: ", str(err), file=sys.stderr)
            return False
        

    def DefaultDeviceProfile(self, name=''):
        """
        list_default_device_profile parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listDefaultDeviceProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'userHoldMohAudioSourceId': '', 'userLocale': '', 'phoneButtonTemplate': '', 'softkeyTemplate': '', 'privacy': '', 'singleButtonBarge': '', 'joinAcrossLines': '', 'ignorePi': '', 'dndStatus': '', 'dndRingSetting': '', 'dndOption': '', 'mlppIndication': '', 'preemption': '', 'alwaysUsePrimeLine': '', 'alwaysUsePrimeLineForVoiceMessage': ''}
            )
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
            print(f"AXL error listDefaultDeviceProfile: ", str(err), file=sys.stderr)
            return False
        

    def H323Phone(self, name=''):
        """
        list_h323_phone parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listH323Phone(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'commonPhoneConfigName': '', 'locationName': '', 'mediaResourceListName': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'traceFlag': '', 'useTrustedRelayPoint': '', 'retryVideoCallAsAudio': '', 'remoteDevice': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'alwaysUsePrimeLine': '', 'alwaysUsePrimeLineForVoiceMessage': '', 'srtpAllowed': '', 'unattendedPort': '', 'subscribeCallingSearchSpaceName': '', 'mtpRequired': '', 'mtpPreferredCodec': '', 'callerIdDn': '', 'callingPartySelection': '', 'callingLineIdPresentation': '', 'displayIEDelivery': '', 'redirectOutboundNumberIe': '', 'redirectInboundNumberIe': '', 'presenceGroupName': '', 'hlogStatus': '', 'ownerUserName': '', 'signalingPort': '', 'ignorePresentationIndicators': ''}
            )
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
            print(f"AXL error listH323Phone: ", str(err), file=sys.stderr)
            return False
        

    def MohServer(self, name=''):
        """
        list_moh_server parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listMohServer(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'processNodeName': '', 'devicePoolName': '', 'locationName': '', 'maxUnicastConnections': '', 'maxMulticastConnections': '', 'fixedAudioSourceDevice': '', 'runFlag': '', 'useTrustedRelayPoint': '', 'isMultiCastEnabled': '', 'baseMulticastIpaddress': '', 'baseMulticastPort': '', 'multicastIncrementOnIp': ''}
            )
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
            print(f"AXL error listMohServer: ", str(err), file=sys.stderr)
            return False
        

    def H323Trunk(self, name=''):
        """
        list_h323_trunk parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listH323Trunk(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'networkLocation': '', 'locationName': '', 'mediaResourceListName': '', 'aarNeighborhoodName': '', 'traceFlag': '', 'mlppIndicationStatus': '', 'preemption': '', 'useTrustedRelayPoint': '', 'retryVideoCallAsAudio': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'geoLocationFilterName': '', 'sendGeoLocation': '', 'cdpnTransformationCssName': '', 'useDevicePoolCdpnTransformCss': '', 'packetCaptureMode': '', 'packetCaptureDuration': '', 'srtpAllowed': '', 'unattendedPort': '', 'mtpRequired': '', 'callerIdDn': '', 'callingPartySelection': '', 'callingLineIdPresentation': '', 'displayIEDelivery': '', 'redirectOutboundNumberIe': '', 'redirectInboundNumberIe': '', 'enableInboundFaststart': '', 'enableOutboundFaststart': '', 'codecForOutboundFaststart': '', 'allowH235PassThrough': '', 'tunneledProtocol': '', 'asn1RoseOidEncoding': '', 'qsigVariant': '', 'transmitUtf8': '', 'signalingPort': '', 'nationalPrefix': '', 'internationalPrefix': '', 'unknownPrefix': '', 'subscriberPrefix': '', 'sigDigits': '', 'prefixDn': '', 'calledPartyIeNumberType': '', 'callingPartyIeNumberType': '', 'calledNumberingPlan': '', 'callingNumberingPlan': '', 'pathReplacementSupport': '', 'ictPassingPrecedenceLevelThroughUuie': '', 'ictSecurityAccessLevel': '', 'isSafEnabled': '', 'callingPartyNationalStripDigits': '', 'callingPartyInternationalStripDigits': '', 'callingPartyUnknownStripDigits': '', 'callingPartySubscriberStripDigits': '', 'callingPartyNationalTransformationCssName': '', 'callingPartyInternationalTransformationCssName': '', 'callingPartyUnknownTransformationCssName': '', 'callingPartySubscriberTransformationCssName': '', 'calledPartyNationalPrefix': '', 'calledPartyInternationalPrefix': '', 'calledPartyUnknownPrefix': '', 'calledPartySubscriberPrefix': '', 'pstnAccess': '', 'imeE164TransformationName': '', 'automatedAlternateRoutingCssName': '', 'useDevicePoolCgpnTransformCssNatl': '', 'useDevicePoolCgpnTransformCssIntl': '', 'useDevicePoolCgpnTransformCssUnkn': '', 'useDevicePoolCgpnTransformCssSubs': '', 'useDevicePoolCalledCssNatl': '', 'useDevicePoolCalledCssIntl': '', 'useDevicePoolCalledCssUnkn': '', 'useDevicePoolCalledCssSubs': '', 'calledPartyNationalStripDigits': '', 'calledPartyInternationalStripDigits': '', 'calledPartyUnknownStripDigits': '', 'calledPartySubscriberStripDigits': '', 'calledPartyNationalTransformationCssName': '', 'calledPartyInternationalTransformationCssName': '', 'calledPartyUnknownTransformationCssName': '', 'calledPartySubscriberTransformationCssName': '', 'runOnEveryNode': '', 'useDevicePoolCntdPnTransformationCss': '', 'confidentialAccess': '', 'addressIpv4': '', 'sortOrder': ''}
            )
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
            print(f"AXL error listH323Trunk: ", str(err), file=sys.stderr)
            return False
        

    def Phone(self, name=''):
        """
        list_phone parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param protocol: protocol
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
		:param securityProfileName: securityProfileName
        """
        try:
            resp = self.client.listPhone(
                {'name': '%'+name}, returnedTags={'ipAddress': '', 'ipv6Address': '', 'description': '', 'mode': '', 'name': '', 'isUserModifiable': '', 'phoneType': '', 'protocol': '', 'deviceSecurityMode': '', 'authenticationMode': '', 'keySize': '', 'keyOrder': '', 'ecKeySize': '', 'tftpEncryptedConfig': '', 'EnableOAuthAuthentication': '', 'nonceValidityTime': '', 'transportType': '', 'sipPhonePort': '', 'enableDigestAuthentication': '', 'excludeDigestCredentials': '', 'product': '', 'model': '', 'class': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'commonPhoneConfigName': '', 'networkLocation': '', 'locationName': '', 'mediaResourceListName': '', 'networkHoldMohAudioSourceId': '', 'userHoldMohAudioSourceId': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'loadInformation': '', 'traceFlag': '', 'mlppIndicationStatus': '', 'preemption': '', 'useTrustedRelayPoint': '', 'retryVideoCallAsAudio': '', 'securityProfileName': '', 'sipProfileName': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'geoLocationFilterName': '', 'sendGeoLocation': '', 'numberOfButtons': '', 'phoneTemplateName': '', 'primaryPhoneName': '', 'ringSettingIdleBlfAudibleAlert': '', 'ringSettingBusyBlfAudibleAlert': '', 'userLocale': '', 'networkLocale': '', 'idleTimeout': '', 'authenticationUrl': '', 'directoryUrl': '', 'idleUrl': '', 'informationUrl': '', 'messagesUrl': '', 'proxyServerUrl': '', 'servicesUrl': '', 'softkeyTemplateName': '', 'loginUserId': '', 'defaultProfileName': '', 'enableExtensionMobility': '', 'currentProfileName': '', 'loginTime': '', 'loginDuration': '', 'currentConfig': '', 'singleButtonBarge': '', 'joinAcrossLines': '', 'builtInBridgeStatus': '', 'callInfoPrivacyStatus': '', 'hlogStatus': '', 'ownerUserName': '', 'ignorePresentationIndicators': '', 'packetCaptureMode': '', 'packetCaptureDuration': '', 'subscribeCallingSearchSpaceName': '', 'rerouteCallingSearchSpaceName': '', 'allowCtiControlFlag': '', 'presenceGroupName': '', 'unattendedPort': '', 'requireDtmfReception': '', 'rfc2833Disabled': '', 'certificateOperation': '', 'authenticationString': '', 'certificateStatus': '', 'upgradeFinishTime': '', 'deviceMobilityMode': '', 'roamingDevicePoolName': '', 'remoteDevice': '', 'dndOption': '', 'dndRingSetting': '', 'dndStatus': '', 'isActive': '', 'isDualMode': '', 'mobilityUserIdName': '', 'phoneSuite': '', 'phoneServiceDisplay': '', 'isProtected': '', 'mtpRequired': '', 'mtpPreferedCodec': '', 'dialRulesName': '', 'sshUserId': '', 'digestUser': '', 'outboundCallRollover': '', 'hotlineDevice': '', 'secureInformationUrl': '', 'secureDirectoryUrl': '', 'secureMessageUrl': '', 'secureServicesUrl': '', 'secureAuthenticationUrl': '', 'secureIdleUrl': '', 'alwaysUsePrimeLine': '', 'alwaysUsePrimeLineForVoiceMessage': '', 'featureControlPolicy': '', 'deviceTrustMode': '', 'earlyOfferSupportForVoiceCall': '', 'requireThirdPartyRegistration': '', 'blockIncomingCallsWhenRoaming': '', 'homeNetworkId': '', 'AllowPresentationSharingUsingBfcp': '', 'confidentialAccess': '', 'requireOffPremiseLocation': '', 'allowiXApplicableMedia': '', 'enableCallRoutingToRdWhenNoneIsActive': '', 'enableActivationID': '', 'mraServiceDomain': '', 'allowMraMode': '', 'activationCode': '', 'activationCodeExpiry': '', 'phoneName': '', 'phoneDescription': '', 'phoneModel': '', 'enableActivationId': '', 'userId': '', 'index': '', 'label': '', 'display': '', 'dirn': '', 'ringSetting': '', 'consecutiveRingSetting': '', 'ringSettingIdlePickupAlert': '', 'ringSettingActivePickupAlert': '', 'displayAscii': '', 'e164Mask': '', 'dialPlanWizardId': '', 'mwlPolicy': '', 'maxNumCalls': '', 'busyTrigger': '', 'callInfoDisplay': '', 'recordingProfileName': '', 'monitoringCssName': '', 'recordingFlag': '', 'audibleMwi': '', 'speedDial': '', 'partitionUsage': '', 'associatedEndusers': '', 'missedCallLogging': '', 'recordingMediaSource': ''}
            )
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
            print(f"AXL error listPhone: ", str(err), file=sys.stderr)
            return False
        

    def H323Gateway(self, name=''):
        """
        list_h323_gateway parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param protocol: protocol
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listH323Gateway(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'networkLocation': '', 'locationName': '', 'mediaResourceListName': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'loadInformation': '', 'tunneledProtocol': '', 'asn1RoseOidEncoding': '', 'qsigVariant': '', 'pathReplacementSupport': '', 'traceFlag': '', 'useTrustedRelayPoint': '', 'retryVideoCallAsAudio': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'geoLocationFilterName': '', 'cdpnTransformationCssName': '', 'useDevicePoolCdpnTransformCss': '', 'packetCaptureMode': '', 'packetCaptureDuration': '', 'srtpAllowed': '', 'mtpRequired': '', 'callerIdDn': '', 'callingPartySelection': '', 'callingLineIdPresentation': '', 'enableInboundFaststart': '', 'enableOutboundFaststart': '', 'codecForOutboundFaststart': '', 'transmitUtf8': '', 'signalingPort': '', 'allowH235PassThrough': '', 'sigDigits': '', 'prefixDn': '', 'calledPartyIeNumberType': '', 'callingPartyIeNumberType': '', 'calledNumberingPlan': '', 'callingNumberingPlan': '', 'callingPartyNationalPrefix': '', 'callingPartyInternationalPrefix': '', 'callingPartyUnknownPrefix': '', 'callingPartySubscriberPrefix': '', 'callingPartyNationalStripDigits': '', 'callingPartyInternationalStripDigits': '', 'callingPartyUnknownStripDigits': '', 'callingPartySubscriberStripDigits': '', 'callingPartyNationalTransformationCssName': '', 'callingPartyInternationalTransformationCssName': '', 'callingPartyUnknownTransformationCssName': '', 'callingPartySubscriberTransformationCssName': '', 'calledPartyNationalPrefix': '', 'calledPartyInternationalPrefix': '', 'calledPartyUnknownPrefix': '', 'calledPartySubscriberPrefix': '', 'calledPartyNationalStripDigits': '', 'calledPartyInternationalStripDigits': '', 'calledPartyUnknownStripDigits': '', 'calledPartySubscriberStripDigits': '', 'calledPartyNationalTransformationCssName': '', 'calledPartyInternationalTransformationCssName': '', 'calledPartyUnknownTransformationCssName': '', 'calledPartySubscriberTransformationCssName': '', 'pstnAccess': '', 'imeE164TransformationName': '', 'displayIeDelivery': '', 'redirectOutboundNumberIe': '', 'redirectInboundNumberIe': '', 'useDevicePoolCgpnTransformCssNatl': '', 'useDevicePoolCgpnTransformCssIntl': '', 'useDevicePoolCgpnTransformCssUnkn': '', 'useDevicePoolCgpnTransformCssSubs': '', 'useDevicePoolCalledCssNatl': '', 'useDevicePoolCalledCssIntl': '', 'useDevicePoolCalledCssUnkn': '', 'useDevicePoolCalledCssSubs': '', 'useDevicePoolCntdPnTransformationCss': '', 'confidentialAccess': ''}
            )
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
            print(f"AXL error listH323Gateway: ", str(err), file=sys.stderr)
            return False
        

    def DeviceProfile(self, name=''):
        """
        list_device_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listDeviceProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'userHoldMohAudioSourceId': '', 'traceFlag': '', 'mlppIndicationStatus': '', 'preemption': '', 'phoneTemplateName': '', 'userLocale': '', 'defaultProfileName': '', 'currentProfileName': '', 'loginTime': '', 'loginDuration': '', 'singleButtonBarge': '', 'joinAcrossLines': '', 'loginUserId': '', 'ignorePresentationIndicators': '', 'dndOption': '', 'dndRingSetting': '', 'dndStatus': '', 'emccCallingSearchSpace': '', 'alwaysUsePrimeLine': '', 'alwaysUsePrimeLineForVoiceMessage': '', 'softkeyTemplateName': '', 'callInfoPrivacyStatus': '', 'currentConfig': '', 'featureControlPolicy': ''}
            )
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
            print(f"AXL error listDeviceProfile: ", str(err), file=sys.stderr)
            return False
        

    def RemoteDestination(self, name=''):
        """
        list_remote_destination parameters
        :param uuid: uuid
        :param name: name
		:param remoteDestinationProfileName: remoteDestinationProfileName
		:param ctiRemoteDeviceName: ctiRemoteDeviceName
		:param dualModeDeviceName: dualModeDeviceName
        """
        try:
            resp = self.client.listRemoteDestination(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'networkHoldMohAudioSourceId': '', 'userHoldMohAudioSourceId': '', 'callInfoPrivacyStatus': '', 'userId': '', 'ignorePresentationIndicators': '', 'rerouteCallingSearchSpaceName': '', 'cgpnTransformationCssName': '', 'automatedAlternateRoutingCssName': '', 'useDevicePoolCgpnTransformCss': '', 'userLocale': '', 'networkLocale': '', 'primaryPhoneName': '', 'dndOption': '', 'dndStatus': '', 'mobileSmartClientProfileName': '', 'destination': '', 'answerTooSoonTimer': '', 'answerTooLateTimer': '', 'delayBeforeRingingCell': '', 'remoteDestinationProfileName': '', 'ctiRemoteDeviceName': '', 'dualModeDeviceName': '', 'isMobilePhone': '', 'enableMobileConnect': '', 'timeZone': '', 'todAccessName': '', 'mobileSmartClientName': '', 'mobilityProfileName': '', 'singleNumberReachVoicemail': '', 'dialViaOfficeReverseVoicemail': ''}
            )
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
            print(f"AXL error listRemoteDestination: ", str(err), file=sys.stderr)
            return False
        

    def Gateway(self, name=''):
        """
        list_gateway parameters
        :param uuid: uuid
        :param domainName: domainName
		:param description: description
		:param product: product
		:param protocol: protocol
        """
        try:
            resp = self.client.listGateway(
                {'name': '%'+name}, returnedTags={'domainName': '', 'description': '', 'product': '', 'protocol': '', 'callManagerGroupName': '', 'scratch': '', 'loadInformation': '', 'unit': '', 'subunit': '', 'endpoint': '', 'index': '', 'name': '', 'model': '', 'class': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'networkLocale': '', 'locationName': '', 'mediaResourceListName': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'vendorConfig': '', 'mlppDomainId': '', 'useTrustedRelayPoint': '', 'retryVideoCallAsAudio': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'geoLocationFilterName': '', 'port': '', 'trunkSelectionOrder': '', 'transmitUtf8': '', 'cdpnTransformationCssName': '', 'useDevicePoolCdpnTransformCss': '', 'callingPartyNumberPrefix': '', 'callingPartyStripDigits': '', 'callingPartyUnknownTransformationCssName': '', 'useDevicePoolCgpnTransformCssUnknown': '', 'hotlineDevice': '', 'packetCaptureMode': '', 'packetCaptureDuration': '', 'pstnAccess': '', 'imeE164TransformationName': '', 'imeE164DirectoryNumber': '', 'confidentialAccess': '', 'networkLocation': '', 'mlppIndicationStatus': '', 'mlppPreemption': '', 'redirectInboundNumberIe': '', 'calledPlan': '', 'calledPri': '', 'callerIdDn': '', 'callingPartySelection': '', 'callingPlan': '', 'callingPri': '', 'chanIE': '', 'clockReference': '', 'dChannelEnable': '', 'channelSelectionOrder': '', 'displayIe': '', 'pcmType': '', 'csuParam': '', 'firstDelay': '', 'interfaceIdPresent': '', 'interfaceId': '', 'intraDelay': '', 'mcdnEnable': '', 'redirectOutboundNumberIe': '', 'numDigitsToStrip': '', 'passingPrecedenceLevelThrough': '', 'prefix': '', 'callingLinePresentationBit': '', 'connectedLineIdPresentation': '', 'priProtocol': '', 'securityAccessLevel': '', 'sendCallingNameInFacilityIe': '', 'sendExLeadingCharInDispIe': '', 'sendRestart': '', 'setupNonIsdnPi': '', 'sigDigits': '', 'span': '', 'statusPoll': '', 'smdiBasePort': '', 'GClearEnable': '', 'v150': '', 'asn1RoseOidEncoding': '', 'qsigVariant': '', 'unattendedPort': '', 'nationalPrefix': '', 'internationalPrefix': '', 'unknownPrefix': '', 'subscriberPrefix': '', 'routeClassSignalling': '', 'nationalStripDigits': '', 'internationalStripDigits': '', 'unknownStripDigits': '', 'subscriberStripDigits': '', 'nationalTransformationCssName': '', 'internationalTransformationCssName': '', 'unknownTransformationCssName': '', 'subscriberTransformationCssName': '', 'useDevicePoolCgpnTransformCssNatl': '', 'useDevicePoolCgpnTransformCssIntl': '', 'useDevicePoolCgpnTransformCssUnkn': '', 'useDevicePoolCgpnTransformCssSubs': '', 'calledPartyNationalPrefix': '', 'calledPartyInternationalPrefix': '', 'calledPartyUnknownPrefix': '', 'calledPartySubscriberPrefix': '', 'calledPartyNationalStripDigits': '', 'calledPartyInternationalStripDigits': '', 'calledPartyUnknownStripDigits': '', 'calledPartySubscriberStripDigits': '', 'calledPartyNationalTransformationCssName': '', 'calledPartyInternationalTransformationCssName': '', 'calledPartyUnknownTransformationCssName': '', 'calledPartySubscriberTransformationCssName': '', 'useDevicePoolCalledCssNatl': '', 'useDevicePoolCalledCssIntl': '', 'useDevicePoolCalledCssUnkn': '', 'useDevicePoolCalledCssSubs': '', 'useDevicePoolCntdPartyTransformationCss': '', 'cntdPartyTransformationCssName': '', 'briProtocol': '', 'presentationBit': '', 'enableDatalinkOnFirstCall': '', 'traceFlag': '', 'preemption': '', 'sendGeoLocation': '', 'ports': '', 'digitSending': '', 'fdlChannel': '', 'yellowAlarm': '', 'zeroSupression': '', 'handleDtmfPrecedenceSignals': '', 'encodeOutboundVoiceRouteClass': '', 'phoneTemplateName': '', 'securityProfileName': '', 'userLocale': '', 'deviceMobilityMode': '', 'ownerUserId': '', 'commonPhoneConfigName': '', 'alwaysUsePrimeLine': '', 'alwaysUsePrimeLineForVM': '', 'allowCtiControlFlag': '', 'remoteDevice': '', 'subscribeCallingSearchSpaceName': '', 'presenceGroupName': '', 'hlogStatus': '', 'ignorePresentationIndicators': '', 'lines': ''}
            )
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
            print(f"AXL error listGateway: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst600024PortFXSGateway(self, name=''):
        """
        list_cisco_catalyst600024_port_fxs_gateway parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listCiscoCatalyst600024PortFXSGateway(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'networkLocale': '', 'locationName': '', 'mediaResourceListName': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'loadInformation': '', 'traceFlag': '', 'useTrustedRelayPoint': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'portSelectionOrder': '', 'transmitUtf8': '', 'geoLocationFilterName': ''}
            )
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
            print(f"AXL error listCiscoCatalyst600024PortFXSGateway: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000E1VoIPGateway(self, name=''):
        """
        list_cisco_catalyst6000_e1_vo_ip_gateway parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listCiscoCatalyst6000E1VoIPGateway(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'networkLocation': '', 'locationName': '', 'networkLocale': '', 'mediaResourceListName': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'loadInformation': '', 'useTrustedRelayPoint': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'redirectInboundNumberIe': '', 'calledPlan': '', 'calledPri': '', 'callerIdDn': '', 'callingPartySelection': '', 'callingPlan': '', 'callingPri': '', 'chanIe': '', 'clockReference': '', 'dChannelEnable': '', 'channelSelectionOrder': '', 'displayIE': '', 'pcmType': '', 'csuParam': '', 'firstDelay': '', 'interfaceIdPresent': '', 'interfaceId': '', 'intraDelay': '', 'mcdnEnable': '', 'redirectOutboundNumberIe': '', 'numDigitsToStrip': '', 'passingPrecedenceLevelThrough': '', 'prefix': '', 'callingLinePresentationBit': '', 'connectedLineIdPresentation': '', 'priProtocol': '', 'securityAccessLevel': '', 'sendCallingNameInFacilityIe': '', 'sendExLeadingCharInDispIe': '', 'sendRestart': '', 'setupNonIsdnPi': '', 'sigDigits': '', 'span': '', 'statusPoll': '', 'smdiBasePort': '', 'packetCaptureMode': '', 'packetCaptureDuration': '', 'transmitUtf8': '', 'v150': '', 'asn1RoseOidEncoding': '', 'QSIGVariant': '', 'unattendedPort': '', 'cdpnTransformationCssName': '', 'useDevicePoolCdpnTransformCss': '', 'nationalPrefix': '', 'internationalPrefix': '', 'unknownPrefix': '', 'subscriberPrefix': '', 'geoLocationFilterName': '', 'nationalStripDigits': '', 'internationalStripDigits': '', 'unknownStripDigits': '', 'subscriberStripDigits': '', 'nationalTransformationCssName': '', 'internationalTransformationCssName': '', 'unknownTransformationCssName': '', 'subscriberTransformationCssName': '', 'useDevicePoolCgpnTransformCssNatl': '', 'useDevicePoolCgpnTransformCssIntl': '', 'useDevicePoolCgpnTransformCssUnkn': '', 'useDevicePoolCgpnTransformCssSubs': '', 'pstnAccess': '', 'imeE164TransformationName': ''}
            )
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
            print(f"AXL error listCiscoCatalyst6000E1VoIPGateway: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000T1VoIPGatewayPri(self, name=''):
        """
        list_cisco_catalyst6000_t1_vo_ip_gateway_pri parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listCiscoCatalyst6000T1VoIPGatewayPri(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'networkLocation': '', 'locationName': '', 'networkLocale': '', 'mediaResourceListName': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'loadInformation': '', 'mlppIndicationStatus': '', 'mlppPreemption': '', 'useTrustedRelayPoint': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'redirectInboundNumberIe': '', 'calledPlan': '', 'calledPri': '', 'callerIdDn': '', 'callingPartySelection': '', 'callingPlan': '', 'callingPri': '', 'chanIe': '', 'clockReference': '', 'dChannelEnable': '', 'channelSelectionOrder': '', 'displayIE': '', 'pcmType': '', 'csuParam': '', 'firstDelay': '', 'interfaceIdPresent': '', 'interfaceId': '', 'intraDelay': '', 'mcdnEnable': '', 'redirectOutboundNumberIe': '', 'numDigitsToStrip': '', 'passingPrecedenceLevelThrough': '', 'prefix': '', 'callingLinePresentationBit': '', 'connectedLineIdPresentation': '', 'priProtocol': '', 'securityAccessLevel': '', 'sendCallingNameInFacilityIe': '', 'sendExLeadingCharInDispIe': '', 'sendRestart': '', 'setupNonIsdnPi': '', 'sigDigits': '', 'span': '', 'statusPoll': '', 'smdiBasePort': '', 'packetCaptureMode': '', 'packetCaptureDuration': '', 'transmitUtf8': '', 'v150': '', 'asn1RoseOidEncoding': '', 'QSIGVariant': '', 'unattendedPort': '', 'cdpnTransformationCssName': '', 'useDevicePoolCdpnTransformCss': '', 'nationalPrefix': '', 'internationalPrefix': '', 'unknownPrefix': '', 'subscriberPrefix': '', 'geoLocationFilterName': '', 'nationalStripDigits': '', 'internationalStripDigits': '', 'unknownStripDigits': '', 'subscriberStripDigits': '', 'nationalTransformationCssName': '', 'internationalTransformationCssName': '', 'unknownTransformationCssName': '', 'subscriberTransformationCssName': '', 'useDevicePoolCgpnTransformCssNatl': '', 'useDevicePoolCgpnTransformCssIntl': '', 'useDevicePoolCgpnTransformCssUnkn': '', 'useDevicePoolCgpnTransformCssSubs': '', 'pstnAccess': '', 'imeE164TransformationName': ''}
            )
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
            print(f"AXL error listCiscoCatalyst6000T1VoIPGatewayPri: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000T1VoIPGatewayT1(self, name=''):
        """
        list_cisco_catalyst6000_t1_vo_ip_gateway_t1 parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listCiscoCatalyst6000T1VoIPGatewayT1(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'networkLocation': '', 'locationName': '', 'mediaResourceListName': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'loadInformation': '', 'traceFlag': '', 'mlppIndicationStatus': '', 'preemption': '', 'useTrustedRelayPoint': '', 'retryVideoCallAsAudio': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'sendGeoLocation': '', 'trunkSelectionOrder': '', 'clockReference': '', 'csuParam': '', 'digitSending': '', 'pcmType': '', 'fdlChannel': '', 'yellowAlarm': '', 'zeroSupression': '', 'smdiBasePort': '', 'handleDtmfPrecedenceSignals': '', 'cdpnTransformationCssName': '', 'useDevicePoolCdpnTransformCss': '', 'geoLocationFilterName': '', 'pstnAccess': '', 'imeE164TransformationName': ''}
            )
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
            print(f"AXL error listCiscoCatalyst6000T1VoIPGatewayT1: ", str(err), file=sys.stderr)
            return False
        

    def CallPickupGroup(self, name=''):
        """
        list_call_pickup_group parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
        """
        try:
            resp = self.client.listCallPickupGroup(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'pickupNotification': '', 'pickupNotificationTimer': '', 'callInfoForPickupNotification': '', 'name': ''}
            )
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
            print(f"AXL error listCallPickupGroup: ", str(err), file=sys.stderr)
            return False
        

    def RoutePlan(self, name=''):
        """
        list_route_plan parameters
        :param uuid: uuid
        :param dnOrPattern: dnOrPattern
		:param partition: partition
		:param type: type
        """
        try:
            resp = self.client.listRoutePlan(
                {'name': '%'+name}, returnedTags={'dnOrPattern': '', 'partition': '', 'type': '', 'routeDetail': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['routePlan']
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
            print(f"AXL error listRoutePlan: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocationPolicy(self, name=''):
        """
        list_geo_location_policy parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listGeoLocationPolicy(
                {'name': '%'+name}, returnedTags={'name': '', 'country': '', 'description': '', 'nationalSubDivision': '', 'district': '', 'communityName': '', 'cityDivision': '', 'neighbourhood': '', 'street': '', 'leadingStreetDirection': '', 'trailingStreetSuffix': '', 'streetSuffix': '', 'houseNumber': '', 'houseNumberSuffix': '', 'landmark': '', 'location': '', 'floor': '', 'occupantName': '', 'postalCode': ''}
            )
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
            print(f"AXL error listGeoLocationPolicy: ", str(err), file=sys.stderr)
            return False
        

    def SipTrunk(self, name=''):
        """
        list_sip_trunk parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param callingSearchSpaceName: callingSearchSpaceName
		:param devicePoolName: devicePoolName
        """
        try:
            resp = self.client.listSipTrunk(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'securityMode': '', 'incomingTransport': '', 'outgoingTransport': '', 'digestAuthentication': '', 'noncePolicyTime': '', 'x509SubjectName': '', 'incomingPort': '', 'applLevelAuthentication': '', 'acceptPresenceSubscription': '', 'acceptOutOfDialogRefer': '', 'acceptUnsolicitedNotification': '', 'allowReplaceHeader': '', 'transmitSecurityStatus': '', 'sipV150OutboundSdpOfferFiltering': '', 'allowChargingHeader': '', 'product': '', 'model': '', 'class': '', 'protocol': '', 'protocolSide': '', 'callingSearchSpaceName': '', 'devicePoolName': '', 'commonDeviceConfigName': '', 'networkLocation': '', 'locationName': '', 'mediaResourceListName': '', 'networkHoldMohAudioSourceId': '', 'userHoldMohAudioSourceId': '', 'automatedAlternateRoutingCssName': '', 'aarNeighborhoodName': '', 'packetCaptureMode': '', 'packetCaptureDuration': '', 'loadInformation': '', 'traceFlag': '', 'mlppIndicationStatus': '', 'preemption': '', 'useTrustedRelayPoint': '', 'retryVideoCallAsAudio': '', 'securityProfileName': '', 'sipProfileName': '', 'cgpnTransformationCssName': '', 'useDevicePoolCgpnTransformCss': '', 'geoLocationName': '', 'geoLocationFilterName': '', 'sendGeoLocation': '', 'cdpnTransformationCssName': '', 'useDevicePoolCdpnTransformCss': '', 'unattendedPort': '', 'transmitUtf8': '', 'subscribeCallingSearchSpaceName': '', 'rerouteCallingSearchSpaceName': '', 'referCallingSearchSpaceName': '', 'mtpRequired': '', 'presenceGroupName': '', 'unknownPrefix': '', 'destAddrIsSrv': '', 'tkSipCodec': '', 'sigDigits': '', 'connectedNamePresentation': '', 'connectedPartyIdPresentation': '', 'callingPartySelection': '', 'callingname': '', 'callingLineIdPresentation': '', 'prefixDn': '', 'acceptInboundRdnis': '', 'acceptOutboundRdnis': '', 'srtpAllowed': '', 'srtpFallbackAllowed': '', 'isPaiEnabled': '', 'sipPrivacy': '', 'isRpidEnabled': '', 'sipAssertedType': '', 'trustReceivedIdentity': '', 'dtmfSignalingMethod': '', 'routeClassSignalling': '', 'sipTrunkType': '', 'pstnAccess': '', 'imeE164TransformationName': '', 'useImePublicIpPort': '', 'useDevicePoolCntdPnTransformationCss': '', 'useDevicePoolCgpnTransformCssUnkn': '', 'rdnTransformationCssName': '', 'useDevicePoolRdnTransformCss': '', 'useOrigCallingPartyPresOnDivert': '', 'sipNormalizationScriptName': '', 'runOnEveryNode': '', 'unknownStripDigits': '', 'cgpnTransformationUnknownCssName': '', 'tunneledProtocol': '', 'asn1RoseOidEncoding': '', 'qsigVariant': '', 'pathReplacementSupport': '', 'enableQsigUtf8': '', 'scriptParameters': '', 'scriptTraceEnabled': '', 'trunkTrafficSecure': '', 'callingAndCalledPartyInfoFormat': '', 'useCallerIdCallerNameinUriOutgoingRequest': '', 'requestUriDomainName': '', 'enableCiscoRecordingQsigTunneling': '', 'calledPartyUnknownTransformationCssName': '', 'calledPartyUnknownPrefix': '', 'calledPartyUnknownStripDigits': '', 'useDevicePoolCalledCssUnkn': '', 'confidentialAccess': '', 'addressIpv4': '', 'addressIpv6': '', 'port': '', 'sortOrder': ''}
            )
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
            print(f"AXL error listSipTrunk: ", str(err), file=sys.stderr)
            return False
        

    def CalledPartyTransformationPattern(self, name=''):
        """
        list_called_party_transformation_pattern parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param routePartitionName: routePartitionName
		:param dialPlanName: dialPlanName
		:param routeFilterName: routeFilterName
        """
        try:
            resp = self.client.listCalledPartyTransformationPattern(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'usage': '', 'routePartitionName': '', 'calledPartyTransformationMask': '', 'dialPlanName': '', 'digitDiscardInstructionName': '', 'patternUrgency': '', 'routeFilterName': '', 'calledPartyPrefixDigits': '', 'calledPartyNumberingPlan': '', 'calledPartyNumberType': '', 'mlppPreemptionDisabled': ''}
            )
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
            print(f"AXL error listCalledPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
        

    def ExternalCallControlProfile(self, name=''):
        """
        list_external_call_control_profile parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listExternalCallControlProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'primaryUri': '', 'secondaryUri': '', 'enableLoadBalancing': '', 'routingRequestTimer': '', 'diversionReroutingCssName': '', 'callTreatmentOnFailure': ''}
            )
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
            print(f"AXL error listExternalCallControlProfile: ", str(err), file=sys.stderr)
            return False
        

    def SafSecurityProfile(self, name=''):
        """
        list_saf_security_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param userid: userid
        """
        try:
            resp = self.client.listSafSecurityProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'userid': ''}
            )
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
            print(f"AXL error listSafSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def SafForwarder(self, name=''):
        """
        list_saf_forwarder parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listSafForwarder(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'clientLabel': '', 'safSecurityProfile': '', 'ipAddress': '', 'port': '', 'enableTcpKeepAlive': '', 'safReconnectInterval': '', 'safNotificationsWindowSize': '', 'callManagerName': ''}
            )
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
            print(f"AXL error listSafForwarder: ", str(err), file=sys.stderr)
            return False
        

    def CcdHostedDN(self, name=''):
        """
        list_ccd_hosted_dn parameters
        :param uuid: uuid
        :param hostedPattern: hostedPattern
		:param description: description
        """
        try:
            resp = self.client.listCcdHostedDN(
                {'name': '%'+name}, returnedTags={'hostedPattern': '', 'description': '', 'CcdHostedDnGroup': '', 'pstnFailoverStripDigits': '', 'pstnFailoverPrependDigits': '', 'usePstnFailover': '', 'name': ''}
            )
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
            print(f"AXL error listCcdHostedDN: ", str(err), file=sys.stderr)
            return False
        

    def CcdHostedDNGroup(self, name=''):
        """
        list_ccd_hosted_dn_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listCcdHostedDNGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'pstnFailoverStripDigits': '', 'pstnFailoverPrependDigits': '', 'usePstnFailover': ''}
            )
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
            print(f"AXL error listCcdHostedDNGroup: ", str(err), file=sys.stderr)
            return False
        

    def RemoteCluster(self, name=''):
        """
        list_remote_cluster parameters
        :param uuid: uuid
        :param clusterId: clusterId
		:param description: description
        """
        try:
            resp = self.client.listRemoteCluster(
                {'name': '%'+name}, returnedTags={'clusterId': '', 'description': '', 'fullyQualifiedName': '', 'emcc': '', 'pstnAccess': '', 'rsvpAgent': '', 'tftp': '', 'lbm': '', 'uds': '', 'enabled': '', 'remoteIpAddress1': '', 'remoteIpAddress2': '', 'remoteIpAddress3': ''}
            )
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
            print(f"AXL error listRemoteCluster: ", str(err), file=sys.stderr)
            return False
        

    def CcdAdvertisingService(self, name=''):
        """
        list_ccd_advertising_service parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listCcdAdvertisingService(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'isActivated': ''}
            )
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
            print(f"AXL error listCcdAdvertisingService: ", str(err), file=sys.stderr)
            return False
        

    def LdapDirectory(self, name=''):
        """
        list_ldap_directory parameters
        :param uuid: uuid
        :param name: name
		:param ldapDn: ldapDn
		:param userSearchBase: userSearchBase
        """
        try:
            resp = self.client.listLdapDirectory(
                {'name': '%'+name}, returnedTags={'name': '', 'ldapDn': '', 'userSearchBase': '', 'repeatable': '', 'intervalValue': '', 'scheduleUnit': '', 'nextExecTime': '', 'accessControlGroupInfo': ''}
            )
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
            print(f"AXL error listLdapDirectory: ", str(err), file=sys.stderr)
            return False
        

    def SafCcdPurgeBlockLearnedRoutes(self, name=''):
        """
        list_saf_ccd_purge_block_learned_routes parameters
        :param uuid: uuid
        :param learnedPattern: learnedPattern
		:param learnedPatternPrefix: learnedPatternPrefix
		:param callControlIdentity: callControlIdentity
		:param ipAddress: ipAddress
        """
        try:
            resp = self.client.listSafCcdPurgeBlockLearnedRoutes(
                {'name': '%'+name}, returnedTags={'learnedPattern': '', 'learnedPatternPrefix': '', 'callControlIdentity': '', 'ipAddress': ''}
            )
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
            print(f"AXL error listSafCcdPurgeBlockLearnedRoutes: ", str(err), file=sys.stderr)
            return False
        

    def VpnGateway(self, name=''):
        """
        list_vpn_gateway parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listVpnGateway(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'url': '', 'issuerName': '', 'serialNumber': ''}
            )
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
            print(f"AXL error listVpnGateway: ", str(err), file=sys.stderr)
            return False
        

    def VpnGroup(self, name=''):
        """
        list_vpn_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listVpnGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'vpnGatewayName': '', 'priority': ''}
            )
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
            print(f"AXL error listVpnGroup: ", str(err), file=sys.stderr)
            return False
        

    def VpnProfile(self, name=''):
        """
        list_vpn_profile parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listVpnProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'autoNetworkDetection': '', 'mtu': '', 'failToConnect': '', 'clientAuthentication': '', 'pwdPersistant': '', 'enableHostIdCheck': ''}
            )
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
            print(f"AXL error listVpnProfile: ", str(err), file=sys.stderr)
            return False
        

    def ImeServer(self, name=''):
        """
        list_ime_server parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listImeServer(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'ipAddress': '', 'port': '', 'deviceSecurityMode': '', 'applicationUser': '', 'reconnectInterval': ''}
            )
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
            print(f"AXL error listImeServer: ", str(err), file=sys.stderr)
            return False
        

    def ImeRouteFilterGroup(self, name=''):
        """
        list_ime_route_filter_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listImeRouteFilterGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'groupTrustSetting': ''}
            )
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
            print(f"AXL error listImeRouteFilterGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeRouteFilterElement(self, name=''):
        """
        list_ime_route_filter_element parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listImeRouteFilterElement(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'elementType': '', 'imeRouteFilterGroupName': ''}
            )
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
            print(f"AXL error listImeRouteFilterElement: ", str(err), file=sys.stderr)
            return False
        

    def ImeClient(self, name=''):
        """
        list_ime_client parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param domain: domain
        """
        try:
            resp = self.client.listImeClient(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'domain': '', 'isActivated': '', 'sipTrunkName': '', 'primaryImeServerName': '', 'secondaryImeServerName': '', 'learnedRouteFilterGroupName': '', 'exclusionNumberGroupName': '', 'firewallName': '', 'enrolledPatternGroupName': ''}
            )
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
            print(f"AXL error listImeClient: ", str(err), file=sys.stderr)
            return False
        

    def ImeEnrolledPattern(self, name=''):
        """
        list_ime_enrolled_pattern parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param imeEnrolledPatternGroupName: imeEnrolledPatternGroupName
        """
        try:
            resp = self.client.listImeEnrolledPattern(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'imeEnrolledPatternGroupName': '', 'name': '', 'fallbackProfileName': '', 'isPatternAllAlias': ''}
            )
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
            print(f"AXL error listImeEnrolledPattern: ", str(err), file=sys.stderr)
            return False
        

    def ImeEnrolledPatternGroup(self, name=''):
        """
        list_ime_enrolled_pattern_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listImeEnrolledPatternGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'fallbackProfileName': '', 'isPatternAllAlias': ''}
            )
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
            print(f"AXL error listImeEnrolledPatternGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeExclusionNumber(self, name=''):
        """
        list_ime_exclusion_number parameters
        :param uuid: uuid
        :param pattern: pattern
		:param description: description
		:param imeExclusionNumberGroupName: imeExclusionNumberGroupName
        """
        try:
            resp = self.client.listImeExclusionNumber(
                {'name': '%'+name}, returnedTags={'pattern': '', 'description': '', 'imeExclusionNumberGroupName': '', 'name': ''}
            )
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
            print(f"AXL error listImeExclusionNumber: ", str(err), file=sys.stderr)
            return False
        

    def ImeExclusionNumberGroup(self, name=''):
        """
        list_ime_exclusion_number_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listImeExclusionNumberGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listImeExclusionNumberGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeFirewall(self, name=''):
        """
        list_ime_firewall parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param ipAddress: ipAddress
        """
        try:
            resp = self.client.listImeFirewall(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'ipAddress': '', 'port': ''}
            )
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
            print(f"AXL error listImeFirewall: ", str(err), file=sys.stderr)
            return False
        

    def ImeE164Transformation(self, name=''):
        """
        list_ime_e164_transformation parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listImeE164Transformation(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'cgpnTransformationCssName': '', 'isCgpnPreTransformation': '', 'cdpnTransformationCssName': '', 'isCdpnPreTransformation': '', 'incomingCgpnTransformationProfileName': '', 'incomingCdpnTransformationProfileName': ''}
            )
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
            print(f"AXL error listImeE164Transformation: ", str(err), file=sys.stderr)
            return False
        

    def TransformationProfile(self, name=''):
        """
        list_transformation_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listTransformationProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'nationalStripDigits': '', 'internationalStripDigits': '', 'unknownStripDigits': '', 'subscriberStripDigits': '', 'nationalPrefix': '', 'internationalPrefix': '', 'unknownPrefix': '', 'subscriberPrefix': '', 'nationalCssName': '', 'internationalCssName': '', 'unknownCssName': '', 'subscriberCssName': ''}
            )
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
            print(f"AXL error listTransformationProfile: ", str(err), file=sys.stderr)
            return False
        

    def FallbackProfile(self, name=''):
        """
        list_fallback_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listFallbackProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'advertisedFallbackDirectoryE164Number': '', 'qosSensistivityLevel': '', 'callCss': '', 'callAnswerTimer': '', 'directoryNumberPartition': '', 'directoryNumber': '', 'numberOfDigitsForCallerIDPartialMatch': '', 'numberOfCorrelationDtmfDigits': ''}
            )
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
            print(f"AXL error listFallbackProfile: ", str(err), file=sys.stderr)
            return False
        

    def LdapFilter(self, name=''):
        """
        list_ldap_filter parameters
        :param uuid: uuid
        :param name: name
		:param filter: filter
        """
        try:
            resp = self.client.listLdapFilter(
                {'name': '%'+name}, returnedTags={'name': '', 'filter': ''}
            )
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
            print(f"AXL error listLdapFilter: ", str(err), file=sys.stderr)
            return False
        

    def TvsCertificate(self, name=''):
        """
        list_tvs_certificate parameters
        :param uuid: uuid
        :param subjectName: subjectName
		:param issuerName: issuerName
		:param serialNumber: serialNumber
		:param timeToLive: timeToLive
        """
        try:
            resp = self.client.listTvsCertificate(
                {'name': '%'+name}, returnedTags={'subjectName': '', 'issuerName': '', 'serialNumber': '', 'timeToLive': '', 'ipv4Address': '', 'ipv6Address': '', 'serviceName': ''}
            )
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
            print(f"AXL error listTvsCertificate: ", str(err), file=sys.stderr)
            return False
        

    def FeatureControlPolicy(self, name=''):
        """
        list_feature_control_policy parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listFeatureControlPolicy(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listFeatureControlPolicy: ", str(err), file=sys.stderr)
            return False
        

    def MobilityProfile(self, name=''):
        """
        list_mobility_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listMobilityProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'mobileClientCallingOption': '', 'dvofServiceAccessNumber': '', 'dvorCallerId': ''}
            )
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
            print(f"AXL error listMobilityProfile: ", str(err), file=sys.stderr)
            return False
        

    def EnterpriseFeatureAccessConfiguration(self, name=''):
        """
        list_enterprise_feature_access_configuration parameters
        :param uuid: uuid
        :param pattern: pattern
		:param routePartitionName: routePartitionName
        """
        try:
            resp = self.client.listEnterpriseFeatureAccessConfiguration(
                {'name': '%'+name}, returnedTags={'pattern': '', 'routePartitionName': '', 'description': ''}
            )
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
            print(f"AXL error listEnterpriseFeatureAccessConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def CalledPartyTracing(self, name=''):
        """
        list_called_party_tracing parameters
        :param uuid: uuid
        :param directorynumber: directorynumber
        """
        try:
            resp = self.client.listCalledPartyTracing(
                {'name': '%'+name}, returnedTags={'directorynumber': '', 'description': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['calledPartyTracing']
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
            print(f"AXL error listCalledPartyTracing: ", str(err), file=sys.stderr)
            return False
        

    def SIPNormalizationScript(self, name=''):
        """
        list_sip_normalization_script parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listSIPNormalizationScript(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'scriptExecutionErrorRecoveryAction': '', 'systemResourceErrorRecoveryAction': '', 'maxMemoryThreshold': '', 'maxLuaInstructionsThreshold': '', 'isStandard': ''}
            )
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
            print(f"AXL error listSIPNormalizationScript: ", str(err), file=sys.stderr)
            return False
        

    def CustomUserField(self, name=''):
        """
        list_custom_user_field parameters
        :param uuid: uuid
        :param field: field
        """
        try:
            resp = self.client.listCustomUserField(
                {'name': '%'+name}, returnedTags={'field': ''}
            )
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
            print(f"AXL error listCustomUserField: ", str(err), file=sys.stderr)
            return False
        

    def BillingServer(self, name=''):
        """
        list_billing_server parameters
        :param uuid: uuid
        :param hostName: hostName
        """
        try:
            resp = self.client.listBillingServer(
                {'name': '%'+name}, returnedTags={'hostName': '', 'userId': '', 'password': '', 'directory': '', 'resendOnFailure': '', 'billingServerProtocol': ''}
            )
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
            print(f"AXL error listBillingServer: ", str(err), file=sys.stderr)
            return False
        

    def LbmGroup(self, name=''):
        """
        list_lbm_group parameters
        :param uuid: uuid
        :param name: name
		:param Description: Description
        """
        try:
            resp = self.client.listLbmGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'Description': '', 'ProcessnodeActive': '', 'ProcessnodeStandby': ''}
            )
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
            print(f"AXL error listLbmGroup: ", str(err), file=sys.stderr)
            return False
        

    def Announcement(self, name=''):
        """
        list_announcement parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listAnnouncement(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'announcementFile': ''}
            )
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
            print(f"AXL error listAnnouncement: ", str(err), file=sys.stderr)
            return False
        

    def ServiceProfile(self, name=''):
        """
        list_service_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listServiceProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'isDefault': '', 'profileName': '', 'primary': '', 'secondary': '', 'tertiary': '', 'serverCertificateVerification': '', 'serviceProfileXml': ''}
            )
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
            print(f"AXL error listServiceProfile: ", str(err), file=sys.stderr)
            return False
        

    def AudioCodecPreferenceList(self, name=''):
        """
        list_audio_codec_preference_list parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listAudioCodecPreferenceList(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listAudioCodecPreferenceList: ", str(err), file=sys.stderr)
            return False
        

    def UcService(self, name=''):
        """
        list_uc_service parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listUcService(
                {'name': '%'+name}, returnedTags={'serviceType': '', 'productType': '', 'name': '', 'description': '', 'hostnameorip': '', 'port': '', 'protocol': ''}
            )
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
            print(f"AXL error listUcService: ", str(err), file=sys.stderr)
            return False
        

    def LbmHubGroup(self, name=''):
        """
        list_lbm_hub_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listLbmHubGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'member1': '', 'member2': '', 'member3': ''}
            )
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
            print(f"AXL error listLbmHubGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImportedDirectoryUriCatalogs(self, name=''):
        """
        list_imported_directory_uri_catalogs parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param routeString: routeString
        """
        try:
            resp = self.client.listImportedDirectoryUriCatalogs(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'routeString': '', 'lastLoadedFileName': '', 'fileLoadDateTime': ''}
            )
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
            print(f"AXL error listImportedDirectoryUriCatalogs: ", str(err), file=sys.stderr)
            return False
        

    def VohServer(self, name=''):
        """
        list_voh_server parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param defaultVideoStreamId: defaultVideoStreamId
        """
        try:
            resp = self.client.listVohServer(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'sipTrunkName': '', 'defaultVideoStreamId': ''}
            )
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
            print(f"AXL error listVohServer: ", str(err), file=sys.stderr)
            return False
        

    def SdpTransparencyProfile(self, name=''):
        """
        list_sdp_transparency_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listSdpTransparencyProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listSdpTransparencyProfile: ", str(err), file=sys.stderr)
            return False
        

    def FeatureGroupTemplate(self, name=''):
        """
        list_feature_group_template parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listFeatureGroupTemplate(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'homeCluster': '', 'imAndUcPresenceEnable': '', 'serviceProfile': '', 'enableUserToHostConferenceNow': '', 'allowCTIControl': '', 'enableEMCC': '', 'enableMobility': '', 'enableMobileVoiceAccess': '', 'maxDeskPickupWait': '', 'remoteDestinationLimit': '', 'BLFPresenceGp': '', 'subscribeCallingSearch': '', 'userLocale': '', 'userProfile': '', 'meetingInformation': ''}
            )
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
            print(f"AXL error listFeatureGroupTemplate: ", str(err), file=sys.stderr)
            return False
        

    def DirNumberAliasLookupandSync(self, name=''):
        """
        list_dir_number_alias_lookupand_sync parameters
        :param uuid: uuid
        :param ldapConfigName: ldapConfigName
		:param ldapManagerDisgName: ldapManagerDisgName
		:param ldapUserSearch: ldapUserSearch
        """
        try:
            resp = self.client.listDirNumberAliasLookupandSync(
                {'name': '%'+name}, returnedTags={'ldapConfigName': '', 'ldapManagerDisgName': '', 'ldapPassword': '', 'ldapUserSearch': '', 'ldapDirectoryServerUsage': '', 'keepAliveSearch': '', 'keepAliveTime': '', 'sipAliasSuffix': '', 'enableCachingofRecords': '', 'cacheSizeforAliasLookup': '', 'cacheAgeforAliasLookup': ''}
            )
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
            print(f"AXL error listDirNumberAliasLookupandSync: ", str(err), file=sys.stderr)
            return False
        

    def LocalRouteGroup(self, name=''):
        """
        list_local_route_group parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listLocalRouteGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listLocalRouteGroup: ", str(err), file=sys.stderr)
            return False
        

    def AdvertisedPatterns(self, name=''):
        """
        list_advertised_patterns parameters
        :param uuid: uuid
        :param description: description
		:param pattern: pattern
        """
        try:
            resp = self.client.listAdvertisedPatterns(
                {'name': '%'+name}, returnedTags={'description': '', 'pattern': '', 'patternType': '', 'hostedRoutePSTNRule': '', 'pstnFailStrip': '', 'pstnFailPrepend': ''}
            )
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
            print(f"AXL error listAdvertisedPatterns: ", str(err), file=sys.stderr)
            return False
        

    def BlockedLearnedPatterns(self, name=''):
        """
        list_blocked_learned_patterns parameters
        :param uuid: uuid
        :param description: description
		:param pattern: pattern
        """
        try:
            resp = self.client.listBlockedLearnedPatterns(
                {'name': '%'+name}, returnedTags={'description': '', 'pattern': '', 'prefix': '', 'clusterId': '', 'patternType': ''}
            )
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
            print(f"AXL error listBlockedLearnedPatterns: ", str(err), file=sys.stderr)
            return False
        

    def CCAProfiles(self, name=''):
        """
        list_cca_profiles parameters
        :param uuid: uuid
        :param ccaId: ccaId
		:param primarySoftSwitchId: primarySoftSwitchId
        """
        try:
            resp = self.client.listCCAProfiles(
                {'name': '%'+name}, returnedTags={'ccaId': '', 'primarySoftSwitchId': '', 'secondarySoftSwitchId': '', 'objectClass': '', 'subscriberType': '', 'sipAliasSuffix': '', 'sipUserNameSuffix': ''}
            )
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
            print(f"AXL error listCCAProfiles: ", str(err), file=sys.stderr)
            return False
        

    def UniversalDeviceTemplate(self, name=''):
        """
        list_universal_device_template parameters
        :param uuid: uuid
        :param name: name
		:param deviceDescription: deviceDescription
        """
        try:
            resp = self.client.listUniversalDeviceTemplate(
                {'name': '%'+name}, returnedTags={'name': '', 'deviceDescription': '', 'devicePool': '', 'deviceSecurityProfile': '', 'sipProfile': '', 'phoneButtonTemplate': '', 'sipDialRules': '', 'callingSearchSpace': '', 'callingPartyTransformationCSSForInboundCalls': '', 'callingPartyTransformationCSSForOutboundCalls': '', 'reroutingCallingSearchSpace': '', 'subscribeCallingSearchSpaceName': '', 'useDevicePoolCallingPartyTransformationCSSforInboundCalls': '', 'useDevicePoolCallingPartyTransformationCSSforOutboundCalls': '', 'commonPhoneProfile': '', 'commonDeviceConfiguration': '', 'softkeyTemplate': '', 'featureControlPolicy': '', 'phonePersonalization': '', 'mtpPreferredOriginatingCodec': '', 'outboundCallRollover': '', 'mediaTerminationPointRequired': '', 'unattendedPort': '', 'requiredDtmfReception': '', 'rfc2833Disabled': '', 'useTrustedRelayPoint': '', 'protectedDevice': '', 'certificateOperation': '', 'authenticationMode': '', 'authenticationString': '', 'keySize': '', 'keyOrder': '', 'ecKeySize': '', 'servicesProvisioning': '', 'packetCaptureMode': '', 'packetCaptureDuration': '', 'secureShellUser': '', 'secureShellPassword': '', 'userLocale': '', 'networkLocale': '', 'mlppDomain': '', 'mlppIndication': '', 'mlppPreemption': '', 'doNotDisturb': '', 'dndOption': '', 'dndIncomingCallAlert': '', 'aarGroup': '', 'aarCallingSearchSpace': '', 'blfPresenceGroup': '', 'blfAudibleAlertSettingPhoneBusy': '', 'blfAudibleAlertSettingPhoneIdle': '', 'userHoldMohAudioSource': '', 'networkHoldMohAudioSource': '', 'location': '', 'geoLocation': '', 'deviceMobilityMode': '', 'mediaResourceGroupList': '', 'remoteDevice': '', 'hotlineDevice': '', 'retryVideoCallAsAudio': '', 'requireOffPremiseLocation': '', 'ownerUserId': '', 'mobilityUserId': '', 'joinAcrossLines': '', 'alwaysUsePrimeLine': '', 'alwaysUsePrimeLineForVoiceMessage': '', 'singleButtonBarge': '', 'builtInBridge': '', 'allowControlOfDeviceFromCti': '', 'ignorePresentationIndicators': '', 'enableExtensionMobility': '', 'privacy': '', 'loggedIntoHuntGroup': '', 'proxyServer': '', 'servicesUrl': '', 'idle': '', 'idleTimer': '', 'secureDirUrl': '', 'messages': '', 'secureIdleUrl': '', 'authenticationServer': '', 'directory': '', 'secureServicesUrl': '', 'information': '', 'secureMessagesUrl': '', 'secureInformationUrl': '', 'secureAuthenticationUrl': '', 'confidentialAccess': ''}
            )
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
            print(f"AXL error listUniversalDeviceTemplate: ", str(err), file=sys.stderr)
            return False
        

    def UserProfileProvision(self, name=''):
        """
        list_user_profile_provision parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listUserProfileProvision(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'allowProvision': '', 'limitProvision': '', 'allowPhoneReassign': '', 'defaultUserProfile': '', 'allowProvisionEMMaxLoginTime': ''}
            )
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
            print(f"AXL error listUserProfileProvision: ", str(err), file=sys.stderr)
            return False
        

    def PresenceRedundancyGroup(self, name=''):
        """
        list_presence_redundancy_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listPresenceRedundancyGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'server1': '', 'server2': '', 'haEnabled': '', 'numUsers': ''}
            )
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
            print(f"AXL error listPresenceRedundancyGroup: ", str(err), file=sys.stderr)
            return False
        

    def AssignedPresenceServers(self, name=''):
        """
        list_assigned_presence_servers parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listAssignedPresenceServers(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'nodeUsage': '', 'numUsers': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['assignedPresenceServers']
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
            print(f"AXL error listAssignedPresenceServers: ", str(err), file=sys.stderr)
            return False
        

    def UnassignedPresenceServers(self, name=''):
        """
        list_unassigned_presence_servers parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listUnassignedPresenceServers(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'nodeUsage': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['unassignedPresenceServers']
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
            print(f"AXL error listUnassignedPresenceServers: ", str(err), file=sys.stderr)
            return False
        

    def AssignedPresenceUsers(self, name=''):
        """
        list_assigned_presence_users parameters
        :param uuid: uuid
        :param userid: userid
		:param server: server
		:param presenceRedundancyGroup: presenceRedundancyGroup
        """
        try:
            resp = self.client.listAssignedPresenceUsers(
                {'name': '%'+name}, returnedTags={'userid': '', 'server': '', 'presenceRedundancyGroup': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['assignedPresenceUsers']
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
            print(f"AXL error listAssignedPresenceUsers: ", str(err), file=sys.stderr)
            return False
        

    def UnassignedPresenceUsers(self, name=''):
        """
        list_unassigned_presence_users parameters
        :param uuid: uuid
        :param userid: userid
        """
        try:
            resp = self.client.listUnassignedPresenceUsers(
                {'name': '%'+name}, returnedTags={'userid': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['unassignedPresenceUsers']
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
            print(f"AXL error listUnassignedPresenceUsers: ", str(err), file=sys.stderr)
            return False
        

    def WifiHotspot(self, name=''):
        """
        list_wifi_hotspot parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param ssidPrefix: ssidPrefix
		:param authenticationMethod: authenticationMethod
        """
        try:
            resp = self.client.listWifiHotspot(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'ssidPrefix': '', 'authenticationMethod': ''}
            )
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
            print(f"AXL error listWifiHotspot: ", str(err), file=sys.stderr)
            return False
        

    def WlanProfileGroup(self, name=''):
        """
        list_wlan_profile_group parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listWlanProfileGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listWlanProfileGroup: ", str(err), file=sys.stderr)
            return False
        

    def WLANProfile(self, name=''):
        """
        list_wlan_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
		:param ssid: ssid
		:param networkAccessProfile: networkAccessProfile
        """
        try:
            resp = self.client.listWLANProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'ssid': '', 'frequencyBand': '', 'userModifiable': '', 'authMethod': '', 'userName': '', 'password': '', 'pskPassphrase': '', 'wepKey': '', 'passwordDescription': '', 'networkAccessProfile': ''}
            )
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
            print(f"AXL error listWLANProfile: ", str(err), file=sys.stderr)
            return False
        

    def UniversalLineTemplate(self, name=''):
        """
        list_universal_line_template parameters
        :param uuid: uuid
        :param name: name
		:param lineDescription: lineDescription
        """
        try:
            resp = self.client.listUniversalLineTemplate(
                {'name': '%'+name}, returnedTags={'name': '', 'urgentPriority': '', 'lineDescription': '', 'routePartition': '', 'voiceMailProfile': '', 'callingSearchSpace': '', 'alertingName': '', 'extCallControlProfile': '', 'blfPresenceGroup': '', 'callPickupGroup': '', 'partyEntranceTone': '', 'autoAnswer': '', 'rejectAnonymousCall': '', 'userHoldMohAudioSource': '', 'networkHoldMohAudioSource': '', 'aarDestinationMask': '', 'aarGroup': '', 'retainDestInCallFwdHistory': '', 'forwardDestAllCalls': '', 'primaryCssForwardingAllCalls': '', 'secondaryCssForwardingAllCalls': '', 'CssActivationPolicy': '', 'fwdDestExtCallsWhenNotRetrieved': '', 'cssFwdExtCallsWhenNotRetrieved': '', 'fwdDestInternalCallsWhenNotRetrieved': '', 'cssFwdInternalCallsWhenNotRetrieved': '', 'parkMonitorReversionTime': '', 'target': '', 'mlppCss': '', 'mlppNoAnsRingDuration': '', 'confidentialAccess': '', 'holdReversionRingDuration': '', 'holdReversionNotificationInterval': '', 'busyIntCallsDestination': '', 'busyIntCallsCss': '', 'busyExtCallsDestination': '', 'busyExtCallsCss': '', 'noAnsIntCallsDestination': '', 'noAnsIntCallsCss': '', 'noAnsExtCallsDestination': '', 'noAnsExtCallsCss': '', 'noCoverageIntCallsDestination': '', 'noCoverageIntCallsCss': '', 'noCoverageExtCallsDestination': '', 'noCoverageExtCallsCss': '', 'unregisteredIntCallsDestination': '', 'unregisteredIntCallsCss': '', 'unregisteredExtCallsDestination': '', 'unregisteredExtCallsCss': '', 'ctiFailureDestination': '', 'ctiFailureCss': '', 'callControlAgentProfile': '', 'enterpriseAltNum': '', 'e164AltNum': '', 'advertisedFailoverNumber': ''}
            )
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
            print(f"AXL error listUniversalLineTemplate: ", str(err), file=sys.stderr)
            return False
        

    def NetworkAccessProfile(self, name=''):
        """
        list_network_access_profile parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listNetworkAccessProfile(
                {'name': '%'+name}, returnedTags={'name': '', 'description': ''}
            )
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
            print(f"AXL error listNetworkAccessProfile: ", str(err), file=sys.stderr)
            return False
        

    def LicensedUser(self, name=''):
        """
        list_licensed_user parameters
        :param uuid: uuid
        :param userId: userId
		:param firstName: firstName
		:param lastName: lastName
        """
        try:
            resp = self.client.listLicensedUser(
                {'name': '%'+name}, returnedTags={'userId': '', 'firstName': '', 'lastName': '', 'snrEnabled': '', 'emEnabled': '', 'deviceCount': '', 'licenseType': '', 'licenseUsed': ''}
            )
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
            print(f"AXL error listLicensedUser: ", str(err), file=sys.stderr)
            return False
        

    def ElinGroup(self, name=''):
        """
        list_elin_group parameters
        :param uuid: uuid
        :param name: name
        """
        try:
            resp = self.client.listElinGroup(
                {'name': '%'+name}, returnedTags={'name': '', 'elinNumbers': ''}
            )
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
            print(f"AXL error listElinGroup: ", str(err), file=sys.stderr)
            return False
        

    def UnassignedDevice(self, name=''):
        """
        list_unassigned_device parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listUnassignedDevice(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'deviceType': '', 'licenseType': '', 'extension': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['unassignedDevice']
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
            print(f"AXL error listUnassignedDevice: ", str(err), file=sys.stderr)
            return False
        

    def RegistrationDynamic(self, name=''):
        """
        list_registration_dynamic parameters
        :param uuid: uuid
        :param device: device
        """
        try:
            resp = self.client.listRegistrationDynamic(
                {'name': '%'+name}, returnedTags={'device': '', 'lastKnownIpAddress': '', 'lastKnownUcm': '', 'lastKnownConfigVersion': '', 'locationDetails': '', 'endpointConnection': '', 'portOrSsid': '', 'lastSeen': '', 'risStatus': ''}
            )
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
            print(f"AXL error listRegistrationDynamic: ", str(err), file=sys.stderr)
            return False
        

    def InfrastructureDevice(self, name=''):
        """
        list_infrastructure_device parameters
        :param uuid: uuid
        :param name: name
		:param isActive: isActive
        """
        try:
            resp = self.client.listInfrastructureDevice(
                {'name': '%'+name}, returnedTags={'name': '', 'ipv4Address': '', 'ipv6Address': '', 'bssidWithMask': '', 'wapLocation': '', 'isActive': ''}
            )
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
            print(f"AXL error listInfrastructureDevice: ", str(err), file=sys.stderr)
            return False
        

    def LdapSearch(self, name=''):
        """
        list_ldap_search parameters
        :param uuid: uuid
        :param distinguishedName: distinguishedName
        """
        try:
            resp = self.client.listLdapSearch(
                {'name': '%'+name}, returnedTags={'enableDirectorySearch': '', 'distinguishedName': '', 'userSearchBase1': '', 'userSearchBase2': '', 'userSearchBase3': '', 'enableRecursiveSearch': '', 'primary': '', 'secondary': '', 'tertiary': ''}
            )
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
            print(f"AXL error listLdapSearch: ", str(err), file=sys.stderr)
            return False
        

    def WirelessAccessPointControllers(self, name=''):
        """
        list_wireless_access_point_controllers parameters
        :param uuid: uuid
        :param name: name
		:param description: description
        """
        try:
            resp = self.client.listWirelessAccessPointControllers(
                {'name': '%'+name}, returnedTags={'name': '', 'description': '', 'snmpVersion': '', 'snmpUserIdOrCommunityString': '', 'snmpAuthenticationProtocol': '', 'snmpAuthenticationPassword': '', 'snmpPrivacyProtocol': '', 'snmpPrivacyPassword': '', 'syncNow': '', 'syncStatus': '', 'resyncInterval': '', 'nextSyncTime': '', 'scheduleUnit': ''}
            )
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
            print(f"AXL error listWirelessAccessPointControllers: ", str(err), file=sys.stderr)
            return False
        

    def PhoneActivationCode(self, name=''):
        """
        list_phone_activation_code parameters
        :param uuid: uuid
        :param phoneName: phoneName
		:param userId: userId
        """
        try:
            resp = self.client.listPhoneActivationCode(
                {'name': '%'+name}, returnedTags={'activationCode': '', 'activationCodeExpiry': '', 'phoneName': '', 'phoneDescription': '', 'phoneModel': '', 'enableActivationId': '', 'userId': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['phoneActivationCode']
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
            print(f"AXL error listPhoneActivationCode: ", str(err), file=sys.stderr)
            return False
        

    def DeviceDefaults(self, name=''):
        """
        list_device_defaults parameters
        :param uuid: uuid
        :param Model: Model
		:param Protocol: Protocol
        """
        try:
            resp = self.client.listDeviceDefaults(
                {'name': '%'+name}, returnedTags={'Model': '', 'Protocol': '', 'LoadInformation': '', 'InactiveLoadInformation': '', 'DevicePoolName': '', 'PhoneButtonTemplate': '', 'PreferActCodeOverAutoReg': ''}
            )
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
            print(f"AXL error listDeviceDefaults: ", str(err), file=sys.stderr)
            return False
        

    def MraServiceDomain(self, name=''):
        """
        list_mra_service_domain parameters
        :param uuid: uuid
        :param name: name
		:param isDefault: isDefault
		:param serviceDomains: serviceDomains
        """
        try:
            resp = self.client.listMraServiceDomain(
                {'name': '%'+name}, returnedTags={'name': '', 'isDefault': '', 'serviceDomains': ''}
            )
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
            print(f"AXL error listMraServiceDomain: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCloudOnboarding(self, name=''):
        """
        list_cisco_cloud_onboarding parameters
        :param uuid: uuid
        
        """
        try:
            resp = self.client.listCiscoCloudOnboarding(
                {'name': '%'+name}, returnedTags={'voucherExists': '', 'enablePushNotifications': '', 'enableHttpProxy': '', 'httpProxyAddress': '', 'proxyUsername': '', 'proxyPassword': '', 'enableTrustCACertificate': '', 'allowAnalyticsCollection': '', 'enableTroubleshooting': '', 'alarmSendEncryptedData': '', 'orgId': '', 'alarmPushIntervalSecs': '', 'alarmEncryptKey': '', 'serviceAddress': '', 'onboardingRegistrationStatus': '', 'email': '', 'partnerEmail': '', 'orgName': '', 'customerOneTimePassword': '', 'alarmSeverity': '', 'alarmPushNowToggle': '', 'enableGDSCommunication': '', 'mraActivationDomain': '', 'errorStatus': ''}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['ciscoCloudOnboarding']
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
            print(f"AXL error listCiscoCloudOnboarding: ", str(err), file=sys.stderr)
            return False
        

    def LdapSyncCustomField(self, name=''):
        """
        list_ldap_sync_custom_field parameters
        :param uuid: uuid
        :param ldapConfigurationName: ldapConfigurationName
        """
        try:
            resp = self.client.listLdapSyncCustomField(
                {'name': '%'+name}, returnedTags={'ldapConfigurationName': '', 'customUserField': '', 'ldapUserField': ''}
            )
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
            print(f"AXL error listLdapSyncCustomField: ", str(err), file=sys.stderr)
            return False
        

    def Change(self, name=''):
        """
        list_change parameters
        :param uuid: uuid
        
        """
        try:
            resp = self.client.listChange(
                {'name': '%'+name}, returnedTags={}
            )
            if resp['return']:
                soap_result = serialize_object(resp['return'], dict)['change']
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
            print(f"AXL error listChange: ", str(err), file=sys.stderr)
            return False
        

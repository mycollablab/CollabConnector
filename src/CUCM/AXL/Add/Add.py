from zeep.helpers import serialize_object
from zeep.exceptions import Fault
import sys


class Add:
    def __init__(self, soap_client):
        self.client = soap_client

    def SipProfile(self, **args):
        """
        SipProfile parameters
        :param name: name
	:param description: description
	:param defaultTelephonyEventPayloadType: defaultTelephonyEventPayloadType
	:param redirectByApplication: redirectByApplication
	:param ringing180: ringing180
	:param timerInvite: timerInvite
	:param timerRegisterDelta: timerRegisterDelta
	:param timerRegister: timerRegister
	:param timerT1: timerT1
	:param timerT2: timerT2
	:param retryInvite: retryInvite
	:param retryNotInvite: retryNotInvite
	:param startMediaPort: startMediaPort
	:param stopMediaPort: stopMediaPort
	:param startVideoPort: startVideoPort
	:param stopVideoPort: stopVideoPort
	:param dscpForAudioCalls: dscpForAudioCalls
	:param dscpForVideoCalls: dscpForVideoCalls
	:param dscpForAudioPortionOfVideoCalls: dscpForAudioPortionOfVideoCalls
	:param dscpForTelePresenceCalls: dscpForTelePresenceCalls
	:param dscpForAudioPortionOfTelePresenceCalls: dscpForAudioPortionOfTelePresenceCalls
	:param callpickupListUri: callpickupListUri
	:param callpickupGroupUri: callpickupGroupUri
	:param meetmeServiceUrl: meetmeServiceUrl
	:param userInfo: userInfo
	:param dtmfDbLevel: dtmfDbLevel
	:param callHoldRingback: callHoldRingback
	:param anonymousCallBlock: anonymousCallBlock
	:param callerIdBlock: callerIdBlock
	:param dndControl: dndControl
	:param telnetLevel: telnetLevel
	:param timerKeepAlive: timerKeepAlive
	:param timerSubscribe: timerSubscribe
	:param timerSubscribeDelta: timerSubscribeDelta
	:param maxRedirects: maxRedirects
	:param timerOffHookToFirstDigit: timerOffHookToFirstDigit
	:param callForwardUri: callForwardUri
	:param abbreviatedDialUri: abbreviatedDialUri
	:param confJointEnable: confJointEnable
	:param rfc2543Hold: rfc2543Hold
	:param semiAttendedTransfer: semiAttendedTransfer
	:param enableVad: enableVad
	:param stutterMsgWaiting: stutterMsgWaiting
	:param callStats: callStats
	:param t38Invite: t38Invite
	:param faxInvite: faxInvite
	:param rerouteIncomingRequest: rerouteIncomingRequest
	:param resourcePriorityNamespaceListName: resourcePriorityNamespaceListName
	:param enableAnatForEarlyOfferCalls: enableAnatForEarlyOfferCalls
	:param rsvpOverSip: rsvpOverSip
	:param fallbackToLocalRsvp: fallbackToLocalRsvp
	:param sipRe11XxEnabled: sipRe11XxEnabled
	:param gClear: gClear
	:param sendRecvSDPInMidCallInvite: sendRecvSDPInMidCallInvite
	:param enableOutboundOptionsPing: enableOutboundOptionsPing
	:param optionsPingIntervalWhenStatusOK: optionsPingIntervalWhenStatusOK
	:param optionsPingIntervalWhenStatusNotOK: optionsPingIntervalWhenStatusNotOK
	:param deliverConferenceBridgeIdentifier: deliverConferenceBridgeIdentifier
	:param sipOptionsRetryCount: sipOptionsRetryCount
	:param sipOptionsRetryTimer: sipOptionsRetryTimer
	:param sipBandwidthModifier: sipBandwidthModifier
	:param enableUriOutdialSupport: enableUriOutdialSupport
	:param userAgentServerHeaderInfo: userAgentServerHeaderInfo
	:param allowPresentationSharingUsingBfcp: allowPresentationSharingUsingBfcp
	:param scriptParameters: scriptParameters
	:param isScriptTraceEnabled: isScriptTraceEnabled
	:param sipNormalizationScript: sipNormalizationScript
	:param allowiXApplicationMedia: allowiXApplicationMedia
	:param dialStringInterpretation: dialStringInterpretation
	:param acceptAudioCodecPreferences: acceptAudioCodecPreferences
	:param mlppUserAuthorization: mlppUserAuthorization
	:param isAssuredSipServiceEnabled: isAssuredSipServiceEnabled
	:param enableExternalQoS: enableExternalQoS
	:param resourcePriorityNamespace: resourcePriorityNamespace
	:param useCallerIdCallerNameinUriOutgoingRequest: useCallerIdCallerNameinUriOutgoingRequest
	:param externalPresentationInfo: externalPresentationInfo
	:param callingLineIdentification: callingLineIdentification
	:param rejectAnonymousIncomingCall: rejectAnonymousIncomingCall
	:param callpickupUri: callpickupUri
	:param rejectAnonymousOutgoingCall: rejectAnonymousOutgoingCall
	:param videoCallTrafficClass: videoCallTrafficClass
	:param sdpTransparency: sdpTransparency
	:param allowMultipleCodecs: allowMultipleCodecs
	:param sipSessionRefreshMethod: sipSessionRefreshMethod
	:param earlyOfferSuppVoiceCall: earlyOfferSuppVoiceCall
	:param cucmVersionInSipHeader: cucmVersionInSipHeader
	:param confidentialAccessLevelHeaders: confidentialAccessLevelHeaders
	:param destRouteString: destRouteString
	:param inactiveSDPRequired: inactiveSDPRequired
	:param allowRRAndRSBandwidthModifier: allowRRAndRSBandwidthModifier
	:param connectCallBeforePlayingAnnouncement: connectCallBeforePlayingAnnouncement
	:param userInfo: userInfo
	:param dtmfDbLevel: dtmfDbLevel
	:param callHoldRingback: callHoldRingback
	:param anonymousCallBlock: anonymousCallBlock
	:param callerIdBlock: callerIdBlock
	:param dndControl: dndControl
	:param telnetLevel: telnetLevel
	:param rerouteIncomingRequest: rerouteIncomingRequest
	:param resourcePriorityNamespaceListName: resourcePriorityNamespaceListName
	:param rsvpOverSip: rsvpOverSip
	:param sipRe11XxEnabled: sipRe11XxEnabled
	:param gClear: gClear
	:param sipBandwidthModifier: sipBandwidthModifier
	:param userAgentServerHeaderInfo: userAgentServerHeaderInfo
	:param sipNormalizationScript: sipNormalizationScript
	:param dialStringInterpretation: dialStringInterpretation
	:param acceptAudioCodecPreferences: acceptAudioCodecPreferences
	:param resourcePriorityNamespace: resourcePriorityNamespace
	:param callingLineIdentification: callingLineIdentification
	:param videoCallTrafficClass: videoCallTrafficClass
	:param sdpTransparency: sdpTransparency
	:param sipSessionRefreshMethod: sipSessionRefreshMethod
	:param earlyOfferSuppVoiceCall: earlyOfferSuppVoiceCall
	:param cucmVersionInSipHeader: cucmVersionInSipHeader
	:param confidentialAccessLevelHeaders: confidentialAccessLevelHeaders
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSipProfile(**args)
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
            print(f"AXL error addSipProfile: ", str(err), file=sys.stderr)
            return False
        

    def SipTrunkSecurityProfile(self, **args):
        """
        SipTrunkSecurityProfile parameters
        :param name: name
	:param description: description
	:param securityMode: securityMode
	:param incomingTransport: incomingTransport
	:param outgoingTransport: outgoingTransport
	:param digestAuthentication: digestAuthentication
	:param noncePolicyTime: noncePolicyTime
	:param x509SubjectName: x509SubjectName
	:param incomingPort: incomingPort
	:param applLevelAuthentication: applLevelAuthentication
	:param acceptPresenceSubscription: acceptPresenceSubscription
	:param acceptOutOfDialogRefer: acceptOutOfDialogRefer
	:param acceptUnsolicitedNotification: acceptUnsolicitedNotification
	:param allowReplaceHeader: allowReplaceHeader
	:param transmitSecurityStatus: transmitSecurityStatus
	:param sipV150OutboundSdpOfferFiltering: sipV150OutboundSdpOfferFiltering
	:param allowChargingHeader: allowChargingHeader
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSipTrunkSecurityProfile(**args)
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
            print(f"AXL error addSipTrunkSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def TimePeriod(self, **args):
        """
        TimePeriod parameters
        :param name: name
	:param startTime: startTime
	:param endTime: endTime
	:param startDay: startDay
	:param endDay: endDay
	:param monthOfYear: monthOfYear
	:param dayOfMonth: dayOfMonth
	:param description: description
	:param isPublished: isPublished
	:param todOwnerIdName: todOwnerIdName
	:param dayOfMonthEnd: dayOfMonthEnd
	:param monthOfYearEnd: monthOfYearEnd
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addTimePeriod(**args)
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
            print(f"AXL error addTimePeriod: ", str(err), file=sys.stderr)
            return False
        

    def TimeSchedule(self, **args):
        """
        TimeSchedule parameters
        :param name: name
	:param members: members
	:param description: description
	:param isPublished: isPublished
	:param timeScheduleCategory: timeScheduleCategory
	:param todOwnerIdName: todOwnerIdName
	:param timePeriodName: timePeriodName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addTimeSchedule(**args)
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
            print(f"AXL error addTimeSchedule: ", str(err), file=sys.stderr)
            return False
        

    def TodAccess(self, **args):
        """
        TodAccess parameters
        :param name: name
	:param description: description
	:param ownerIdName: ownerIdName
	:param members: members
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addTodAccess(**args)
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
            print(f"AXL error addTodAccess: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailPilot(self, **args):
        """
        VoiceMailPilot parameters
        :param dirn: dirn
	:param description: description
	:param cssName: cssName
	:param isDefault: isDefault
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addVoiceMailPilot(**args)
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
            print(f"AXL error addVoiceMailPilot: ", str(err), file=sys.stderr)
            return False
        

    def ProcessNode(self, **args):
        """
        ProcessNode parameters
        :param name: name
	:param description: description
	:param mac: mac
	:param ipv6Name: ipv6Name
	:param lbmHubGroup: lbmHubGroup
	:param processNodeRole: processNodeRole
	:param cupDomain: cupDomain
	:param processNodeName: processNodeName
	:param service: service
	:param traceLevel: traceLevel
	:param userCategories: userCategories
	:param enable: enable
	:param numFiles: numFiles
	:param maxFileSize: maxFileSize
	:param lbmAssignedServices: lbmAssignedServices
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addProcessNode(**args)
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
            print(f"AXL error addProcessNode: ", str(err), file=sys.stderr)
            return False
        

    def CallerFilterList(self, **args):
        """
        CallerFilterList parameters
        :param name: name
	:param description: description
	:param isAllowedType: isAllowedType
	:param endUserIdName: endUserIdName
	:param members: members
	:param DnMask: DnMask
	:param callerFilterMask: callerFilterMask
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCallerFilterList(**args)
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
            print(f"AXL error addCallerFilterList: ", str(err), file=sys.stderr)
            return False
        

    def RoutePartition(self, **args):
        """
        RoutePartition parameters
        :param name: name
	:param description: description
	:param timeScheduleIdName: timeScheduleIdName
	:param useOriginatingDeviceTimeZone: useOriginatingDeviceTimeZone
	:param timeZone: timeZone
	:param partitionUsage: partitionUsage
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRoutePartition(**args)
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
            print(f"AXL error addRoutePartition: ", str(err), file=sys.stderr)
            return False
        

    def Css(self, **args):
        """
        Css parameters
        :param description: description
	:param members: members
	:param partitionUsage: partitionUsage
	:param name: name
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCss(**args)
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
            print(f"AXL error addCss: ", str(err), file=sys.stderr)
            return False
        

    def ExpresswayCConfiguration(self, **args):
        """
        ExpresswayCConfiguration parameters
        :param HostNameOrIP: HostNameOrIP
	:param description: description
	:param X509SubjectNameorSubjectAlternateName: X509SubjectNameorSubjectAlternateName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addExpresswayCConfiguration(**args)
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
            print(f"AXL error addExpresswayCConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def MediaResourceGroup(self, **args):
        """
        MediaResourceGroup parameters
        :param name: name
	:param description: description
	:param multicast: multicast
	:param members: members
	:param deviceName: deviceName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMediaResourceGroup(**args)
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
            print(f"AXL error addMediaResourceGroup: ", str(err), file=sys.stderr)
            return False
        

    def MediaResourceList(self, **args):
        """
        MediaResourceList parameters
        :param name: name
	:param members: members
	:param mediaResourceGroupName: mediaResourceGroupName
	:param order: order
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMediaResourceList(**args)
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
            print(f"AXL error addMediaResourceList: ", str(err), file=sys.stderr)
            return False
        

    def Region(self, **args):
        """
        Region parameters
        :param name: name
	:param relatedRegions: relatedRegions
	:param defaultCodec: defaultCodec
	:param bandwidth: bandwidth
	:param videoBandwidth: videoBandwidth
	:param regionAName: regionAName
	:param regionBName: regionBName
	:param codecPreference: codecPreference
	:param regionName: regionName
	:param bandwidth: bandwidth
	:param videoBandwidth: videoBandwidth
	:param lossyNetwork: lossyNetwork
	:param codecPreference: codecPreference
	:param immersiveVideoBandwidth: immersiveVideoBandwidth
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRegion(**args)
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
            print(f"AXL error addRegion: ", str(err), file=sys.stderr)
            return False
        

    def AarGroup(self, **args):
        """
        AarGroup parameters
        :param name: name
	:param prefixDigit: prefixDigit
	:param aarGroupFromName: aarGroupFromName
	:param aarGroupToName: aarGroupToName
	:param aarGroupFromName: aarGroupFromName
	:param aarGroupToName: aarGroupToName
	:param prefixDigit: prefixDigit
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addAarGroup(**args)
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
            print(f"AXL error addAarGroup: ", str(err), file=sys.stderr)
            return False
        

    def PhysicalLocation(self, **args):
        """
        PhysicalLocation parameters
        :param name: name
	:param description: description
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addPhysicalLocation(**args)
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
            print(f"AXL error addPhysicalLocation: ", str(err), file=sys.stderr)
            return False
        

    def Customer(self, **args):
        """
        Customer parameters
        :param name: name
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCustomer(**args)
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
            print(f"AXL error addCustomer: ", str(err), file=sys.stderr)
            return False
        

    def RouteGroup(self, **args):
        """
        RouteGroup parameters
        :param distributionAlgorithm: distributionAlgorithm
	:param members: members
	:param name: name
	:param deviceSelectionOrder: deviceSelectionOrder
	:param deviceName: deviceName
	:param port: port
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRouteGroup(**args)
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
            print(f"AXL error addRouteGroup: ", str(err), file=sys.stderr)
            return False
        

    def DevicePool(self, **args):
        """
        DevicePool parameters
        :param name: name
	:param autoSearchSpaceName: autoSearchSpaceName
	:param dateTimeSettingName: dateTimeSettingName
	:param callManagerGroupName: callManagerGroupName
	:param mediaResourceListName: mediaResourceListName
	:param regionName: regionName
	:param networkLocale: networkLocale
	:param srstName: srstName
	:param connectionMonitorDuration: connectionMonitorDuration
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param locationName: locationName
	:param mobilityCssName: mobilityCssName
	:param physicalLocationName: physicalLocationName
	:param deviceMobilityGroupName: deviceMobilityGroupName
	:param revertPriority: revertPriority
	:param singleButtonBarge: singleButtonBarge
	:param joinAcrossLines: joinAcrossLines
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param localRouteGroupName: localRouteGroupName
	:param geoLocationName: geoLocationName
	:param geoLocationFilterName: geoLocationFilterName
	:param callingPartyNationalPrefix: callingPartyNationalPrefix
	:param callingPartyInternationalPrefix: callingPartyInternationalPrefix
	:param callingPartyUnknownPrefix: callingPartyUnknownPrefix
	:param callingPartySubscriberPrefix: callingPartySubscriberPrefix
	:param adjunctCallingSearchSpace: adjunctCallingSearchSpace
	:param callingPartyNationalStripDigits: callingPartyNationalStripDigits
	:param callingPartyInternationalStripDigits: callingPartyInternationalStripDigits
	:param callingPartyUnknownStripDigits: callingPartyUnknownStripDigits
	:param callingPartySubscriberStripDigits: callingPartySubscriberStripDigits
	:param callingPartyNationalTransformationCssName: callingPartyNationalTransformationCssName
	:param callingPartyInternationalTransformationCssName: callingPartyInternationalTransformationCssName
	:param callingPartyUnknownTransformationCssName: callingPartyUnknownTransformationCssName
	:param callingPartySubscriberTransformationCssName: callingPartySubscriberTransformationCssName
	:param calledPartyNationalPrefix: calledPartyNationalPrefix
	:param calledPartyInternationalPrefix: calledPartyInternationalPrefix
	:param calledPartyUnknownPrefix: calledPartyUnknownPrefix
	:param calledPartySubscriberPrefix: calledPartySubscriberPrefix
	:param calledPartyNationalStripDigits: calledPartyNationalStripDigits
	:param calledPartyInternationalStripDigits: calledPartyInternationalStripDigits
	:param calledPartyUnknownStripDigits: calledPartyUnknownStripDigits
	:param calledPartySubscriberStripDigits: calledPartySubscriberStripDigits
	:param calledPartyNationalTransformationCssName: calledPartyNationalTransformationCssName
	:param calledPartyInternationalTransformationCssName: calledPartyInternationalTransformationCssName
	:param calledPartyUnknownTransformationCssName: calledPartyUnknownTransformationCssName
	:param calledPartySubscriberTransformationCssName: calledPartySubscriberTransformationCssName
	:param imeEnrolledPatternGroupName: imeEnrolledPatternGroupName
	:param cntdPnTransformationCssName: cntdPnTransformationCssName
	:param localRouteGroup: localRouteGroup
	:param redirectingPartyTransformationCSS: redirectingPartyTransformationCSS
	:param callingPartyTransformationCSS: callingPartyTransformationCSS
	:param wirelessLanProfileGroup: wirelessLanProfileGroup
	:param elinGroup: elinGroup
	:param mraServiceDomain: mraServiceDomain
	:param devicePoolName: devicePoolName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDevicePool(**args)
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
            print(f"AXL error addDevicePool: ", str(err), file=sys.stderr)
            return False
        

    def DeviceMobilityGroup(self, **args):
        """
        DeviceMobilityGroup parameters
        :param name: name
	:param description: description
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDeviceMobilityGroup(**args)
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
            print(f"AXL error addDeviceMobilityGroup: ", str(err), file=sys.stderr)
            return False
        

    def Location(self, **args):
        """
        Location parameters
        :param name: name
	:param relatedLocations: relatedLocations
	:param withinAudioBandwidth: withinAudioBandwidth
	:param withinVideoBandwidth: withinVideoBandwidth
	:param withinImmersiveKbits: withinImmersiveKbits
	:param betweenLocations: betweenLocations
	:param locationName: locationName
	:param rsvpSetting: rsvpSetting
	:param locationName: locationName
	:param weight: weight
	:param audioBandwidth: audioBandwidth
	:param videoBandwidth: videoBandwidth
	:param immersiveBandwidth: immersiveBandwidth
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLocation(**args)
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
            print(f"AXL error addLocation: ", str(err), file=sys.stderr)
            return False
        

    def SoftKeyTemplate(self, **args):
        """
        SoftKeyTemplate parameters
        :param name: name
	:param description: description
	:param baseSoftkeyTemplateName: baseSoftkeyTemplateName
	:param isDefault: isDefault
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSoftKeyTemplate(**args)
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
            print(f"AXL error addSoftKeyTemplate: ", str(err), file=sys.stderr)
            return False
        

    def Transcoder(self, **args):
        """
        Transcoder parameters
        :param name: name
	:param description: description
	:param product: product
	:param subUnit: subUnit
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param isTrustedRelayPoint: isTrustedRelayPoint
	:param maximumCapacity: maximumCapacity
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addTranscoder(**args)
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
            print(f"AXL error addTranscoder: ", str(err), file=sys.stderr)
            return False
        

    def CommonDeviceConfig(self, **args):
        """
        CommonDeviceConfig parameters
        :param name: name
	:param softkeyTemplateName: softkeyTemplateName
	:param userLocale: userLocale
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param preemption: preemption
	:param ipAddressingMode: ipAddressingMode
	:param ipAddressingModePreferenceControl: ipAddressingModePreferenceControl
	:param allowAutoConfigurationForPhones: allowAutoConfigurationForPhones
	:param useImeForOutboundCalls: useImeForOutboundCalls
	:param confidentialAccess: confidentialAccess
	:param allowDuplicateAddressDetection: allowDuplicateAddressDetection
	:param acceptRedirectMessages: acceptRedirectMessages
	:param replyMulticastEchoRequest: replyMulticastEchoRequest
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCommonDeviceConfig(**args)
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
            print(f"AXL error addCommonDeviceConfig: ", str(err), file=sys.stderr)
            return False
        

    def ResourcePriorityNamespace(self, **args):
        """
        ResourcePriorityNamespace parameters
        :param namespace: namespace
	:param description: description
	:param isDefault: isDefault
	:param name: name
	:param description: description
	:param members: members
	:param resourcePriorityNamespaceName: resourcePriorityNamespaceName
	:param index: index
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addResourcePriorityNamespace(**args)
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
            print(f"AXL error addResourcePriorityNamespace: ", str(err), file=sys.stderr)
            return False
        

    def ResourcePriorityNamespaceList(self, **args):
        """
        ResourcePriorityNamespaceList parameters
        :param name: name
	:param description: description
	:param members: members
	:param resourcePriorityNamespaceName: resourcePriorityNamespaceName
	:param index: index
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addResourcePriorityNamespaceList(**args)
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
            print(f"AXL error addResourcePriorityNamespaceList: ", str(err), file=sys.stderr)
            return False
        

    def DeviceMobility(self, **args):
        """
        DeviceMobility parameters
        :param name: name
	:param description: description
	:param name: name
	:param subNetDetails: subNetDetails
	:param members: members
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDeviceMobility(**args)
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
            print(f"AXL error addDeviceMobility: ", str(err), file=sys.stderr)
            return False
        

    def CmcInfo(self, **args):
        """
        CmcInfo parameters
        :param code: code
	:param description: description
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCmcInfo(**args)
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
            print(f"AXL error addCmcInfo: ", str(err), file=sys.stderr)
            return False
        

    def CredentialPolicy(self, **args):
        """
        CredentialPolicy parameters
        :param name: name
	:param failedLogon: failedLogon
	:param resetFailedLogonAttempts: resetFailedLogonAttempts
	:param lockoutDuration: lockoutDuration
	:param credChangeDuration: credChangeDuration
	:param credExpiresAfter: credExpiresAfter
	:param minCredLength: minCredLength
	:param prevCredStoredNum: prevCredStoredNum
	:param inactiveDaysAllowed: inactiveDaysAllowed
	:param expiryWarningDays: expiryWarningDays
	:param trivialCredCheck: trivialCredCheck
	:param minCharsToChange: minCharsToChange
	:param credentialUser: credentialUser
	:param credentialType: credentialType
	:param credPolicyName: credPolicyName
	:param credentials: credentials
	:param confirmCredentials: confirmCredentials
	:param credUserCantChange: credUserCantChange
	:param credUserMustChange: credUserMustChange
	:param credDoesNotExpire: credDoesNotExpire
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCredentialPolicy(**args)
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
            print(f"AXL error addCredentialPolicy: ", str(err), file=sys.stderr)
            return False
        

    def FacInfo(self, **args):
        """
        FacInfo parameters
        :param name: name
	:param code: code
	:param authorizationLevel: authorizationLevel
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addFacInfo(**args)
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
            print(f"AXL error addFacInfo: ", str(err), file=sys.stderr)
            return False
        

    def HuntList(self, **args):
        """
        HuntList parameters
        :param description: description
	:param callManagerGroupName: callManagerGroupName
	:param routeListEnabled: routeListEnabled
	:param voiceMailUsage: voiceMailUsage
	:param members: members
	:param name: name
	:param lineGroupName: lineGroupName
	:param selectionOrder: selectionOrder
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addHuntList(**args)
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
            print(f"AXL error addHuntList: ", str(err), file=sys.stderr)
            return False
        

    def IvrUserLocale(self, **args):
        """
        IvrUserLocale parameters
        :param userLocale: userLocale
	:param orderIndex: orderIndex
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addIvrUserLocale(**args)
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
            print(f"AXL error addIvrUserLocale: ", str(err), file=sys.stderr)
            return False
        

    def LineGroup(self, **args):
        """
        LineGroup parameters
        :param distributionAlgorithm: distributionAlgorithm
	:param rnaReversionTimeOut: rnaReversionTimeOut
	:param huntAlgorithmNoAnswer: huntAlgorithmNoAnswer
	:param huntAlgorithmBusy: huntAlgorithmBusy
	:param huntAlgorithmNotAvailable: huntAlgorithmNotAvailable
	:param members: members
	:param name: name
	:param autoLogOffHunt: autoLogOffHunt
	:param lineSelectionOrder: lineSelectionOrder
	:param directoryNumber: directoryNumber
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLineGroup(**args)
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
            print(f"AXL error addLineGroup: ", str(err), file=sys.stderr)
            return False
        

    def RecordingProfile(self, **args):
        """
        RecordingProfile parameters
        :param name: name
	:param recordingCssName: recordingCssName
	:param recorderDestination: recorderDestination
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRecordingProfile(**args)
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
            print(f"AXL error addRecordingProfile: ", str(err), file=sys.stderr)
            return False
        

    def RouteFilter(self, **args):
        """
        RouteFilter parameters
        :param name: name
	:param dialPlanName: dialPlanName
	:param members: members
	:param dialPlanTagName: dialPlanTagName
	:param digits: digits
	:param operator: operator
	:param priority: priority
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRouteFilter(**args)
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
            print(f"AXL error addRouteFilter: ", str(err), file=sys.stderr)
            return False
        

    def CallManagerGroup(self, **args):
        """
        CallManagerGroup parameters
        :param name: name
	:param tftpDefault: tftpDefault
	:param members: members
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCallManagerGroup(**args)
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
            print(f"AXL error addCallManagerGroup: ", str(err), file=sys.stderr)
            return False
        

    def UserGroup(self, **args):
        """
        UserGroup parameters
        :param members: members
	:param userRoles: userRoles
	:param name: name
	:param userId: userId
	:param roleName: roleName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addUserGroup(**args)
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
            print(f"AXL error addUserGroup: ", str(err), file=sys.stderr)
            return False
        

    def DhcpServer(self, **args):
        """
        DhcpServer parameters
        :param processNodeName: processNodeName
	:param primaryDnsIpAddress: primaryDnsIpAddress
	:param secondaryDnsIpAddress: secondaryDnsIpAddress
	:param primaryTftpServerIpAddress: primaryTftpServerIpAddress
	:param secondaryTftpServerIpAddress: secondaryTftpServerIpAddress
	:param bootstrapServerIpAddress: bootstrapServerIpAddress
	:param domainName: domainName
	:param tftpServerName: tftpServerName
	:param arpCacheTimeout: arpCacheTimeout
	:param ipAddressLeaseTime: ipAddressLeaseTime
	:param renewalTime: renewalTime
	:param rebindingTime: rebindingTime
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDhcpServer(**args)
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
            print(f"AXL error addDhcpServer: ", str(err), file=sys.stderr)
            return False
        

    def DhcpSubnet(self, **args):
        """
        DhcpSubnet parameters
        :param dhcpServerName: dhcpServerName
	:param subnetIpAddress: subnetIpAddress
	:param primaryStartIpAddress: primaryStartIpAddress
	:param primaryEndIpAddress: primaryEndIpAddress
	:param secondaryStartIpAddress: secondaryStartIpAddress
	:param secondaryEndIpAddress: secondaryEndIpAddress
	:param primaryRouterIpAddress: primaryRouterIpAddress
	:param secondaryRouterIpAddress: secondaryRouterIpAddress
	:param subnetMask: subnetMask
	:param domainName: domainName
	:param primaryDnsIpAddress: primaryDnsIpAddress
	:param secondaryDnsIpAddress: secondaryDnsIpAddress
	:param tftpServerName: tftpServerName
	:param primaryTftpServerIpAddress: primaryTftpServerIpAddress
	:param secondaryTftpServerIpAddress: secondaryTftpServerIpAddress
	:param bootstrapServerIpAddress: bootstrapServerIpAddress
	:param arpCacheTimeout: arpCacheTimeout
	:param ipAddressLeaseTime: ipAddressLeaseTime
	:param renewalTime: renewalTime
	:param rebindingTime: rebindingTime
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDhcpSubnet(**args)
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
            print(f"AXL error addDhcpSubnet: ", str(err), file=sys.stderr)
            return False
        

    def CallPark(self, **args):
        """
        CallPark parameters
        :param pattern: pattern
	:param description: description
	:param routePartitionName: routePartitionName
	:param callManagerName: callManagerName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCallPark(**args)
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
            print(f"AXL error addCallPark: ", str(err), file=sys.stderr)
            return False
        

    def DirectedCallPark(self, **args):
        """
        DirectedCallPark parameters
        :param pattern: pattern
	:param description: description
	:param routePartitionName: routePartitionName
	:param retrievalPrefix: retrievalPrefix
	:param reversionPattern: reversionPattern
	:param revertCssName: revertCssName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDirectedCallPark(**args)
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
            print(f"AXL error addDirectedCallPark: ", str(err), file=sys.stderr)
            return False
        

    def MeetMe(self, **args):
        """
        MeetMe parameters
        :param pattern: pattern
	:param description: description
	:param routePartitionName: routePartitionName
	:param minimumSecurityLevel: minimumSecurityLevel
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMeetMe(**args)
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
            print(f"AXL error addMeetMe: ", str(err), file=sys.stderr)
            return False
        

    def ConferenceNow(self, **args):
        """
        ConferenceNow parameters
        :param conferenceNowNumber: conferenceNowNumber
	:param routePartitionName: routePartitionName
	:param description: description
	:param maxWaitTimeForHost: maxWaitTimeForHost
	:param MohAudioSourceId: MohAudioSourceId
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addConferenceNow(**args)
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
            print(f"AXL error addConferenceNow: ", str(err), file=sys.stderr)
            return False
        

    def MobileVoiceAccess(self, **args):
        """
        MobileVoiceAccess parameters
        :param pattern: pattern
	:param routePartitionName: routePartitionName
	:param locales: locales
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMobileVoiceAccess(**args)
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
            print(f"AXL error addMobileVoiceAccess: ", str(err), file=sys.stderr)
            return False
        

    def RouteList(self, **args):
        """
        RouteList parameters
        :param name: name
	:param description: description
	:param callManagerGroupName: callManagerGroupName
	:param routeListEnabled: routeListEnabled
	:param members: members
	:param runOnEveryNode: runOnEveryNode
	:param routeGroupName: routeGroupName
	:param selectionOrder: selectionOrder
	:param calledPartyTransformationMask: calledPartyTransformationMask
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param prefixDigitsOut: prefixDigitsOut
	:param useFullyQualifiedCallingPartyNumber: useFullyQualifiedCallingPartyNumber
	:param callingPartyNumberingPlan: callingPartyNumberingPlan
	:param callingPartyNumberType: callingPartyNumberType
	:param calledPartyNumberingPlan: calledPartyNumberingPlan
	:param calledPartyNumberType: calledPartyNumberType
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRouteList(**args)
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
            print(f"AXL error addRouteList: ", str(err), file=sys.stderr)
            return False
        

    def User(self, **args):
        """
        User parameters
        :param members: members
	:param userRoles: userRoles
	:param name: name
	:param firstName: firstName
	:param displayName: displayName
	:param middleName: middleName
	:param lastName: lastName
	:param emMaxLoginTime: emMaxLoginTime
	:param userid: userid
	:param password: password
	:param pin: pin
	:param mailid: mailid
	:param department: department
	:param manager: manager
	:param userLocale: userLocale
	:param associatedDevices: associatedDevices
	:param primaryExtension: primaryExtension
	:param associatedPc: associatedPc
	:param associatedGroups: associatedGroups
	:param enableCti: enableCti
	:param digestCredentials: digestCredentials
	:param phoneProfiles: phoneProfiles
	:param defaultProfile: defaultProfile
	:param presenceGroupName: presenceGroupName
	:param subscribeCallingSearchSpaceName: subscribeCallingSearchSpaceName
	:param enableMobility: enableMobility
	:param enableMobileVoiceAccess: enableMobileVoiceAccess
	:param maxDeskPickupWaitTime: maxDeskPickupWaitTime
	:param remoteDestinationLimit: remoteDestinationLimit
	:param passwordCredentials: passwordCredentials
	:param pinCredentials: pinCredentials
	:param enableEmcc: enableEmcc
	:param ctiControlledDeviceProfiles: ctiControlledDeviceProfiles
	:param patternPrecedence: patternPrecedence
	:param numericUserId: numericUserId
	:param mlppPassword: mlppPassword
	:param customUserFields: customUserFields
	:param homeCluster: homeCluster
	:param imAndPresenceEnable: imAndPresenceEnable
	:param serviceProfile: serviceProfile
	:param lineAppearanceAssociationForPresences: lineAppearanceAssociationForPresences
	:param directoryUri: directoryUri
	:param telephoneNumber: telephoneNumber
	:param title: title
	:param mobileNumber: mobileNumber
	:param homeNumber: homeNumber
	:param pagerNumber: pagerNumber
	:param extensionsInfo: extensionsInfo
	:param selfService: selfService
	:param userProfile: userProfile
	:param calendarPresence: calendarPresence
	:param ldapDirectoryName: ldapDirectoryName
	:param userIdentity: userIdentity
	:param nameDialing: nameDialing
	:param ipccExtension: ipccExtension
	:param ipccRoutePartition: ipccRoutePartition
	:param convertUserAccount: convertUserAccount
	:param enableUserToHostConferenceNow: enableUserToHostConferenceNow
	:param attendeesAccessCode: attendeesAccessCode
	:param zeroHop: zeroHop
	:param customerName: customerName
	:param associatedHeadsets: associatedHeadsets
	:param userId: userId
	:param password: password
	:param pin: pin
	:param lastName: lastName
	:param middleName: middleName
	:param firstName: firstName
	:param productType: productType
	:param name: name
	:param dnCssName: dnCssName
	:param phoneCssName: phoneCssName
	:param e164Mask: e164Mask
	:param extension: extension
	:param routePartitionName: routePartitionName
	:param voiceMailProfileName: voiceMailProfileName
	:param enableExtensionMobility: enableExtensionMobility
	:param DirectoryURI: DirectoryURI
	:param DirectoryNumberURIPartition: DirectoryNumberURIPartition
	:param name: name
	:param description: description
	:param deskPhones: deskPhones
	:param mobileDevices: mobileDevices
	:param profile: profile
	:param universalLineTemplate: universalLineTemplate
	:param allowProvision: allowProvision
	:param limitProvision: limitProvision
	:param allowPhoneReassign: allowPhoneReassign
	:param defaultUserProfile: defaultUserProfile
	:param enableMra: enableMra
	:param mraPolicy_Desktop: mraPolicy_Desktop
	:param mraPolicy_Mobile: mraPolicy_Mobile
	:param allowProvisionEMMaxLoginTime: allowProvisionEMMaxLoginTime
	:param userId: userId
	:param roleName: roleName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addUser(**args)
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
            print(f"AXL error addUser: ", str(err), file=sys.stderr)
            return False
        

    def AppUser(self, **args):
        """
        AppUser parameters
        :param userid: userid
	:param password: password
	:param passwordCredentials: passwordCredentials
	:param digestCredentials: digestCredentials
	:param presenceGroupName: presenceGroupName
	:param acceptPresenceSubscription: acceptPresenceSubscription
	:param acceptOutOfDialogRefer: acceptOutOfDialogRefer
	:param acceptUnsolicitedNotification: acceptUnsolicitedNotification
	:param allowReplaceHeader: allowReplaceHeader
	:param associatedDevices: associatedDevices
	:param associatedGroups: associatedGroups
	:param ctiControlledDeviceProfiles: ctiControlledDeviceProfiles
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addAppUser(**args)
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
            print(f"AXL error addAppUser: ", str(err), file=sys.stderr)
            return False
        

    def SipRealm(self, **args):
        """
        SipRealm parameters
        :param realm: realm
	:param userid: userid
	:param digestCredentials: digestCredentials
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSipRealm(**args)
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
            print(f"AXL error addSipRealm: ", str(err), file=sys.stderr)
            return False
        

    def PhoneNtp(self, **args):
        """
        PhoneNtp parameters
        :param ipAddress: ipAddress
	:param ipv6Address: ipv6Address
	:param description: description
	:param mode: mode
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addPhoneNtp(**args)
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
            print(f"AXL error addPhoneNtp: ", str(err), file=sys.stderr)
            return False
        

    def DateTimeGroup(self, **args):
        """
        DateTimeGroup parameters
        :param name: name
	:param timeZone: timeZone
	:param separator: separator
	:param dateformat: dateformat
	:param timeFormat: timeFormat
	:param phoneNtpReferences: phoneNtpReferences
	:param phoneNtpName: phoneNtpName
	:param selectionOrder: selectionOrder
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDateTimeGroup(**args)
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
            print(f"AXL error addDateTimeGroup: ", str(err), file=sys.stderr)
            return False
        

    def PresenceGroup(self, **args):
        """
        PresenceGroup parameters
        :param name: name
	:param description: description
	:param presenceGroups: presenceGroups
	:param presenceGroupName: presenceGroupName
	:param subscriptionPermission: subscriptionPermission
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addPresenceGroup(**args)
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
            print(f"AXL error addPresenceGroup: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocation(self, **args):
        """
        GeoLocation parameters
        :param name: name
	:param country: country
	:param description: description
	:param nationalSubDivision: nationalSubDivision
	:param district: district
	:param communityName: communityName
	:param cityDivision: cityDivision
	:param neighbourhood: neighbourhood
	:param street: street
	:param leadingStreetDirection: leadingStreetDirection
	:param trailingStreetSuffix: trailingStreetSuffix
	:param streetSuffix: streetSuffix
	:param houseNumber: houseNumber
	:param houseNumberSuffix: houseNumberSuffix
	:param landmark: landmark
	:param location: location
	:param floor: floor
	:param occupantName: occupantName
	:param postalCode: postalCode
	:param name: name
	:param description: description
	:param useCountry: useCountry
	:param useNationalSubDivision: useNationalSubDivision
	:param useDistrict: useDistrict
	:param useCommunityName: useCommunityName
	:param useCityDivision: useCityDivision
	:param useNeighbourhood: useNeighbourhood
	:param useStreet: useStreet
	:param useLeadingStreetDirection: useLeadingStreetDirection
	:param useTrailingStreetSuffix: useTrailingStreetSuffix
	:param useStreetSuffix: useStreetSuffix
	:param useHouseNumber: useHouseNumber
	:param useHouseNumberSuffix: useHouseNumberSuffix
	:param useLandmark: useLandmark
	:param useLocation: useLocation
	:param useFloor: useFloor
	:param useOccupantName: useOccupantName
	:param usePostalCode: usePostalCode
	:param name: name
	:param country: country
	:param description: description
	:param nationalSubDivision: nationalSubDivision
	:param district: district
	:param communityName: communityName
	:param cityDivision: cityDivision
	:param neighbourhood: neighbourhood
	:param street: street
	:param leadingStreetDirection: leadingStreetDirection
	:param trailingStreetSuffix: trailingStreetSuffix
	:param streetSuffix: streetSuffix
	:param houseNumber: houseNumber
	:param houseNumberSuffix: houseNumberSuffix
	:param landmark: landmark
	:param location: location
	:param floor: floor
	:param occupantName: occupantName
	:param postalCode: postalCode
	:param relatedPolicies: relatedPolicies
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGeoLocation(**args)
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
            print(f"AXL error addGeoLocation: ", str(err), file=sys.stderr)
            return False
        

    def Srst(self, **args):
        """
        Srst parameters
        :param name: name
	:param port: port
	:param ipAddress: ipAddress
	:param ipv6Address: ipv6Address
	:param SipNetwork: SipNetwork
	:param SipPort: SipPort
	:param isSecure: isSecure
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSrst(**args)
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
            print(f"AXL error addSrst: ", str(err), file=sys.stderr)
            return False
        

    def MlppDomain(self, **args):
        """
        MlppDomain parameters
        :param domainName: domainName
	:param domainId: domainId
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMlppDomain(**args)
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
            print(f"AXL error addMlppDomain: ", str(err), file=sys.stderr)
            return False
        

    def CumaServerSecurityProfile(self, **args):
        """
        CumaServerSecurityProfile parameters
        :param name: name
	:param description: description
	:param securityMode: securityMode
	:param transportType: transportType
	:param x509SubjectName: x509SubjectName
	:param serverIpHostName: serverIpHostName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCumaServerSecurityProfile(**args)
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
            print(f"AXL error addCumaServerSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationServer(self, **args):
        """
        ApplicationServer parameters
        :param appServerType: appServerType
	:param name: name
	:param ipAddress: ipAddress
	:param appUsers: appUsers
	:param url: url
	:param endUserUrl: endUserUrl
	:param processNodeName: processNodeName
	:param endUsers: endUsers
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addApplicationServer(**args)
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
            print(f"AXL error addApplicationServer: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationUserCapfProfile(self, **args):
        """
        ApplicationUserCapfProfile parameters
        :param applicationUser: applicationUser
	:param instanceId: instanceId
	:param certificateOperation: certificateOperation
	:param authenticationMode: authenticationMode
	:param authenticationString: authenticationString
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param operationCompletion: operationCompletion
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addApplicationUserCapfProfile(**args)
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
            print(f"AXL error addApplicationUserCapfProfile: ", str(err), file=sys.stderr)
            return False
        

    def EndUserCapfProfile(self, **args):
        """
        EndUserCapfProfile parameters
        :param endUserId: endUserId
	:param instanceId: instanceId
	:param certificationOperation: certificationOperation
	:param authenticationMode: authenticationMode
	:param authenticationString: authenticationString
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param operationCompletion: operationCompletion
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addEndUserCapfProfile(**args)
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
            print(f"AXL error addEndUserCapfProfile: ", str(err), file=sys.stderr)
            return False
        

    def UserPhoneAssociation(self, **args):
        """
        UserPhoneAssociation parameters
        :param userId: userId
	:param password: password
	:param pin: pin
	:param lastName: lastName
	:param middleName: middleName
	:param firstName: firstName
	:param productType: productType
	:param name: name
	:param dnCssName: dnCssName
	:param phoneCssName: phoneCssName
	:param e164Mask: e164Mask
	:param extension: extension
	:param routePartitionName: routePartitionName
	:param voiceMailProfileName: voiceMailProfileName
	:param enableExtensionMobility: enableExtensionMobility
	:param DirectoryURI: DirectoryURI
	:param DirectoryNumberURIPartition: DirectoryNumberURIPartition
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addUserPhoneAssociation(**args)
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
            print(f"AXL error addUserPhoneAssociation: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocationFilter(self, **args):
        """
        GeoLocationFilter parameters
        :param name: name
	:param description: description
	:param useCountry: useCountry
	:param useNationalSubDivision: useNationalSubDivision
	:param useDistrict: useDistrict
	:param useCommunityName: useCommunityName
	:param useCityDivision: useCityDivision
	:param useNeighbourhood: useNeighbourhood
	:param useStreet: useStreet
	:param useLeadingStreetDirection: useLeadingStreetDirection
	:param useTrailingStreetSuffix: useTrailingStreetSuffix
	:param useStreetSuffix: useStreetSuffix
	:param useHouseNumber: useHouseNumber
	:param useHouseNumberSuffix: useHouseNumberSuffix
	:param useLandmark: useLandmark
	:param useLocation: useLocation
	:param useFloor: useFloor
	:param useOccupantName: useOccupantName
	:param usePostalCode: usePostalCode
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGeoLocationFilter(**args)
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
            print(f"AXL error addGeoLocationFilter: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailProfile(self, **args):
        """
        VoiceMailProfile parameters
        :param name: name
	:param description: description
	:param isDefault: isDefault
	:param voiceMailboxMask: voiceMailboxMask
	:param voiceMailPilot: voiceMailPilot
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addVoiceMailProfile(**args)
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
            print(f"AXL error addVoiceMailProfile: ", str(err), file=sys.stderr)
            return False
        

    def VoiceMailPort(self, **args):
        """
        VoiceMailPort parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param locationName: locationName
	:param preemption: preemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param securityProfileName: securityProfileName
	:param geoLocationName: geoLocationName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param dnPattern: dnPattern
	:param routePartition: routePartition
	:param dnCallingSearchSpace: dnCallingSearchSpace
	:param aarNeighborhoodName: aarNeighborhoodName
	:param callerIdDisplay: callerIdDisplay
	:param callerIdDisplayAscii: callerIdDisplayAscii
	:param externalMask: externalMask
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addVoiceMailPort(**args)
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
            print(f"AXL error addVoiceMailPort: ", str(err), file=sys.stderr)
            return False
        

    def Gatekeeper(self, **args):
        """
        Gatekeeper parameters
        :param name: name
	:param description: description
	:param rrqTimeToLive: rrqTimeToLive
	:param retryTimeout: retryTimeout
	:param enableDevice: enableDevice
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGatekeeper(**args)
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
            print(f"AXL error addGatekeeper: ", str(err), file=sys.stderr)
            return False
        

    def PhoneButtonTemplate(self, **args):
        """
        PhoneButtonTemplate parameters
        :param name: name
	:param basePhoneTemplateName: basePhoneTemplateName
	:param buttons: buttons
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addPhoneButtonTemplate(**args)
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
            print(f"AXL error addPhoneButtonTemplate: ", str(err), file=sys.stderr)
            return False
        

    def CommonPhoneConfig(self, **args):
        """
        CommonPhoneConfig parameters
        :param name: name
	:param description: description
	:param unlockPwd: unlockPwd
	:param dndOption: dndOption
	:param dndAlertingType: dndAlertingType
	:param backgroundImage: backgroundImage
	:param phonePersonalization: phonePersonalization
	:param phoneServiceDisplay: phoneServiceDisplay
	:param sshUserId: sshUserId
	:param sshPwd: sshPwd
	:param vendorConfig: vendorConfig
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVoiceMessage: alwaysUsePrimeLineForVoiceMessage
	:param vpnGroupName: vpnGroupName
	:param vpnProfileName: vpnProfileName
	:param featureControlPolicy: featureControlPolicy
	:param wifiHotspotProfile: wifiHotspotProfile
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCommonPhoneConfig(**args)
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
            print(f"AXL error addCommonPhoneConfig: ", str(err), file=sys.stderr)
            return False
        

    def MessageWaiting(self, **args):
        """
        MessageWaiting parameters
        :param pattern: pattern
	:param routePartitionName: routePartitionName
	:param description: description
	:param messageWaitingIndicator: messageWaitingIndicator
	:param callingSearchSpaceName: callingSearchSpaceName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMessageWaiting(**args)
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
            print(f"AXL error addMessageWaiting: ", str(err), file=sys.stderr)
            return False
        

    def IpPhoneServices(self, **args):
        """
        IpPhoneServices parameters
        :param serviceName: serviceName
	:param asciiServiceName: asciiServiceName
	:param serviceDescription: serviceDescription
	:param serviceUrl: serviceUrl
	:param secureServiceUrl: secureServiceUrl
	:param serviceCategory: serviceCategory
	:param serviceType: serviceType
	:param serviceVendor: serviceVendor
	:param serviceVersion: serviceVersion
	:param enabled: enabled
	:param enterpriseSubscription: enterpriseSubscription
	:param parameters: parameters
	:param name: name
	:param displayName: displayName
	:param default: default
	:param description: description
	:param paramRequired: paramRequired
	:param paramPassword: paramPassword
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addIpPhoneServices(**args)
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
            print(f"AXL error addIpPhoneServices: ", str(err), file=sys.stderr)
            return False
        

    def CtiRoutePoint(self, **args):
        """
        CtiRoutePoint parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param userLocale: userLocale
	:param lines: lines
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCtiRoutePoint(**args)
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
            print(f"AXL error addCtiRoutePoint: ", str(err), file=sys.stderr)
            return False
        

    def TransPattern(self, **args):
        """
        TransPattern parameters
        :param pattern: pattern
	:param description: description
	:param usage: usage
	:param routePartitionName: routePartitionName
	:param blockEnable: blockEnable
	:param calledPartyTransformationMask: calledPartyTransformationMask
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param dialPlanName: dialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param patternUrgency: patternUrgency
	:param prefixDigitsOut: prefixDigitsOut
	:param routeFilterName: routeFilterName
	:param callingLinePresentationBit: callingLinePresentationBit
	:param callingNamePresentationBit: callingNamePresentationBit
	:param connectedLinePresentationBit: connectedLinePresentationBit
	:param connectedNamePresentationBit: connectedNamePresentationBit
	:param patternPrecedence: patternPrecedence
	:param provideOutsideDialtone: provideOutsideDialtone
	:param callingPartyNumberingPlan: callingPartyNumberingPlan
	:param callingPartyNumberType: callingPartyNumberType
	:param calledPartyNumberingPlan: calledPartyNumberingPlan
	:param calledPartyNumberType: calledPartyNumberType
	:param callingSearchSpaceName: callingSearchSpaceName
	:param resourcePriorityNamespaceName: resourcePriorityNamespaceName
	:param routeNextHopByCgpn: routeNextHopByCgpn
	:param routeClass: routeClass
	:param callInterceptProfileName: callInterceptProfileName
	:param releaseClause: releaseClause
	:param useOriginatorCss: useOriginatorCss
	:param dontWaitForIDTOnSubsequentHops: dontWaitForIDTOnSubsequentHops
	:param isEmergencyServiceNumber: isEmergencyServiceNumber
	:param usage: usage
	:param routePartitionName: routePartitionName
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param dialPlanName: dialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param routeFilterName: routeFilterName
	:param callingLinePresentationBit: callingLinePresentationBit
	:param callingNamePresentationBit: callingNamePresentationBit
	:param connectedLinePresentationBit: connectedLinePresentationBit
	:param connectedNamePresentationBit: connectedNamePresentationBit
	:param patternPrecedence: patternPrecedence
	:param callingPartyNumberingPlan: callingPartyNumberingPlan
	:param callingPartyNumberType: callingPartyNumberType
	:param calledPartyNumberingPlan: calledPartyNumberingPlan
	:param calledPartyNumberType: calledPartyNumberType
	:param callingSearchSpaceName: callingSearchSpaceName
	:param resourcePriorityNamespaceName: resourcePriorityNamespaceName
	:param routeClass: routeClass
	:param callInterceptProfileName: callInterceptProfileName
	:param releaseClause: releaseClause
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addTransPattern(**args)
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
            print(f"AXL error addTransPattern: ", str(err), file=sys.stderr)
            return False
        

    def CallingPartyTransformationPattern(self, **args):
        """
        CallingPartyTransformationPattern parameters
        :param pattern: pattern
	:param description: description
	:param routePartitionName: routePartitionName
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param dialPlanName: dialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param routeFilterName: routeFilterName
	:param callingLinePresentationBit: callingLinePresentationBit
	:param callingPartyNumberingPlan: callingPartyNumberingPlan
	:param callingPartyNumberType: callingPartyNumberType
	:param mlppPreemptionDisabled: mlppPreemptionDisabled
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCallingPartyTransformationPattern(**args)
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
            print(f"AXL error addCallingPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
        

    def SipRoutePattern(self, **args):
        """
        SipRoutePattern parameters
        :param pattern: pattern
	:param description: description
	:param usage: usage
	:param routePartitionName: routePartitionName
	:param blockEnable: blockEnable
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param callingLinePresentationBit: callingLinePresentationBit
	:param callingNamePresentationBit: callingNamePresentationBit
	:param connectedLinePresentationBit: connectedLinePresentationBit
	:param connectedNamePresentationBit: connectedNamePresentationBit
	:param sipTrunkName: sipTrunkName
	:param dnOrPatternIpv6: dnOrPatternIpv6
	:param routeOnUserPart: routeOnUserPart
	:param useCallerCss: useCallerCss
	:param domainRoutingCssName: domainRoutingCssName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSipRoutePattern(**args)
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
            print(f"AXL error addSipRoutePattern: ", str(err), file=sys.stderr)
            return False
        

    def HuntPilot(self, **args):
        """
        HuntPilot parameters
        :param pattern: pattern
	:param description: description
	:param routePartitionName: routePartitionName
	:param blockEnable: blockEnable
	:param calledPartyTransformationMask: calledPartyTransformationMask
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param dialPlanName: dialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param patternUrgency: patternUrgency
	:param prefixDigitsOut: prefixDigitsOut
	:param routeFilterName: routeFilterName
	:param callingLinePresentationBit: callingLinePresentationBit
	:param callingNamePresentationBit: callingNamePresentationBit
	:param connectedLinePresentationBit: connectedLinePresentationBit
	:param connectedNamePresentationBit: connectedNamePresentationBit
	:param patternPrecedence: patternPrecedence
	:param provideOutsideDialtone: provideOutsideDialtone
	:param callingPartyNumberingPlan: callingPartyNumberingPlan
	:param callingPartyNumberType: callingPartyNumberType
	:param calledPartyNumberingPlan: calledPartyNumberingPlan
	:param calledPartyNumberType: calledPartyNumberType
	:param huntListName: huntListName
	:param parkMonForwardNoRetrieve: parkMonForwardNoRetrieve
	:param alertingName: alertingName
	:param asciiAlertingName: asciiAlertingName
	:param e164Mask: e164Mask
	:param aarNeighborhoodName: aarNeighborhoodName
	:param forwardHuntNoAnswer: forwardHuntNoAnswer
	:param forwardHuntBusy: forwardHuntBusy
	:param callPickupGroupName: callPickupGroupName
	:param maxHuntduration: maxHuntduration
	:param releaseClause: releaseClause
	:param displayConnectedNumber: displayConnectedNumber
	:param queueCalls: queueCalls
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addHuntPilot(**args)
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
            print(f"AXL error addHuntPilot: ", str(err), file=sys.stderr)
            return False
        

    def RoutePattern(self, **args):
        """
        RoutePattern parameters
        :param pattern: pattern
	:param description: description
	:param routePartitionName: routePartitionName
	:param blockEnable: blockEnable
	:param calledPartyTransformationMask: calledPartyTransformationMask
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param dialPlanName: dialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param networkLocation: networkLocation
	:param patternUrgency: patternUrgency
	:param prefixDigitsOut: prefixDigitsOut
	:param routeFilterName: routeFilterName
	:param callingLinePresentationBit: callingLinePresentationBit
	:param callingNamePresentationBit: callingNamePresentationBit
	:param connectedLinePresentationBit: connectedLinePresentationBit
	:param connectedNamePresentationBit: connectedNamePresentationBit
	:param supportOverlapSending: supportOverlapSending
	:param patternPrecedence: patternPrecedence
	:param releaseClause: releaseClause
	:param allowDeviceOverride: allowDeviceOverride
	:param provideOutsideDialtone: provideOutsideDialtone
	:param callingPartyNumberingPlan: callingPartyNumberingPlan
	:param callingPartyNumberType: callingPartyNumberType
	:param calledPartyNumberingPlan: calledPartyNumberingPlan
	:param calledPartyNumberType: calledPartyNumberType
	:param destination: destination
	:param authorizationCodeRequired: authorizationCodeRequired
	:param authorizationLevelRequired: authorizationLevelRequired
	:param clientCodeRequired: clientCodeRequired
	:param isdnNsfInfoElement: isdnNsfInfoElement
	:param resourcePriorityNamespaceName: resourcePriorityNamespaceName
	:param routeClass: routeClass
	:param enableDccEnforcement: enableDccEnforcement
	:param blockedCallPercentage: blockedCallPercentage
	:param externalCallControl: externalCallControl
	:param isEmergencyServiceNumber: isEmergencyServiceNumber
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRoutePattern(**args)
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
            print(f"AXL error addRoutePattern: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationDialRules(self, **args):
        """
        ApplicationDialRules parameters
        :param name: name
	:param description: description
	:param numberBeginWith: numberBeginWith
	:param numberOfDigits: numberOfDigits
	:param digitsToBeRemoved: digitsToBeRemoved
	:param prefixPattern: prefixPattern
	:param priority: priority
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addApplicationDialRules(**args)
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
            print(f"AXL error addApplicationDialRules: ", str(err), file=sys.stderr)
            return False
        

    def DirectoryLookupDialRules(self, **args):
        """
        DirectoryLookupDialRules parameters
        :param name: name
	:param description: description
	:param numberBeginWith: numberBeginWith
	:param numberOfDigits: numberOfDigits
	:param digitsToBeRemoved: digitsToBeRemoved
	:param prefixPattern: prefixPattern
	:param priority: priority
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDirectoryLookupDialRules(**args)
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
            print(f"AXL error addDirectoryLookupDialRules: ", str(err), file=sys.stderr)
            return False
        

    def PhoneSecurityProfile(self, **args):
        """
        PhoneSecurityProfile parameters
        :param phoneType: phoneType
	:param protocol: protocol
	:param name: name
	:param description: description
	:param deviceSecurityMode: deviceSecurityMode
	:param authenticationMode: authenticationMode
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param tftpEncryptedConfig: tftpEncryptedConfig
	:param EnableOAuthAuthentication: EnableOAuthAuthentication
	:param nonceValidityTime: nonceValidityTime
	:param transportType: transportType
	:param sipPhonePort: sipPhonePort
	:param enableDigestAuthentication: enableDigestAuthentication
	:param excludeDigestCredentials: excludeDigestCredentials
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addPhoneSecurityProfile(**args)
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
            print(f"AXL error addPhoneSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def SipDialRules(self, **args):
        """
        SipDialRules parameters
        :param dialPattern: dialPattern
	:param name: name
	:param description: description
	:param patterns: patterns
	:param plars: plars
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSipDialRules(**args)
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
            print(f"AXL error addSipDialRules: ", str(err), file=sys.stderr)
            return False
        

    def ConferenceBridge(self, **args):
        """
        ConferenceBridge parameters
        :param name: name
	:param description: description
	:param product: product
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param locationName: locationName
	:param subUnit: subUnit
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param maximumCapacity: maximumCapacity
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param securityProfileName: securityProfileName
	:param destinationAddress: destinationAddress
	:param mcuConferenceBridgeSipPort: mcuConferenceBridgeSipPort
	:param sipProfile: sipProfile
	:param srtpAllowed: srtpAllowed
	:param normalizationScript: normalizationScript
	:param enableTrace: enableTrace
	:param normalizationScriptInfos: normalizationScriptInfos
	:param userName: userName
	:param password: password
	:param httpPort: httpPort
	:param useHttps: useHttps
	:param addresses: addresses
	:param conferenceBridgePrefix: conferenceBridgePrefix
	:param allowCFBControlOfCallSecurityIcon: allowCFBControlOfCallSecurityIcon
	:param overrideSIPTrunkAddress: overrideSIPTrunkAddress
	:param sipTrunkName: sipTrunkName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addConferenceBridge(**args)
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
            print(f"AXL error addConferenceBridge: ", str(err), file=sys.stderr)
            return False
        

    def Mtp(self, **args):
        """
        Mtp parameters
        :param mtpType: mtpType
	:param name: name
	:param description: description
	:param devicePoolName: devicePoolName
	:param trustedRelayPoint: trustedRelayPoint
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMtp(**args)
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
            print(f"AXL error addMtp: ", str(err), file=sys.stderr)
            return False
        

    def RemoteDestinationProfile(self, **args):
        """
        RemoteDestinationProfile parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param lines: lines
	:param callInfoPrivacyStatus: callInfoPrivacyStatus
	:param userId: userId
	:param ignorePresentationIndicators: ignorePresentationIndicators
	:param rerouteCallingSearchSpaceName: rerouteCallingSearchSpaceName
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param userLocale: userLocale
	:param networkLocale: networkLocale
	:param primaryPhoneName: primaryPhoneName
	:param dndOption: dndOption
	:param dndStatus: dndStatus
	:param mobileSmartClientProfileName: mobileSmartClientProfileName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRemoteDestinationProfile(**args)
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
            print(f"AXL error addRemoteDestinationProfile: ", str(err), file=sys.stderr)
            return False
        

    def Line(self, **args):
        """
        Line parameters
        :param distributionAlgorithm: distributionAlgorithm
	:param rnaReversionTimeOut: rnaReversionTimeOut
	:param huntAlgorithmNoAnswer: huntAlgorithmNoAnswer
	:param huntAlgorithmBusy: huntAlgorithmBusy
	:param huntAlgorithmNotAvailable: huntAlgorithmNotAvailable
	:param members: members
	:param name: name
	:param autoLogOffHunt: autoLogOffHunt
	:param pattern: pattern
	:param description: description
	:param usage: usage
	:param routePartitionName: routePartitionName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param aarDestinationMask: aarDestinationMask
	:param aarKeepCallHistory: aarKeepCallHistory
	:param aarVoiceMailEnabled: aarVoiceMailEnabled
	:param callForwardAll: callForwardAll
	:param callForwardBusy: callForwardBusy
	:param callForwardBusyInt: callForwardBusyInt
	:param callForwardNoAnswer: callForwardNoAnswer
	:param callForwardNoAnswerInt: callForwardNoAnswerInt
	:param callForwardNoCoverage: callForwardNoCoverage
	:param callForwardNoCoverageInt: callForwardNoCoverageInt
	:param callForwardOnFailure: callForwardOnFailure
	:param callForwardAlternateParty: callForwardAlternateParty
	:param callForwardNotRegistered: callForwardNotRegistered
	:param callForwardNotRegisteredInt: callForwardNotRegisteredInt
	:param callPickupGroupName: callPickupGroupName
	:param autoAnswer: autoAnswer
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param callingIdPresentationWhenDiverted: callingIdPresentationWhenDiverted
	:param alertingName: alertingName
	:param asciiAlertingName: asciiAlertingName
	:param presenceGroupName: presenceGroupName
	:param shareLineAppearanceCssName: shareLineAppearanceCssName
	:param voiceMailProfileName: voiceMailProfileName
	:param patternPrecedence: patternPrecedence
	:param releaseClause: releaseClause
	:param hrDuration: hrDuration
	:param hrInterval: hrInterval
	:param cfaCssPolicy: cfaCssPolicy
	:param defaultActivatedDeviceName: defaultActivatedDeviceName
	:param parkMonForwardNoRetrieveDn: parkMonForwardNoRetrieveDn
	:param parkMonForwardNoRetrieveIntDn: parkMonForwardNoRetrieveIntDn
	:param parkMonForwardNoRetrieveVmEnabled: parkMonForwardNoRetrieveVmEnabled
	:param parkMonForwardNoRetrieveIntVmEnabled: parkMonForwardNoRetrieveIntVmEnabled
	:param parkMonForwardNoRetrieveCssName: parkMonForwardNoRetrieveCssName
	:param parkMonForwardNoRetrieveIntCssName: parkMonForwardNoRetrieveIntCssName
	:param parkMonReversionTimer: parkMonReversionTimer
	:param partyEntranceTone: partyEntranceTone
	:param directoryURIs: directoryURIs
	:param allowCtiControlFlag: allowCtiControlFlag
	:param rejectAnonymousCall: rejectAnonymousCall
	:param patternUrgency: patternUrgency
	:param confidentialAccess: confidentialAccess
	:param externalCallControlProfile: externalCallControlProfile
	:param enterpriseAltNum: enterpriseAltNum
	:param e164AltNum: e164AltNum
	:param pstnFailover: pstnFailover
	:param callControlAgentProfile: callControlAgentProfile
	:param useEnterpriseAltNum: useEnterpriseAltNum
	:param useE164AltNum: useE164AltNum
	:param active: active
	:param externalPresentationInfo: externalPresentationInfo
	:param usage: usage
	:param routePartitionName: routePartitionName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param callForwardAll: callForwardAll
	:param callForwardBusy: callForwardBusy
	:param callForwardBusyInt: callForwardBusyInt
	:param callForwardNoAnswer: callForwardNoAnswer
	:param callForwardNoAnswerInt: callForwardNoAnswerInt
	:param callForwardNoCoverage: callForwardNoCoverage
	:param callForwardNoCoverageInt: callForwardNoCoverageInt
	:param callForwardOnFailure: callForwardOnFailure
	:param callForwardAlternateParty: callForwardAlternateParty
	:param callForwardNotRegistered: callForwardNotRegistered
	:param callForwardNotRegisteredInt: callForwardNotRegisteredInt
	:param callPickupGroupName: callPickupGroupName
	:param autoAnswer: autoAnswer
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param callingIdPresentationWhenDiverted: callingIdPresentationWhenDiverted
	:param presenceGroupName: presenceGroupName
	:param shareLineAppearanceCssName: shareLineAppearanceCssName
	:param voiceMailProfileName: voiceMailProfileName
	:param patternPrecedence: patternPrecedence
	:param releaseClause: releaseClause
	:param cfaCssPolicy: cfaCssPolicy
	:param defaultActivatedDeviceName: defaultActivatedDeviceName
	:param parkMonForwardNoRetrieveCssName: parkMonForwardNoRetrieveCssName
	:param parkMonForwardNoRetrieveIntCssName: parkMonForwardNoRetrieveIntCssName
	:param partyEntranceTone: partyEntranceTone
	:param directoryURIs: directoryURIs
	:param confidentialAccess: confidentialAccess
	:param externalCallControlProfile: externalCallControlProfile
	:param enterpriseAltNum: enterpriseAltNum
	:param e164AltNum: e164AltNum
	:param lineSelectionOrder: lineSelectionOrder
	:param directoryNumber: directoryNumber
	:param laapAssociate: laapAssociate
	:param laapProductType: laapProductType
	:param laapDeviceName: laapDeviceName
	:param laapDirectory: laapDirectory
	:param laapPartition: laapPartition
	:param laapDescription: laapDescription
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLine(**args)
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
            print(f"AXL error addLine: ", str(err), file=sys.stderr)
            return False
        

    def DefaultDeviceProfile(self, **args):
        """
        DefaultDeviceProfile parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param userLocale: userLocale
	:param phoneButtonTemplate: phoneButtonTemplate
	:param softkeyTemplate: softkeyTemplate
	:param privacy: privacy
	:param singleButtonBarge: singleButtonBarge
	:param joinAcrossLines: joinAcrossLines
	:param ignorePi: ignorePi
	:param dndStatus: dndStatus
	:param dndRingSetting: dndRingSetting
	:param dndOption: dndOption
	:param mlppDomainId: mlppDomainId
	:param mlppIndication: mlppIndication
	:param preemption: preemption
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVoiceMessage: alwaysUsePrimeLineForVoiceMessage
	:param emccCallingSearchSpace: emccCallingSearchSpace
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDefaultDeviceProfile(**args)
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
            print(f"AXL error addDefaultDeviceProfile: ", str(err), file=sys.stderr)
            return False
        

    def H323Phone(self, **args):
        """
        H323Phone parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param commonPhoneConfigName: commonPhoneConfigName
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param remoteDevice: remoteDevice
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVoiceMessage: alwaysUsePrimeLineForVoiceMessage
	:param srtpAllowed: srtpAllowed
	:param unattendedPort: unattendedPort
	:param subscribeCallingSearchSpaceName: subscribeCallingSearchSpaceName
	:param waitForFarEndH245TerminalSet: waitForFarEndH245TerminalSet
	:param mtpRequired: mtpRequired
	:param mtpPreferredCodec: mtpPreferredCodec
	:param callerIdDn: callerIdDn
	:param callingPartySelection: callingPartySelection
	:param callingLineIdPresentation: callingLineIdPresentation
	:param displayIEDelivery: displayIEDelivery
	:param redirectOutboundNumberIe: redirectOutboundNumberIe
	:param redirectInboundNumberIe: redirectInboundNumberIe
	:param presenceGroupName: presenceGroupName
	:param hlogStatus: hlogStatus
	:param ownerUserName: ownerUserName
	:param signalingPort: signalingPort
	:param gateKeeperInfo: gateKeeperInfo
	:param lines: lines
	:param ignorePresentationIndicators: ignorePresentationIndicators
	:param elinGroup: elinGroup
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addH323Phone(**args)
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
            print(f"AXL error addH323Phone: ", str(err), file=sys.stderr)
            return False
        

    def H323Trunk(self, **args):
        """
        H323Trunk parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param rdnTransformationCssName: rdnTransformationCssName
	:param useDevicePoolRdnTransformCss: useDevicePoolRdnTransformCss
	:param geoLocationName: geoLocationName
	:param geoLocationFilterName: geoLocationFilterName
	:param sendGeoLocation: sendGeoLocation
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param srtpAllowed: srtpAllowed
	:param unattendedPort: unattendedPort
	:param waitForFarEndH245TerminalSet: waitForFarEndH245TerminalSet
	:param mtpRequired: mtpRequired
	:param callerIdDn: callerIdDn
	:param callingPartySelection: callingPartySelection
	:param callingLineIdPresentation: callingLineIdPresentation
	:param displayIEDelivery: displayIEDelivery
	:param redirectOutboundNumberIe: redirectOutboundNumberIe
	:param redirectInboundNumberIe: redirectInboundNumberIe
	:param enableInboundFaststart: enableInboundFaststart
	:param enableOutboundFaststart: enableOutboundFaststart
	:param codecForOutboundFaststart: codecForOutboundFaststart
	:param allowH235PassThrough: allowH235PassThrough
	:param tunneledProtocol: tunneledProtocol
	:param asn1RoseOidEncoding: asn1RoseOidEncoding
	:param qsigVariant: qsigVariant
	:param transmitUtf8: transmitUtf8
	:param signalingPort: signalingPort
	:param nationalPrefix: nationalPrefix
	:param internationalPrefix: internationalPrefix
	:param unknownPrefix: unknownPrefix
	:param subscriberPrefix: subscriberPrefix
	:param sigDigits: sigDigits
	:param prefixDn: prefixDn
	:param calledPartyIeNumberType: calledPartyIeNumberType
	:param callingPartyIeNumberType: callingPartyIeNumberType
	:param calledNumberingPlan: calledNumberingPlan
	:param callingNumberingPlan: callingNumberingPlan
	:param pathReplacementSupport: pathReplacementSupport
	:param ictPassingPrecedenceLevelThroughUuie: ictPassingPrecedenceLevelThroughUuie
	:param ictSecurityAccessLevel: ictSecurityAccessLevel
	:param isSafEnabled: isSafEnabled
	:param callingPartyNationalStripDigits: callingPartyNationalStripDigits
	:param callingPartyInternationalStripDigits: callingPartyInternationalStripDigits
	:param callingPartyUnknownStripDigits: callingPartyUnknownStripDigits
	:param callingPartySubscriberStripDigits: callingPartySubscriberStripDigits
	:param callingPartyNationalTransformationCssName: callingPartyNationalTransformationCssName
	:param callingPartyInternationalTransformationCssName: callingPartyInternationalTransformationCssName
	:param callingPartyUnknownTransformationCssName: callingPartyUnknownTransformationCssName
	:param callingPartySubscriberTransformationCssName: callingPartySubscriberTransformationCssName
	:param calledPartyNationalPrefix: calledPartyNationalPrefix
	:param calledPartyInternationalPrefix: calledPartyInternationalPrefix
	:param calledPartyUnknownPrefix: calledPartyUnknownPrefix
	:param calledPartySubscriberPrefix: calledPartySubscriberPrefix
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param useDevicePoolCgpnTransformCssNatl: useDevicePoolCgpnTransformCssNatl
	:param useDevicePoolCgpnTransformCssIntl: useDevicePoolCgpnTransformCssIntl
	:param useDevicePoolCgpnTransformCssUnkn: useDevicePoolCgpnTransformCssUnkn
	:param useDevicePoolCgpnTransformCssSubs: useDevicePoolCgpnTransformCssSubs
	:param useDevicePoolCalledCssNatl: useDevicePoolCalledCssNatl
	:param useDevicePoolCalledCssIntl: useDevicePoolCalledCssIntl
	:param useDevicePoolCalledCssUnkn: useDevicePoolCalledCssUnkn
	:param useDevicePoolCalledCssSubs: useDevicePoolCalledCssSubs
	:param calledPartyNationalStripDigits: calledPartyNationalStripDigits
	:param calledPartyInternationalStripDigits: calledPartyInternationalStripDigits
	:param calledPartyUnknownStripDigits: calledPartyUnknownStripDigits
	:param calledPartySubscriberStripDigits: calledPartySubscriberStripDigits
	:param calledPartyNationalTransformationCssName: calledPartyNationalTransformationCssName
	:param calledPartyInternationalTransformationCssName: calledPartyInternationalTransformationCssName
	:param calledPartyUnknownTransformationCssName: calledPartyUnknownTransformationCssName
	:param calledPartySubscriberTransformationCssName: calledPartySubscriberTransformationCssName
	:param runOnEveryNode: runOnEveryNode
	:param destinations: destinations
	:param useDevicePoolCntdPnTransformationCss: useDevicePoolCntdPnTransformationCss
	:param cntdPnTransformationCssName: cntdPnTransformationCssName
	:param confidentialAccess: confidentialAccess
	:param connectCallBeforePlayingAnnouncement: connectCallBeforePlayingAnnouncement
	:param addressIpv4: addressIpv4
	:param sortOrder: sortOrder
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addH323Trunk(**args)
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
            print(f"AXL error addH323Trunk: ", str(err), file=sys.stderr)
            return False
        

    def Phone(self, **args):
        """
        Phone parameters
        :param ipAddress: ipAddress
	:param ipv6Address: ipv6Address
	:param description: description
	:param mode: mode
	:param name: name
	:param basePhoneTemplateName: basePhoneTemplateName
	:param buttons: buttons
	:param phoneType: phoneType
	:param protocol: protocol
	:param name: name
	:param description: description
	:param deviceSecurityMode: deviceSecurityMode
	:param authenticationMode: authenticationMode
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param tftpEncryptedConfig: tftpEncryptedConfig
	:param EnableOAuthAuthentication: EnableOAuthAuthentication
	:param nonceValidityTime: nonceValidityTime
	:param transportType: transportType
	:param sipPhonePort: sipPhonePort
	:param enableDigestAuthentication: enableDigestAuthentication
	:param excludeDigestCredentials: excludeDigestCredentials
	:param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param commonPhoneConfigName: commonPhoneConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param versionStamp: versionStamp
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param securityProfileName: securityProfileName
	:param sipProfileName: sipProfileName
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param geoLocationFilterName: geoLocationFilterName
	:param sendGeoLocation: sendGeoLocation
	:param lines: lines
	:param phoneTemplateName: phoneTemplateName
	:param speeddials: speeddials
	:param busyLampFields: busyLampFields
	:param primaryPhoneName: primaryPhoneName
	:param ringSettingIdleBlfAudibleAlert: ringSettingIdleBlfAudibleAlert
	:param ringSettingBusyBlfAudibleAlert: ringSettingBusyBlfAudibleAlert
	:param blfDirectedCallParks: blfDirectedCallParks
	:param addOnModules: addOnModules
	:param userLocale: userLocale
	:param networkLocale: networkLocale
	:param idleTimeout: idleTimeout
	:param authenticationUrl: authenticationUrl
	:param directoryUrl: directoryUrl
	:param idleUrl: idleUrl
	:param informationUrl: informationUrl
	:param messagesUrl: messagesUrl
	:param proxyServerUrl: proxyServerUrl
	:param servicesUrl: servicesUrl
	:param services: services
	:param softkeyTemplateName: softkeyTemplateName
	:param defaultProfileName: defaultProfileName
	:param enableExtensionMobility: enableExtensionMobility
	:param singleButtonBarge: singleButtonBarge
	:param joinAcrossLines: joinAcrossLines
	:param builtInBridgeStatus: builtInBridgeStatus
	:param callInfoPrivacyStatus: callInfoPrivacyStatus
	:param hlogStatus: hlogStatus
	:param ownerUserName: ownerUserName
	:param ignorePresentationIndicators: ignorePresentationIndicators
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param subscribeCallingSearchSpaceName: subscribeCallingSearchSpaceName
	:param rerouteCallingSearchSpaceName: rerouteCallingSearchSpaceName
	:param allowCtiControlFlag: allowCtiControlFlag
	:param presenceGroupName: presenceGroupName
	:param unattendedPort: unattendedPort
	:param requireDtmfReception: requireDtmfReception
	:param rfc2833Disabled: rfc2833Disabled
	:param certificateOperation: certificateOperation
	:param authenticationMode: authenticationMode
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param authenticationString: authenticationString
	:param upgradeFinishTime: upgradeFinishTime
	:param deviceMobilityMode: deviceMobilityMode
	:param remoteDevice: remoteDevice
	:param dndOption: dndOption
	:param dndRingSetting: dndRingSetting
	:param dndStatus: dndStatus
	:param isActive: isActive
	:param isDualMode: isDualMode
	:param mobilityUserIdName: mobilityUserIdName
	:param phoneSuite: phoneSuite
	:param phoneServiceDisplay: phoneServiceDisplay
	:param isProtected: isProtected
	:param mtpRequired: mtpRequired
	:param mtpPreferedCodec: mtpPreferedCodec
	:param dialRulesName: dialRulesName
	:param sshUserId: sshUserId
	:param sshPwd: sshPwd
	:param digestUser: digestUser
	:param outboundCallRollover: outboundCallRollover
	:param hotlineDevice: hotlineDevice
	:param secureInformationUrl: secureInformationUrl
	:param secureDirectoryUrl: secureDirectoryUrl
	:param secureMessageUrl: secureMessageUrl
	:param secureServicesUrl: secureServicesUrl
	:param secureAuthenticationUrl: secureAuthenticationUrl
	:param secureIdleUrl: secureIdleUrl
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVoiceMessage: alwaysUsePrimeLineForVoiceMessage
	:param featureControlPolicy: featureControlPolicy
	:param deviceTrustMode: deviceTrustMode
	:param earlyOfferSupportForVoiceCall: earlyOfferSupportForVoiceCall
	:param requireThirdPartyRegistration: requireThirdPartyRegistration
	:param blockIncomingCallsWhenRoaming: blockIncomingCallsWhenRoaming
	:param homeNetworkId: homeNetworkId
	:param AllowPresentationSharingUsingBfcp: AllowPresentationSharingUsingBfcp
	:param confidentialAccess: confidentialAccess
	:param requireOffPremiseLocation: requireOffPremiseLocation
	:param allowiXApplicableMedia: allowiXApplicableMedia
	:param cgpnIngressDN: cgpnIngressDN
	:param useDevicePoolCgpnIngressDN: useDevicePoolCgpnIngressDN
	:param msisdn: msisdn
	:param enableCallRoutingToRdWhenNoneIsActive: enableCallRoutingToRdWhenNoneIsActive
	:param wifiHotspotProfile: wifiHotspotProfile
	:param wirelessLanProfileGroup: wirelessLanProfileGroup
	:param elinGroup: elinGroup
	:param enableActivationID: enableActivationID
	:param mraServiceDomain: mraServiceDomain
	:param allowMraMode: allowMraMode
	:param activationCodeExpiry: activationCodeExpiry
	:param phoneName: phoneName
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param commonPhoneConfigName: commonPhoneConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param securityProfileName: securityProfileName
	:param sipProfileName: sipProfileName
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param geoLocationName: geoLocationName
	:param geoLocationFilterName: geoLocationFilterName
	:param lines: lines
	:param phoneTemplateName: phoneTemplateName
	:param primaryPhoneName: primaryPhoneName
	:param ringSettingIdleBlfAudibleAlert: ringSettingIdleBlfAudibleAlert
	:param ringSettingBusyBlfAudibleAlert: ringSettingBusyBlfAudibleAlert
	:param blfDirectedCallParks: blfDirectedCallParks
	:param addOnModules: addOnModules
	:param userLocale: userLocale
	:param networkLocale: networkLocale
	:param services: services
	:param softkeyTemplateName: softkeyTemplateName
	:param defaultProfileName: defaultProfileName
	:param singleButtonBarge: singleButtonBarge
	:param joinAcrossLines: joinAcrossLines
	:param builtInBridgeStatus: builtInBridgeStatus
	:param callInfoPrivacyStatus: callInfoPrivacyStatus
	:param ownerUserName: ownerUserName
	:param packetCaptureMode: packetCaptureMode
	:param subscribeCallingSearchSpaceName: subscribeCallingSearchSpaceName
	:param rerouteCallingSearchSpaceName: rerouteCallingSearchSpaceName
	:param presenceGroupName: presenceGroupName
	:param certificateOperation: certificateOperation
	:param authenticationMode: authenticationMode
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param deviceMobilityMode: deviceMobilityMode
	:param dndOption: dndOption
	:param dndRingSetting: dndRingSetting
	:param mobilityUserIdName: mobilityUserIdName
	:param phoneSuite: phoneSuite
	:param phoneServiceDisplay: phoneServiceDisplay
	:param mtpPreferedCodec: mtpPreferedCodec
	:param dialRulesName: dialRulesName
	:param outboundCallRollover: outboundCallRollover
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVoiceMessage: alwaysUsePrimeLineForVoiceMessage
	:param featureControlPolicy: featureControlPolicy
	:param deviceTrustMode: deviceTrustMode
	:param confidentialAccess: confidentialAccess
	:param cgpnIngressDN: cgpnIngressDN
	:param wifiHotspotProfile: wifiHotspotProfile
	:param wirelessLanProfileGroup: wirelessLanProfileGroup
	:param elinGroup: elinGroup
	:param mraServiceDomain: mraServiceDomain
	:param dirn: dirn
	:param ringSetting: ringSetting
	:param consecutiveRingSetting: consecutiveRingSetting
	:param ringSettingIdlePickupAlert: ringSettingIdlePickupAlert
	:param ringSettingActivePickupAlert: ringSettingActivePickupAlert
	:param mwlPolicy: mwlPolicy
	:param recordingProfileName: recordingProfileName
	:param monitoringCssName: monitoringCssName
	:param recordingFlag: recordingFlag
	:param audibleMwi: audibleMwi
	:param partitionUsage: partitionUsage
	:param recordingMediaSource: recordingMediaSource
	:param index: index
	:param label: label
	:param display: display
	:param dirn: dirn
	:param ringSetting: ringSetting
	:param consecutiveRingSetting: consecutiveRingSetting
	:param ringSettingIdlePickupAlert: ringSettingIdlePickupAlert
	:param ringSettingActivePickupAlert: ringSettingActivePickupAlert
	:param displayAscii: displayAscii
	:param e164Mask: e164Mask
	:param mwlPolicy: mwlPolicy
	:param maxNumCalls: maxNumCalls
	:param busyTrigger: busyTrigger
	:param callInfoDisplay: callInfoDisplay
	:param recordingProfileName: recordingProfileName
	:param monitoringCssName: monitoringCssName
	:param recordingFlag: recordingFlag
	:param audibleMwi: audibleMwi
	:param speedDial: speedDial
	:param partitionUsage: partitionUsage
	:param associatedEndusers: associatedEndusers
	:param missedCallLogging: missedCallLogging
	:param recordingMediaSource: recordingMediaSource
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addPhone(**args)
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
            print(f"AXL error addPhone: ", str(err), file=sys.stderr)
            return False
        

    def H323Gateway(self, **args):
        """
        H323Gateway parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param loadInformation: loadInformation
	:param tunneledProtocol: tunneledProtocol
	:param asn1RoseOidEncoding: asn1RoseOidEncoding
	:param qsigVariant: qsigVariant
	:param vendorConfig: vendorConfig
	:param pathReplacementSupport: pathReplacementSupport
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param geoLocationFilterName: geoLocationFilterName
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param srtpAllowed: srtpAllowed
	:param waitForFarEndH245TerminalSet: waitForFarEndH245TerminalSet
	:param mtpRequired: mtpRequired
	:param callerIdDn: callerIdDn
	:param callingPartySelection: callingPartySelection
	:param callingLineIdPresentation: callingLineIdPresentation
	:param enableInboundFaststart: enableInboundFaststart
	:param enableOutboundFaststart: enableOutboundFaststart
	:param codecForOutboundFaststart: codecForOutboundFaststart
	:param transmitUtf8: transmitUtf8
	:param signalingPort: signalingPort
	:param allowH235PassThrough: allowH235PassThrough
	:param sigDigits: sigDigits
	:param prefixDn: prefixDn
	:param calledPartyIeNumberType: calledPartyIeNumberType
	:param callingPartyIeNumberType: callingPartyIeNumberType
	:param calledNumberingPlan: calledNumberingPlan
	:param callingNumberingPlan: callingNumberingPlan
	:param callingPartyNationalPrefix: callingPartyNationalPrefix
	:param callingPartyInternationalPrefix: callingPartyInternationalPrefix
	:param callingPartyUnknownPrefix: callingPartyUnknownPrefix
	:param callingPartySubscriberPrefix: callingPartySubscriberPrefix
	:param callingPartyNationalStripDigits: callingPartyNationalStripDigits
	:param callingPartyInternationalStripDigits: callingPartyInternationalStripDigits
	:param callingPartyUnknownStripDigits: callingPartyUnknownStripDigits
	:param callingPartySubscriberStripDigits: callingPartySubscriberStripDigits
	:param callingPartyNationalTransformationCssName: callingPartyNationalTransformationCssName
	:param callingPartyInternationalTransformationCssName: callingPartyInternationalTransformationCssName
	:param callingPartyUnknownTransformationCssName: callingPartyUnknownTransformationCssName
	:param callingPartySubscriberTransformationCssName: callingPartySubscriberTransformationCssName
	:param calledPartyNationalPrefix: calledPartyNationalPrefix
	:param calledPartyInternationalPrefix: calledPartyInternationalPrefix
	:param calledPartyUnknownPrefix: calledPartyUnknownPrefix
	:param calledPartySubscriberPrefix: calledPartySubscriberPrefix
	:param calledPartyNationalStripDigits: calledPartyNationalStripDigits
	:param calledPartyInternationalStripDigits: calledPartyInternationalStripDigits
	:param calledPartyUnknownStripDigits: calledPartyUnknownStripDigits
	:param calledPartySubscriberStripDigits: calledPartySubscriberStripDigits
	:param calledPartyNationalTransformationCssName: calledPartyNationalTransformationCssName
	:param calledPartyInternationalTransformationCssName: calledPartyInternationalTransformationCssName
	:param calledPartyUnknownTransformationCssName: calledPartyUnknownTransformationCssName
	:param calledPartySubscriberTransformationCssName: calledPartySubscriberTransformationCssName
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:param displayIeDelivery: displayIeDelivery
	:param redirectOutboundNumberIe: redirectOutboundNumberIe
	:param redirectInboundNumberIe: redirectInboundNumberIe
	:param useDevicePoolCgpnTransformCssNatl: useDevicePoolCgpnTransformCssNatl
	:param useDevicePoolCgpnTransformCssIntl: useDevicePoolCgpnTransformCssIntl
	:param useDevicePoolCgpnTransformCssUnkn: useDevicePoolCgpnTransformCssUnkn
	:param useDevicePoolCgpnTransformCssSubs: useDevicePoolCgpnTransformCssSubs
	:param useDevicePoolCalledCssNatl: useDevicePoolCalledCssNatl
	:param useDevicePoolCalledCssIntl: useDevicePoolCalledCssIntl
	:param useDevicePoolCalledCssUnkn: useDevicePoolCalledCssUnkn
	:param useDevicePoolCalledCssSubs: useDevicePoolCalledCssSubs
	:param useDevicePoolCntdPnTransformationCss: useDevicePoolCntdPnTransformationCss
	:param cntdPnTransformationCssName: cntdPnTransformationCssName
	:param confidentialAccess: confidentialAccess
	:param redirectingPartyTransformationCSS: redirectingPartyTransformationCSS
	:param connectCallBeforePlayingAnnouncement: connectCallBeforePlayingAnnouncement
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addH323Gateway(**args)
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
            print(f"AXL error addH323Gateway: ", str(err), file=sys.stderr)
            return False
        

    def DeviceProfile(self, **args):
        """
        DeviceProfile parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param vendorConfig: vendorConfig
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param lines: lines
	:param phoneTemplateName: phoneTemplateName
	:param speeddials: speeddials
	:param busyLampFields: busyLampFields
	:param blfDirectedCallParks: blfDirectedCallParks
	:param addOnModules: addOnModules
	:param userLocale: userLocale
	:param singleButtonBarge: singleButtonBarge
	:param joinAcrossLines: joinAcrossLines
	:param loginUserId: loginUserId
	:param ignorePresentationIndicators: ignorePresentationIndicators
	:param dndOption: dndOption
	:param dndRingSetting: dndRingSetting
	:param dndStatus: dndStatus
	:param emccCallingSearchSpace: emccCallingSearchSpace
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVoiceMessage: alwaysUsePrimeLineForVoiceMessage
	:param softkeyTemplateName: softkeyTemplateName
	:param callInfoPrivacyStatus: callInfoPrivacyStatus
	:param services: services
	:param featureControlPolicy: featureControlPolicy
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param lines: lines
	:param phoneTemplateName: phoneTemplateName
	:param blfDirectedCallParks: blfDirectedCallParks
	:param addOnModules: addOnModules
	:param userLocale: userLocale
	:param singleButtonBarge: singleButtonBarge
	:param joinAcrossLines: joinAcrossLines
	:param loginUserId: loginUserId
	:param dndOption: dndOption
	:param dndRingSetting: dndRingSetting
	:param emccCallingSearchSpace: emccCallingSearchSpace
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVoiceMessage: alwaysUsePrimeLineForVoiceMessage
	:param softkeyTemplateName: softkeyTemplateName
	:param callInfoPrivacyStatus: callInfoPrivacyStatus
	:param services: services
	:param featureControlPolicy: featureControlPolicy
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDeviceProfile(**args)
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
            print(f"AXL error addDeviceProfile: ", str(err), file=sys.stderr)
            return False
        

    def RemoteDestination(self, **args):
        """
        RemoteDestination parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param lines: lines
	:param callInfoPrivacyStatus: callInfoPrivacyStatus
	:param userId: userId
	:param ignorePresentationIndicators: ignorePresentationIndicators
	:param rerouteCallingSearchSpaceName: rerouteCallingSearchSpaceName
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param userLocale: userLocale
	:param networkLocale: networkLocale
	:param primaryPhoneName: primaryPhoneName
	:param dndOption: dndOption
	:param dndStatus: dndStatus
	:param mobileSmartClientProfileName: mobileSmartClientProfileName
	:param name: name
	:param destination: destination
	:param answerTooSoonTimer: answerTooSoonTimer
	:param answerTooLateTimer: answerTooLateTimer
	:param delayBeforeRingingCell: delayBeforeRingingCell
	:param ownerUserId: ownerUserId
	:param enableUnifiedMobility: enableUnifiedMobility
	:param remoteDestinationProfileName: remoteDestinationProfileName
	:param enableExtendAndConnect: enableExtendAndConnect
	:param ctiRemoteDeviceName: ctiRemoteDeviceName
	:param dualModeDeviceName: dualModeDeviceName
	:param isMobilePhone: isMobilePhone
	:param enableMobileConnect: enableMobileConnect
	:param lineAssociations: lineAssociations
	:param timeZone: timeZone
	:param todAccessName: todAccessName
	:param mobileSmartClientName: mobileSmartClientName
	:param mobilityProfileName: mobilityProfileName
	:param singleNumberReachVoicemail: singleNumberReachVoicemail
	:param dialViaOfficeReverseVoicemail: dialViaOfficeReverseVoicemail
	:param ringSchedule: ringSchedule
	:param accessListName: accessListName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRemoteDestination(**args)
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
            print(f"AXL error addRemoteDestination: ", str(err), file=sys.stderr)
            return False
        

    def Vg224(self, **args):
        """
        Vg224 parameters
        :param domainName: domainName
	:param description: description
	:param product: product
	:param protocol: protocol
	:param callManagerGroupName: callManagerGroupName
	:param units: units
	:param vendorConfig: vendorConfig
	:param versionStamp: versionStamp
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addVg224(**args)
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
            print(f"AXL error addVg224: ", str(err), file=sys.stderr)
            return False
        

    def Gateway(self, **args):
        """
        Gateway parameters
        :param domainName: domainName
	:param description: description
	:param product: product
	:param protocol: protocol
	:param callManagerGroupName: callManagerGroupName
	:param units: units
	:param vendorConfig: vendorConfig
	:param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:param unit: unit
	:param subunits: subunits
	:param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:param index: index
	:param name: name
	:param description: description
	:param product: product
	:param model: model
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocale: networkLocale
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param vendorConfig: vendorConfig
	:param mlppDomainId: mlppDomainId
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param geoLocationFilterName: geoLocationFilterName
	:param port: port
	:param trunkSelectionOrder: trunkSelectionOrder
	:param transmitUtf8: transmitUtf8
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param callingPartyNumberPrefix: callingPartyNumberPrefix
	:param callingPartyStripDigits: callingPartyStripDigits
	:param callingPartyUnknownTransformationCssName: callingPartyUnknownTransformationCssName
	:param useDevicePoolCgpnTransformCssUnknown: useDevicePoolCgpnTransformCssUnknown
	:param hotlineDevice: hotlineDevice
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:param imeE164DirectoryNumber: imeE164DirectoryNumber
	:param confidentialAccess: confidentialAccess
	:param elinGroup: elinGroup
	:param index: index
	:param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param networkLocale: networkLocale
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param mlppPreemption: mlppPreemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param redirectInboundNumberIe: redirectInboundNumberIe
	:param calledPlan: calledPlan
	:param calledPri: calledPri
	:param callerIdDn: callerIdDn
	:param callingPartySelection: callingPartySelection
	:param callingPlan: callingPlan
	:param callingPri: callingPri
	:param chanIE: chanIE
	:param clockReference: clockReference
	:param dChannelEnable: dChannelEnable
	:param channelSelectionOrder: channelSelectionOrder
	:param displayIe: displayIe
	:param pcmType: pcmType
	:param csuParam: csuParam
	:param firstDelay: firstDelay
	:param interfaceIdPresent: interfaceIdPresent
	:param interfaceId: interfaceId
	:param intraDelay: intraDelay
	:param mcdnEnable: mcdnEnable
	:param redirectOutboundNumberIe: redirectOutboundNumberIe
	:param numDigitsToStrip: numDigitsToStrip
	:param passingPrecedenceLevelThrough: passingPrecedenceLevelThrough
	:param prefix: prefix
	:param callingLinePresentationBit: callingLinePresentationBit
	:param connectedLineIdPresentation: connectedLineIdPresentation
	:param priProtocol: priProtocol
	:param securityAccessLevel: securityAccessLevel
	:param sendCallingNameInFacilityIe: sendCallingNameInFacilityIe
	:param sendExLeadingCharInDispIe: sendExLeadingCharInDispIe
	:param sendRestart: sendRestart
	:param setupNonIsdnPi: setupNonIsdnPi
	:param sigDigits: sigDigits
	:param span: span
	:param statusPoll: statusPoll
	:param smdiBasePort: smdiBasePort
	:param GClearEnable: GClearEnable
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param transmitUtf8: transmitUtf8
	:param v150: v150
	:param asn1RoseOidEncoding: asn1RoseOidEncoding
	:param qsigVariant: qsigVariant
	:param unattendedPort: unattendedPort
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param nationalPrefix: nationalPrefix
	:param internationalPrefix: internationalPrefix
	:param unknownPrefix: unknownPrefix
	:param subscriberPrefix: subscriberPrefix
	:param geoLocationFilterName: geoLocationFilterName
	:param routeClassSignalling: routeClassSignalling
	:param nationalStripDigits: nationalStripDigits
	:param internationalStripDigits: internationalStripDigits
	:param unknownStripDigits: unknownStripDigits
	:param subscriberStripDigits: subscriberStripDigits
	:param nationalTransformationCssName: nationalTransformationCssName
	:param internationalTransformationCssName: internationalTransformationCssName
	:param unknownTransformationCssName: unknownTransformationCssName
	:param subscriberTransformationCssName: subscriberTransformationCssName
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:param useDevicePoolCgpnTransformCssNatl: useDevicePoolCgpnTransformCssNatl
	:param useDevicePoolCgpnTransformCssIntl: useDevicePoolCgpnTransformCssIntl
	:param useDevicePoolCgpnTransformCssUnkn: useDevicePoolCgpnTransformCssUnkn
	:param useDevicePoolCgpnTransformCssSubs: useDevicePoolCgpnTransformCssSubs
	:param calledPartyNationalPrefix: calledPartyNationalPrefix
	:param calledPartyInternationalPrefix: calledPartyInternationalPrefix
	:param calledPartyUnknownPrefix: calledPartyUnknownPrefix
	:param calledPartySubscriberPrefix: calledPartySubscriberPrefix
	:param calledPartyNationalStripDigits: calledPartyNationalStripDigits
	:param calledPartyInternationalStripDigits: calledPartyInternationalStripDigits
	:param calledPartyUnknownStripDigits: calledPartyUnknownStripDigits
	:param calledPartySubscriberStripDigits: calledPartySubscriberStripDigits
	:param calledPartyNationalTransformationCssName: calledPartyNationalTransformationCssName
	:param calledPartyInternationalTransformationCssName: calledPartyInternationalTransformationCssName
	:param calledPartyUnknownTransformationCssName: calledPartyUnknownTransformationCssName
	:param calledPartySubscriberTransformationCssName: calledPartySubscriberTransformationCssName
	:param useDevicePoolCalledCssNatl: useDevicePoolCalledCssNatl
	:param useDevicePoolCalledCssIntl: useDevicePoolCalledCssIntl
	:param useDevicePoolCalledCssUnkn: useDevicePoolCalledCssUnkn
	:param useDevicePoolCalledCssSubs: useDevicePoolCalledCssSubs
	:param useDevicePoolCntdPartyTransformationCss: useDevicePoolCntdPartyTransformationCss
	:param cntdPartyTransformationCssName: cntdPartyTransformationCssName
	:param confidentialAccess: confidentialAccess
	:param connectCallBeforePlayingAnnouncement: connectCallBeforePlayingAnnouncement
	:param index: index
	:param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param networkLocale: networkLocale
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param vendorConfig: vendorConfig
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param redirectInboundNumberIe: redirectInboundNumberIe
	:param briProtocol: briProtocol
	:param calledPlan: calledPlan
	:param calledPri: calledPri
	:param callerIdDn: callerIdDn
	:param callingPartySelection: callingPartySelection
	:param callingPlan: callingPlan
	:param callingPri: callingPri
	:param clockReference: clockReference
	:param csuParam: csuParam
	:param dChannelEnable: dChannelEnable
	:param channelSelectionOrder: channelSelectionOrder
	:param pcmType: pcmType
	:param firstDelay: firstDelay
	:param intraDelay: intraDelay
	:param redirectOutboundNumberIe: redirectOutboundNumberIe
	:param numDigitsToStrip: numDigitsToStrip
	:param prefix: prefix
	:param presentationBit: presentationBit
	:param sendRestart: sendRestart
	:param setupNonIsdnPi: setupNonIsdnPi
	:param sigDigits: sigDigits
	:param statusPoll: statusPoll
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param geoLocationFilterName: geoLocationFilterName
	:param nationalPrefix: nationalPrefix
	:param internationalPrefix: internationalPrefix
	:param unknownPrefix: unknownPrefix
	:param subscriberPrefix: subscriberPrefix
	:param nationalStripDigits: nationalStripDigits
	:param internationalStripDigits: internationalStripDigits
	:param unknownStripDigits: unknownStripDigits
	:param subscriberStripDigits: subscriberStripDigits
	:param nationalTransformationCssName: nationalTransformationCssName
	:param internationalTransformationCssName: internationalTransformationCssName
	:param unknownTransformationCssName: unknownTransformationCssName
	:param subscriberTransformationCssName: subscriberTransformationCssName
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:param useDevicePoolCgpnTransformCssNatl: useDevicePoolCgpnTransformCssNatl
	:param useDevicePoolCgpnTransformCssIntl: useDevicePoolCgpnTransformCssIntl
	:param useDevicePoolCgpnTransformCssUnkn: useDevicePoolCgpnTransformCssUnkn
	:param useDevicePoolCgpnTransformCssSubs: useDevicePoolCgpnTransformCssSubs
	:param unattendedPort: unattendedPort
	:param GClearEnable: GClearEnable
	:param enableDatalinkOnFirstCall: enableDatalinkOnFirstCall
	:param calledPartyNationalPrefix: calledPartyNationalPrefix
	:param calledPartyInternationalPrefix: calledPartyInternationalPrefix
	:param calledPartyUnknownPrefix: calledPartyUnknownPrefix
	:param calledPartySubscriberPrefix: calledPartySubscriberPrefix
	:param calledPartyNationalStripDigits: calledPartyNationalStripDigits
	:param calledPartyInternationalStripDigits: calledPartyInternationalStripDigits
	:param calledPartyUnknownStripDigits: calledPartyUnknownStripDigits
	:param calledPartySubscriberStripDigits: calledPartySubscriberStripDigits
	:param calledPartyNationalTransformationCssName: calledPartyNationalTransformationCssName
	:param calledPartyInternationalTransformationCssName: calledPartyInternationalTransformationCssName
	:param calledPartyUnknownTransformationCssName: calledPartyUnknownTransformationCssName
	:param calledPartySubscriberTransformationCssName: calledPartySubscriberTransformationCssName
	:param useDevicePoolCalledCssNatl: useDevicePoolCalledCssNatl
	:param useDevicePoolCalledCssIntl: useDevicePoolCalledCssIntl
	:param useDevicePoolCalledCssUnkn: useDevicePoolCalledCssUnkn
	:param useDevicePoolCalledCssSubs: useDevicePoolCalledCssSubs
	:param connectCallBeforePlayingAnnouncement: connectCallBeforePlayingAnnouncement
	:param index: index
	:param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param sendGeoLocation: sendGeoLocation
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param v150: v150
	:param geoLocationFilterName: geoLocationFilterName
	:param ports: ports
	:param trunkSelectionOrder: trunkSelectionOrder
	:param clockReference: clockReference
	:param csuParam: csuParam
	:param digitSending: digitSending
	:param pcmType: pcmType
	:param fdlChannel: fdlChannel
	:param yellowAlarm: yellowAlarm
	:param zeroSupression: zeroSupression
	:param smdiBasePort: smdiBasePort
	:param handleDtmfPrecedenceSignals: handleDtmfPrecedenceSignals
	:param encodeOutboundVoiceRouteClass: encodeOutboundVoiceRouteClass
	:param routeClassSignalling: routeClassSignalling
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:param confidentialAccess: confidentialAccess
	:param connectCallBeforePlayingAnnouncement: connectCallBeforePlayingAnnouncement
	:param calledPartyUnknownPrefix: calledPartyUnknownPrefix
	:param calledPartyUnknownStripDigits: calledPartyUnknownStripDigits
	:param calledPartyUnknownTransformationCssName: calledPartyUnknownTransformationCssName
	:param useDevicePoolCalledCssUnkn: useDevicePoolCalledCssUnkn
	:param index: index
	:param name: name
	:param description: description
	:param product: product
	:param model: model
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocale: networkLocale
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param vendorConfig: vendorConfig
	:param mlppDomainId: mlppDomainId
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param geoLocationFilterName: geoLocationFilterName
	:param transmitUtf8: transmitUtf8
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param callingPartyNumberPrefix: callingPartyNumberPrefix
	:param callingPartyStripDigits: callingPartyStripDigits
	:param callingPartyUnknownTransformationCssName: callingPartyUnknownTransformationCssName
	:param useDevicePoolCgpnTransformCssUnknown: useDevicePoolCgpnTransformCssUnknown
	:param hotlineDevice: hotlineDevice
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:param phoneTemplateName: phoneTemplateName
	:param securityProfileName: securityProfileName
	:param userLocale: userLocale
	:param deviceMobilityMode: deviceMobilityMode
	:param ownerUserId: ownerUserId
	:param commonPhoneConfigName: commonPhoneConfigName
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVM: alwaysUsePrimeLineForVM
	:param allowCtiControlFlag: allowCtiControlFlag
	:param remoteDevice: remoteDevice
	:param subscribeCallingSearchSpaceName: subscribeCallingSearchSpaceName
	:param unattendedPort: unattendedPort
	:param presenceGroupName: presenceGroupName
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param hlogStatus: hlogStatus
	:param ignorePresentationIndicators: ignorePresentationIndicators
	:param lines: lines
	:param confidentialAccess: confidentialAccess
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGateway(**args)
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
            print(f"AXL error addGateway: ", str(err), file=sys.stderr)
            return False
        

    def GatewayEndpointAnalogAccess(self, **args):
        """
        GatewayEndpointAnalogAccess parameters
        :param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGatewayEndpointAnalogAccess(**args)
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
            print(f"AXL error addGatewayEndpointAnalogAccess: ", str(err), file=sys.stderr)
            return False
        

    def GatewayEndpointDigitalAccessPri(self, **args):
        """
        GatewayEndpointDigitalAccessPri parameters
        :param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGatewayEndpointDigitalAccessPri(**args)
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
            print(f"AXL error addGatewayEndpointDigitalAccessPri: ", str(err), file=sys.stderr)
            return False
        

    def GatewayEndpointDigitalAccessBri(self, **args):
        """
        GatewayEndpointDigitalAccessBri parameters
        :param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGatewayEndpointDigitalAccessBri(**args)
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
            print(f"AXL error addGatewayEndpointDigitalAccessBri: ", str(err), file=sys.stderr)
            return False
        

    def GatewayEndpointDigitalAccessT1(self, **args):
        """
        GatewayEndpointDigitalAccessT1 parameters
        :param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGatewayEndpointDigitalAccessT1(**args)
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
            print(f"AXL error addGatewayEndpointDigitalAccessT1: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst600024PortFXSGateway(self, **args):
        """
        CiscoCatalyst600024PortFXSGateway parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocale: networkLocale
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param ports: ports
	:param portSelectionOrder: portSelectionOrder
	:param transmitUtf8: transmitUtf8
	:param geoLocationFilterName: geoLocationFilterName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCiscoCatalyst600024PortFXSGateway(**args)
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
            print(f"AXL error addCiscoCatalyst600024PortFXSGateway: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000E1VoIPGateway(self, **args):
        """
        CiscoCatalyst6000E1VoIPGateway parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param networkLocale: networkLocale
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param mlppDomainId: mlppDomainId
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param redirectInboundNumberIe: redirectInboundNumberIe
	:param calledPlan: calledPlan
	:param calledPri: calledPri
	:param callerIdDn: callerIdDn
	:param callingPartySelection: callingPartySelection
	:param callingPlan: callingPlan
	:param callingPri: callingPri
	:param chanIe: chanIe
	:param clockReference: clockReference
	:param dChannelEnable: dChannelEnable
	:param channelSelectionOrder: channelSelectionOrder
	:param displayIE: displayIE
	:param pcmType: pcmType
	:param csuParam: csuParam
	:param firstDelay: firstDelay
	:param interfaceIdPresent: interfaceIdPresent
	:param interfaceId: interfaceId
	:param intraDelay: intraDelay
	:param mcdnEnable: mcdnEnable
	:param redirectOutboundNumberIe: redirectOutboundNumberIe
	:param numDigitsToStrip: numDigitsToStrip
	:param passingPrecedenceLevelThrough: passingPrecedenceLevelThrough
	:param prefix: prefix
	:param callingLinePresentationBit: callingLinePresentationBit
	:param connectedLineIdPresentation: connectedLineIdPresentation
	:param priProtocol: priProtocol
	:param securityAccessLevel: securityAccessLevel
	:param sendCallingNameInFacilityIe: sendCallingNameInFacilityIe
	:param sendExLeadingCharInDispIe: sendExLeadingCharInDispIe
	:param sendRestart: sendRestart
	:param setupNonIsdnPi: setupNonIsdnPi
	:param sigDigits: sigDigits
	:param span: span
	:param statusPoll: statusPoll
	:param smdiBasePort: smdiBasePort
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param transmitUtf8: transmitUtf8
	:param v150: v150
	:param asn1RoseOidEncoding: asn1RoseOidEncoding
	:param QSIGVariant: QSIGVariant
	:param unattendedPort: unattendedPort
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param nationalPrefix: nationalPrefix
	:param internationalPrefix: internationalPrefix
	:param unknownPrefix: unknownPrefix
	:param subscriberPrefix: subscriberPrefix
	:param geoLocationFilterName: geoLocationFilterName
	:param nationalStripDigits: nationalStripDigits
	:param internationalStripDigits: internationalStripDigits
	:param unknownStripDigits: unknownStripDigits
	:param subscriberStripDigits: subscriberStripDigits
	:param nationalTransformationCssName: nationalTransformationCssName
	:param internationalTransformationCssName: internationalTransformationCssName
	:param unknownTransformationCssName: unknownTransformationCssName
	:param subscriberTransformationCssName: subscriberTransformationCssName
	:param useDevicePoolCgpnTransformCssNatl: useDevicePoolCgpnTransformCssNatl
	:param useDevicePoolCgpnTransformCssIntl: useDevicePoolCgpnTransformCssIntl
	:param useDevicePoolCgpnTransformCssUnkn: useDevicePoolCgpnTransformCssUnkn
	:param useDevicePoolCgpnTransformCssSubs: useDevicePoolCgpnTransformCssSubs
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCiscoCatalyst6000E1VoIPGateway(**args)
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
            print(f"AXL error addCiscoCatalyst6000E1VoIPGateway: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000T1VoIPGatewayPri(self, **args):
        """
        CiscoCatalyst6000T1VoIPGatewayPri parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param networkLocale: networkLocale
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param mlppPreemption: mlppPreemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param redirectInboundNumberIe: redirectInboundNumberIe
	:param calledPlan: calledPlan
	:param calledPri: calledPri
	:param callerIdDn: callerIdDn
	:param callingPartySelection: callingPartySelection
	:param callingPlan: callingPlan
	:param callingPri: callingPri
	:param chanIe: chanIe
	:param clockReference: clockReference
	:param dChannelEnable: dChannelEnable
	:param channelSelectionOrder: channelSelectionOrder
	:param displayIE: displayIE
	:param pcmType: pcmType
	:param csuParam: csuParam
	:param firstDelay: firstDelay
	:param interfaceIdPresent: interfaceIdPresent
	:param interfaceId: interfaceId
	:param intraDelay: intraDelay
	:param mcdnEnable: mcdnEnable
	:param redirectOutboundNumberIe: redirectOutboundNumberIe
	:param numDigitsToStrip: numDigitsToStrip
	:param passingPrecedenceLevelThrough: passingPrecedenceLevelThrough
	:param prefix: prefix
	:param callingLinePresentationBit: callingLinePresentationBit
	:param connectedLineIdPresentation: connectedLineIdPresentation
	:param priProtocol: priProtocol
	:param securityAccessLevel: securityAccessLevel
	:param sendCallingNameInFacilityIe: sendCallingNameInFacilityIe
	:param sendExLeadingCharInDispIe: sendExLeadingCharInDispIe
	:param sendRestart: sendRestart
	:param setupNonIsdnPi: setupNonIsdnPi
	:param sigDigits: sigDigits
	:param span: span
	:param statusPoll: statusPoll
	:param smdiBasePort: smdiBasePort
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param transmitUtf8: transmitUtf8
	:param v150: v150
	:param asn1RoseOidEncoding: asn1RoseOidEncoding
	:param QSIGVariant: QSIGVariant
	:param unattendedPort: unattendedPort
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param nationalPrefix: nationalPrefix
	:param internationalPrefix: internationalPrefix
	:param unknownPrefix: unknownPrefix
	:param subscriberPrefix: subscriberPrefix
	:param geoLocationFilterName: geoLocationFilterName
	:param nationalStripDigits: nationalStripDigits
	:param internationalStripDigits: internationalStripDigits
	:param unknownStripDigits: unknownStripDigits
	:param subscriberStripDigits: subscriberStripDigits
	:param nationalTransformationCssName: nationalTransformationCssName
	:param internationalTransformationCssName: internationalTransformationCssName
	:param unknownTransformationCssName: unknownTransformationCssName
	:param subscriberTransformationCssName: subscriberTransformationCssName
	:param useDevicePoolCgpnTransformCssNatl: useDevicePoolCgpnTransformCssNatl
	:param useDevicePoolCgpnTransformCssIntl: useDevicePoolCgpnTransformCssIntl
	:param useDevicePoolCgpnTransformCssUnkn: useDevicePoolCgpnTransformCssUnkn
	:param useDevicePoolCgpnTransformCssSubs: useDevicePoolCgpnTransformCssSubs
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCiscoCatalyst6000T1VoIPGatewayPri(**args)
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
            print(f"AXL error addCiscoCatalyst6000T1VoIPGatewayPri: ", str(err), file=sys.stderr)
            return False
        

    def CiscoCatalyst6000T1VoIPGatewayT1(self, **args):
        """
        CiscoCatalyst6000T1VoIPGatewayT1 parameters
        :param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param sendGeoLocation: sendGeoLocation
	:param ports: ports
	:param trunkSelectionOrder: trunkSelectionOrder
	:param clockReference: clockReference
	:param csuParam: csuParam
	:param digitSending: digitSending
	:param pcmType: pcmType
	:param fdlChannel: fdlChannel
	:param yellowAlarm: yellowAlarm
	:param zeroSupression: zeroSupression
	:param smdiBasePort: smdiBasePort
	:param handleDtmfPrecedenceSignals: handleDtmfPrecedenceSignals
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param geoLocationFilterName: geoLocationFilterName
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCiscoCatalyst6000T1VoIPGatewayT1(**args)
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
            print(f"AXL error addCiscoCatalyst6000T1VoIPGatewayT1: ", str(err), file=sys.stderr)
            return False
        

    def CallPickupGroup(self, **args):
        """
        CallPickupGroup parameters
        :param pattern: pattern
	:param description: description
	:param routePartitionName: routePartitionName
	:param members: members
	:param pickupNotification: pickupNotification
	:param pickupNotificationTimer: pickupNotificationTimer
	:param callInfoForPickupNotification: callInfoForPickupNotification
	:param name: name
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCallPickupGroup(**args)
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
            print(f"AXL error addCallPickupGroup: ", str(err), file=sys.stderr)
            return False
        

    def GeoLocationPolicy(self, **args):
        """
        GeoLocationPolicy parameters
        :param name: name
	:param country: country
	:param description: description
	:param nationalSubDivision: nationalSubDivision
	:param district: district
	:param communityName: communityName
	:param cityDivision: cityDivision
	:param neighbourhood: neighbourhood
	:param street: street
	:param leadingStreetDirection: leadingStreetDirection
	:param trailingStreetSuffix: trailingStreetSuffix
	:param streetSuffix: streetSuffix
	:param houseNumber: houseNumber
	:param houseNumberSuffix: houseNumberSuffix
	:param landmark: landmark
	:param location: location
	:param floor: floor
	:param occupantName: occupantName
	:param postalCode: postalCode
	:param relatedPolicies: relatedPolicies
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGeoLocationPolicy(**args)
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
            print(f"AXL error addGeoLocationPolicy: ", str(err), file=sys.stderr)
            return False
        

    def SipTrunk(self, **args):
        """
        SipTrunk parameters
        :param name: name
	:param description: description
	:param securityMode: securityMode
	:param incomingTransport: incomingTransport
	:param outgoingTransport: outgoingTransport
	:param digestAuthentication: digestAuthentication
	:param noncePolicyTime: noncePolicyTime
	:param x509SubjectName: x509SubjectName
	:param incomingPort: incomingPort
	:param applLevelAuthentication: applLevelAuthentication
	:param acceptPresenceSubscription: acceptPresenceSubscription
	:param acceptOutOfDialogRefer: acceptOutOfDialogRefer
	:param acceptUnsolicitedNotification: acceptUnsolicitedNotification
	:param allowReplaceHeader: allowReplaceHeader
	:param transmitSecurityStatus: transmitSecurityStatus
	:param sipV150OutboundSdpOfferFiltering: sipV150OutboundSdpOfferFiltering
	:param allowChargingHeader: allowChargingHeader
	:param name: name
	:param description: description
	:param product: product
	:param class: class
	:param protocol: protocol
	:param protocolSide: protocolSide
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param networkLocation: networkLocation
	:param locationName: locationName
	:param mediaResourceListName: mediaResourceListName
	:param networkHoldMohAudioSourceId: networkHoldMohAudioSourceId
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param automatedAlternateRoutingCssName: automatedAlternateRoutingCssName
	:param aarNeighborhoodName: aarNeighborhoodName
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param loadInformation: loadInformation
	:param traceFlag: traceFlag
	:param mlppDomainId: mlppDomainId
	:param mlppIndicationStatus: mlppIndicationStatus
	:param preemption: preemption
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param securityProfileName: securityProfileName
	:param sipProfileName: sipProfileName
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param useDevicePoolCgpnTransformCss: useDevicePoolCgpnTransformCss
	:param geoLocationName: geoLocationName
	:param geoLocationFilterName: geoLocationFilterName
	:param sendGeoLocation: sendGeoLocation
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param useDevicePoolCdpnTransformCss: useDevicePoolCdpnTransformCss
	:param unattendedPort: unattendedPort
	:param transmitUtf8: transmitUtf8
	:param subscribeCallingSearchSpaceName: subscribeCallingSearchSpaceName
	:param rerouteCallingSearchSpaceName: rerouteCallingSearchSpaceName
	:param referCallingSearchSpaceName: referCallingSearchSpaceName
	:param mtpRequired: mtpRequired
	:param presenceGroupName: presenceGroupName
	:param unknownPrefix: unknownPrefix
	:param destAddrIsSrv: destAddrIsSrv
	:param tkSipCodec: tkSipCodec
	:param sigDigits: sigDigits
	:param connectedNamePresentation: connectedNamePresentation
	:param connectedPartyIdPresentation: connectedPartyIdPresentation
	:param callingPartySelection: callingPartySelection
	:param callingname: callingname
	:param callingLineIdPresentation: callingLineIdPresentation
	:param prefixDn: prefixDn
	:param externalPresentationInfo: externalPresentationInfo
	:param acceptInboundRdnis: acceptInboundRdnis
	:param acceptOutboundRdnis: acceptOutboundRdnis
	:param srtpAllowed: srtpAllowed
	:param srtpFallbackAllowed: srtpFallbackAllowed
	:param isPaiEnabled: isPaiEnabled
	:param sipPrivacy: sipPrivacy
	:param isRpidEnabled: isRpidEnabled
	:param sipAssertedType: sipAssertedType
	:param trustReceivedIdentity: trustReceivedIdentity
	:param dtmfSignalingMethod: dtmfSignalingMethod
	:param routeClassSignalling: routeClassSignalling
	:param sipTrunkType: sipTrunkType
	:param pstnAccess: pstnAccess
	:param imeE164TransformationName: imeE164TransformationName
	:param useImePublicIpPort: useImePublicIpPort
	:param useDevicePoolCntdPnTransformationCss: useDevicePoolCntdPnTransformationCss
	:param cntdPnTransformationCssName: cntdPnTransformationCssName
	:param useDevicePoolCgpnTransformCssUnkn: useDevicePoolCgpnTransformCssUnkn
	:param rdnTransformationCssName: rdnTransformationCssName
	:param useDevicePoolRdnTransformCss: useDevicePoolRdnTransformCss
	:param useOrigCallingPartyPresOnDivert: useOrigCallingPartyPresOnDivert
	:param sipNormalizationScriptName: sipNormalizationScriptName
	:param runOnEveryNode: runOnEveryNode
	:param destinations: destinations
	:param unknownStripDigits: unknownStripDigits
	:param cgpnTransformationUnknownCssName: cgpnTransformationUnknownCssName
	:param tunneledProtocol: tunneledProtocol
	:param asn1RoseOidEncoding: asn1RoseOidEncoding
	:param qsigVariant: qsigVariant
	:param pathReplacementSupport: pathReplacementSupport
	:param enableQsigUtf8: enableQsigUtf8
	:param scriptParameters: scriptParameters
	:param scriptTraceEnabled: scriptTraceEnabled
	:param trunkTrafficSecure: trunkTrafficSecure
	:param callingAndCalledPartyInfoFormat: callingAndCalledPartyInfoFormat
	:param useCallerIdCallerNameinUriOutgoingRequest: useCallerIdCallerNameinUriOutgoingRequest
	:param service: service
	:param parameterLabel: parameterLabel
	:param originatingParameterValue: originatingParameterValue
	:param terminatingParameterValue: terminatingParameterValue
	:param outboundUriRoutingInstructions: outboundUriRoutingInstructions
	:param requestUriDomainName: requestUriDomainName
	:param enableCiscoRecordingQsigTunneling: enableCiscoRecordingQsigTunneling
	:param recordingInformation: recordingInformation
	:param calledPartyUnknownTransformationCssName: calledPartyUnknownTransformationCssName
	:param calledPartyUnknownPrefix: calledPartyUnknownPrefix
	:param calledPartyUnknownStripDigits: calledPartyUnknownStripDigits
	:param useDevicePoolCalledCssUnkn: useDevicePoolCalledCssUnkn
	:param confidentialAccess: confidentialAccess
	:param addressIpv4: addressIpv4
	:param addressIpv6: addressIpv6
	:param port: port
	:param sortOrder: sortOrder
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSipTrunk(**args)
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
            print(f"AXL error addSipTrunk: ", str(err), file=sys.stderr)
            return False
        

    def CalledPartyTransformationPattern(self, **args):
        """
        CalledPartyTransformationPattern parameters
        :param pattern: pattern
	:param description: description
	:param routePartitionName: routePartitionName
	:param calledPartyTransformationMask: calledPartyTransformationMask
	:param dialPlanName: dialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param routeFilterName: routeFilterName
	:param calledPartyPrefixDigits: calledPartyPrefixDigits
	:param calledPartyNumberingPlan: calledPartyNumberingPlan
	:param calledPartyNumberType: calledPartyNumberType
	:param mlppPreemptionDisabled: mlppPreemptionDisabled
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCalledPartyTransformationPattern(**args)
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
            print(f"AXL error addCalledPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
        

    def ExternalCallControlProfile(self, **args):
        """
        ExternalCallControlProfile parameters
        :param name: name
	:param primaryUri: primaryUri
	:param secondaryUri: secondaryUri
	:param enableLoadBalancing: enableLoadBalancing
	:param routingRequestTimer: routingRequestTimer
	:param diversionReroutingCssName: diversionReroutingCssName
	:param callTreatmentOnFailure: callTreatmentOnFailure
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addExternalCallControlProfile(**args)
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
            print(f"AXL error addExternalCallControlProfile: ", str(err), file=sys.stderr)
            return False
        

    def SafSecurityProfile(self, **args):
        """
        SafSecurityProfile parameters
        :param name: name
	:param description: description
	:param userid: userid
	:param password: password
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSafSecurityProfile(**args)
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
            print(f"AXL error addSafSecurityProfile: ", str(err), file=sys.stderr)
            return False
        

    def SafForwarder(self, **args):
        """
        SafForwarder parameters
        :param name: name
	:param description: description
	:param clientLabel: clientLabel
	:param safSecurityProfile: safSecurityProfile
	:param ipAddress: ipAddress
	:param port: port
	:param enableTcpKeepAlive: enableTcpKeepAlive
	:param safReconnectInterval: safReconnectInterval
	:param safNotificationsWindowSize: safNotificationsWindowSize
	:param associatedCucms: associatedCucms
	:param callManagerName: callManagerName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSafForwarder(**args)
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
            print(f"AXL error addSafForwarder: ", str(err), file=sys.stderr)
            return False
        

    def CcdHostedDN(self, **args):
        """
        CcdHostedDN parameters
        :param hostedPattern: hostedPattern
	:param description: description
	:param CcdHostedDnGroup: CcdHostedDnGroup
	:param pstnFailoverStripDigits: pstnFailoverStripDigits
	:param pstnFailoverPrependDigits: pstnFailoverPrependDigits
	:param usePstnFailover: usePstnFailover
	:param name: name
	:param description: description
	:param pstnFailoverStripDigits: pstnFailoverStripDigits
	:param pstnFailoverPrependDigits: pstnFailoverPrependDigits
	:param usePstnFailover: usePstnFailover
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCcdHostedDN(**args)
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
            print(f"AXL error addCcdHostedDN: ", str(err), file=sys.stderr)
            return False
        

    def CcdHostedDNGroup(self, **args):
        """
        CcdHostedDNGroup parameters
        :param name: name
	:param description: description
	:param pstnFailoverStripDigits: pstnFailoverStripDigits
	:param pstnFailoverPrependDigits: pstnFailoverPrependDigits
	:param usePstnFailover: usePstnFailover
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCcdHostedDNGroup(**args)
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
            print(f"AXL error addCcdHostedDNGroup: ", str(err), file=sys.stderr)
            return False
        

    def Ccd(self, **args):
        """
        Ccd parameters
        :param name: name
	:param description: description
	:param isActivated: isActivated
	:param routePartitionName: routePartitionName
	:param learnedPatternPrefix: learnedPatternPrefix
	:param pstnPrefix: pstnPrefix
	:param associatedTrunks: associatedTrunks
	:param trunkName: trunkName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCcd(**args)
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
            print(f"AXL error addCcd: ", str(err), file=sys.stderr)
            return False
        

    def RemoteCluster(self, **args):
        """
        RemoteCluster parameters
        :param clusterId: clusterId
	:param description: description
	:param fullyQualifiedName: fullyQualifiedName
	:param emcc: emcc
	:param pstnAccess: pstnAccess
	:param rsvpAgent: rsvpAgent
	:param tftp: tftp
	:param lbm: lbm
	:param uds: uds
	:param enabled: enabled
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addRemoteCluster(**args)
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
            print(f"AXL error addRemoteCluster: ", str(err), file=sys.stderr)
            return False
        

    def CcdAdvertisingService(self, **args):
        """
        CcdAdvertisingService parameters
        :param name: name
	:param description: description
	:param isActivated: isActivated
	:param hostDnGroup: hostDnGroup
	:param safSipTrunk: safSipTrunk
	:param safH323Trunk: safH323Trunk
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCcdAdvertisingService(**args)
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
            print(f"AXL error addCcdAdvertisingService: ", str(err), file=sys.stderr)
            return False
        

    def UnitsToGateway(self, **args):
        """
        UnitsToGateway parameters
        :param units: units
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addUnitsToGateway(**args)
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
            print(f"AXL error addUnitsToGateway: ", str(err), file=sys.stderr)
            return False
        

    def GatewaySubunits(self, **args):
        """
        GatewaySubunits parameters
        :param unit: unit
	:param subunits: subunits
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGatewaySubunits(**args)
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
            print(f"AXL error addGatewaySubunits: ", str(err), file=sys.stderr)
            return False
        

    def LdapDirectory(self, **args):
        """
        LdapDirectory parameters
        :param name: name
	:param ldapDn: ldapDn
	:param ldapPassword: ldapPassword
	:param userSearchBase: userSearchBase
	:param repeatable: repeatable
	:param intervalValue: intervalValue
	:param scheduleUnit: scheduleUnit
	:param nextExecTime: nextExecTime
	:param servers: servers
	:param middleName: middleName
	:param phoneNumber: phoneNumber
	:param mailId: mailId
	:param ldapFilter: ldapFilter
	:param synchronize: synchronize
	:param ldapFilterForGroups: ldapFilterForGroups
	:param directoryUri: directoryUri
	:param accessControlGroupInfo: accessControlGroupInfo
	:param featureGroupTemplate: featureGroupTemplate
	:param applyMask: applyMask
	:param mask: mask
	:param applyPoolList: applyPoolList
	:param addDns: addDns
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLdapDirectory(**args)
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
            print(f"AXL error addLdapDirectory: ", str(err), file=sys.stderr)
            return False
        

    def SafCcdPurgeBlockLearnedRoutes(self, **args):
        """
        SafCcdPurgeBlockLearnedRoutes parameters
        :param learnedPattern: learnedPattern
	:param learnedPatternPrefix: learnedPatternPrefix
	:param callControlIdentity: callControlIdentity
	:param ipAddress: ipAddress
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSafCcdPurgeBlockLearnedRoutes(**args)
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
            print(f"AXL error addSafCcdPurgeBlockLearnedRoutes: ", str(err), file=sys.stderr)
            return False
        

    def VpnGateway(self, **args):
        """
        VpnGateway parameters
        :param name: name
	:param description: description
	:param url: url
	:param certificates: certificates
	:param issuerName: issuerName
	:param serialNumber: serialNumber
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addVpnGateway(**args)
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
            print(f"AXL error addVpnGateway: ", str(err), file=sys.stderr)
            return False
        

    def VpnGroup(self, **args):
        """
        VpnGroup parameters
        :param name: name
	:param description: description
	:param vpnGateways: vpnGateways
	:param vpnGatewayName: vpnGatewayName
	:param priority: priority
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addVpnGroup(**args)
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
            print(f"AXL error addVpnGroup: ", str(err), file=sys.stderr)
            return False
        

    def VpnProfile(self, **args):
        """
        VpnProfile parameters
        :param name: name
	:param description: description
	:param autoNetworkDetection: autoNetworkDetection
	:param mtu: mtu
	:param failToConnect: failToConnect
	:param clientAuthentication: clientAuthentication
	:param pwdPersistant: pwdPersistant
	:param enableHostIdCheck: enableHostIdCheck
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addVpnProfile(**args)
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
            print(f"AXL error addVpnProfile: ", str(err), file=sys.stderr)
            return False
        

    def ImeServer(self, **args):
        """
        ImeServer parameters
        :param name: name
	:param description: description
	:param ipAddress: ipAddress
	:param port: port
	:param deviceSecurityMode: deviceSecurityMode
	:param applicationUser: applicationUser
	:param reconnectInterval: reconnectInterval
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeServer(**args)
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
            print(f"AXL error addImeServer: ", str(err), file=sys.stderr)
            return False
        

    def ImeRouteFilterGroup(self, **args):
        """
        ImeRouteFilterGroup parameters
        :param name: name
	:param description: description
	:param groupTrustSetting: groupTrustSetting
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeRouteFilterGroup(**args)
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
            print(f"AXL error addImeRouteFilterGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeRouteFilterElement(self, **args):
        """
        ImeRouteFilterElement parameters
        :param name: name
	:param description: description
	:param elementType: elementType
	:param imeRouteFilterGroupName: imeRouteFilterGroupName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeRouteFilterElement(**args)
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
            print(f"AXL error addImeRouteFilterElement: ", str(err), file=sys.stderr)
            return False
        

    def ImeClient(self, **args):
        """
        ImeClient parameters
        :param name: name
	:param description: description
	:param domain: domain
	:param isActivated: isActivated
	:param sipTrunkName: sipTrunkName
	:param primaryImeServerName: primaryImeServerName
	:param secondaryImeServerName: secondaryImeServerName
	:param learnedRouteFilterGroupName: learnedRouteFilterGroupName
	:param exclusionNumberGroupName: exclusionNumberGroupName
	:param firewallName: firewallName
	:param members: members
	:param ccmExternalIpMaps: ccmExternalIpMaps
	:param enrolledPatternGroupName: enrolledPatternGroupName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeClient(**args)
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
            print(f"AXL error addImeClient: ", str(err), file=sys.stderr)
            return False
        

    def ImeEnrolledPattern(self, **args):
        """
        ImeEnrolledPattern parameters
        :param pattern: pattern
	:param description: description
	:param imeEnrolledPatternGroupName: imeEnrolledPatternGroupName
	:param name: name
	:param description: description
	:param fallbackProfileName: fallbackProfileName
	:param isPatternAllAlias: isPatternAllAlias
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeEnrolledPattern(**args)
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
            print(f"AXL error addImeEnrolledPattern: ", str(err), file=sys.stderr)
            return False
        

    def ImeEnrolledPatternGroup(self, **args):
        """
        ImeEnrolledPatternGroup parameters
        :param name: name
	:param description: description
	:param fallbackProfileName: fallbackProfileName
	:param isPatternAllAlias: isPatternAllAlias
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeEnrolledPatternGroup(**args)
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
            print(f"AXL error addImeEnrolledPatternGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeExclusionNumber(self, **args):
        """
        ImeExclusionNumber parameters
        :param pattern: pattern
	:param description: description
	:param imeExclusionNumberGroupName: imeExclusionNumberGroupName
	:param name: name
	:param description: description
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeExclusionNumber(**args)
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
            print(f"AXL error addImeExclusionNumber: ", str(err), file=sys.stderr)
            return False
        

    def ImeExclusionNumberGroup(self, **args):
        """
        ImeExclusionNumberGroup parameters
        :param name: name
	:param description: description
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeExclusionNumberGroup(**args)
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
            print(f"AXL error addImeExclusionNumberGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImeFirewall(self, **args):
        """
        ImeFirewall parameters
        :param name: name
	:param description: description
	:param ipAddress: ipAddress
	:param port: port
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeFirewall(**args)
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
            print(f"AXL error addImeFirewall: ", str(err), file=sys.stderr)
            return False
        

    def ImeE164Transformation(self, **args):
        """
        ImeE164Transformation parameters
        :param name: name
	:param description: description
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param isCgpnPreTransformation: isCgpnPreTransformation
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param isCdpnPreTransformation: isCdpnPreTransformation
	:param incomingCgpnTransformationProfileName: incomingCgpnTransformationProfileName
	:param incomingCdpnTransformationProfileName: incomingCdpnTransformationProfileName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImeE164Transformation(**args)
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
            print(f"AXL error addImeE164Transformation: ", str(err), file=sys.stderr)
            return False
        

    def TransformationProfile(self, **args):
        """
        TransformationProfile parameters
        :param name: name
	:param description: description
	:param nationalStripDigits: nationalStripDigits
	:param internationalStripDigits: internationalStripDigits
	:param unknownStripDigits: unknownStripDigits
	:param subscriberStripDigits: subscriberStripDigits
	:param nationalPrefix: nationalPrefix
	:param internationalPrefix: internationalPrefix
	:param unknownPrefix: unknownPrefix
	:param subscriberPrefix: subscriberPrefix
	:param nationalCssName: nationalCssName
	:param internationalCssName: internationalCssName
	:param unknownCssName: unknownCssName
	:param subscriberCssName: subscriberCssName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addTransformationProfile(**args)
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
            print(f"AXL error addTransformationProfile: ", str(err), file=sys.stderr)
            return False
        

    def FallbackProfile(self, **args):
        """
        FallbackProfile parameters
        :param name: name
	:param description: description
	:param advertisedFallbackDirectoryE164Number: advertisedFallbackDirectoryE164Number
	:param qosSensistivityLevel: qosSensistivityLevel
	:param callCss: callCss
	:param callAnswerTimer: callAnswerTimer
	:param directoryNumberPartition: directoryNumberPartition
	:param directoryNumber: directoryNumber
	:param numberOfDigitsForCallerIDPartialMatch: numberOfDigitsForCallerIDPartialMatch
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addFallbackProfile(**args)
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
            print(f"AXL error addFallbackProfile: ", str(err), file=sys.stderr)
            return False
        

    def LdapFilter(self, **args):
        """
        LdapFilter parameters
        :param name: name
	:param filter: filter
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLdapFilter(**args)
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
            print(f"AXL error addLdapFilter: ", str(err), file=sys.stderr)
            return False
        

    def AppServerInfo(self, **args):
        """
        AppServerInfo parameters
        :param appServerName: appServerName
	:param appServerContent: appServerContent
	:param content: content
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addAppServerInfo(**args)
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
            print(f"AXL error addAppServerInfo: ", str(err), file=sys.stderr)
            return False
        

    def FeatureControlPolicy(self, **args):
        """
        FeatureControlPolicy parameters
        :param name: name
	:param description: description
	:param features: features
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addFeatureControlPolicy(**args)
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
            print(f"AXL error addFeatureControlPolicy: ", str(err), file=sys.stderr)
            return False
        

    def MobilityProfile(self, **args):
        """
        MobilityProfile parameters
        :param name: name
	:param description: description
	:param mobileClientCallingOption: mobileClientCallingOption
	:param dvofServiceAccessNumber: dvofServiceAccessNumber
	:param dirn: dirn
	:param dvorCallerId: dvorCallerId
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMobilityProfile(**args)
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
            print(f"AXL error addMobilityProfile: ", str(err), file=sys.stderr)
            return False
        

    def EnterpriseFeatureAccessConfiguration(self, **args):
        """
        EnterpriseFeatureAccessConfiguration parameters
        :param pattern: pattern
	:param routePartitionName: routePartitionName
	:param description: description
	:param isDefaultEafNumber: isDefaultEafNumber
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addEnterpriseFeatureAccessConfiguration(**args)
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
            print(f"AXL error addEnterpriseFeatureAccessConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def HandoffConfiguration(self, **args):
        """
        HandoffConfiguration parameters
        :param pattern: pattern
	:param routePartitionName: routePartitionName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addHandoffConfiguration(**args)
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
            print(f"AXL error addHandoffConfiguration: ", str(err), file=sys.stderr)
            return False
        

    def CalledPartyTracing(self, **args):
        """
        CalledPartyTracing parameters
        :param directorynumber: directorynumber
	:param description: description
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCalledPartyTracing(**args)
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
            print(f"AXL error addCalledPartyTracing: ", str(err), file=sys.stderr)
            return False
        

    def SIPNormalizationScript(self, **args):
        """
        SIPNormalizationScript parameters
        :param name: name
	:param description: description
	:param content: content
	:param scriptExecutionErrorRecoveryAction: scriptExecutionErrorRecoveryAction
	:param systemResourceErrorRecoveryAction: systemResourceErrorRecoveryAction
	:param maxMemoryThreshold: maxMemoryThreshold
	:param maxLuaInstructionsThreshold: maxLuaInstructionsThreshold
	:param isStandard: isStandard
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSIPNormalizationScript(**args)
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
            print(f"AXL error addSIPNormalizationScript: ", str(err), file=sys.stderr)
            return False
        

    def CustomUserField(self, **args):
        """
        CustomUserField parameters
        :param field: field
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCustomUserField(**args)
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
            print(f"AXL error addCustomUserField: ", str(err), file=sys.stderr)
            return False
        

    def GatewaySccpEndpoints(self, **args):
        """
        GatewaySccpEndpoints parameters
        :param unit: unit
	:param subunit: subunit
	:param endpoint: endpoint
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addGatewaySccpEndpoints(**args)
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
            print(f"AXL error addGatewaySccpEndpoints: ", str(err), file=sys.stderr)
            return False
        

    def BillingServer(self, **args):
        """
        BillingServer parameters
        :param hostName: hostName
	:param userId: userId
	:param password: password
	:param directory: directory
	:param resendOnFailure: resendOnFailure
	:param billingServerProtocol: billingServerProtocol
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addBillingServer(**args)
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
            print(f"AXL error addBillingServer: ", str(err), file=sys.stderr)
            return False
        

    def LbmGroup(self, **args):
        """
        LbmGroup parameters
        :param name: name
	:param Description: Description
	:param ProcessnodeActive: ProcessnodeActive
	:param ProcessnodeStandby: ProcessnodeStandby
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLbmGroup(**args)
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
            print(f"AXL error addLbmGroup: ", str(err), file=sys.stderr)
            return False
        

    def Announcement(self, **args):
        """
        Announcement parameters
        :param name: name
	:param description: description
	:param announcementFile: announcementFile
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addAnnouncement(**args)
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
            print(f"AXL error addAnnouncement: ", str(err), file=sys.stderr)
            return False
        

    def ServiceProfile(self, **args):
        """
        ServiceProfile parameters
        :param name: name
	:param description: description
	:param isDefault: isDefault
	:param serviceProfileInfos: serviceProfileInfos
	:param profileName: profileName
	:param primary: primary
	:param secondary: secondary
	:param tertiary: tertiary
	:param serverCertificateVerification: serverCertificateVerification
	:param serviceProfileXml: serviceProfileXml
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addServiceProfile(**args)
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
            print(f"AXL error addServiceProfile: ", str(err), file=sys.stderr)
            return False
        

    def LdapSyncCustomField(self, **args):
        """
        LdapSyncCustomField parameters
        :param ldapConfigurationName: ldapConfigurationName
	:param customUserField: customUserField
	:param ldapUserField: ldapUserField
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLdapSyncCustomField(**args)
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
            print(f"AXL error addLdapSyncCustomField: ", str(err), file=sys.stderr)
            return False
        

    def AudioCodecPreferenceList(self, **args):
        """
        AudioCodecPreferenceList parameters
        :param name: name
	:param description: description
	:param codecsInList: codecsInList
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addAudioCodecPreferenceList(**args)
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
            print(f"AXL error addAudioCodecPreferenceList: ", str(err), file=sys.stderr)
            return False
        

    def UcService(self, **args):
        """
        UcService parameters
        :param serviceType: serviceType
	:param productType: productType
	:param name: name
	:param description: description
	:param hostnameorip: hostnameorip
	:param port: port
	:param protocol: protocol
	:param ucServiceXml: ucServiceXml
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addUcService(**args)
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
            print(f"AXL error addUcService: ", str(err), file=sys.stderr)
            return False
        

    def LbmHubGroup(self, **args):
        """
        LbmHubGroup parameters
        :param name: name
	:param description: description
	:param member1: member1
	:param member2: member2
	:param member3: member3
	:param members: members
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLbmHubGroup(**args)
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
            print(f"AXL error addLbmHubGroup: ", str(err), file=sys.stderr)
            return False
        

    def ImportedDirectoryUriCatalogs(self, **args):
        """
        ImportedDirectoryUriCatalogs parameters
        :param name: name
	:param description: description
	:param routeString: routeString
	:param lastLoadedFileName: lastLoadedFileName
	:param fileLoadDateTime: fileLoadDateTime
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addImportedDirectoryUriCatalogs(**args)
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
            print(f"AXL error addImportedDirectoryUriCatalogs: ", str(err), file=sys.stderr)
            return False
        

    def VohServer(self, **args):
        """
        VohServer parameters
        :param name: name
	:param description: description
	:param sipTrunkName: sipTrunkName
	:param defaultVideoStreamId: defaultVideoStreamId
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addVohServer(**args)
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
            print(f"AXL error addVohServer: ", str(err), file=sys.stderr)
            return False
        

    def SdpTransparencyProfile(self, **args):
        """
        SdpTransparencyProfile parameters
        :param name: name
	:param description: description
	:param attributeSet: attributeSet
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSdpTransparencyProfile(**args)
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
            print(f"AXL error addSdpTransparencyProfile: ", str(err), file=sys.stderr)
            return False
        

    def FeatureGroupTemplate(self, **args):
        """
        FeatureGroupTemplate parameters
        :param name: name
	:param description: description
	:param homeCluster: homeCluster
	:param imAndUcPresenceEnable: imAndUcPresenceEnable
	:param serviceProfile: serviceProfile
	:param enableUserToHostConferenceNow: enableUserToHostConferenceNow
	:param allowCTIControl: allowCTIControl
	:param enableEMCC: enableEMCC
	:param enableMobility: enableMobility
	:param enableMobileVoiceAccess: enableMobileVoiceAccess
	:param maxDeskPickupWait: maxDeskPickupWait
	:param remoteDestinationLimit: remoteDestinationLimit
	:param BLFPresenceGp: BLFPresenceGp
	:param subscribeCallingSearch: subscribeCallingSearch
	:param userLocale: userLocale
	:param userProfile: userProfile
	:param meetingInformation: meetingInformation
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addFeatureGroupTemplate(**args)
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
            print(f"AXL error addFeatureGroupTemplate: ", str(err), file=sys.stderr)
            return False
        

    def DirNumberAliasLookupandSync(self, **args):
        """
        DirNumberAliasLookupandSync parameters
        :param ldapConfigName: ldapConfigName
	:param ldapManagerDisgName: ldapManagerDisgName
	:param ldapPassword: ldapPassword
	:param ldapUserSearch: ldapUserSearch
	:param ldapDirectoryServerUsage: ldapDirectoryServerUsage
	:param keepAliveSearch: keepAliveSearch
	:param keepAliveTime: keepAliveTime
	:param sipAliasSuffix: sipAliasSuffix
	:param enableCachingofRecords: enableCachingofRecords
	:param servers: servers
	:param cacheSizeforAliasLookup: cacheSizeforAliasLookup
	:param cacheAgeforAliasLookup: cacheAgeforAliasLookup
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addDirNumberAliasLookupandSync(**args)
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
            print(f"AXL error addDirNumberAliasLookupandSync: ", str(err), file=sys.stderr)
            return False
        

    def LocalRouteGroup(self, **args):
        """
        LocalRouteGroup parameters
        :param name: name
	:param description: description
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addLocalRouteGroup(**args)
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
            print(f"AXL error addLocalRouteGroup: ", str(err), file=sys.stderr)
            return False
        

    def AdvertisedPatterns(self, **args):
        """
        AdvertisedPatterns parameters
        :param description: description
	:param pattern: pattern
	:param patternType: patternType
	:param hostedRoutePSTNRule: hostedRoutePSTNRule
	:param pstnFailStrip: pstnFailStrip
	:param pstnFailPrepend: pstnFailPrepend
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addAdvertisedPatterns(**args)
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
            print(f"AXL error addAdvertisedPatterns: ", str(err), file=sys.stderr)
            return False
        

    def BlockedLearnedPatterns(self, **args):
        """
        BlockedLearnedPatterns parameters
        :param description: description
	:param pattern: pattern
	:param prefix: prefix
	:param clusterId: clusterId
	:param patternType: patternType
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addBlockedLearnedPatterns(**args)
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
            print(f"AXL error addBlockedLearnedPatterns: ", str(err), file=sys.stderr)
            return False
        

    def CCAProfiles(self, **args):
        """
        CCAProfiles parameters
        :param ccaId: ccaId
	:param primarySoftSwitchId: primarySoftSwitchId
	:param secondarySoftSwitchId: secondarySoftSwitchId
	:param objectClass: objectClass
	:param subscriberType: subscriberType
	:param sipAliasSuffix: sipAliasSuffix
	:param sipUserNameSuffix: sipUserNameSuffix
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addCCAProfiles(**args)
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
            print(f"AXL error addCCAProfiles: ", str(err), file=sys.stderr)
            return False
        

    def UniversalDeviceTemplate(self, **args):
        """
        UniversalDeviceTemplate parameters
        :param name: name
	:param deviceDescription: deviceDescription
	:param devicePool: devicePool
	:param deviceSecurityProfile: deviceSecurityProfile
	:param sipProfile: sipProfile
	:param phoneButtonTemplate: phoneButtonTemplate
	:param sipDialRules: sipDialRules
	:param callingSearchSpace: callingSearchSpace
	:param callingPartyTransformationCSSForInboundCalls: callingPartyTransformationCSSForInboundCalls
	:param callingPartyTransformationCSSForOutboundCalls: callingPartyTransformationCSSForOutboundCalls
	:param reroutingCallingSearchSpace: reroutingCallingSearchSpace
	:param subscribeCallingSearchSpaceName: subscribeCallingSearchSpaceName
	:param useDevicePoolCallingPartyTransformationCSSforInboundCalls: useDevicePoolCallingPartyTransformationCSSforInboundCalls
	:param useDevicePoolCallingPartyTransformationCSSforOutboundCalls: useDevicePoolCallingPartyTransformationCSSforOutboundCalls
	:param commonPhoneProfile: commonPhoneProfile
	:param commonDeviceConfiguration: commonDeviceConfiguration
	:param softkeyTemplate: softkeyTemplate
	:param featureControlPolicy: featureControlPolicy
	:param phonePersonalization: phonePersonalization
	:param mtpPreferredOriginatingCodec: mtpPreferredOriginatingCodec
	:param outboundCallRollover: outboundCallRollover
	:param mediaTerminationPointRequired: mediaTerminationPointRequired
	:param unattendedPort: unattendedPort
	:param requiredDtmfReception: requiredDtmfReception
	:param rfc2833Disabled: rfc2833Disabled
	:param speeddials: speeddials
	:param lines: lines
	:param blfDirectedCallParks: blfDirectedCallParks
	:param busyLampFields: busyLampFields
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param protectedDevice: protectedDevice
	:param certificateOperation: certificateOperation
	:param authenticationMode: authenticationMode
	:param authenticationString: authenticationString
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param servicesProvisioning: servicesProvisioning
	:param packetCaptureMode: packetCaptureMode
	:param packetCaptureDuration: packetCaptureDuration
	:param secureShellUser: secureShellUser
	:param secureShellPassword: secureShellPassword
	:param userLocale: userLocale
	:param networkLocale: networkLocale
	:param mlppDomain: mlppDomain
	:param mlppIndication: mlppIndication
	:param mlppPreemption: mlppPreemption
	:param doNotDisturb: doNotDisturb
	:param dndOption: dndOption
	:param dndIncomingCallAlert: dndIncomingCallAlert
	:param aarGroup: aarGroup
	:param aarCallingSearchSpace: aarCallingSearchSpace
	:param blfPresenceGroup: blfPresenceGroup
	:param blfAudibleAlertSettingPhoneBusy: blfAudibleAlertSettingPhoneBusy
	:param blfAudibleAlertSettingPhoneIdle: blfAudibleAlertSettingPhoneIdle
	:param userHoldMohAudioSource: userHoldMohAudioSource
	:param networkHoldMohAudioSource: networkHoldMohAudioSource
	:param location: location
	:param geoLocation: geoLocation
	:param deviceMobilityMode: deviceMobilityMode
	:param mediaResourceGroupList: mediaResourceGroupList
	:param remoteDevice: remoteDevice
	:param hotlineDevice: hotlineDevice
	:param retryVideoCallAsAudio: retryVideoCallAsAudio
	:param requireOffPremiseLocation: requireOffPremiseLocation
	:param ownerUserId: ownerUserId
	:param mobilityUserId: mobilityUserId
	:param joinAcrossLines: joinAcrossLines
	:param alwaysUsePrimeLine: alwaysUsePrimeLine
	:param alwaysUsePrimeLineForVoiceMessage: alwaysUsePrimeLineForVoiceMessage
	:param singleButtonBarge: singleButtonBarge
	:param builtInBridge: builtInBridge
	:param allowControlOfDeviceFromCti: allowControlOfDeviceFromCti
	:param ignorePresentationIndicators: ignorePresentationIndicators
	:param enableExtensionMobility: enableExtensionMobility
	:param privacy: privacy
	:param loggedIntoHuntGroup: loggedIntoHuntGroup
	:param proxyServer: proxyServer
	:param servicesUrl: servicesUrl
	:param idle: idle
	:param idleTimer: idleTimer
	:param secureDirUrl: secureDirUrl
	:param messages: messages
	:param secureIdleUrl: secureIdleUrl
	:param authenticationServer: authenticationServer
	:param directory: directory
	:param secureServicesUrl: secureServicesUrl
	:param information: information
	:param secureMessagesUrl: secureMessagesUrl
	:param secureInformationUrl: secureInformationUrl
	:param secureAuthenticationUrl: secureAuthenticationUrl
	:param confidentialAccess: confidentialAccess
	:param services: services
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addUniversalDeviceTemplate(**args)
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
            print(f"AXL error addUniversalDeviceTemplate: ", str(err), file=sys.stderr)
            return False
        

    def UserProfileProvision(self, **args):
        """
        UserProfileProvision parameters
        :param name: name
	:param description: description
	:param deskPhones: deskPhones
	:param mobileDevices: mobileDevices
	:param profile: profile
	:param universalLineTemplate: universalLineTemplate
	:param allowProvision: allowProvision
	:param limitProvision: limitProvision
	:param allowPhoneReassign: allowPhoneReassign
	:param defaultUserProfile: defaultUserProfile
	:param enableMra: enableMra
	:param mraPolicy_Desktop: mraPolicy_Desktop
	:param mraPolicy_Mobile: mraPolicy_Mobile
	:param allowProvisionEMMaxLoginTime: allowProvisionEMMaxLoginTime
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addUserProfileProvision(**args)
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
            print(f"AXL error addUserProfileProvision: ", str(err), file=sys.stderr)
            return False
        

    def PresenceRedundancyGroup(self, **args):
        """
        PresenceRedundancyGroup parameters
        :param name: name
	:param description: description
	:param server1: server1
	:param server2: server2
	:param haEnabled: haEnabled
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addPresenceRedundancyGroup(**args)
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
            print(f"AXL error addPresenceRedundancyGroup: ", str(err), file=sys.stderr)
            return False
        

    def WifiHotspot(self, **args):
        """
        WifiHotspot parameters
        :param name: name
	:param description: description
	:param ssidPrefix: ssidPrefix
	:param userModifiable: userModifiable
	:param frequencyBand: frequencyBand
	:param authenticationMethod: authenticationMethod
	:param hostName: hostName
	:param port: port
	:param sharedSecret: sharedSecret
	:param pskPassPhrase: pskPassPhrase
	:param wepKey: wepKey
	:param passwordDescription: passwordDescription
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addWifiHotspot(**args)
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
            print(f"AXL error addWifiHotspot: ", str(err), file=sys.stderr)
            return False
        

    def WlanProfileGroup(self, **args):
        """
        WlanProfileGroup parameters
        :param name: name
	:param description: description
	:param members: members
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addWlanProfileGroup(**args)
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
            print(f"AXL error addWlanProfileGroup: ", str(err), file=sys.stderr)
            return False
        

    def WLANProfile(self, **args):
        """
        WLANProfile parameters
        :param name: name
	:param description: description
	:param ssid: ssid
	:param frequencyBand: frequencyBand
	:param userModifiable: userModifiable
	:param authMethod: authMethod
	:param userName: userName
	:param password: password
	:param pskPassphrase: pskPassphrase
	:param wepKey: wepKey
	:param passwordDescription: passwordDescription
	:param networkAccessProfile: networkAccessProfile
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addWLANProfile(**args)
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
            print(f"AXL error addWLANProfile: ", str(err), file=sys.stderr)
            return False
        

    def UniversalLineTemplate(self, **args):
        """
        UniversalLineTemplate parameters
        :param name: name
	:param urgentPriority: urgentPriority
	:param lineDescription: lineDescription
	:param routePartition: routePartition
	:param voiceMailProfile: voiceMailProfile
	:param callingSearchSpace: callingSearchSpace
	:param alertingName: alertingName
	:param extCallControlProfile: extCallControlProfile
	:param blfPresenceGroup: blfPresenceGroup
	:param callPickupGroup: callPickupGroup
	:param partyEntranceTone: partyEntranceTone
	:param autoAnswer: autoAnswer
	:param rejectAnonymousCall: rejectAnonymousCall
	:param userHoldMohAudioSource: userHoldMohAudioSource
	:param networkHoldMohAudioSource: networkHoldMohAudioSource
	:param aarDestinationMask: aarDestinationMask
	:param aarGroup: aarGroup
	:param retainDestInCallFwdHistory: retainDestInCallFwdHistory
	:param forwardDestAllCalls: forwardDestAllCalls
	:param primaryCssForwardingAllCalls: primaryCssForwardingAllCalls
	:param secondaryCssForwardingAllCalls: secondaryCssForwardingAllCalls
	:param CssActivationPolicy: CssActivationPolicy
	:param fwdDestExtCallsWhenNotRetrieved: fwdDestExtCallsWhenNotRetrieved
	:param cssFwdExtCallsWhenNotRetrieved: cssFwdExtCallsWhenNotRetrieved
	:param fwdDestInternalCallsWhenNotRetrieved: fwdDestInternalCallsWhenNotRetrieved
	:param cssFwdInternalCallsWhenNotRetrieved: cssFwdInternalCallsWhenNotRetrieved
	:param parkMonitorReversionTime: parkMonitorReversionTime
	:param target: target
	:param mlppCss: mlppCss
	:param mlppNoAnsRingDuration: mlppNoAnsRingDuration
	:param confidentialAccess: confidentialAccess
	:param holdReversionRingDuration: holdReversionRingDuration
	:param holdReversionNotificationInterval: holdReversionNotificationInterval
	:param busyIntCallsDestination: busyIntCallsDestination
	:param busyIntCallsCss: busyIntCallsCss
	:param busyExtCallsDestination: busyExtCallsDestination
	:param busyExtCallsCss: busyExtCallsCss
	:param noAnsIntCallsDestination: noAnsIntCallsDestination
	:param noAnsIntCallsCss: noAnsIntCallsCss
	:param noAnsExtCallsDestination: noAnsExtCallsDestination
	:param noAnsExtCallsCss: noAnsExtCallsCss
	:param noCoverageIntCallsDestination: noCoverageIntCallsDestination
	:param noCoverageIntCallsCss: noCoverageIntCallsCss
	:param noCoverageExtCallsDestination: noCoverageExtCallsDestination
	:param noCoverageExtCallsCss: noCoverageExtCallsCss
	:param unregisteredIntCallsDestination: unregisteredIntCallsDestination
	:param unregisteredIntCallsCss: unregisteredIntCallsCss
	:param unregisteredExtCallsDestination: unregisteredExtCallsDestination
	:param unregisteredExtCallsCss: unregisteredExtCallsCss
	:param ctiFailureDestination: ctiFailureDestination
	:param ctiFailureCss: ctiFailureCss
	:param callControlAgentProfile: callControlAgentProfile
	:param noAnswerRingDuration: noAnswerRingDuration
	:param enterpriseAltNum: enterpriseAltNum
	:param e164AltNum: e164AltNum
	:param advertisedFailoverNumber: advertisedFailoverNumber
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addUniversalLineTemplate(**args)
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
            print(f"AXL error addUniversalLineTemplate: ", str(err), file=sys.stderr)
            return False
        

    def NetworkAccessProfile(self, **args):
        """
        NetworkAccessProfile parameters
        :param name: name
	:param description: description
	:param vpnRequired: vpnRequired
	:param proxySettings: proxySettings
	:param proxyHostname: proxyHostname
	:param proxyPort: proxyPort
	:param proxyRequiresAuthentication: proxyRequiresAuthentication
	:param provideSharedCredentials: provideSharedCredentials
	:param username: username
	:param password: password
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addNetworkAccessProfile(**args)
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
            print(f"AXL error addNetworkAccessProfile: ", str(err), file=sys.stderr)
            return False
        

    def HttpProfile(self, **args):
        """
        HttpProfile parameters
        :param name: name
	:param userName: userName
	:param password: password
	:param requestTimeout: requestTimeout
	:param retryCount: retryCount
	:param webServiceRootUri: webServiceRootUri
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addHttpProfile(**args)
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
            print(f"AXL error addHttpProfile: ", str(err), file=sys.stderr)
            return False
        

    def ElinGroup(self, **args):
        """
        ElinGroup parameters
        :param name: name
	:param description: description
	:param elinNumbers: elinNumbers
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addElinGroup(**args)
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
            print(f"AXL error addElinGroup: ", str(err), file=sys.stderr)
            return False
        

    def InfrastructureDevice(self, **args):
        """
        InfrastructureDevice parameters
        :param name: name
	:param ipv4Address: ipv4Address
	:param ipv6Address: ipv6Address
	:param bssidWithMask: bssidWithMask
	:param wapLocation: wapLocation
	:param isActive: isActive
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addInfrastructureDevice(**args)
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
            print(f"AXL error addInfrastructureDevice: ", str(err), file=sys.stderr)
            return False
        

    def WirelessAccessPointControllers(self, **args):
        """
        WirelessAccessPointControllers parameters
        :param name: name
	:param description: description
	:param snmpVersion: snmpVersion
	:param snmpUserIdOrCommunityString: snmpUserIdOrCommunityString
	:param snmpAuthenticationProtocol: snmpAuthenticationProtocol
	:param snmpAuthenticationPassword: snmpAuthenticationPassword
	:param snmpPrivacyProtocol: snmpPrivacyProtocol
	:param snmpPrivacyPassword: snmpPrivacyPassword
	:param syncNow: syncNow
	:param resyncInterval: resyncInterval
	:param nextSyncTime: nextSyncTime
	:param scheduleUnit: scheduleUnit
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addWirelessAccessPointControllers(**args)
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
            print(f"AXL error addWirelessAccessPointControllers: ", str(err), file=sys.stderr)
            return False
        

    def PhoneActivationCode(self, **args):
        """
        PhoneActivationCode parameters
        :param activationCodeExpiry: activationCodeExpiry
	:param phoneName: phoneName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addPhoneActivationCode(**args)
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
            print(f"AXL error addPhoneActivationCode: ", str(err), file=sys.stderr)
            return False
        

    def MraServiceDomain(self, **args):
        """
        MraServiceDomain parameters
        :param name: name
	:param isDefault: isDefault
	:param serviceDomains: serviceDomains
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMraServiceDomain(**args)
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
            print(f"AXL error addMraServiceDomain: ", str(err), file=sys.stderr)
            return False
        

    def Mobility(self, **args):
        """
        Mobility parameters
        :param name: name
	:param description: description
	:param mobileClientCallingOption: mobileClientCallingOption
	:param dvofServiceAccessNumber: dvofServiceAccessNumber
	:param dirn: dirn
	:param dvorCallerId: dvorCallerId
	:param handoffNumber: handoffNumber
	:param handoffPartitionName: handoffPartitionName
	:param DTMFNumber: DTMFNumber
	:param DTMFPartitionName: DTMFPartitionName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addMobility(**args)
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
            print(f"AXL error addMobility: ", str(err), file=sys.stderr)
            return False
        

    def ApplicationToSoftkeyTemplate(self, **args):
        """
        ApplicationToSoftkeyTemplate parameters
        :param softKeyTemplateName: softKeyTemplateName
	:param standardSoftKeyTemplateName: standardSoftKeyTemplateName
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addApplicationToSoftkeyTemplate(**args)
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
            print(f"AXL error addApplicationToSoftkeyTemplate: ", str(err), file=sys.stderr)
            return False
        

    def SNMPCommunityString(self, **args):
        """
        SNMPCommunityString parameters
        :param communityName: communityName
	:param accessPrivilege: accessPrivilege
	:param ArrayOfHosts: ArrayOfHosts
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSNMPCommunityString(**args)
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
            print(f"AXL error addSNMPCommunityString: ", str(err), file=sys.stderr)
            return False
        

    def SNMPUser(self, **args):
        """
        SNMPUser parameters
        :param userName: userName
	:param authRequired: authRequired
	:param authPassword: authPassword
	:param authProtocol: authProtocol
	:param privacyRequired: privacyRequired
	:param privacyPassword: privacyPassword
	:param privacyProtocol: privacyProtocol
	:param accessPrivilege: accessPrivilege
	:param ArrayOfHosts: ArrayOfHosts
	:return: API Response message
        """
        result = {
            'success': False,
            'response': '',
            'error': '',
        }
        try:
            resp = self.client.addSNMPUser(**args)
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
            print(f"AXL error addSNMPUser: ", str(err), file=sys.stderr)
            return False
        

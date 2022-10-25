from zeep.helpers import serialize_object
from zeep.exceptions import Fault
import sys


class Update:
    def __init__(self, soap_client):
        self.client = soap_client

    def SipProfile(self, **args):
        """
        UpdateSipProfile parameters
        :param newName: newName
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
	:return: API Response message
        """
        try:
            resp = self.client.updateSipProfile(**args)
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
            print(f"AXL error updateSipProfile: ", str(err), file=sys.stderr)
            return False
    

    def SipTrunkSecurityProfile(self, **args):
        """
        UpdateSipTrunkSecurityProfile parameters
        :param newName: newName
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
        try:
            resp = self.client.updateSipTrunkSecurityProfile(**args)
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
            print(f"AXL error updateSipTrunkSecurityProfile: ", str(err), file=sys.stderr)
            return False
    

    def TimePeriod(self, **args):
        """
        UpdateTimePeriod parameters
        :param newName: newName
	:param startTime: startTime
	:param endTime: endTime
	:param startDay: startDay
	:param endDay: endDay
	:param monthOfYear: monthOfYear
	:param dayOfMonth: dayOfMonth
	:param description: description
	:param dayOfMonthEnd: dayOfMonthEnd
	:param monthOfYearEnd: monthOfYearEnd
	:return: API Response message
        """
        try:
            resp = self.client.updateTimePeriod(**args)
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
            print(f"AXL error updateTimePeriod: ", str(err), file=sys.stderr)
            return False
    

    def TimeSchedule(self, **args):
        """
        UpdateTimeSchedule parameters
        :param newName: newName
	:param description: description
	:param timeScheduleCategory: timeScheduleCategory
	:return: API Response message
        """
        try:
            resp = self.client.updateTimeSchedule(**args)
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
            print(f"AXL error updateTimeSchedule: ", str(err), file=sys.stderr)
            return False
    

    def TodAccess(self, **args):
        """
        UpdateTodAccess parameters
        :param newName: newName
	:param description: description
	:param members: members
	:return: API Response message
        """
        try:
            resp = self.client.updateTodAccess(**args)
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
            print(f"AXL error updateTodAccess: ", str(err), file=sys.stderr)
            return False
    

    def VoiceMailPilot(self, **args):
        """
        UpdateVoiceMailPilot parameters
        :param newDirn: newDirn
	:param description: description
	:param newCssName: newCssName
	:param isDefault: isDefault
	:return: API Response message
        """
        try:
            resp = self.client.updateVoiceMailPilot(**args)
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
            print(f"AXL error updateVoiceMailPilot: ", str(err), file=sys.stderr)
            return False
    

    def ProcessNode(self, **args):
        """
        UpdateProcessNode parameters
        :param newName: newName
	:param description: description
	:param mac: mac
	:param ipv6Name: ipv6Name
	:param lbmHubGroup: lbmHubGroup
	:param cupDomain: cupDomain
	:return: API Response message
        """
        try:
            resp = self.client.updateProcessNode(**args)
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
            print(f"AXL error updateProcessNode: ", str(err), file=sys.stderr)
            return False
    

    def CallerFilterList(self, **args):
        """
        UpdateCallerFilterList parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateCallerFilterList(**args)
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
            print(f"AXL error updateCallerFilterList: ", str(err), file=sys.stderr)
            return False
    

    def RoutePartition(self, **args):
        """
        UpdateRoutePartition parameters
        :param newName: newName
	:param description: description
	:param timeScheduleIdName: timeScheduleIdName
	:param useOriginatingDeviceTimeZone: useOriginatingDeviceTimeZone
	:param timeZone: timeZone
	:return: API Response message
        """
        try:
            resp = self.client.updateRoutePartition(**args)
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
            print(f"AXL error updateRoutePartition: ", str(err), file=sys.stderr)
            return False
    

    def Css(self, **args):
        """
        UpdateCss parameters
        :param description: description
	:param newName: newName
	:return: API Response message
        """
        try:
            resp = self.client.updateCss(**args)
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
            print(f"AXL error updateCss: ", str(err), file=sys.stderr)
            return False
    

    def CallManager(self, **args):
        """
        UpdateCallManager parameters
        :param newName: newName
	:param description: description
	:param autoRegistration: autoRegistration
	:param ports: ports
	:param lbmGroup: lbmGroup
	:return: API Response message
        """
        try:
            resp = self.client.updateCallManager(**args)
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
            print(f"AXL error updateCallManager: ", str(err), file=sys.stderr)
            return False
    

    def ExpresswayCConfiguration(self, **args):
        """
        UpdateExpresswayCConfiguration parameters
        :param newHostNameOrIP: newHostNameOrIP
	:param description: description
	:param X509SubjectNameorSubjectAlternateName: X509SubjectNameorSubjectAlternateName
	:return: API Response message
        """
        try:
            resp = self.client.updateExpresswayCConfiguration(**args)
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
            print(f"AXL error updateExpresswayCConfiguration: ", str(err), file=sys.stderr)
            return False
    

    def MediaResourceGroup(self, **args):
        """
        UpdateMediaResourceGroup parameters
        :param newName: newName
	:param description: description
	:param multicast: multicast
	:return: API Response message
        """
        try:
            resp = self.client.updateMediaResourceGroup(**args)
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
            print(f"AXL error updateMediaResourceGroup: ", str(err), file=sys.stderr)
            return False
    

    def MediaResourceList(self, **args):
        """
        UpdateMediaResourceList parameters
        :param newName: newName
	:return: API Response message
        """
        try:
            resp = self.client.updateMediaResourceList(**args)
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
            print(f"AXL error updateMediaResourceList: ", str(err), file=sys.stderr)
            return False
    

    def Region(self, **args):
        """
        UpdateRegion parameters
        :param newName: newName
	:param relatedRegions: relatedRegions
	:return: API Response message
        """
        try:
            resp = self.client.updateRegion(**args)
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
            print(f"AXL error updateRegion: ", str(err), file=sys.stderr)
            return False
    

    def AarGroup(self, **args):
        """
        UpdateAarGroup parameters
        :param newName: newName
	:return: API Response message
        """
        try:
            resp = self.client.updateAarGroup(**args)
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
            print(f"AXL error updateAarGroup: ", str(err), file=sys.stderr)
            return False
    

    def PhysicalLocation(self, **args):
        """
        UpdatePhysicalLocation parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updatePhysicalLocation(**args)
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
            print(f"AXL error updatePhysicalLocation: ", str(err), file=sys.stderr)
            return False
    

    def Customer(self, **args):
        """
        UpdateCustomer parameters
        :param newName: newName
	:return: API Response message
        """
        try:
            resp = self.client.updateCustomer(**args)
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
            print(f"AXL error updateCustomer: ", str(err), file=sys.stderr)
            return False
    

    def RouteGroup(self, **args):
        """
        UpdateRouteGroup parameters
        :param distributionAlgorithm: distributionAlgorithm
	:param newName: newName
	:return: API Response message
        """
        try:
            resp = self.client.updateRouteGroup(**args)
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
            print(f"AXL error updateRouteGroup: ", str(err), file=sys.stderr)
            return False
    

    def DevicePool(self, **args):
        """
        UpdateDevicePool parameters
        :param newName: newName
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
	:return: API Response message
        """
        try:
            resp = self.client.updateDevicePool(**args)
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
            print(f"AXL error updateDevicePool: ", str(err), file=sys.stderr)
            return False
    

    def DeviceMobilityGroup(self, **args):
        """
        UpdateDeviceMobilityGroup parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateDeviceMobilityGroup(**args)
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
            print(f"AXL error updateDeviceMobilityGroup: ", str(err), file=sys.stderr)
            return False
    

    def Location(self, **args):
        """
        UpdateLocation parameters
        :param newName: newName
	:param relatedLocations: relatedLocations
	:param withinAudioBandwidth: withinAudioBandwidth
	:param withinVideoBandwidth: withinVideoBandwidth
	:param withinImmersiveKbits: withinImmersiveKbits
	:param betweenLocations: betweenLocations
	:return: API Response message
        """
        try:
            resp = self.client.updateLocation(**args)
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
            print(f"AXL error updateLocation: ", str(err), file=sys.stderr)
            return False
    

    def SoftKeyTemplate(self, **args):
        """
        UpdateSoftKeyTemplate parameters
        :param newName: newName
	:param description: description
	:param isDefault: isDefault
	:return: API Response message
        """
        try:
            resp = self.client.updateSoftKeyTemplate(**args)
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
            print(f"AXL error updateSoftKeyTemplate: ", str(err), file=sys.stderr)
            return False
    

    def Transcoder(self, **args):
        """
        UpdateTranscoder parameters
        :param newName: newName
	:param description: description
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param loadInformation: loadInformation
	:param vendorConfig: vendorConfig
	:param isTrustedRelayPoint: isTrustedRelayPoint
	:param maximumCapacity: maximumCapacity
	:return: API Response message
        """
        try:
            resp = self.client.updateTranscoder(**args)
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
            print(f"AXL error updateTranscoder: ", str(err), file=sys.stderr)
            return False
    

    def CommonDeviceConfig(self, **args):
        """
        UpdateCommonDeviceConfig parameters
        :param newName: newName
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
        try:
            resp = self.client.updateCommonDeviceConfig(**args)
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
            print(f"AXL error updateCommonDeviceConfig: ", str(err), file=sys.stderr)
            return False
    

    def ResourcePriorityNamespace(self, **args):
        """
        UpdateResourcePriorityNamespace parameters
        :param newNamespace: newNamespace
	:param description: description
	:param isDefault: isDefault
	:return: API Response message
        """
        try:
            resp = self.client.updateResourcePriorityNamespace(**args)
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
            print(f"AXL error updateResourcePriorityNamespace: ", str(err), file=sys.stderr)
            return False
    

    def ResourcePriorityNamespaceList(self, **args):
        """
        UpdateResourcePriorityNamespaceList parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateResourcePriorityNamespaceList(**args)
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
            print(f"AXL error updateResourcePriorityNamespaceList: ", str(err), file=sys.stderr)
            return False
    

    def DeviceMobility(self, **args):
        """
        UpdateDeviceMobility parameters
        :param newName: newName
	:param subNetDetails: subNetDetails
	:return: API Response message
        """
        try:
            resp = self.client.updateDeviceMobility(**args)
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
            print(f"AXL error updateDeviceMobility: ", str(err), file=sys.stderr)
            return False
    

    def CmcInfo(self, **args):
        """
        UpdateCmcInfo parameters
        :param newCode: newCode
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateCmcInfo(**args)
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
            print(f"AXL error updateCmcInfo: ", str(err), file=sys.stderr)
            return False
    

    def CredentialPolicy(self, **args):
        """
        UpdateCredentialPolicy parameters
        :param newName: newName
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
	:return: API Response message
        """
        try:
            resp = self.client.updateCredentialPolicy(**args)
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
            print(f"AXL error updateCredentialPolicy: ", str(err), file=sys.stderr)
            return False
    

    def FacInfo(self, **args):
        """
        UpdateFacInfo parameters
        :param newName: newName
	:param code: code
	:param authorizationLevel: authorizationLevel
	:return: API Response message
        """
        try:
            resp = self.client.updateFacInfo(**args)
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
            print(f"AXL error updateFacInfo: ", str(err), file=sys.stderr)
            return False
    

    def HuntList(self, **args):
        """
        UpdateHuntList parameters
        :param description: description
	:param callManagerGroupName: callManagerGroupName
	:param routeListEnabled: routeListEnabled
	:param voiceMailUsage: voiceMailUsage
	:param newName: newName
	:return: API Response message
        """
        try:
            resp = self.client.updateHuntList(**args)
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
            print(f"AXL error updateHuntList: ", str(err), file=sys.stderr)
            return False
    

    def IvrUserLocale(self, **args):
        """
        UpdateIvrUserLocale parameters
        :param newUserLocale: newUserLocale
	:param orderIndex: orderIndex
	:return: API Response message
        """
        try:
            resp = self.client.updateIvrUserLocale(**args)
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
            print(f"AXL error updateIvrUserLocale: ", str(err), file=sys.stderr)
            return False
    

    def LineGroup(self, **args):
        """
        UpdateLineGroup parameters
        :param distributionAlgorithm: distributionAlgorithm
	:param rnaReversionTimeOut: rnaReversionTimeOut
	:param huntAlgorithmNoAnswer: huntAlgorithmNoAnswer
	:param huntAlgorithmBusy: huntAlgorithmBusy
	:param huntAlgorithmNotAvailable: huntAlgorithmNotAvailable
	:param newName: newName
	:param autoLogOffHunt: autoLogOffHunt
	:return: API Response message
        """
        try:
            resp = self.client.updateLineGroup(**args)
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
            print(f"AXL error updateLineGroup: ", str(err), file=sys.stderr)
            return False
    

    def RecordingProfile(self, **args):
        """
        UpdateRecordingProfile parameters
        :param newName: newName
	:param recordingCssName: recordingCssName
	:param recorderDestination: recorderDestination
	:return: API Response message
        """
        try:
            resp = self.client.updateRecordingProfile(**args)
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
            print(f"AXL error updateRecordingProfile: ", str(err), file=sys.stderr)
            return False
    

    def RouteFilter(self, **args):
        """
        UpdateRouteFilter parameters
        :param newName: newName
	:param dialPlanName: dialPlanName
	:return: API Response message
        """
        try:
            resp = self.client.updateRouteFilter(**args)
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
            print(f"AXL error updateRouteFilter: ", str(err), file=sys.stderr)
            return False
    

    def CallManagerGroup(self, **args):
        """
        UpdateCallManagerGroup parameters
        :param newName: newName
	:param tftpDefault: tftpDefault
	:return: API Response message
        """
        try:
            resp = self.client.updateCallManagerGroup(**args)
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
            print(f"AXL error updateCallManagerGroup: ", str(err), file=sys.stderr)
            return False
    

    def UserGroup(self, **args):
        """
        UpdateUserGroup parameters
        :param newName: newName
	:return: API Response message
        """
        try:
            resp = self.client.updateUserGroup(**args)
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
            print(f"AXL error updateUserGroup: ", str(err), file=sys.stderr)
            return False
    

    def ProcessNodeService(self, **args):
        """
        UpdateProcessNodeService parameters
        :param traceLevel: traceLevel
	:param userCategories: userCategories
	:param enable: enable
	:param numFiles: numFiles
	:param maxFileSize: maxFileSize
	:return: API Response message
        """
        try:
            resp = self.client.updateProcessNodeService(**args)
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
            print(f"AXL error updateProcessNodeService: ", str(err), file=sys.stderr)
            return False
    

    def MohAudioSource(self, **args):
        """
        UpdateMohAudioSource parameters
        :param newName: newName
	:param sourceFile: sourceFile
	:param multicast: multicast
	:param mohFileStatus: mohFileStatus
	:param initialAnnouncement: initialAnnouncement
	:param periodicAnnouncement: periodicAnnouncement
	:param periodicAnnouncementInterval: periodicAnnouncementInterval
	:param localeAnnouncement: localeAnnouncement
	:param initialAnnouncementPlayed: initialAnnouncementPlayed
	:param isExternalSource: isExternalSource
	:return: API Response message
        """
        try:
            resp = self.client.updateMohAudioSource(**args)
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
            print(f"AXL error updateMohAudioSource: ", str(err), file=sys.stderr)
            return False
    

    def DhcpServer(self, **args):
        """
        UpdateDhcpServer parameters
        :param newProcessNodeName: newProcessNodeName
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
        try:
            resp = self.client.updateDhcpServer(**args)
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
            print(f"AXL error updateDhcpServer: ", str(err), file=sys.stderr)
            return False
    

    def DhcpSubnet(self, **args):
        """
        UpdateDhcpSubnet parameters
        :param newDhcpServerName: newDhcpServerName
	:param newSubnetIpAddress: newSubnetIpAddress
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
        try:
            resp = self.client.updateDhcpSubnet(**args)
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
            print(f"AXL error updateDhcpSubnet: ", str(err), file=sys.stderr)
            return False
    

    def CallPark(self, **args):
        """
        UpdateCallPark parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
	:param callManagerName: callManagerName
	:return: API Response message
        """
        try:
            resp = self.client.updateCallPark(**args)
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
            print(f"AXL error updateCallPark: ", str(err), file=sys.stderr)
            return False
    

    def DirectedCallPark(self, **args):
        """
        UpdateDirectedCallPark parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
	:param retrievalPrefix: retrievalPrefix
	:param reversionPattern: reversionPattern
	:param revertCssName: revertCssName
	:return: API Response message
        """
        try:
            resp = self.client.updateDirectedCallPark(**args)
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
            print(f"AXL error updateDirectedCallPark: ", str(err), file=sys.stderr)
            return False
    

    def MeetMe(self, **args):
        """
        UpdateMeetMe parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
	:param minimumSecurityLevel: minimumSecurityLevel
	:return: API Response message
        """
        try:
            resp = self.client.updateMeetMe(**args)
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
            print(f"AXL error updateMeetMe: ", str(err), file=sys.stderr)
            return False
    

    def ConferenceNow(self, **args):
        """
        UpdateConferenceNow parameters
        :param newConferenceNowNumber: newConferenceNowNumber
	:param newRoutePartitionName: newRoutePartitionName
	:param description: description
	:param maxWaitTimeForHost: maxWaitTimeForHost
	:param MohAudioSourceId: MohAudioSourceId
	:return: API Response message
        """
        try:
            resp = self.client.updateConferenceNow(**args)
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
            print(f"AXL error updateConferenceNow: ", str(err), file=sys.stderr)
            return False
    

    def MobileVoiceAccess(self, **args):
        """
        UpdateMobileVoiceAccess parameters
        :param newPattern: newPattern
	:param routePartitionName: routePartitionName
	:return: API Response message
        """
        try:
            resp = self.client.updateMobileVoiceAccess(**args)
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
            print(f"AXL error updateMobileVoiceAccess: ", str(err), file=sys.stderr)
            return False
    

    def RouteList(self, **args):
        """
        UpdateRouteList parameters
        :param newName: newName
	:param description: description
	:param callManagerGroupName: callManagerGroupName
	:param routeListEnabled: routeListEnabled
	:param runOnEveryNode: runOnEveryNode
	:return: API Response message
        """
        try:
            resp = self.client.updateRouteList(**args)
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
            print(f"AXL error updateRouteList: ", str(err), file=sys.stderr)
            return False
    

    def User(self, **args):
        """
        UpdateUser parameters
        :param firstName: firstName
	:param displayName: displayName
	:param middleName: middleName
	:param lastName: lastName
	:param emMaxLoginTime: emMaxLoginTime
	:param newUserid: newUserid
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
	:return: API Response message
        """
        try:
            resp = self.client.updateUser(**args)
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
            print(f"AXL error updateUser: ", str(err), file=sys.stderr)
            return False
    

    def AppUser(self, **args):
        """
        UpdateAppUser parameters
        :param newUserid: newUserid
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
        try:
            resp = self.client.updateAppUser(**args)
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
            print(f"AXL error updateAppUser: ", str(err), file=sys.stderr)
            return False
    

    def SipRealm(self, **args):
        """
        UpdateSipRealm parameters
        :param newRealm: newRealm
	:param userid: userid
	:param digestCredentials: digestCredentials
	:return: API Response message
        """
        try:
            resp = self.client.updateSipRealm(**args)
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
            print(f"AXL error updateSipRealm: ", str(err), file=sys.stderr)
            return False
    

    def PhoneNtp(self, **args):
        """
        UpdatePhoneNtp parameters
        :param newIpAddress: newIpAddress
	:param newIpv6Address: newIpv6Address
	:param description: description
	:param mode: mode
	:return: API Response message
        """
        try:
            resp = self.client.updatePhoneNtp(**args)
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
            print(f"AXL error updatePhoneNtp: ", str(err), file=sys.stderr)
            return False
    

    def DateTimeGroup(self, **args):
        """
        UpdateDateTimeGroup parameters
        :param newName: newName
	:param timeZone: timeZone
	:param separator: separator
	:param dateformat: dateformat
	:param timeFormat: timeFormat
	:return: API Response message
        """
        try:
            resp = self.client.updateDateTimeGroup(**args)
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
            print(f"AXL error updateDateTimeGroup: ", str(err), file=sys.stderr)
            return False
    

    def PresenceGroup(self, **args):
        """
        UpdatePresenceGroup parameters
        :param newName: newName
	:param description: description
	:param presenceGroups: presenceGroups
	:return: API Response message
        """
        try:
            resp = self.client.updatePresenceGroup(**args)
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
            print(f"AXL error updatePresenceGroup: ", str(err), file=sys.stderr)
            return False
    

    def GeoLocation(self, **args):
        """
        UpdateGeoLocation parameters
        :param newName: newName
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
	:return: API Response message
        """
        try:
            resp = self.client.updateGeoLocation(**args)
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
            print(f"AXL error updateGeoLocation: ", str(err), file=sys.stderr)
            return False
    

    def Srst(self, **args):
        """
        UpdateSrst parameters
        :param newName: newName
	:param port: port
	:param ipAddress: ipAddress
	:param ipv6Address: ipv6Address
	:param SipNetwork: SipNetwork
	:param SipPort: SipPort
	:param isSecure: isSecure
	:return: API Response message
        """
        try:
            resp = self.client.updateSrst(**args)
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
            print(f"AXL error updateSrst: ", str(err), file=sys.stderr)
            return False
    

    def MlppDomain(self, **args):
        """
        UpdateMlppDomain parameters
        :param newDomainName: newDomainName
	:param domainId: domainId
	:return: API Response message
        """
        try:
            resp = self.client.updateMlppDomain(**args)
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
            print(f"AXL error updateMlppDomain: ", str(err), file=sys.stderr)
            return False
    

    def CumaServerSecurityProfile(self, **args):
        """
        UpdateCumaServerSecurityProfile parameters
        :param newName: newName
	:param description: description
	:param securityMode: securityMode
	:param transportType: transportType
	:param x509SubjectName: x509SubjectName
	:param serverIpHostName: serverIpHostName
	:return: API Response message
        """
        try:
            resp = self.client.updateCumaServerSecurityProfile(**args)
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
            print(f"AXL error updateCumaServerSecurityProfile: ", str(err), file=sys.stderr)
            return False
    

    def ApplicationServer(self, **args):
        """
        UpdateApplicationServer parameters
        :param newName: newName
	:param ipAddress: ipAddress
	:param url: url
	:param endUserUrl: endUserUrl
	:param processNodeName: processNodeName
	:return: API Response message
        """
        try:
            resp = self.client.updateApplicationServer(**args)
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
            print(f"AXL error updateApplicationServer: ", str(err), file=sys.stderr)
            return False
    

    def ApplicationUserCapfProfile(self, **args):
        """
        UpdateApplicationUserCapfProfile parameters
        :param certificateOperation: certificateOperation
	:param authenticationMode: authenticationMode
	:param authenticationString: authenticationString
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param operationCompletion: operationCompletion
	:return: API Response message
        """
        try:
            resp = self.client.updateApplicationUserCapfProfile(**args)
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
            print(f"AXL error updateApplicationUserCapfProfile: ", str(err), file=sys.stderr)
            return False
    

    def EndUserCapfProfile(self, **args):
        """
        UpdateEndUserCapfProfile parameters
        :param certificationOperation: certificationOperation
	:param authenticationMode: authenticationMode
	:param authenticationString: authenticationString
	:param keySize: keySize
	:param keyOrder: keyOrder
	:param ecKeySize: ecKeySize
	:param operationCompletion: operationCompletion
	:return: API Response message
        """
        try:
            resp = self.client.updateEndUserCapfProfile(**args)
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
            print(f"AXL error updateEndUserCapfProfile: ", str(err), file=sys.stderr)
            return False
    

    def ServiceParameter(self, **args):
        """
        UpdateServiceParameter parameters
        :param value: value
	:return: API Response message
        """
        try:
            resp = self.client.updateServiceParameter(**args)
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
            print(f"AXL error updateServiceParameter: ", str(err), file=sys.stderr)
            return False
    

    def GeoLocationFilter(self, **args):
        """
        UpdateGeoLocationFilter parameters
        :param newName: newName
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
        try:
            resp = self.client.updateGeoLocationFilter(**args)
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
            print(f"AXL error updateGeoLocationFilter: ", str(err), file=sys.stderr)
            return False
    

    def VoiceMailProfile(self, **args):
        """
        UpdateVoiceMailProfile parameters
        :param newName: newName
	:param description: description
	:param isDefault: isDefault
	:param voiceMailboxMask: voiceMailboxMask
	:param voiceMailPilot: voiceMailPilot
	:return: API Response message
        """
        try:
            resp = self.client.updateVoiceMailProfile(**args)
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
            print(f"AXL error updateVoiceMailProfile: ", str(err), file=sys.stderr)
            return False
    

    def VoiceMailPort(self, **args):
        """
        UpdateVoiceMailPort parameters
        :param newName: newName
	:param description: description
	:param callingSearchSpaceName: callingSearchSpaceName
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param locationName: locationName
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
        try:
            resp = self.client.updateVoiceMailPort(**args)
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
            print(f"AXL error updateVoiceMailPort: ", str(err), file=sys.stderr)
            return False
    

    def Gatekeeper(self, **args):
        """
        UpdateGatekeeper parameters
        :param newName: newName
	:param description: description
	:param rrqTimeToLive: rrqTimeToLive
	:param retryTimeout: retryTimeout
	:param enableDevice: enableDevice
	:return: API Response message
        """
        try:
            resp = self.client.updateGatekeeper(**args)
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
            print(f"AXL error updateGatekeeper: ", str(err), file=sys.stderr)
            return False
    

    def PhoneButtonTemplate(self, **args):
        """
        UpdatePhoneButtonTemplate parameters
        :param newName: newName
	:param buttons: buttons
	:return: API Response message
        """
        try:
            resp = self.client.updatePhoneButtonTemplate(**args)
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
            print(f"AXL error updatePhoneButtonTemplate: ", str(err), file=sys.stderr)
            return False
    

    def CommonPhoneConfig(self, **args):
        """
        UpdateCommonPhoneConfig parameters
        :param newName: newName
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
        try:
            resp = self.client.updateCommonPhoneConfig(**args)
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
            print(f"AXL error updateCommonPhoneConfig: ", str(err), file=sys.stderr)
            return False
    

    def MessageWaiting(self, **args):
        """
        UpdateMessageWaiting parameters
        :param newPattern: newPattern
	:param newRoutePartitionName: newRoutePartitionName
	:param description: description
	:param messageWaitingIndicator: messageWaitingIndicator
	:param callingSearchSpaceName: callingSearchSpaceName
	:return: API Response message
        """
        try:
            resp = self.client.updateMessageWaiting(**args)
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
            print(f"AXL error updateMessageWaiting: ", str(err), file=sys.stderr)
            return False
    

    def IpPhoneServices(self, **args):
        """
        UpdateIpPhoneServices parameters
        :param newServiceName: newServiceName
	:param asciiServiceName: asciiServiceName
	:param serviceDescription: serviceDescription
	:param serviceUrl: serviceUrl
	:param secureServiceUrl: secureServiceUrl
	:param serviceCategory: serviceCategory
	:param serviceType: serviceType
	:param serviceVendor: serviceVendor
	:param serviceVersion: serviceVersion
	:param enabled: enabled
	:return: API Response message
        """
        try:
            resp = self.client.updateIpPhoneServices(**args)
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
            print(f"AXL error updateIpPhoneServices: ", str(err), file=sys.stderr)
            return False
    

    def CtiRoutePoint(self, **args):
        """
        UpdateCtiRoutePoint parameters
        :param newName: newName
	:param description: description
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
        try:
            resp = self.client.updateCtiRoutePoint(**args)
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
            print(f"AXL error updateCtiRoutePoint: ", str(err), file=sys.stderr)
            return False
    

    def TransPattern(self, **args):
        """
        UpdateTransPattern parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
	:param blockEnable: blockEnable
	:param calledPartyTransformationMask: calledPartyTransformationMask
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param newDialPlanName: newDialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param patternUrgency: patternUrgency
	:param prefixDigitsOut: prefixDigitsOut
	:param newRouteFilterName: newRouteFilterName
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
	:return: API Response message
        """
        try:
            resp = self.client.updateTransPattern(**args)
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
            print(f"AXL error updateTransPattern: ", str(err), file=sys.stderr)
            return False
    

    def CallingPartyTransformationPattern(self, **args):
        """
        UpdateCallingPartyTransformationPattern parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param newDialPlanName: newDialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param newRouteFilterName: newRouteFilterName
	:param callingLinePresentationBit: callingLinePresentationBit
	:param callingPartyNumberingPlan: callingPartyNumberingPlan
	:param callingPartyNumberType: callingPartyNumberType
	:param mlppPreemptionDisabled: mlppPreemptionDisabled
	:return: API Response message
        """
        try:
            resp = self.client.updateCallingPartyTransformationPattern(**args)
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
            print(f"AXL error updateCallingPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
    

    def SipRoutePattern(self, **args):
        """
        UpdateSipRoutePattern parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
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
        try:
            resp = self.client.updateSipRoutePattern(**args)
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
            print(f"AXL error updateSipRoutePattern: ", str(err), file=sys.stderr)
            return False
    

    def HuntPilot(self, **args):
        """
        UpdateHuntPilot parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
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
        try:
            resp = self.client.updateHuntPilot(**args)
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
            print(f"AXL error updateHuntPilot: ", str(err), file=sys.stderr)
            return False
    

    def RoutePattern(self, **args):
        """
        UpdateRoutePattern parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
	:param blockEnable: blockEnable
	:param calledPartyTransformationMask: calledPartyTransformationMask
	:param callingPartyTransformationMask: callingPartyTransformationMask
	:param useCallingPartyPhoneMask: useCallingPartyPhoneMask
	:param callingPartyPrefixDigits: callingPartyPrefixDigits
	:param newDialPlanName: newDialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param networkLocation: networkLocation
	:param patternUrgency: patternUrgency
	:param prefixDigitsOut: prefixDigitsOut
	:param newRouteFilterName: newRouteFilterName
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
        try:
            resp = self.client.updateRoutePattern(**args)
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
            print(f"AXL error updateRoutePattern: ", str(err), file=sys.stderr)
            return False
    

    def ApplicationDialRules(self, **args):
        """
        UpdateApplicationDialRules parameters
        :param newName: newName
	:param description: description
	:param numberBeginWith: numberBeginWith
	:param numberOfDigits: numberOfDigits
	:param digitsToBeRemoved: digitsToBeRemoved
	:param prefixPattern: prefixPattern
	:param priority: priority
	:return: API Response message
        """
        try:
            resp = self.client.updateApplicationDialRules(**args)
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
            print(f"AXL error updateApplicationDialRules: ", str(err), file=sys.stderr)
            return False
    

    def DirectoryLookupDialRules(self, **args):
        """
        UpdateDirectoryLookupDialRules parameters
        :param newName: newName
	:param description: description
	:param numberBeginWith: numberBeginWith
	:param numberOfDigits: numberOfDigits
	:param digitsToBeRemoved: digitsToBeRemoved
	:param prefixPattern: prefixPattern
	:param priority: priority
	:return: API Response message
        """
        try:
            resp = self.client.updateDirectoryLookupDialRules(**args)
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
            print(f"AXL error updateDirectoryLookupDialRules: ", str(err), file=sys.stderr)
            return False
    

    def PhoneSecurityProfile(self, **args):
        """
        UpdatePhoneSecurityProfile parameters
        :param newName: newName
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
        try:
            resp = self.client.updatePhoneSecurityProfile(**args)
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
            print(f"AXL error updatePhoneSecurityProfile: ", str(err), file=sys.stderr)
            return False
    

    def SipDialRules(self, **args):
        """
        UpdateSipDialRules parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateSipDialRules(**args)
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
            print(f"AXL error updateSipDialRules: ", str(err), file=sys.stderr)
            return False
    

    def ConferenceBridge(self, **args):
        """
        UpdateConferenceBridge parameters
        :param newName: newName
	:param description: description
	:param product: product
	:param devicePoolName: devicePoolName
	:param commonDeviceConfigName: commonDeviceConfigName
	:param locationName: locationName
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
        try:
            resp = self.client.updateConferenceBridge(**args)
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
            print(f"AXL error updateConferenceBridge: ", str(err), file=sys.stderr)
            return False
    

    def Annunciator(self, **args):
        """
        UpdateAnnunciator parameters
        :param newName: newName
	:param description: description
	:param devicePoolName: devicePoolName
	:param locationName: locationName
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:return: API Response message
        """
        try:
            resp = self.client.updateAnnunciator(**args)
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
            print(f"AXL error updateAnnunciator: ", str(err), file=sys.stderr)
            return False
    

    def InteractiveVoiceResponse(self, **args):
        """
        UpdateInteractiveVoiceResponse parameters
        :param newName: newName
	:param description: description
	:param devicePoolName: devicePoolName
	:param locationName: locationName
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:return: API Response message
        """
        try:
            resp = self.client.updateInteractiveVoiceResponse(**args)
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
            print(f"AXL error updateInteractiveVoiceResponse: ", str(err), file=sys.stderr)
            return False
    

    def Mtp(self, **args):
        """
        UpdateMtp parameters
        :param newName: newName
	:param description: description
	:param devicePoolName: devicePoolName
	:param trustedRelayPoint: trustedRelayPoint
	:return: API Response message
        """
        try:
            resp = self.client.updateMtp(**args)
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
            print(f"AXL error updateMtp: ", str(err), file=sys.stderr)
            return False
    

    def FixedMohAudioSource(self, **args):
        """
        UpdateFixedMohAudioSource parameters
        :param newName: newName
	:param multicast: multicast
	:param enable: enable
	:param initialAnnouncement: initialAnnouncement
	:param periodicAnnouncement: periodicAnnouncement
	:param periodicAnnouncementInterval: periodicAnnouncementInterval
	:param localeAnnouncement: localeAnnouncement
	:param initialAnnouncementPlayed: initialAnnouncementPlayed
	:return: API Response message
        """
        try:
            resp = self.client.updateFixedMohAudioSource(**args)
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
            print(f"AXL error updateFixedMohAudioSource: ", str(err), file=sys.stderr)
            return False
    

    def AarGroupMatrix(self, **args):
        """
        UpdateAarGroupMatrix parameters
        :param prefixDigit: prefixDigit
	:return: API Response message
        """
        try:
            resp = self.client.updateAarGroupMatrix(**args)
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
            print(f"AXL error updateAarGroupMatrix: ", str(err), file=sys.stderr)
            return False
    

    def RemoteDestinationProfile(self, **args):
        """
        UpdateRemoteDestinationProfile parameters
        :param newName: newName
	:param description: description
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
        try:
            resp = self.client.updateRemoteDestinationProfile(**args)
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
            print(f"AXL error updateRemoteDestinationProfile: ", str(err), file=sys.stderr)
            return False
    

    def Line(self, **args):
        """
        UpdateLine parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
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
	:return: API Response message
        """
        try:
            resp = self.client.updateLine(**args)
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
            print(f"AXL error updateLine: ", str(err), file=sys.stderr)
            return False
    

    def DefaultDeviceProfile(self, **args):
        """
        UpdateDefaultDeviceProfile parameters
        :param description: description
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
        try:
            resp = self.client.updateDefaultDeviceProfile(**args)
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
            print(f"AXL error updateDefaultDeviceProfile: ", str(err), file=sys.stderr)
            return False
    

    def H323Phone(self, **args):
        """
        UpdateH323Phone parameters
        :param newName: newName
	:param description: description
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
        try:
            resp = self.client.updateH323Phone(**args)
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
            print(f"AXL error updateH323Phone: ", str(err), file=sys.stderr)
            return False
    

    def MohServer(self, **args):
        """
        UpdateMohServer parameters
        :param newName: newName
	:param description: description
	:param devicePoolName: devicePoolName
	:param locationName: locationName
	:param maxUnicastConnections: maxUnicastConnections
	:param maxMulticastConnections: maxMulticastConnections
	:param fixedAudioSourceDevice: fixedAudioSourceDevice
	:param runFlag: runFlag
	:param useTrustedRelayPoint: useTrustedRelayPoint
	:param isMultiCastEnabled: isMultiCastEnabled
	:param baseMulticastIpaddress: baseMulticastIpaddress
	:param baseMulticastPort: baseMulticastPort
	:param multicastIncrementOnIp: multicastIncrementOnIp
	:param audioSources: audioSources
	:return: API Response message
        """
        try:
            resp = self.client.updateMohServer(**args)
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
            print(f"AXL error updateMohServer: ", str(err), file=sys.stderr)
            return False
    

    def H323Trunk(self, **args):
        """
        UpdateH323Trunk parameters
        :param newName: newName
	:param description: description
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
	:param useDevicePoolCntdPnTransformationCss: useDevicePoolCntdPnTransformationCss
	:param cntdPnTransformationCssName: cntdPnTransformationCssName
	:param confidentialAccess: confidentialAccess
	:param connectCallBeforePlayingAnnouncement: connectCallBeforePlayingAnnouncement
	:return: API Response message
        """
        try:
            resp = self.client.updateH323Trunk(**args)
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
            print(f"AXL error updateH323Trunk: ", str(err), file=sys.stderr)
            return False
    

    def Phone(self, **args):
        """
        UpdatePhone parameters
        :param newName: newName
	:param description: description
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
	:return: API Response message
        """
        try:
            resp = self.client.updatePhone(**args)
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
            print(f"AXL error updatePhone: ", str(err), file=sys.stderr)
            return False
    

    def H323Gateway(self, **args):
        """
        UpdateH323Gateway parameters
        :param newName: newName
	:param description: description
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
        try:
            resp = self.client.updateH323Gateway(**args)
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
            print(f"AXL error updateH323Gateway: ", str(err), file=sys.stderr)
            return False
    

    def DeviceProfile(self, **args):
        """
        UpdateDeviceProfile parameters
        :param newName: newName
	:param description: description
	:param userHoldMohAudioSourceId: userHoldMohAudioSourceId
	:param vendorConfig: vendorConfig
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
	:return: API Response message
        """
        try:
            resp = self.client.updateDeviceProfile(**args)
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
            print(f"AXL error updateDeviceProfile: ", str(err), file=sys.stderr)
            return False
    

    def RemoteDestination(self, **args):
        """
        UpdateRemoteDestination parameters
        :param newName: newName
	:param newDestination: newDestination
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
	:param accessListName: accessListName
	:return: API Response message
        """
        try:
            resp = self.client.updateRemoteDestination(**args)
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
            print(f"AXL error updateRemoteDestination: ", str(err), file=sys.stderr)
            return False
    

    def Vg224(self, **args):
        """
        UpdateVg224 parameters
        :param newDomainName: newDomainName
	:param description: description
	:param callManagerGroupName: callManagerGroupName
	:param vendorConfig: vendorConfig
	:return: API Response message
        """
        try:
            resp = self.client.updateVg224(**args)
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
            print(f"AXL error updateVg224: ", str(err), file=sys.stderr)
            return False
    

    def Gateway(self, **args):
        """
        UpdateGateway parameters
        :param newDomainName: newDomainName
	:param description: description
	:param product: product
	:param protocol: protocol
	:param callManagerGroupName: callManagerGroupName
	:param vendorConfig: vendorConfig
	:return: API Response message
        """
        try:
            resp = self.client.updateGateway(**args)
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
            print(f"AXL error updateGateway: ", str(err), file=sys.stderr)
            return False
    

    def GatewayEndpointAnalogAccess(self, **args):
        """
        UpdateGatewayEndpointAnalogAccess parameters
        :param endpoint: endpoint
	:return: API Response message
        """
        try:
            resp = self.client.updateGatewayEndpointAnalogAccess(**args)
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
            print(f"AXL error updateGatewayEndpointAnalogAccess: ", str(err), file=sys.stderr)
            return False
    

    def GatewayEndpointDigitalAccessPri(self, **args):
        """
        UpdateGatewayEndpointDigitalAccessPri parameters
        :param endpoint: endpoint
	:return: API Response message
        """
        try:
            resp = self.client.updateGatewayEndpointDigitalAccessPri(**args)
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
            print(f"AXL error updateGatewayEndpointDigitalAccessPri: ", str(err), file=sys.stderr)
            return False
    

    def GatewayEndpointDigitalAccessBri(self, **args):
        """
        UpdateGatewayEndpointDigitalAccessBri parameters
        :param endpoint: endpoint
	:return: API Response message
        """
        try:
            resp = self.client.updateGatewayEndpointDigitalAccessBri(**args)
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
            print(f"AXL error updateGatewayEndpointDigitalAccessBri: ", str(err), file=sys.stderr)
            return False
    

    def GatewayEndpointDigitalAccessT1(self, **args):
        """
        UpdateGatewayEndpointDigitalAccessT1 parameters
        :param endpoint: endpoint
	:return: API Response message
        """
        try:
            resp = self.client.updateGatewayEndpointDigitalAccessT1(**args)
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
            print(f"AXL error updateGatewayEndpointDigitalAccessT1: ", str(err), file=sys.stderr)
            return False
    

    def CiscoCatalyst600024PortFXSGateway(self, **args):
        """
        UpdateCiscoCatalyst600024PortFXSGateway parameters
        :param newName: newName
	:param description: description
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
        try:
            resp = self.client.updateCiscoCatalyst600024PortFXSGateway(**args)
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
            print(f"AXL error updateCiscoCatalyst600024PortFXSGateway: ", str(err), file=sys.stderr)
            return False
    

    def CiscoCatalyst6000E1VoIPGateway(self, **args):
        """
        UpdateCiscoCatalyst6000E1VoIPGateway parameters
        :param newName: newName
	:param description: description
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
        try:
            resp = self.client.updateCiscoCatalyst6000E1VoIPGateway(**args)
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
            print(f"AXL error updateCiscoCatalyst6000E1VoIPGateway: ", str(err), file=sys.stderr)
            return False
    

    def CiscoCatalyst6000T1VoIPGatewayPri(self, **args):
        """
        UpdateCiscoCatalyst6000T1VoIPGatewayPri parameters
        :param newName: newName
	:param description: description
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
        try:
            resp = self.client.updateCiscoCatalyst6000T1VoIPGatewayPri(**args)
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
            print(f"AXL error updateCiscoCatalyst6000T1VoIPGatewayPri: ", str(err), file=sys.stderr)
            return False
    

    def CiscoCatalyst6000T1VoIPGatewayT1(self, **args):
        """
        UpdateCiscoCatalyst6000T1VoIPGatewayT1 parameters
        :param newName: newName
	:param description: description
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
        try:
            resp = self.client.updateCiscoCatalyst6000T1VoIPGatewayT1(**args)
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
            print(f"AXL error updateCiscoCatalyst6000T1VoIPGatewayT1: ", str(err), file=sys.stderr)
            return False
    

    def CallPickupGroup(self, **args):
        """
        UpdateCallPickupGroup parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
	:param pickupNotification: pickupNotification
	:param pickupNotificationTimer: pickupNotificationTimer
	:param callInfoForPickupNotification: callInfoForPickupNotification
	:param newName: newName
	:return: API Response message
        """
        try:
            resp = self.client.updateCallPickupGroup(**args)
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
            print(f"AXL error updateCallPickupGroup: ", str(err), file=sys.stderr)
            return False
    

    def GeoLocationPolicy(self, **args):
        """
        UpdateGeoLocationPolicy parameters
        :param newName: newName
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
	:return: API Response message
        """
        try:
            resp = self.client.updateGeoLocationPolicy(**args)
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
            print(f"AXL error updateGeoLocationPolicy: ", str(err), file=sys.stderr)
            return False
    

    def SipTrunk(self, **args):
        """
        UpdateSipTrunk parameters
        :param newName: newName
	:param description: description
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
	:return: API Response message
        """
        try:
            resp = self.client.updateSipTrunk(**args)
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
            print(f"AXL error updateSipTrunk: ", str(err), file=sys.stderr)
            return False
    

    def RegionMatrix(self, **args):
        """
        UpdateRegionMatrix parameters
        :param bandwidth: bandwidth
	:param videoBandwidth: videoBandwidth
	:param codecPreference: codecPreference
	:return: API Response message
        """
        try:
            resp = self.client.updateRegionMatrix(**args)
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
            print(f"AXL error updateRegionMatrix: ", str(err), file=sys.stderr)
            return False
    

    def CalledPartyTransformationPattern(self, **args):
        """
        UpdateCalledPartyTransformationPattern parameters
        :param newPattern: newPattern
	:param description: description
	:param newRoutePartitionName: newRoutePartitionName
	:param calledPartyTransformationMask: calledPartyTransformationMask
	:param newDialPlanName: newDialPlanName
	:param digitDiscardInstructionName: digitDiscardInstructionName
	:param newRouteFilterName: newRouteFilterName
	:param calledPartyPrefixDigits: calledPartyPrefixDigits
	:param calledPartyNumberingPlan: calledPartyNumberingPlan
	:param calledPartyNumberType: calledPartyNumberType
	:param mlppPreemptionDisabled: mlppPreemptionDisabled
	:return: API Response message
        """
        try:
            resp = self.client.updateCalledPartyTransformationPattern(**args)
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
            print(f"AXL error updateCalledPartyTransformationPattern: ", str(err), file=sys.stderr)
            return False
    

    def ExternalCallControlProfile(self, **args):
        """
        UpdateExternalCallControlProfile parameters
        :param newName: newName
	:param primaryUri: primaryUri
	:param secondaryUri: secondaryUri
	:param enableLoadBalancing: enableLoadBalancing
	:param routingRequestTimer: routingRequestTimer
	:param diversionReroutingCssName: diversionReroutingCssName
	:param callTreatmentOnFailure: callTreatmentOnFailure
	:return: API Response message
        """
        try:
            resp = self.client.updateExternalCallControlProfile(**args)
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
            print(f"AXL error updateExternalCallControlProfile: ", str(err), file=sys.stderr)
            return False
    

    def SafSecurityProfile(self, **args):
        """
        UpdateSafSecurityProfile parameters
        :param newName: newName
	:param description: description
	:param userid: userid
	:param password: password
	:return: API Response message
        """
        try:
            resp = self.client.updateSafSecurityProfile(**args)
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
            print(f"AXL error updateSafSecurityProfile: ", str(err), file=sys.stderr)
            return False
    

    def SafForwarder(self, **args):
        """
        UpdateSafForwarder parameters
        :param newName: newName
	:param description: description
	:param clientLabel: clientLabel
	:param safSecurityProfile: safSecurityProfile
	:param ipAddress: ipAddress
	:param port: port
	:param enableTcpKeepAlive: enableTcpKeepAlive
	:param safReconnectInterval: safReconnectInterval
	:param safNotificationsWindowSize: safNotificationsWindowSize
	:return: API Response message
        """
        try:
            resp = self.client.updateSafForwarder(**args)
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
            print(f"AXL error updateSafForwarder: ", str(err), file=sys.stderr)
            return False
    

    def CcdHostedDN(self, **args):
        """
        UpdateCcdHostedDN parameters
        :param newHostedPattern: newHostedPattern
	:param description: description
	:param CcdHostedDnGroup: CcdHostedDnGroup
	:param pstnFailoverStripDigits: pstnFailoverStripDigits
	:param pstnFailoverPrependDigits: pstnFailoverPrependDigits
	:param usePstnFailover: usePstnFailover
	:return: API Response message
        """
        try:
            resp = self.client.updateCcdHostedDN(**args)
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
            print(f"AXL error updateCcdHostedDN: ", str(err), file=sys.stderr)
            return False
    

    def CcdHostedDNGroup(self, **args):
        """
        UpdateCcdHostedDNGroup parameters
        :param newName: newName
	:param description: description
	:param pstnFailoverStripDigits: pstnFailoverStripDigits
	:param pstnFailoverPrependDigits: pstnFailoverPrependDigits
	:param usePstnFailover: usePstnFailover
	:return: API Response message
        """
        try:
            resp = self.client.updateCcdHostedDNGroup(**args)
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
            print(f"AXL error updateCcdHostedDNGroup: ", str(err), file=sys.stderr)
            return False
    

    def Ccd(self, **args):
        """
        UpdateCcd parameters
        :param newName: newName
	:param description: description
	:param isActivated: isActivated
	:param routePartitionName: routePartitionName
	:param learnedPatternPrefix: learnedPatternPrefix
	:param pstnPrefix: pstnPrefix
	:return: API Response message
        """
        try:
            resp = self.client.updateCcd(**args)
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
            print(f"AXL error updateCcd: ", str(err), file=sys.stderr)
            return False
    

    def InterClusterServiceProfile(self, **args):
        """
        UpdateInterClusterServiceProfile parameters
        :param isActivated: isActivated
	:param sipTrunkName: sipTrunkName
	:return: API Response message
        """
        try:
            resp = self.client.updateInterClusterServiceProfile(**args)
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
            print(f"AXL error updateInterClusterServiceProfile: ", str(err), file=sys.stderr)
            return False
    

    def RemoteCluster(self, **args):
        """
        UpdateRemoteCluster parameters
        :param emcc: emcc
	:param pstnAccess: pstnAccess
	:param rsvpAgent: rsvpAgent
	:param tftp: tftp
	:param lbm: lbm
	:param uds: uds
	:return: API Response message
        """
        try:
            resp = self.client.updateRemoteCluster(**args)
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
            print(f"AXL error updateRemoteCluster: ", str(err), file=sys.stderr)
            return False
    

    def CcdAdvertisingService(self, **args):
        """
        UpdateCcdAdvertisingService parameters
        :param newName: newName
	:param description: description
	:param isActivated: isActivated
	:param hostDnGroup: hostDnGroup
	:param safSipTrunk: safSipTrunk
	:param safH323Trunk: safH323Trunk
	:return: API Response message
        """
        try:
            resp = self.client.updateCcdAdvertisingService(**args)
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
            print(f"AXL error updateCcdAdvertisingService: ", str(err), file=sys.stderr)
            return False
    

    def LdapDirectory(self, **args):
        """
        UpdateLdapDirectory parameters
        :param newName: newName
	:param ldapDn: ldapDn
	:param ldapPassword: ldapPassword
	:param userSearchBase: userSearchBase
	:param repeatable: repeatable
	:param intervalValue: intervalValue
	:param scheduleUnit: scheduleUnit
	:param nextExecTime: nextExecTime
	:param servers: servers
	:param ldapFilter: ldapFilter
	:param synchronize: synchronize
	:param ldapFilterForGroups: ldapFilterForGroups
	:param featureGroupTemplate: featureGroupTemplate
	:param applyMask: applyMask
	:param mask: mask
	:param applyPoolList: applyPoolList
	:param addDns: addDns
	:return: API Response message
        """
        try:
            resp = self.client.updateLdapDirectory(**args)
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
            print(f"AXL error updateLdapDirectory: ", str(err), file=sys.stderr)
            return False
    

    def EmccFeatureConfig(self, **args):
        """
        UpdateEmccFeatureConfig parameters
        :param value: value
	:return: API Response message
        """
        try:
            resp = self.client.updateEmccFeatureConfig(**args)
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
            print(f"AXL error updateEmccFeatureConfig: ", str(err), file=sys.stderr)
            return False
    

    def SafCcdPurgeBlockLearnedRoutes(self, **args):
        """
        UpdateSafCcdPurgeBlockLearnedRoutes parameters
        :param newLearnedPattern: newLearnedPattern
	:param newLearnedPatternPrefix: newLearnedPatternPrefix
	:param newCallControlIdentity: newCallControlIdentity
	:param newIpAddress: newIpAddress
	:return: API Response message
        """
        try:
            resp = self.client.updateSafCcdPurgeBlockLearnedRoutes(**args)
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
            print(f"AXL error updateSafCcdPurgeBlockLearnedRoutes: ", str(err), file=sys.stderr)
            return False
    

    def VpnGateway(self, **args):
        """
        UpdateVpnGateway parameters
        :param newName: newName
	:param description: description
	:param url: url
	:param certificates: certificates
	:return: API Response message
        """
        try:
            resp = self.client.updateVpnGateway(**args)
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
            print(f"AXL error updateVpnGateway: ", str(err), file=sys.stderr)
            return False
    

    def VpnGroup(self, **args):
        """
        UpdateVpnGroup parameters
        :param newName: newName
	:param description: description
	:param vpnGateways: vpnGateways
	:return: API Response message
        """
        try:
            resp = self.client.updateVpnGroup(**args)
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
            print(f"AXL error updateVpnGroup: ", str(err), file=sys.stderr)
            return False
    

    def VpnProfile(self, **args):
        """
        UpdateVpnProfile parameters
        :param newName: newName
	:param description: description
	:param autoNetworkDetection: autoNetworkDetection
	:param mtu: mtu
	:param failToConnect: failToConnect
	:param clientAuthentication: clientAuthentication
	:param pwdPersistant: pwdPersistant
	:param enableHostIdCheck: enableHostIdCheck
	:return: API Response message
        """
        try:
            resp = self.client.updateVpnProfile(**args)
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
            print(f"AXL error updateVpnProfile: ", str(err), file=sys.stderr)
            return False
    

    def ImeServer(self, **args):
        """
        UpdateImeServer parameters
        :param newName: newName
	:param description: description
	:param ipAddress: ipAddress
	:param port: port
	:param deviceSecurityMode: deviceSecurityMode
	:param applicationUser: applicationUser
	:param reconnectInterval: reconnectInterval
	:return: API Response message
        """
        try:
            resp = self.client.updateImeServer(**args)
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
            print(f"AXL error updateImeServer: ", str(err), file=sys.stderr)
            return False
    

    def ImeRouteFilterGroup(self, **args):
        """
        UpdateImeRouteFilterGroup parameters
        :param newName: newName
	:param description: description
	:param groupTrustSetting: groupTrustSetting
	:return: API Response message
        """
        try:
            resp = self.client.updateImeRouteFilterGroup(**args)
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
            print(f"AXL error updateImeRouteFilterGroup: ", str(err), file=sys.stderr)
            return False
    

    def ImeRouteFilterElement(self, **args):
        """
        UpdateImeRouteFilterElement parameters
        :param newName: newName
	:param description: description
	:param elementType: elementType
	:param imeRouteFilterGroupName: imeRouteFilterGroupName
	:return: API Response message
        """
        try:
            resp = self.client.updateImeRouteFilterElement(**args)
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
            print(f"AXL error updateImeRouteFilterElement: ", str(err), file=sys.stderr)
            return False
    

    def ImeClient(self, **args):
        """
        UpdateImeClient parameters
        :param newName: newName
	:param description: description
	:param domain: domain
	:param isActivated: isActivated
	:param sipTrunkName: sipTrunkName
	:param primaryImeServerName: primaryImeServerName
	:param secondaryImeServerName: secondaryImeServerName
	:param learnedRouteFilterGroupName: learnedRouteFilterGroupName
	:param exclusionNumberGroupName: exclusionNumberGroupName
	:param firewallName: firewallName
	:return: API Response message
        """
        try:
            resp = self.client.updateImeClient(**args)
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
            print(f"AXL error updateImeClient: ", str(err), file=sys.stderr)
            return False
    

    def ImeEnrolledPattern(self, **args):
        """
        UpdateImeEnrolledPattern parameters
        :param newPattern: newPattern
	:param description: description
	:param imeEnrolledPatternGroupName: imeEnrolledPatternGroupName
	:return: API Response message
        """
        try:
            resp = self.client.updateImeEnrolledPattern(**args)
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
            print(f"AXL error updateImeEnrolledPattern: ", str(err), file=sys.stderr)
            return False
    

    def ImeEnrolledPatternGroup(self, **args):
        """
        UpdateImeEnrolledPatternGroup parameters
        :param newName: newName
	:param description: description
	:param fallbackProfileName: fallbackProfileName
	:param isPatternAllAlias: isPatternAllAlias
	:return: API Response message
        """
        try:
            resp = self.client.updateImeEnrolledPatternGroup(**args)
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
            print(f"AXL error updateImeEnrolledPatternGroup: ", str(err), file=sys.stderr)
            return False
    

    def ImeExclusionNumber(self, **args):
        """
        UpdateImeExclusionNumber parameters
        :param newPattern: newPattern
	:param description: description
	:param imeExclusionNumberGroupName: imeExclusionNumberGroupName
	:return: API Response message
        """
        try:
            resp = self.client.updateImeExclusionNumber(**args)
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
            print(f"AXL error updateImeExclusionNumber: ", str(err), file=sys.stderr)
            return False
    

    def ImeExclusionNumberGroup(self, **args):
        """
        UpdateImeExclusionNumberGroup parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateImeExclusionNumberGroup(**args)
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
            print(f"AXL error updateImeExclusionNumberGroup: ", str(err), file=sys.stderr)
            return False
    

    def ImeFirewall(self, **args):
        """
        UpdateImeFirewall parameters
        :param newName: newName
	:param description: description
	:param ipAddress: ipAddress
	:param port: port
	:return: API Response message
        """
        try:
            resp = self.client.updateImeFirewall(**args)
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
            print(f"AXL error updateImeFirewall: ", str(err), file=sys.stderr)
            return False
    

    def ImeE164Transformation(self, **args):
        """
        UpdateImeE164Transformation parameters
        :param newName: newName
	:param description: description
	:param cgpnTransformationCssName: cgpnTransformationCssName
	:param isCgpnPreTransformation: isCgpnPreTransformation
	:param cdpnTransformationCssName: cdpnTransformationCssName
	:param isCdpnPreTransformation: isCdpnPreTransformation
	:param incomingCgpnTransformationProfileName: incomingCgpnTransformationProfileName
	:param incomingCdpnTransformationProfileName: incomingCdpnTransformationProfileName
	:return: API Response message
        """
        try:
            resp = self.client.updateImeE164Transformation(**args)
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
            print(f"AXL error updateImeE164Transformation: ", str(err), file=sys.stderr)
            return False
    

    def TransformationProfile(self, **args):
        """
        UpdateTransformationProfile parameters
        :param newName: newName
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
        try:
            resp = self.client.updateTransformationProfile(**args)
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
            print(f"AXL error updateTransformationProfile: ", str(err), file=sys.stderr)
            return False
    

    def FallbackProfile(self, **args):
        """
        UpdateFallbackProfile parameters
        :param newName: newName
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
        try:
            resp = self.client.updateFallbackProfile(**args)
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
            print(f"AXL error updateFallbackProfile: ", str(err), file=sys.stderr)
            return False
    

    def LdapFilter(self, **args):
        """
        UpdateLdapFilter parameters
        :param newName: newName
	:param filter: filter
	:return: API Response message
        """
        try:
            resp = self.client.updateLdapFilter(**args)
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
            print(f"AXL error updateLdapFilter: ", str(err), file=sys.stderr)
            return False
    

    def AppServerInfo(self, **args):
        """
        UpdateAppServerInfo parameters
        :param appServerName: appServerName
	:param appServerContent: appServerContent
	:param content: content
	:return: API Response message
        """
        try:
            resp = self.client.updateAppServerInfo(**args)
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
            print(f"AXL error updateAppServerInfo: ", str(err), file=sys.stderr)
            return False
    

    def TvsCertificate(self, **args):
        """
        UpdateTvsCertificate parameters
        :param timeToLive: timeToLive
	:return: API Response message
        """
        try:
            resp = self.client.updateTvsCertificate(**args)
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
            print(f"AXL error updateTvsCertificate: ", str(err), file=sys.stderr)
            return False
    

    def FeatureControlPolicy(self, **args):
        """
        UpdateFeatureControlPolicy parameters
        :param newName: newName
	:param description: description
	:param features: features
	:return: API Response message
        """
        try:
            resp = self.client.updateFeatureControlPolicy(**args)
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
            print(f"AXL error updateFeatureControlPolicy: ", str(err), file=sys.stderr)
            return False
    

    def MobilityProfile(self, **args):
        """
        UpdateMobilityProfile parameters
        :param newName: newName
	:param description: description
	:param mobileClientCallingOption: mobileClientCallingOption
	:param dvofServiceAccessNumber: dvofServiceAccessNumber
	:param dirn: dirn
	:param dvorCallerId: dvorCallerId
	:return: API Response message
        """
        try:
            resp = self.client.updateMobilityProfile(**args)
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
            print(f"AXL error updateMobilityProfile: ", str(err), file=sys.stderr)
            return False
    

    def EnterpriseFeatureAccessConfiguration(self, **args):
        """
        UpdateEnterpriseFeatureAccessConfiguration parameters
        :param newPattern: newPattern
	:param newRoutePartitionName: newRoutePartitionName
	:param description: description
	:param isDefaultEafNumber: isDefaultEafNumber
	:return: API Response message
        """
        try:
            resp = self.client.updateEnterpriseFeatureAccessConfiguration(**args)
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
            print(f"AXL error updateEnterpriseFeatureAccessConfiguration: ", str(err), file=sys.stderr)
            return False
    

    def HandoffConfiguration(self, **args):
        """
        UpdateHandoffConfiguration parameters
        :param newPattern: newPattern
	:param newRoutePartitionName: newRoutePartitionName
	:return: API Response message
        """
        try:
            resp = self.client.updateHandoffConfiguration(**args)
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
            print(f"AXL error updateHandoffConfiguration: ", str(err), file=sys.stderr)
            return False
    

    def SIPNormalizationScript(self, **args):
        """
        UpdateSIPNormalizationScript parameters
        :param newName: newName
	:param description: description
	:param content: content
	:param scriptExecutionErrorRecoveryAction: scriptExecutionErrorRecoveryAction
	:param systemResourceErrorRecoveryAction: systemResourceErrorRecoveryAction
	:param maxMemoryThreshold: maxMemoryThreshold
	:param maxLuaInstructionsThreshold: maxLuaInstructionsThreshold
	:return: API Response message
        """
        try:
            resp = self.client.updateSIPNormalizationScript(**args)
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
            print(f"AXL error updateSIPNormalizationScript: ", str(err), file=sys.stderr)
            return False
    

    def CustomUserField(self, **args):
        """
        UpdateCustomUserField parameters
        :param newField: newField
	:return: API Response message
        """
        try:
            resp = self.client.updateCustomUserField(**args)
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
            print(f"AXL error updateCustomUserField: ", str(err), file=sys.stderr)
            return False
    

    def GatewaySccpEndpoints(self, **args):
        """
        UpdateGatewaySccpEndpoints parameters
        :param endpoint: endpoint
	:return: API Response message
        """
        try:
            resp = self.client.updateGatewaySccpEndpoints(**args)
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
            print(f"AXL error updateGatewaySccpEndpoints: ", str(err), file=sys.stderr)
            return False
    

    def LbmGroup(self, **args):
        """
        UpdateLbmGroup parameters
        :param newName: newName
	:param Description: Description
	:param ProcessnodeActive: ProcessnodeActive
	:param ProcessnodeStandby: ProcessnodeStandby
	:return: API Response message
        """
        try:
            resp = self.client.updateLbmGroup(**args)
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
            print(f"AXL error updateLbmGroup: ", str(err), file=sys.stderr)
            return False
    

    def Announcement(self, **args):
        """
        UpdateAnnouncement parameters
        :param newName: newName
	:param description: description
	:param announcementFile: announcementFile
	:return: API Response message
        """
        try:
            resp = self.client.updateAnnouncement(**args)
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
            print(f"AXL error updateAnnouncement: ", str(err), file=sys.stderr)
            return False
    

    def ServiceProfile(self, **args):
        """
        UpdateServiceProfile parameters
        :param newName: newName
	:param description: description
	:param isDefault: isDefault
	:param serviceProfileInfos: serviceProfileInfos
	:return: API Response message
        """
        try:
            resp = self.client.updateServiceProfile(**args)
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
            print(f"AXL error updateServiceProfile: ", str(err), file=sys.stderr)
            return False
    

    def LdapSyncCustomField(self, **args):
        """
        UpdateLdapSyncCustomField parameters
        :param ldapUserField: ldapUserField
	:return: API Response message
        """
        try:
            resp = self.client.updateLdapSyncCustomField(**args)
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
            print(f"AXL error updateLdapSyncCustomField: ", str(err), file=sys.stderr)
            return False
    

    def AudioCodecPreferenceList(self, **args):
        """
        UpdateAudioCodecPreferenceList parameters
        :param newName: newName
	:param description: description
	:param codecsInList: codecsInList
	:return: API Response message
        """
        try:
            resp = self.client.updateAudioCodecPreferenceList(**args)
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
            print(f"AXL error updateAudioCodecPreferenceList: ", str(err), file=sys.stderr)
            return False
    

    def UcService(self, **args):
        """
        UpdateUcService parameters
        :param newName: newName
	:param description: description
	:param hostnameorip: hostnameorip
	:param port: port
	:param protocol: protocol
	:param ucServiceXml: ucServiceXml
	:return: API Response message
        """
        try:
            resp = self.client.updateUcService(**args)
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
            print(f"AXL error updateUcService: ", str(err), file=sys.stderr)
            return False
    

    def LbmHubGroup(self, **args):
        """
        UpdateLbmHubGroup parameters
        :param newName: newName
	:param description: description
	:param member1: member1
	:param member2: member2
	:param member3: member3
	:return: API Response message
        """
        try:
            resp = self.client.updateLbmHubGroup(**args)
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
            print(f"AXL error updateLbmHubGroup: ", str(err), file=sys.stderr)
            return False
    

    def ImportedDirectoryUriCatalogs(self, **args):
        """
        UpdateImportedDirectoryUriCatalogs parameters
        :param newName: newName
	:param description: description
	:param routeString: routeString
	:return: API Response message
        """
        try:
            resp = self.client.updateImportedDirectoryUriCatalogs(**args)
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
            print(f"AXL error updateImportedDirectoryUriCatalogs: ", str(err), file=sys.stderr)
            return False
    

    def VohServer(self, **args):
        """
        UpdateVohServer parameters
        :param newName: newName
	:param description: description
	:param sipTrunkName: sipTrunkName
	:param defaultVideoStreamId: defaultVideoStreamId
	:return: API Response message
        """
        try:
            resp = self.client.updateVohServer(**args)
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
            print(f"AXL error updateVohServer: ", str(err), file=sys.stderr)
            return False
    

    def SdpTransparencyProfile(self, **args):
        """
        UpdateSdpTransparencyProfile parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateSdpTransparencyProfile(**args)
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
            print(f"AXL error updateSdpTransparencyProfile: ", str(err), file=sys.stderr)
            return False
    

    def FeatureGroupTemplate(self, **args):
        """
        UpdateFeatureGroupTemplate parameters
        :param newName: newName
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
        try:
            resp = self.client.updateFeatureGroupTemplate(**args)
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
            print(f"AXL error updateFeatureGroupTemplate: ", str(err), file=sys.stderr)
            return False
    

    def DirNumberAliasLookupandSync(self, **args):
        """
        UpdateDirNumberAliasLookupandSync parameters
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
        try:
            resp = self.client.updateDirNumberAliasLookupandSync(**args)
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
            print(f"AXL error updateDirNumberAliasLookupandSync: ", str(err), file=sys.stderr)
            return False
    

    def AdvertisedPatterns(self, **args):
        """
        UpdateAdvertisedPatterns parameters
        :param description: description
	:param newPattern: newPattern
	:param patternType: patternType
	:param hostedRoutePSTNRule: hostedRoutePSTNRule
	:param pstnFailStrip: pstnFailStrip
	:param pstnFailPrepend: pstnFailPrepend
	:return: API Response message
        """
        try:
            resp = self.client.updateAdvertisedPatterns(**args)
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
            print(f"AXL error updateAdvertisedPatterns: ", str(err), file=sys.stderr)
            return False
    

    def BlockedLearnedPatterns(self, **args):
        """
        UpdateBlockedLearnedPatterns parameters
        :param description: description
	:param newPattern: newPattern
	:param prefix: prefix
	:param clusterId: clusterId
	:param patternType: patternType
	:return: API Response message
        """
        try:
            resp = self.client.updateBlockedLearnedPatterns(**args)
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
            print(f"AXL error updateBlockedLearnedPatterns: ", str(err), file=sys.stderr)
            return False
    

    def CCAProfiles(self, **args):
        """
        UpdateCCAProfiles parameters
        :param newCcaId: newCcaId
	:param primarySoftSwitchId: primarySoftSwitchId
	:param secondarySoftSwitchId: secondarySoftSwitchId
	:param objectClass: objectClass
	:param subscriberType: subscriberType
	:param sipAliasSuffix: sipAliasSuffix
	:param sipUserNameSuffix: sipUserNameSuffix
	:return: API Response message
        """
        try:
            resp = self.client.updateCCAProfiles(**args)
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
            print(f"AXL error updateCCAProfiles: ", str(err), file=sys.stderr)
            return False
    

    def UniversalDeviceTemplate(self, **args):
        """
        UpdateUniversalDeviceTemplate parameters
        :param newName: newName
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
        try:
            resp = self.client.updateUniversalDeviceTemplate(**args)
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
            print(f"AXL error updateUniversalDeviceTemplate: ", str(err), file=sys.stderr)
            return False
    

    def UserProfileProvision(self, **args):
        """
        UpdateUserProfileProvision parameters
        :param newName: newName
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
        try:
            resp = self.client.updateUserProfileProvision(**args)
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
            print(f"AXL error updateUserProfileProvision: ", str(err), file=sys.stderr)
            return False
    

    def PresenceRedundancyGroup(self, **args):
        """
        UpdatePresenceRedundancyGroup parameters
        :param newName: newName
	:param description: description
	:param server1: server1
	:param server2: server2
	:param haEnabled: haEnabled
	:return: API Response message
        """
        try:
            resp = self.client.updatePresenceRedundancyGroup(**args)
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
            print(f"AXL error updatePresenceRedundancyGroup: ", str(err), file=sys.stderr)
            return False
    

    def WifiHotspot(self, **args):
        """
        UpdateWifiHotspot parameters
        :param newName: newName
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
        try:
            resp = self.client.updateWifiHotspot(**args)
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
            print(f"AXL error updateWifiHotspot: ", str(err), file=sys.stderr)
            return False
    

    def WlanProfileGroup(self, **args):
        """
        UpdateWlanProfileGroup parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateWlanProfileGroup(**args)
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
            print(f"AXL error updateWlanProfileGroup: ", str(err), file=sys.stderr)
            return False
    

    def WLANProfile(self, **args):
        """
        UpdateWLANProfile parameters
        :param newName: newName
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
        try:
            resp = self.client.updateWLANProfile(**args)
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
            print(f"AXL error updateWLANProfile: ", str(err), file=sys.stderr)
            return False
    

    def UniversalLineTemplate(self, **args):
        """
        UpdateUniversalLineTemplate parameters
        :param newName: newName
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
        try:
            resp = self.client.updateUniversalLineTemplate(**args)
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
            print(f"AXL error updateUniversalLineTemplate: ", str(err), file=sys.stderr)
            return False
    

    def NetworkAccessProfile(self, **args):
        """
        UpdateNetworkAccessProfile parameters
        :param newName: newName
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
        try:
            resp = self.client.updateNetworkAccessProfile(**args)
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
            print(f"AXL error updateNetworkAccessProfile: ", str(err), file=sys.stderr)
            return False
    

    def HttpProfile(self, **args):
        """
        UpdateHttpProfile parameters
        :param newName: newName
	:param userName: userName
	:param password: password
	:param requestTimeout: requestTimeout
	:param retryCount: retryCount
	:param webServiceRootUri: webServiceRootUri
	:return: API Response message
        """
        try:
            resp = self.client.updateHttpProfile(**args)
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
            print(f"AXL error updateHttpProfile: ", str(err), file=sys.stderr)
            return False
    

    def ElinGroup(self, **args):
        """
        UpdateElinGroup parameters
        :param newName: newName
	:param description: description
	:return: API Response message
        """
        try:
            resp = self.client.updateElinGroup(**args)
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
            print(f"AXL error updateElinGroup: ", str(err), file=sys.stderr)
            return False
    

    def SecureConfig(self, **args):
        """
        UpdateSecureConfig parameters
        :param value: value
	:return: API Response message
        """
        try:
            resp = self.client.updateSecureConfig(**args)
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
            print(f"AXL error updateSecureConfig: ", str(err), file=sys.stderr)
            return False
    

    def InfrastructureDevice(self, **args):
        """
        UpdateInfrastructureDevice parameters
        :param newName: newName
	:param ipv4Address: ipv4Address
	:param ipv6Address: ipv6Address
	:param bssidWithMask: bssidWithMask
	:param wapLocation: wapLocation
	:param isActive: isActive
	:return: API Response message
        """
        try:
            resp = self.client.updateInfrastructureDevice(**args)
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
            print(f"AXL error updateInfrastructureDevice: ", str(err), file=sys.stderr)
            return False
    

    def LdapSearch(self, **args):
        """
        UpdateLdapSearch parameters
        :param enableDirectorySearch: enableDirectorySearch
	:param distinguishedName: distinguishedName
	:param password: password
	:param userSearchBase1: userSearchBase1
	:param userSearchBase2: userSearchBase2
	:param userSearchBase3: userSearchBase3
	:param ldapFilterForUser: ldapFilterForUser
	:param ldapFilterForGroups: ldapFilterForGroups
	:param enableRecursiveSearch: enableRecursiveSearch
	:param primary: primary
	:param secondary: secondary
	:param tertiary: tertiary
	:return: API Response message
        """
        try:
            resp = self.client.updateLdapSearch(**args)
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
            print(f"AXL error updateLdapSearch: ", str(err), file=sys.stderr)
            return False
    

    def WirelessAccessPointControllers(self, **args):
        """
        UpdateWirelessAccessPointControllers parameters
        :param newName: newName
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
        try:
            resp = self.client.updateWirelessAccessPointControllers(**args)
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
            print(f"AXL error updateWirelessAccessPointControllers: ", str(err), file=sys.stderr)
            return False
    

    def DeviceDefaults(self, **args):
        """
        UpdateDeviceDefaults parameters
        :param LoadInformation: LoadInformation
	:param InactiveLoadInformation: InactiveLoadInformation
	:param DevicePoolName: DevicePoolName
	:param PhoneButtonTemplate: PhoneButtonTemplate
	:param VersionStamp: VersionStamp
	:param PreferActCodeOverAutoReg: PreferActCodeOverAutoReg
	:return: API Response message
        """
        try:
            resp = self.client.updateDeviceDefaults(**args)
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
            print(f"AXL error updateDeviceDefaults: ", str(err), file=sys.stderr)
            return False
    

    def MraServiceDomain(self, **args):
        """
        UpdateMraServiceDomain parameters
        :param newName: newName
	:param isDefault: isDefault
	:param serviceDomains: serviceDomains
	:return: API Response message
        """
        try:
            resp = self.client.updateMraServiceDomain(**args)
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
            print(f"AXL error updateMraServiceDomain: ", str(err), file=sys.stderr)
            return False
    

    def CiscoCloudOnboarding(self, **args):
        """
        UpdateCiscoCloudOnboarding parameters
        :param voucherExists: voucherExists
	:param enablePushNotifications: enablePushNotifications
	:param enableHttpProxy: enableHttpProxy
	:param httpProxyAddress: httpProxyAddress
	:param proxyUsername: proxyUsername
	:param proxyPassword: proxyPassword
	:param enableTrustCACertificate: enableTrustCACertificate
	:param allowAnalyticsCollection: allowAnalyticsCollection
	:param enableTroubleshooting: enableTroubleshooting
	:param alarmSendEncryptedData: alarmSendEncryptedData
	:param orgId: orgId
	:param serviceAddress: serviceAddress
	:param orgName: orgName
	:param enableGDSCommunication: enableGDSCommunication
	:param mraActivationDomain: mraActivationDomain
	:return: API Response message
        """
        try:
            resp = self.client.updateCiscoCloudOnboarding(**args)
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
            print(f"AXL error updateCiscoCloudOnboarding: ", str(err), file=sys.stderr)
            return False
    

    def DoAuthenticateUser(self, **args):
        """
        DoAuthenticateUser parameters
        :param userid: userid
	:return: API Response message
        """
        try:
            resp = self.client.updateenticateUser(**args)
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
            print(f"AXL error updateenticateUser: ", str(err), file=sys.stderr)
            return False
    

    def DoDeviceLogin(self, **args):
        """
        DoDeviceLogin parameters
        :param deviceName: deviceName
	:param loginDuration: loginDuration
	:param profileName: profileName
	:param userId: userId
	:return: API Response message
        """
        try:
            resp = self.client.updateceLogin(**args)
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
            print(f"AXL error updateceLogin: ", str(err), file=sys.stderr)
            return False
    

    def DoDeviceLogout(self, **args):
        """
        DoDeviceLogout parameters
        :param deviceName: deviceName
	:return: API Response message
        """
        try:
            resp = self.client.updateceLogout(**args)
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
            print(f"AXL error updateceLogout: ", str(err), file=sys.stderr)
            return False
    

    def DoDeviceReset(self, **args):
        """
        DoDeviceReset parameters
        :param deviceName: deviceName
	:return: API Response message
        """
        try:
            resp = self.client.updateceReset(**args)
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
            print(f"AXL error updateceReset: ", str(err), file=sys.stderr)
            return False
    

    def Mobility(self, **args):
        """
        UpdateMobility parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateMobility(**args)
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
            print(f"AXL error updateMobility: ", str(err), file=sys.stderr)
            return False
    

    def EnterprisePhoneConfig(self, **args):
        """
        UpdateEnterprisePhoneConfig parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateEnterprisePhoneConfig(**args)
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
            print(f"AXL error updateEnterprisePhoneConfig: ", str(err), file=sys.stderr)
            return False
    

    def LdapSystem(self, **args):
        """
        UpdateLdapSystem parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateLdapSystem(**args)
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
            print(f"AXL error updateLdapSystem: ", str(err), file=sys.stderr)
            return False
    

    def LdapAuthentication(self, **args):
        """
        UpdateLdapAuthentication parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateLdapAuthentication(**args)
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
            print(f"AXL error updateLdapAuthentication: ", str(err), file=sys.stderr)
            return False
    

    def ImeFeatureConfig(self, **args):
        """
        UpdateImeFeatureConfig parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateImeFeatureConfig(**args)
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
            print(f"AXL error updateImeFeatureConfig: ", str(err), file=sys.stderr)
            return False
    

    def FallbackFeatureConfig(self, **args):
        """
        UpdateFallbackFeatureConfig parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateFallbackFeatureConfig(**args)
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
            print(f"AXL error updateFallbackFeatureConfig: ", str(err), file=sys.stderr)
            return False
    

    def ImeLearnedRoutes(self, **args):
        """
        UpdateImeLearnedRoutes parameters
        :param adminEnabled: adminEnabled
	:return: API Response message
        """
        try:
            resp = self.client.updateImeLearnedRoutes(**args)
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
            print(f"AXL error updateImeLearnedRoutes: ", str(err), file=sys.stderr)
            return False
    

    def DoLdapSync(self, **args):
        """
        DoLdapSync parameters
        :param sync: sync
	:return: API Response message
        """
        try:
            resp = self.client.updateSync(**args)
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
            print(f"AXL error updateSync: ", str(err), file=sys.stderr)
            return False
    

    def SoftKeySet(self, **args):
        """
        UpdateSoftKeySet parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateSoftKeySet(**args)
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
            print(f"AXL error updateSoftKeySet: ", str(err), file=sys.stderr)
            return False
    

    def DoRemoteCluster(self, **args):
        """
        DoUpdateRemoteCluster parameters
        :param server: server
	:param clusterId: clusterId
	:return: API Response message
        """
        try:
            resp = self.client.updateteRemoteCluster(**args)
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
            print(f"AXL error updateteRemoteCluster: ", str(err), file=sys.stderr)
            return False
    

    def SyslogConfiguration(self, **args):
        """
        UpdateSyslogConfiguration parameters
        :param alarmConfigs: alarmConfigs
	:param EndPointAlarm: EndPointAlarm
	:return: API Response message
        """
        try:
            resp = self.client.updateSyslogConfiguration(**args)
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
            print(f"AXL error updateSyslogConfiguration: ", str(err), file=sys.stderr)
            return False
    

    def InterClusterDirectoryUri(self, **args):
        """
        UpdateInterClusterDirectoryUri parameters
        :param exchangeDirectoryUri: exchangeDirectoryUri
	:param routeString: routeString
	:return: API Response message
        """
        try:
            resp = self.client.updateInterClusterDirectoryUri(**args)
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
            print(f"AXL error updateInterClusterDirectoryUri: ", str(err), file=sys.stderr)
            return False
    

    def IlsConfig(self, **args):
        """
        UpdateIlsConfig parameters
        :param role: role
	:param registrationServer: registrationServer
	:param activateIls: activateIls
	:param synchronizeClustersEvery: synchronizeClustersEvery
	:param activatedServers: activatedServers
	:param deactivatedServers: deactivatedServers
	:param useTls: useTls
	:param enableUsePassword: enableUsePassword
	:param usePassword: usePassword
	:return: API Response message
        """
        try:
            resp = self.client.updateIlsConfig(**args)
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
            print(f"AXL error updateIlsConfig: ", str(err), file=sys.stderr)
            return False
    

    def SNMPCommunityString(self, **args):
        """
        UpdateSNMPCommunityString parameters
        :param communityName: communityName
	:param newValues: newValues
	:return: API Response message
        """
        try:
            resp = self.client.updateSNMPCommunityString(**args)
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
            print(f"AXL error updateSNMPCommunityString: ", str(err), file=sys.stderr)
            return False
    

    def SNMPUser(self, **args):
        """
        UpdateSNMPUser parameters
        :param user: user
	:return: API Response message
        """
        try:
            resp = self.client.updateSNMPUser(**args)
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
            print(f"AXL error updateSNMPUser: ", str(err), file=sys.stderr)
            return False
    

    def SNMPMIB2List(self, **args):
        """
        UpdateSNMPMIB2List parameters
        :param sysLocation: sysLocation
	:param sysContact: sysContact
	:return: API Response message
        """
        try:
            resp = self.client.updateSNMPMIB2List(**args)
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
            print(f"AXL error updateSNMPMIB2List: ", str(err), file=sys.stderr)
            return False
    

    def CcdFeatureConfig(self, **args):
        """
        UpdateCcdFeatureConfig parameters
        :param ccdParam: ccdParam
	:return: API Response message
        """
        try:
            resp = self.client.updateCcdFeatureConfig(**args)
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
            print(f"AXL error updateCcdFeatureConfig: ", str(err), file=sys.stderr)
            return False
    

    def BillingServer(self, **args):
        """
        UpdateBillingServer parameters
        :param uuid: uuid
	:param userId: userId
	:param password: password
	:param resendOnFailure: resendOnFailure
	:param billingServerProtocol: billingServerProtocol
	:return: API Response message
        """
        try:
            resp = self.client.updateBillingServer(**args)
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
            print(f"AXL error updateBillingServer: ", str(err), file=sys.stderr)
            return False
    

    def RoutePartitionsForLearnedPatterns(self, **args):
        """
        UpdateRoutePartitionsForLearnedPatterns parameters
        :param partitionForEnterpriseANo: partitionForEnterpriseANo
	:param partitionForE164ANo: partitionForE164ANo
	:param partitionForEnterprisePatterns: partitionForEnterprisePatterns
	:param partitionForE164Pattern: partitionForE164Pattern
	:param markLearnedEntAltNumbers: markLearnedEntAltNumbers
	:param markLearnedE164AltNumbers: markLearnedE164AltNumbers
	:param markFixedLengthEntPatterns: markFixedLengthEntPatterns
	:param markVariableLengthEntPatterns: markVariableLengthEntPatterns
	:param markFixedLengthE164Patterns: markFixedLengthE164Patterns
	:param markVariableLengthE164Patterns: markVariableLengthE164Patterns
	:return: API Response message
        """
        try:
            resp = self.client.updateRoutePartitionsForLearnedPatterns(**args)
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
            print(f"AXL error updateRoutePartitionsForLearnedPatterns: ", str(err), file=sys.stderr)
            return False
    

    def LocalRouteGroup(self, **args):
        """
        UpdateLocalRouteGroup parameters
        :param localRouteGroup: localRouteGroup
	:return: API Response message
        """
        try:
            resp = self.client.updateLocalRouteGroup(**args)
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
            print(f"AXL error updateLocalRouteGroup: ", str(err), file=sys.stderr)
            return False
    

    def PageLayoutPreferences(self, **args):
        """
        UpdatePageLayoutPreferences parameters
        :param pageName: pageName
	:param pageSections: pageSections
	:return: API Response message
        """
        try:
            resp = self.client.updatePageLayoutPreferences(**args)
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
            print(f"AXL error updatePageLayoutPreferences: ", str(err), file=sys.stderr)
            return False
    

    def CredentialPolicyDefault(self, **args):
        """
        UpdateCredentialPolicyDefault parameters
        :param credentialUser: credentialUser
	:param credentialType: credentialType
	:param credPolicyName: credPolicyName
	:param newCredPolicyName: newCredPolicyName
	:param credentials: credentials
	:param confirmCredentials: confirmCredentials
	:param credUserCantChange: credUserCantChange
	:param credUserMustChange: credUserMustChange
	:param credDoesNotExpire: credDoesNotExpire
	:return: API Response message
        """
        try:
            resp = self.client.updateCredentialPolicyDefault(**args)
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
            print(f"AXL error updateCredentialPolicyDefault: ", str(err), file=sys.stderr)
            return False
    

    def SelfProvisioning(self, **args):
        """
        UpdateSelfProvisioning parameters
        :param requireAuthentication: requireAuthentication
	:param allowAuthentication: allowAuthentication
	:param authenticationCode: authenticationCode
	:param ctiRoutePoint: ctiRoutePoint
	:param applicationUser: applicationUser
	:return: API Response message
        """
        try:
            resp = self.client.updateSelfProvisioning(**args)
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
            print(f"AXL error updateSelfProvisioning: ", str(err), file=sys.stderr)
            return False
    

    def DoChangeDNDStatus(self, **args):
        """
        DoChangeDNDStatus parameters
        :param dndStatus: dndStatus
	:return: API Response message
        """
        try:
            resp = self.client.updategeDNDStatus(**args)
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
            print(f"AXL error updategeDNDStatus: ", str(err), file=sys.stderr)
            return False
    

    def DoLicenseUsage(self, **args):
        """
        DoUpdateLicenseUsage parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateteLicenseUsage(**args)
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
            print(f"AXL error updateteLicenseUsage: ", str(err), file=sys.stderr)
            return False
    

    def DoServiceParametersReset(self, **args):
        """
        DoServiceParametersReset parameters
        :param processNodeName: processNodeName
	:param service: service
	:return: API Response message
        """
        try:
            resp = self.client.updateiceParametersReset(**args)
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
            print(f"AXL error updateiceParametersReset: ", str(err), file=sys.stderr)
            return False
    

    def DoEnterpriseParametersReset(self, **args):
        """
        DoEnterpriseParametersReset parameters
        :return: API Response message
        """
        try:
            resp = self.client.updaterpriseParametersReset(**args)
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
            print(f"AXL error updaterpriseParametersReset: ", str(err), file=sys.stderr)
            return False
    

    def DoSmartLicenseRegister(self, **args):
        """
        DoSmartLicenseRegister parameters
        :return: API Response message
        """
        try:
            resp = self.client.updatetLicenseRegister(**args)
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
            print(f"AXL error updatetLicenseRegister: ", str(err), file=sys.stderr)
            return False
    

    def DoSmartLicenseReRegister(self, **args):
        """
        DoSmartLicenseReRegister parameters
        :return: API Response message
        """
        try:
            resp = self.client.updatetLicenseReRegister(**args)
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
            print(f"AXL error updatetLicenseReRegister: ", str(err), file=sys.stderr)
            return False
    

    def DoSmartLicenseDeRegister(self, **args):
        """
        DoSmartLicenseDeRegister parameters
        :return: API Response message
        """
        try:
            resp = self.client.updatetLicenseDeRegister(**args)
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
            print(f"AXL error updatetLicenseDeRegister: ", str(err), file=sys.stderr)
            return False
    

    def DoSmartLicenseRenewAuthorization(self, **args):
        """
        DoSmartLicenseRenewAuthorization parameters
        :return: API Response message
        """
        try:
            resp = self.client.updatetLicenseRenewAuthorization(**args)
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
            print(f"AXL error updatetLicenseRenewAuthorization: ", str(err), file=sys.stderr)
            return False
    

    def DoSmartLicenseRenewRegistration(self, **args):
        """
        DoSmartLicenseRenewRegistration parameters
        :return: API Response message
        """
        try:
            resp = self.client.updatetLicenseRenewRegistration(**args)
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
            print(f"AXL error updatetLicenseRenewRegistration: ", str(err), file=sys.stderr)
            return False
    

    def DoSmartEntitlement(self, **args):
        """
        DoSmartEntitlement parameters
        :return: API Response message
        """
        try:
            resp = self.client.updatetEntitlement(**args)
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
            print(f"AXL error updatetEntitlement: ", str(err), file=sys.stderr)
            return False
    

    def DoSmartEntitlement(self, **args):
        """
        DoSmartEntitlement parameters
        :param return: return
	:return: API Response message
        """
        try:
            resp = self.client.updatetEntitlement(**args)
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
            print(f"AXL error updatetEntitlement: ", str(err), file=sys.stderr)
            return False
    

    def DoTransportSettings(self, **args):
        """
        DoUpdateTransportSettings parameters
        :return: API Response message
        """
        try:
            resp = self.client.updateteTransportSettings(**args)
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
            print(f"AXL error updateteTransportSettings: ", str(err), file=sys.stderr)
            return False
    

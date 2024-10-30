import sqlite3
import sys
from .CDROnDemand import *
try:
    import pandas as pd
except:
    print("Error importing Pandas for CDR", file=sys.stderr)
    print("<< pip3 install pandas >>", file=sys.stderr)


class CDR:
    _TABLE_NAME = None
    on_demand = None

    def __init__(self, ipaddr=None, username=None, passwd=None):
        if ipaddr and username and passwd:
            self.on_demand = CDROnDemand(ipaddr, username, passwd)

    def parse(self, db=None, csv=None, df=None, cdr=None, cmr=None, table="cdr_cdr", cmr_table="cdr_cmr"):
        if csv is None and cdr is not None:
            csv = cdr
        if csv is None and db is None and df is None:
            print("You must specify an Existing DB or a CSV or DataFrame object to import", file=sys.stderr)

        else:
            self._TABLE_NAME = table
            self._TABLE_CMR = cmr_table

            if db is not None:
                self._DB_NAME = db  # set name of DB File if not given
            else:
                if csv is not None:
                    self._DB_NAME = f"{csv}.sqlite"
                elif df is not None:
                    self._DB_NAME = f"DataFramesImport.sqlite"

            if csv is not None or df is not None:
                start = time.time()

                # convert CSV to Pandas DataFrame
                if csv is not None:
                    try:
                        dtypes = {"cdrRecordType": int,
                                  "globalCallID_callManagerId": int,
                                  "globalCallID_callId": int,
                                  "origLegCallIdentifier": int,
                                  "dateTimeOrigination": int,
                                  "origNodeId": int,
                                  "origSpan": int,
                                  "origIpAddr": int,
                                  "callingPartyNumber": str,
                                  "callingPartyUnicodeLoginUserID": str,
                                  "origCause_location": int,
                                  "origCause_value": int,
                                  "origPrecedenceLevel": int,
                                  "origMediaTransportAddress_IP": int,
                                  "origMediaTransportAddress_Port": int,
                                  "origMediaCap_payloadCapability": int,
                                  "origMediaCap_maxFramesPerPacket": int,
                                  "origMediaCap_g723BitRate": int,
                                  "origVideoCap_Codec": int,
                                  "origVideoCap_Bandwidth": int,
                                  "origVideoCap_Resolution": int,
                                  "origVideoTransportAddress_IP": int,
                                  "origVideoTransportAddress_Port": int,
                                  "origRSVPAudioStat": str,
                                  "origRSVPVideoStat": str,
                                  "destLegIdentifier": int,
                                  "destNodeId": int,
                                  "destSpan": int,
                                  "destIpAddr": int,
                                  "originalCalledPartyNumber": str,
                                  "finalCalledPartyNumber": str,
                                  "finalCalledPartyUnicodeLoginUserID": str,
                                  "destCause_location": int,
                                  "destCause_value": int,
                                  "destPrecedenceLevel": int,
                                  "destMediaTransportAddress_IP": int,
                                  "destMediaTransportAddress_Port": int,
                                  "destMediaCap_payloadCapability": int,
                                  "destMediaCap_maxFramesPerPacket": int,
                                  "destMediaCap_g723BitRate": int,
                                  "destVideoCap_Codec": int,
                                  "destVideoCap_Bandwidth": int,
                                  "destVideoCap_Resolution": int,
                                  "destVideoTransportAddress_IP": int,
                                  "destVideoTransportAddress_Port": int,
                                  "destRSVPAudioStat": str,
                                  "destRSVPVideoStat": str,
                                  "dateTimeConnect": int,
                                  "dateTimeDisconnect": int,
                                  "lastRedirectDn": str,
                                  "pkid": str,
                                  "originalCalledPartyNumberPartition": str,
                                  "callingPartyNumberPartition": str,
                                  "finalCalledPartyNumberPartition": str,
                                  "lastRedirectDnPartition": str,
                                  "duration": int,
                                  "origDeviceName": str,
                                  "destDeviceName": str,
                                  "origCallTerminationOnBehalfOf": int,
                                  "destCallTerminationOnBehalfOf": int,
                                  "origCalledPartyRedirectOnBehalfOf": int,
                                  "lastRedirectRedirectOnBehalfOf": int,
                                  "origCalledPartyRedirectReason": int,
                                  "lastRedirectRedirectReason": int,
                                  "destConversationId": int,
                                  "globalCallId_ClusterID": str,
                                  "joinOnBehalfOf": int,
                                  "comment": str,
                                  "authCodeDescription": str,
                                  "authorizationLevel": int,
                                  "clientMatterCode": str,
                                  "origDTMFMethod": int,
                                  "destDTMFMethod": int,
                                  "callSecuredStatus": int,
                                  "origConversationId": int,
                                  "origMediaCap_Bandwidth": int,
                                  "destMediaCap_Bandwidth": int,
                                  "authorizationCodeValue": str,
                                  "outpulsedCallingPartyNumber": str,
                                  "outpulsedCalledPartyNumber": str,
                                  "origIpv4v6Addr": str,
                                  "destIpv4v6Addr": str,
                                  "origVideoCap_Codec_Channel2": int,
                                  "origVideoCap_Bandwidth_Channel2": int,
                                  "origVideoCap_Resolution_Channel2": int,
                                  "origVideoTransportAddress_IP_Channel2": int,
                                  "origVideoTransportAddress_Port_Channel2": int,
                                  "origVideoChannel_Role_Channel2": int,
                                  "destVideoCap_Codec_Channel2": int,
                                  "destVideoCap_Bandwidth_Channel2": int,
                                  "destVideoCap_Resolution_Channel2": int,
                                  "destVideoTransportAddress_IP_Channel2": int,
                                  "destVideoTransportAddress_Port_Channel2": int,
                                  "destVideoChannel_Role_Channel2": int,
                                  "incomingProtocolID": int,
                                  "incomingProtocolCallRef": str,
                                  "outgoingProtocolID": int,
                                  "outgoingProtocolCallRef": str,
                                  "currentRoutingReason": int,
                                  "origRoutingReason": int,
                                  "lastRedirectingRoutingReason": int,
                                  "huntPilotDN": str,
                                  "huntPilotPartition": str,
                                  "calledPartyPatternUsage": int,
                                  "outpulsedOriginalCalledPartyNumber": str,
                                  "outpulsedLastRedirectingNumber": str,
                                  "wasCallQueued": int,
                                  "totalWaitTimeInQueue": int,
                                  "callingPartyNumber_uri": str,
                                  "originalCalledPartyNumber_uri": str,
                                  "finalCalledPartyNumber_uri": str,
                                  "lastRedirectDn_uri": str,
                                  "mobileCallingPartyNumber": str,
                                  "finalMobileCalledPartyNumber": str,
                                  "origMobileDeviceName": str,
                                  "destMobileDeviceName": str,
                                  "origMobileCallDuration": int,
                                  "destMobileCallDuration": int,
                                  "mobileCallType": int,
                                  "originalCalledPartyPattern": str,
                                  "finalCalledPartyPattern": str,
                                  "lastRedirectingPartyPattern": str,
                                  "huntPilotPattern": str}
                        df = pd.concat(pd.read_csv(csv, dtype=dtypes, iterator=True, chunksize=8000))

                    except Exception as err:
                        print(f"Error converting CDR CSV to DataFrame - {err}", file=sys.stderr)
                    else:
                        self.create_table()  # create and load table based on CSV
                        self.load_cdr_table(df)  # create and load table based on DataFrame
                        print(f"\t... CDR DB Created in {(time.time() - start)} sec.")

            if cmr is not None:
                start = time.time()
                try:
                    df = pd.concat(pd.read_csv(cmr, iterator=True, chunksize=8000))
                except Exception as err:
                    print(f"Error converting CMR CSV to DataFrame - {err}", file=sys.stderr)
                else:
                    self.load_cmr_table(df)  # create and load table based on DataFrame
                    print(f"\t... CMR DB Created in {(time.time() - start)} sec.")

    def change_table(self, table):
        self._TABLE_NAME = table

    def create_table(self):
        _cdr_db = sqlite3.connect(self._DB_NAME)
        sql_cdr = f"""CREATE TABLE {self._TABLE_NAME}(
					cdrRecordType INTEGER NULL,
					globalCallID_callManagerId INTEGER NULL,
					globalCallID_callId INTEGER PRIMARY KEY,
					origLegCallIdentifier INTEGER NULL,
					dateTimeOrigination INTEGER NULL,
					origNodeId INTEGER NULL,
					origSpan INTEGER NULL,
					origIpAddr INTEGER NULL,
					callingPartyNumber VARCHAR(50) NULL,
					callingPartyUnicodeLoginUserID VARCHAR(50) NULL,
					origCause_location INTEGER NULL,
					origCause_value INTEGER NULL,
					origPrecedenceLevel INTEGER NULL,
					origMediaTransportAddress_IP INTEGER NULL,
					origMediaTransportAddress_Port INTEGER NULL,
					origMediaCap_payloadCapability INTEGER NULL,
					origMediaCap_maxFramesPerPacket INTEGER NULL,
					origMediaCap_g723BitRate INTEGER NULL,
					origVideoCap_Codec INTEGER NULL,
					origVideoCap_Bandwidth INTEGER NULL,
					origVideoCap_Resolution INTEGER NULL,
					origVideoTransportAddress_IP INTEGER NULL,
					origVideoTransportAddress_Port INTEGER NULL,
					origRSVPAudioStat VARCHAR(64) NULL,
					origRSVPVideoStat VARCHAR(64) NULL,
					destLegIdentifier INTEGER NULL,
					destNodeId INTEGER NULL,
					destSpan INTEGER NULL,
					destIpAddr INTEGER NULL,
					originalCalledPartyNumber VARCHAR(50) NULL,
					finalCalledPartyNumber VARCHAR(50) NULL,
					finalCalledPartyUnicodeLoginUserID VARCHAR(50) NULL,
					destCause_location INTEGER NULL,
					destCause_value INTEGER NULL,
					destPrecedenceLevel INTEGER NULL,
					destMediaTransportAddress_IP INTEGER NULL,
					destMediaTransportAddress_Port INTEGER NULL,
					destMediaCap_payloadCapability INTEGER NULL,
					destMediaCap_maxFramesPerPacket INTEGER NULL,
					destMediaCap_g723BitRate INTEGER NULL,
					destVideoCap_Codec INTEGER NULL,
					destVideoCap_Bandwidth INTEGER NULL,
					destVideoCap_Resolution INTEGER NULL,
					destVideoTransportAddress_IP INTEGER NULL,
					destVideoTransportAddress_Port INTEGER NULL,
					destRSVPAudioStat VARCHAR(64) NULL,
					destRSVPVideoStat VARCHAR(64) NULL,
					dateTimeConnect INTEGER NULL,
					dateTimeDisconnect INTEGER NULL,
					lastRedirectDn VARCHAR(50) NULL,
					pkid varchar(64) NULL,
					originalCalledPartyNumberPartition VARCHAR(50) NULL,
					callingPartyNumberPartition VARCHAR(50) NULL,
					finalCalledPartyNumberPartition VARCHAR(50) NULL,
					lastRedirectDnPartition VARCHAR(50) NULL,
					duration INTEGER NULL,
					origDeviceName VARCHAR(129) NULL,
					destDeviceName VARCHAR(129) NULL,
					origCallTerminationOnBehalfOf INTEGER NULL,
					destCallTerminationOnBehalfOf INTEGER NULL,
					origCalledPartyRedirectOnBehalfOf INTEGER NULL,
					lastRedirectRedirectOnBehalfOf INTEGER NULL,
					origCalledPartyRedirectReason INTEGER NULL,
					lastRedirectRedirectReason INTEGER NULL,
					destConversationId INTEGER NULL,
					globalCallId_ClusterID VARCHAR(50) NULL,
					joinOnBehalfOf INTEGER NULL,
					comment VARCHAR(2048) NULL,
					authCodeDescription VARCHAR(50) NULL,
					authorizationLevel INTEGER NULL,
					clientMatterCode VARCHAR(32) NULL,
					origDTMFMethod INTEGER NULL,
					destDTMFMethod INTEGER NULL,
					callSecuredStatus INTEGER NULL,
					origConversationId INTEGER NULL,
					origMediaCap_Bandwidth INTEGER NULL,
					destMediaCap_Bandwidth INTEGER NULL,
					authorizationCodeValue VARCHAR(32) NULL,
					outpulsedCallingPartyNumber VARCHAR(50) NULL,
					outpulsedCalledPartyNumber VARCHAR(50) NULL,
					origIpv4v6Addr VARCHAR(64) NULL,
					destIpv4v6Addr VARCHAR(64) NULL,
					origVideoCap_Codec_Channel2 INTEGER NULL,
					origVideoCap_Bandwidth_Channel2 INTEGER NULL,
					origVideoCap_Resolution_Channel2 INTEGER NULL,
					origVideoTransportAddress_IP_Channel2 INTEGER NULL,
					origVideoTransportAddress_Port_Channel2 INTEGER NULL,
					origVideoChannel_Role_Channel2 INTEGER NULL,
					destVideoCap_Codec_Channel2 INTEGER NULL,
					destVideoCap_Bandwidth_Channel2 INTEGER NULL,
					destVideoCap_Resolution_Channel2 INTEGER NULL,
					destVideoTransportAddress_IP_Channel2 INTEGER NULL,
					destVideoTransportAddress_Port_Channel2 INTEGER NULL,
					destVideoChannel_Role_Channel2 INTEGER NULL,
					incomingProtocolID INTEGER NULL,
					incomingProtocolCallRef VARCHAR(32) NULL,
					outgoingProtocolID INTEGER NULL,
					outgoingProtocolCallRef VARCHAR(32) NULL,
					currentRoutingReason INTEGER NULL,
					origRoutingReason INTEGER NULL,
					IncomingICID VARCHAR(50) NULL,
					IncomingOrigIOI VARCHAR(50) NULL,
					IncomingTermIOI VARCHAR(50) NULL,
					OutgoingICID VARCHAR(50) NULL,
					OutgoingOrigIOI VARCHAR(50) NULL,
					OutgoingTermIOI VARCHAR(50) NULL,
					lastRedirectingRoutingReason INTEGER NULL,
					huntPilotDN VARCHAR(50) NULL,
					huntPilotPartition VARCHAR(50) NULL,
					calledPartyPatternUsage INTEGER NULL,
					outpulsedOriginalCalledPartyNumber VARCHAR(50) NULL,
					outpulsedLastRedirectingNumber VARCHAR(50) NULL,
					wasCallQueued INTEGER NULL,
					totalWaitTimeInQueue INTEGER NULL,
					callingPartyNumber_uri VARCHAR(254) NULL,
					originalCalledPartyNumber_uri VARCHAR(254) NULL,
					finalCalledPartyNumber_uri VARCHAR(254) NULL,
					lastRedirectDn_uri VARCHAR(254) NULL,
					mobileCallingPartyNumber VARCHAR(50) NULL,
					finalMobileCalledPartyNumber VARCHAR(50) NULL,
					origMobileDeviceName VARCHAR(50) NULL,
					destMobileDeviceName VARCHAR(50) NULL,
					origMobileCallDuration INTEGER NULL,
					destMobileCallDuration INTEGER NULL,
					mobileCallType INTEGER NULL,
					originalCalledPartyPattern VARCHAR(50) NULL,
					finalCalledPartyPattern VARCHAR(50) NULL,
					lastRedirectingPartyPattern VARCHAR(50) NULL,
					huntPilotPattern VARCHAR(50) NULL,
					origDeviceType VARCHAR(100) NULL,
					destDeviceType VARCHAR(100) NULL,
					origDeviceSessionID VARCHAR(128) NULL,
					destDeviceSessionID VARCHAR(128) NULL
					);"""
        sql_cmr = f"""CREATE TABLE {self._TABLE_CMR} (
						cdrRecordType INTEGER ,
						globalCallID_callManagerId INTEGER ,
						globalCallId_callId INTEGER PRIMARY KEY,
						nodeId INTEGER ,
						directoryNumber INTEGER ,
						callIdentifier INTEGER ,
						dateTimeStamp INTEGER ,
						numberPacketsSent INTEGER ,
						numberOctetsSent INTEGER ,
						numberPacketsReceived INTEGER ,
						numberOctetsReceived INTEGER ,
						numberPacketsLost INTEGER ,
						jitter INTEGER ,
						latency INTEGER ,
						pkid VARCHAR(128),
						directoryNumberPartition VARCHAR(128),
						globalCallId_ClusterId VARCHAR(128),
						deviceName VARCHAR(128),
						varVQMetrics VARCHAR(128),
						duration INTEGER ,
						videoContentType VARCHAR(128),
						videoDuration INTEGER ,
						numberVideoPacketsSent INTEGER ,
						numberVideoOctetsSent INTEGER ,
						numberVideoPacketsReceived INTEGER ,
						numberVideoOctetsReceived INTEGER ,
						numberVideoPacketsLost INTEGER ,
						videoAverageJitter INTEGER ,
						videoRoundTripTime INTEGER ,
						videoOneWayDelay VARCHAR(128),
						videoTransmissionMetrics VARCHAR(128),
						videoReceptionMetrics VARCHAR(128),
						videoContentType_channel2 VARCHAR(128),
						videoDuration_channel2 INTEGER ,
						numberVideoPacketsSent_channel2 INTEGER ,
						numberVideoOctetsSent_channel2 INTEGER ,
						numberVideoPacketsReceived_channel2 INTEGER ,
						numberVideoOctetsReceived_channel2 INTEGER ,
						numberVideoPacketsLost_channel2 INTEGER ,
						videoAverageJitter_channel2 INTEGER ,
						videoRoundTripTime_channel2 INTEGER ,
						videoOneWayDelay_channel2 INTEGER ,
						videoReceptionMetrics_channel2 VARCHAR(128),
						videoTransmissionMetrics_channel2 VARCHAR(128),

						);"""
        # Build SQLite Table
        print("Building SQLite DB from CSV...")
        try:
            _cdr_db.execute(sql_cdr)
        except Exception as err:
            print(err, file=sys.stderr)
        else:
            sql_index = "CREATE INDEX cdr_index ON cdr_cdr(dateTimeOrigination, callingPartyNumber, destDeviceName, finalCalledPartyNumber, finalCalledPartyPattern, origDeviceName, originalCalledPartyNumber, originalCalledPartyPattern)"
            _cdr_db.execute(sql_index)

        try:
            _cdr_db.execute(sql_cmr)

        except Exception as err:
            print(err, file=sys.stderr)

        _cdr_db.commit()
        _cdr_db.close()
        return True

    def load_cdr_table(self, cdr_df):
        _cdr_db = sqlite3.connect(self._DB_NAME)

        print("Loading CDR Table")
        try:
            cdr_df.to_sql(self._TABLE_NAME, _cdr_db, if_exists='append', index=False)

        except Exception as err:
            print(err, file=sys.stderr)
            _cdr_db.close()
            return False

        else:
            # remove any 0 numbers to keep it from working forever
            _cdr_db.execute(
                f"DELETE FROM {self._TABLE_NAME} WHERE dateTimeOrigination <= 0 OR dateTimeOrigination IS NULL")

        _cdr_db.commit()
        _cdr_db.close()
        return True

    def load_cmr_table(self, cdr_df):
        _cdr_db = sqlite3.connect(self._DB_NAME)

        print("Loading CMR Table")
        try:
            cdr_df.to_sql(self._TABLE_CMR, _cdr_db, if_exists='append', index=False)

        except Exception as err:
            print(err, file=sys.stderr)
            _cdr_db.close()
            return False

        _cdr_db.commit()
        _cdr_db.close()
        return True

    # Simple query returned as List of Tuples
    def query(self, sql, return_type="dict"):
        _cdr_db = sqlite3.connect(self._DB_NAME)

        # if select statement then start cursor
        if sql.lower().startswith("select"):
            try:
                results = pd.read_sql_query(sql, _cdr_db)

            except Exception as err:
                print(f"SQL Error: {err} - {sql}", file=sys.stderr)

            else:
                _cdr_db.commit()
                _cdr_db.close()

                if return_type == "dict":
                    return results.to_dict(orient='records')

                elif return_type == "df":
                    return results

        # if not select then commit the change and close
        else:
            # loop in case its having IO issus writting
            try:
                _cdr_db.execute(sql)

            except Exception as err:
                print(f"SQL Error: {err} - {sql}", file=sys.stderr)
                _cdr_db.close()
                return False

            else:
                _cdr_db.commit()
                _cdr_db.close()
                return True

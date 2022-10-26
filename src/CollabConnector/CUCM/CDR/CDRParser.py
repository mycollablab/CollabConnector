#! /usr/bin/python3

############################################################################
## Jon Snipes and Friends ##################################################
## CDRParser ###############################################################
## working from CUCM CDR export as a CSV imports full CSV into SQLite3 DB ##
## get_concurrent_call() function count max concurrent calls throughout ####
############################################################################

import time
import sqlite3
import sys
from multiprocessing import cpu_count
import threading


class Parse():
	class ProgressBar():
		progress_bar_scale = .7
		progress_bar_length = int(100 * progress_bar_scale)
		completed_bar_char = "█"
		incomplete_bar_char = "▒"
		completion_message = "Completed!"

		def __init__(self, total):
			self.total = total

		def progress(self, current):
			# print out our progress bar
			percent_complete =  round(current/self.total * 100)
			bars_of_completion = int(percent_complete * self.progress_bar_scale)
			bars_to_be_completed = self.progress_bar_length - bars_of_completion
			print(f'\r{self.completed_bar_char * bars_of_completion}{self.incomplete_bar_char * bars_to_be_completed} {percent_complete}%', end='')

	def __init__(self, db=None, csv=None, df=None, cdr=None, cmr=None, table="cdr_cdr", cmr_table="cdr_cmr"):
		if csv is None and cdr is not None:
			csv = cdr
		if csv is None and db is None and df is None:
			print("You must specify an Existing DB or a CSV or DataFrame object to import", file=sys.stderr)

		else:
			self._TABLE_NAME = table
			self._TABLE_CMR = cmr_table

			if db is not None:
				self._DB_NAME = db # set name of DB File if not given
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
						self.load_cdr_table(df) # create and load table based on DataFrame
						print(f"\t... CDR DB Created in {(time.time() - start)} sec.")

			if cmr is not None:
				start = time.time()
				try:
					df = pd.concat(pd.read_csv(cmr, iterator=True, chunksize=8000))
				except Exception as err:
					print(f"Error converting CMR CSV to DataFrame - {err}", file=sys.stderr)
				else:
					self.load_cmr_table(df) # create and load table based on DataFrame
					print(f"\t... CMR DB Created in {(time.time() - start)} sec.")

	def change_table(self, table):
		self._TABLE_NAME = table

	def create_table(self):
		_cdr_db = sqlite3.connect(self._DB_NAME)
		sql_cdr = f"""CREATE TABLE {self._TABLE_NAME}(
					cdrRecordType INTEGER NULL,
					globalCallID_callManagerId INTEGER NULL,
					globalCallID_callId INTEGER NULL,
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
						globalCallId_callId INTEGER ,
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
			_cdr_db.execute(f"DELETE FROM {self._TABLE_NAME} WHERE dateTimeOrigination <= 0 OR dateTimeOrigination IS NULL")

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
	def query(self,sql,return_type="dict"):
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

	# Count calls per second
	def call_rate(self,rate=1, max_return=5,start=None,stop=None,deviceName=None,origDeviceName='%',destDeviceName='%',return_type="dict"):
		# set min/max datetime from CDR if not provided
		if start is None:
			start = self.query(f"SELECT MIN(dateTimeOrigination) AS min FROM {self._TABLE_NAME}")[0]['min']
		if stop is None:
			stop = self.query(f"SELECT max(dateTimeDisconnect) AS max FROM {self._TABLE_NAME}")[0]['max']


		if deviceName is not None:
			origDeviceName = deviceName
			destDeviceName = deviceName

		result = self.query(f"""SELECT COUNT(*) AS calls,(dateTimeOrigination / {rate}) as dateTimeOrigination
								FROM {self._TABLE_NAME}
								WHERE dateTimeOrigination BETWEEN {start} AND {stop}
								AND ( origDeviceName like "{origDeviceName}" OR destDeviceName like "{destDeviceName}" )
								GROUP BY dateTimeOrigination
								ORDER BY calls DESC
								LIMIT {max_return}
								""")
		if return_type == "dict":
			return result

		elif return_type == "df":
			return pd.DataFrame(result)

	# parse CDR for concurrent peak time for a time frame and endpoint
	def get_concurrent_calls(self, max_return=5,start=None,stop=None,deviceName=None,origDeviceName='%',destDeviceName='%',jm_parser=False, preserve_answers=True,progress=True,SAMPLE_RATE=1,SAMPLE_RANGE=3600,THREADS=round(cpu_count()/2),return_type="dict"):
		_SAMPLE_RATE = SAMPLE_RATE # Second Interval within sample range - Not valid when usinhg jm_parser
		_SAMPLE_RANGE = SAMPLE_RANGE # how large of a window do you want to get results for "all" or "*" to search full range (fastest)
		_THREADS = int(THREADS) # How many thread to use when multithreading default set to half on CPU Count

		# set min/max datetime from CDR if not provided
		if start is None:
			start = int(self.query(f"SELECT MIN(dateTimeOrigination) AS min FROM {self._TABLE_NAME}")[0]['min'])
		if stop is None:
			stop = int(self.query(f"SELECT max(dateTimeDisconnect) AS max FROM {self._TABLE_NAME}")[0]['max'])
		if _SAMPLE_RANGE in ["*","all"]:
			_SAMPLE_RANGE = stop - start

		if deviceName is not None:
			origDeviceName = deviceName
			destDeviceName = deviceName

		# create temp table with only sorted dates to loop faster
		parse_time = int(time.time())
		while True: 
			create_dates_table = self.query(f"""CREATE TABLE cdr_dates_{parse_time}
					AS select DISTINCT origLegCallIdentifier, dateTimeOrigination, dateTimeDisconnect FROM {self._TABLE_NAME} 
					WHERE (origDeviceName LIKE "{origDeviceName}" OR destDeviceName LIKE "{destDeviceName}")
					AND (dateTimeOrigination <= {stop} AND dateTimeDisconnect >= {start})
					AND (duration > 0)
					ORDER BY dateTimeOrigination""")
			if create_dates_table is not False :
				break
			time.sleep(1)
			parse_time +=1

		self.query(f"CREATE TABLE cdr_concurrent_{parse_time} (hour int,count int,duration int,peakstart int,peakstop int)")
		print(f"Processing Time Range {start} - {stop} with {_THREADS}cpu")

		# build list with time range start times for threads
		current_time = start
		threads = []
		while current_time <= stop:
			t = threading.Thread(target=self.count_concurrent_calls,args=(current_time,parse_time,jm_parser,_SAMPLE_RANGE,_SAMPLE_RATE,))
			threads.append(t)

			#timeFrame.append(currentTime)
			current_time += _SAMPLE_RANGE
		
		thread_count = len(threads)

		# thread results getting 
		pb = self.ProgressBar(thread_count)
		# create and start threads for faster processing - based on calculated threads
		thread_loop = 0
		while thread_loop <= thread_count:
			# start threads
			thread_sub_loop = thread_loop
			while thread_sub_loop < thread_loop + _THREADS and thread_sub_loop < thread_count:
				threads[thread_sub_loop].start()
				thread_sub_loop += 1

			# wait for threads to finish
			thread_sub_loop = thread_loop
			while thread_sub_loop < thread_loop + _THREADS and thread_sub_loop < thread_count:
				threads[thread_sub_loop].join()
				thread_sub_loop += 1
			if progress: pb.progress(thread_loop) # update progress bar
			thread_loop += _THREADS

		if progress: pb.progress(thread_count)
		# get results
		result_sql = f"SELECT DATETIME(hour, 'unixepoch') AS hour,count,duration,DATETIME(peakstart, 'unixepoch') AS peakstart,DATETIME(peakstop, 'unixepoch') AS peakstop FROM cdr_concurrent_{parse_time} ORDER BY count DESC LIMIT {max_return}"
		if return_type == "dict":
			results = [f"cdr_dates_{parse_time}",self.query(result_sql)]
		
		elif return_type == "df":
			results = pd.read_sql_query(result_sql, _cdr_db)

		# Drop temp tables not used anymore
		self.query(f"DROP TABLE cdr_dates_{parse_time}")
		if not preserve_answers:
			self.query(f"DROP TABLE cdr_concurrent_{parse_time}")
		print()

		# return results from answers table with max ordered by call peak
		return results


	def jm_parser(self,records):
		###################################################################
		## Jacob Miller ###################################################
		## Fast Ass Method ################################################
		## Qickly finds  concurrent call count and times from a data set ##
		###################################################################
		cs,ce,ps,pe=[[] for _ in range(4)]
		cc=pc=0
		for r in records:
			ce.append(r[1]),ce.sort(),cs.append(r[0])
			for _ in ce:
				if r[0]<=ce[0]:break
				del ce[0],cs[0]
			if (cc:=len(ce))>pc:pc,pe,ps=cc,ce[:],cs[:]
		
		return [pc, ps[-1], ps[0] ]

	#Count concurrent calls within the hour based on orig/dest device
	def count_concurrent_calls(self, hour, parse_time, jm_parser, _SAMPLE_RANGE, _SAMPLE_RATE):
		db = sqlite3.connect(self._DB_NAME)
		cur = db.cursor()
		hour_max = 0
		peak_start = None
		peak_stop = None
		next_hour = hour + _SAMPLE_RANGE # create the range of time to search in

		# make sure there are records within the timeframe otherwise just go away
		if cur.execute(f"""SELECT COUNT(*) AS count FROM cdr_dates_{parse_time}
							WHERE (dateTimeOrigination <= {next_hour} AND dateTimeDisconnect >= {hour})""").fetchall()[0][0] != 0:

			# JM parser is faster at larger time lengths with smaller call volumes, but is fast as hell in general so try before you disable
			if jm_parser:
				hour_max, peak_stop, peak_start = self.jm_parser(db.execute(f"SELECT * FROM cdr_dates_{parse_time} WHERE (dateTimeOrigination <= {next_hour} AND dateTimeDisconnect >= {hour})"))
				# print(hour_max, peak_stop, peak_start)

			else:
				# create a temp table based on active calls within the hour and orig/dest devices.  Already ordered from above
				# loop until it completes. Issues with threading SQLLite and open connections
				while True:
					try:
						db.execute(f"""CREATE TEMPORARY TABLE tmp{hour} AS 
										SELECT dateTimeOrigination,dateTimeDisconnect FROM cdr_dates_{parse_time}
										WHERE (dateTimeOrigination <= {next_hour} AND dateTimeDisconnect >= {hour})
									""") 
					except Exception as err:
						print(err)
						time.sleep(1)
					else:
						break

				db.commit()				

				# Loop through the hour by 10sec and count calls that are active during that second
				current_sec = hour
				while current_sec <= next_hour:
					try:
						# query for conncurrent call
						sec_count = cur.execute(f"SELECT COUNT(*) AS count FROM tmp{hour} WHERE dateTimeDisconnect >= {current_sec} AND dateTimeOrigination <= {current_sec}").fetchall()[0][0]
					except:
						continue
					else:
						# if count for sec is higher than current hour countr replace the high mark
						if sec_count > hour_max:
							hour_max = sec_count
							peak_stop = current_sec
							if peak_start is None:
								peak_start = current_sec

					current_sec += _SAMPLE_RATE

				# Drop temp table and add add results to concurrent_calls table
				db.execute(f"drop table tmp{hour}")

		if peak_start is not None and peak_stop is not None:
			duration = peak_stop - peak_start
			# loop until your able to insert the results into the answers table
			while True:
				try:
					db.execute(f"INSERT INTO cdr_concurrent_{parse_time} (hour,count,duration,peakstart,peakstop) VALUES ({hour},{hour_max},{duration},{peak_start},{peak_stop})")
				except Exception as err:
					print(f"Error writting results: {err}", file=sys.stderr)
					time.sleep(1)
				else:
					try:
						db.commit()
					except:
						pass
					else:
						break		

		db.close()
		return True


"""
scriptStart = time.time()

## create DB either in file or in Memory
cdr = CDRParser(csv="A479A61AC2AE86D1ABA51A5B983232DE20201016155440116CDR.txt")



## Show high hour/day/calls mark
#for r in cdr.get_concurrent_calls(SAMPLE_RANGE="all"):
#	print(r)q

## Show high hour/day/calls mark
for r in cdr.calls_per_sec():
	print(r)

print("\n")
print(f"\n{round((time.time() - scriptStart))} seconds")
"""

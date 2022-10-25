from zeep.transports import Transport
from zeep import Client, Settings
from requests import Session
from requests.auth import HTTPBasicAuth
import sys
import time
from datetime import datetime, timedelta


class CDROnDemand():
    class ProgressBar():
        progress_bar_scale = .7
        progress_bar_length = int(100 * progress_bar_scale)
        completed_bar_char = "█"
        incomplete_bar_char = "▒"
        completion_message = "Completed!"

        def __init__(self, total):
            print()
            self.total = total

        def progress(self, current):
            # print out our progress bar
            percent_complete = round(current / self.total * 100)
            bars_of_completion = int(percent_complete * self.progress_bar_scale)
            bars_to_be_completed = self.progress_bar_length - bars_of_completion
            print(
                f'\r{self.completed_bar_char * bars_of_completion}{self.incomplete_bar_char * bars_to_be_completed} {percent_complete}%',
                end='')

    def __init__(self,ipaddr,username,passwd):
        # set DIME WSDL file from URL
        dime_wsdl = f'https://{ipaddr}:8443/logcollectionservice/services/DimeGetFileService?wsdl'

        # create a SOAP client session
        session = Session()

        # avoid certificate verification by default and setup session
        session.verify = False
        session.auth = HTTPBasicAuth(username, passwd)
        transport = Transport(session=session, timeout=10)
        settings = Settings(strict=False, xml_huge_tree=True)

        # Create client and soap service
        client_dime = Client(dime_wsdl, settings=settings,
                                transport=transport)  # , plugins = plugin )
        self.dime = client_dime.create_service(
            '{http://cisco.com/ccm/serviceability/soap/LogCollection/GetFile/}GetFileBinding',
            dime_wsdl)

        # set CDRonDemand WSDL file from URL for File Transfer
        cdr_on_demand_wsdl = f'https://{ipaddr}:8443/CDRonDemandService2/services/CDRonDemandService?wsdl'

        # Create client and soap service
        client_cdr_on_demand = Client(cdr_on_demand_wsdl, settings=settings,
                                      transport=transport)  # , plugins = plugin )
        self.cdr_on_demand = client_cdr_on_demand.create_service(
            '{http://schemas.cisco.com/ast/soap}CDRonDemandSoapBinding',
            cdr_on_demand_wsdl)

    # File request from CM via DIME
    def get_file(self, filepath):
        # check if file path includes /var/log as required if not assume /var/log/active
        if filepath.find('/var/log') == -1:
            filepath = f"/var/log/active/{filepath}"

        try:
            file_contents = self.dime.GetOneFile(filepath).attachments[0].content.decode('UTF-8')

        except Exception as err:
            print(f"Error pulling {filepath} from CUCM - {err}", file=sys.stderr)
            return False

        else:
            return file_contents

    # get CDR files to get (list or single file with return_type = dict|string|dataframe
    def get_cdr_file(self, filename, return_type="list"):
        cdr_return = {'cdr': { 'columns': [], 'types': [], 'contents': [] },
                      'cmr': { 'columns': [], 'types': [], 'contents': [] } }
        cdr_files = {}

        # if filename is string (single file) then wrap into a list to process
        if isinstance(filename, str):
            filename = [filename]
        pb = self.ProgressBar(len(filename))

        # get each file in list and process into dict formatting
        x = 1
        start = time.time()
        for file in filename:
            pb.progress(x)
            x += 1
            try:
                file_contents = self.get_file(f"/var/log/active/cm/cdr_repository/processed/{file.split('_')[3][:8]}/{file}").replace('"', '').splitlines()

            except Exception as err:
                print(f"Error retrieving filename {file} - {err}", file=sys.stderr)

            else:
                # parse out file lines
                if file.find("cdr_") > -1:
                    if len(cdr_return['cdr']['columns']) == 0:
                        cdr_return['cdr']['columns'] = file_contents[0].split(',')
                        cdr_return['cdr']['types'] = file_contents[1].split(',')

                    for line in file_contents[2:]:
                        y = 0
                        row = []
                        line = line.split(',')
                        while y < len(line):
                            if not cdr_return['cdr']['types'][y] == '':
                                if cdr_return['cdr']['types'][y] == 'INTEGER':
                                    try:
                                        row.append(int(line[y]))
                                    except:
                                        row.append(0)
                                else:
                                    row.append(line[y])
                            else:
                                row.append('')
                            y += 1

                        cdr_return['cdr']['contents'].extend([row])

                elif file.find("cmr_") > -1:
                    if len(cdr_return['cmr']['columns']) == 0:
                        cdr_return['cmr']['columns'] = file_contents[0].split(',')
                        cdr_return['cmr']['types'] = file_contents[1].split(',')
                    for line in file_contents[2:]:
                        y = 0
                        row = []
                        line = line.split(',')
                        while y < len(line):
                            if not cdr_return['cmr']['types'][y] == '':
                                if cdr_return['cmr']['types'][y] == 'INTEGER':
                                    try:
                                        row.append(int(line[y]))
                                    except:
                                        row.append(0)
                                else:
                                    row.append(line[y])
                            else:
                                row.append('')
                            y += 1

                        cdr_return['cmr']['contents'].extend([row])

        print(f"{len(filename)} files in {time.time() - start}sec.")
        if return_type.lower == "str" or return_type.lower() == "string":
            cdr_string = ",".join(cdr_return['cdr']['columns']) + '\n'
            for i in cdr_return['cdr']['contents']:
                cdr_string = cdr_string + ",".join(i) + '\n'

            cmr_string = ",".join(cdr_return['cmr']['columns']) + '\n'
            for i in cdr_return['cmr']['contents']:
                cmr_string = cmr_string + ",".join(i) + '\n'

            return cdr_string

        elif return_type.lower() == "list":
            return { 'cdr': cdr_return['cdr']['contents'],
                     'cmr': cdr_return['cmr']['contents'] }

        else:
            return cdr_return

    # List CDR files used between start/stop epoch time
    def list_cdr_files(self, cdr_start, cdr_stop):
        cdr_start = datetime.strptime(cdr_start,'%Y%m%d%H%M')
        cdr_stop = datetime.strptime(cdr_stop,'%Y%m%d%H%M')
        file_list = []
        while cdr_start < cdr_stop:
            try:
                files = self.cdr_on_demand.get_file_list(cdr_start.strftime('%Y%m%d%H%M'), (cdr_start + timedelta(hours=1)).strftime('%Y%m%d%H%M'), True)
            except Exception as err:
                print(f"Error getting file names - {err}", file=sys.stderr)
            else:
                for file in files:
                    file_list.append(file)
            cdr_start = cdr_start + timedelta(hours=1)

        return file_list


# cm = CMFileCollector.Connect("10.45.50.110","API","API")
# #File path = /var/log/<1>/<2> where CLI = file view <1> <2>
# cdr = cm.dime.GetOneFile('/var/log/active/cm/cdr_repository/processed/20210112/cmr_Nucor-EnterpriseCluster-01_06_202101122006_158160')
# print(cdr.attachments[0].content)
#
# b'"cdrRecordType","globalCallID_callManagerId","globalCallID_callId","nodeId","directoryNum","callIdentifier","dateTimeStamp","numberPacketsSent","numberOctetsSent","numberPacketsReceived","numberOctetsReceived","numberPacketsLost","jitter","latency","pkid","directoryNumPartition","globalCallId_ClusterID","deviceName","varVQMetrics","duration","videoContentType","videoDuration","numberVideoPacketsSent","numberVideoOctetsSent","numberVideoPacketsReceived","numberVideoOctetsReceived","numberVideoPacketsLost","videoAverageJitter","videoRoundTripTime","videoOneWayDelay","videoReceptionMetrics","videoTransmissionMetrics","videoContentType_channel2","videoDuration_channel2","numberVideoPacketsSent_channel2","numberVideoOctetsSent_channel2","numberVideoPacketsReceived_channel2","numberVideoOctetsReceived_channel2","numberVideoPacketsLost_channel2","videoAverageJitter_channel2","videoRoundTripTime_channel2","videoOneWayDelay_channel2","videoReceptionMetrics_channel2","videoTransmissionMetrics_channel2","localSessionID","remoteSessionID","headsetSN","headsetMetrics"\nINTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(50),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,UNIQUEIDENTIFIER,VARCHAR(50),VARCHAR(50),VARCHAR(129),VARCHAR(600),INTEGER,VARCHAR(10),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(600),VARCHAR(600),VARCHAR(10),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(600),VARCHAR(600),VARCHAR(128),VARCHAR(128),VARCHAR(129),VARCHAR(1024)\n2,6,11269506,6,"+193668

# files = cm.list_cdr_files('202101130700','202101130800') #start/stop datetime year,month,day,hour,minute
# file = cm.get_cdr_file(files[0])

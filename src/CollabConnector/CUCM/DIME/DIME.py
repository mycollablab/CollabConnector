from zeep.transports import Transport
from zeep import Client, Settings
from requests import Session
from requests.auth import HTTPBasicAuth
import sys


class Connect():
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
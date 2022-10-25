import requests
from requests.auth import HTTPBasicAuth
import sys
import os
import re
import urllib
import json

requests.packages.urllib3.disable_warnings()


class Connect:
    # initialize object set system type and build DB connectors as needed
    def __init__(self,
                 ipaddr=None,
                 username=None,
                 passwd=None,
                 db=False,
                 unity_db="UnityDirDb"
                 ):

        self.system_type = "Unity Connection"
        self.ipaddr = ipaddr

        # if type= cucm then set username/password for AXL connection
        if ipaddr is None or passwd is None or username is None:
            print(f'Usage: CollabConnector.CUCX("ipaddr", "admin", "password")',
                  file=sys.stderr)
        else:
            self.username = username
            self.auth = HTTPBasicAuth(username, passwd)

            try:
                self.version = self.get("version")[0]['version']
            except Exception as err:
                print(f"Could not connect via vmrest: {err}", file=sys.stderr)

            if db:
                try:
                    import IfxPy
                except:
                    print("""IfxPy module failed to load. If you intend to connect to an Informix DB check the linux enviroment
                            << pip3 install IfxPy >>
                            export INFORMIXDIR=/opt/IBM/Informix_Client-SDK/  
                            export CSDK_HOME=$INFORMIXDIR
                            export LIBPATH=${INFORMIXDIR}/lib:${INFORMIXDIR}/lib/cli:${INFORMIXDIR}/lib/esql:${INFORMIXDIR}/lib:${INFORMIXDIR}/bin:${INFORMIXDIR}/etc:${LIBPATH}
                            export LD_LIBRARY_PATH=$INFORMIXDIR/lib:$INFORMIXDIR/lib/cli:$INFORMIXDIR/lib/esql
                            """, file=sys.stderr)
                    self.INFORMIX = False
                else:
                    connection_string = f'CLIENT_LOCALE=en_US.57372;DB_LOCALE=en_US.57372;uid={username};pwd={passwd};SERVER=ciscounity;DATABASE={unity_db};HOST={ipaddr};SERVICE=20532;PROTOCOL=onsoctcp'
                    try:
                        self.informixConnector = IfxPy.connect(connection_string, "", "")
                    except Exception as err:
                        print(f'Could not Connect to Unity Informix DB: {err}', file=sys.stderr)
                        self.INFORMIX = False
                    else:
                        self.INFORMIX = True
            else:
                self.INFORMIX = False
            print("Connected.")

    # Function query SQL via direct Informix connector
    def informix_query(self, sql_statement):
        if self.INFORMIX is False:
            print("Not connected to INFORMIX DB. Use db=True.", file=sys.stderr)
            return False

        result = []
        if re.search("select", sql_statement.lower()) and not re.search('select.*limit .*from', sql_statement.lower()):
            select_count = re.sub("[sS][eE][lL][eE][cC][tT] .* [fF][rR][oO][mM] ", "SELECT COUNT(*) AS qty FROM ",
                                 sql_statement)
            stmt = IfxPy.exec_immediate(self.informixConnector, select_count)
            return_rows = int(IfxPy.fetch_assoc(stmt)['qty'])

            request_count = 0
            while request_count < return_rows:
                request_rows = re.sub("[sS][eE][lL][eE][cC][tT] ", f"SELECT SKIP {request_count} LIMIT 4000 ",
                                      sql_statement)

                try:
                    stmt = IfxPy.exec_immediate(self.informixConnector, request_rows)
                except Exception as err:
                    print(f"SQL Error: {err}", file=sys.stderr)
                    return False
                else:
                    while True:
                        assoc = IfxPy.fetch_assoc(stmt)
                        if assoc is not False:
                            result.append(assoc)
                        else:
                            break

                request_count = len(result)

        else:
            try:
                stmt = IfxPy.exec_immediate(self.informixConnector, sql_statement)
            except Exception as err:
                print(f"SQL Error: {err}", file=sys.stderr)
                return False
            else:
                assoc = IfxPy

            while True:
                assoc = IfxPy.fetch_assoc(stmt)
                if assoc is not False:
                    result.append(assoc)
                else:
                    break

        return result

    # REST Wrapper for Unity
    def cupi_api(self, target_uri, method='GET', data={}, paging=True):
        # build URL based on URI in funcion call
        if target_uri.find("vmrest/") > -1:
            target_uri = target_uri
        else:
            if target_uri.find('/') == 0:
                target_uri = target_uri[1:]
            target_uri = f"https://{self.ipaddr}:8443/vmrest/{target_uri}"

        headers = {'Accept': "application/json",
                   'Content-Type': "application/json"}

        if method in ['PUT', 'POST', 'DELETE']:
            try:
                response = requests.request(method, target_uri, headers=headers, auth=self.auth,
                                            verify=False, data=json.dumps(data))
            except Exception as err:
                print(f"CXN API {method} Failure: {err} - {target_uri}", file=sys.stderr)
                return False
            else:
                result = [response.text]
        else:
            #  Add parameters to uri if needed
            if len(data) > 0:
                target_uri += f"?{urllib.parse.urlencode(data)}"

            # for pagination set the separator value if URI has get variables or not
            if target_uri.find("?") > -1:
                separator = "&"
            else:
                separator = "?"

            if method == 'GET' and paging is True:

                # get number of results fpr pagination
                try:
                    response = requests.get(f"{target_uri}{separator}pageNumber=0", headers=headers,
                                            auth=self.auth, verify=False)
                except Exception as err:
                    print(f"CXN API GET Failure: {err} - {target_uri}", file=sys.stderr)
                    return False

                # if @totals exist in response then expect more than 1 result and set max entries
                if "@total" in response.text:
                    try:
                        query_count = int(json.loads(response.text)['@total'])
                    except Exception as err:
                        pass
                else:
                    query_count = 1

                if query_count == 0:
                    return []

                # find page count if 1000 items per page for loop
                max_page = round(query_count / 1000) + 1
            else:
                max_page = 1
            current_page = 1

            # create result array
            result = []
            # loop through results getting 500 entries at a time
            while current_page <= max_page:
                try:
                    response = requests.get(f"{target_uri}{separator}rowsPerPage=1000&pageNumber={str(current_page)}",
                                            headers=headers, auth=self.auth, verify=False)
                except Exception as err:
                    print(f"\tCXN GET API Failure: {err} - {target_uri}", file=sys.stderr)
                    return False

                # confirm if valid response
                if response.status_code == 200:
                    query_result = json.loads(response.text)

                    # if multiple results in response loop through each and add to result array
                    if "@total" in query_result.keys():
                        for key in query_result:
                            if not key == "@total":
                                if query_result['@total'] == "1":
                                    result.append(query_result[key])
                                else:
                                    for item in query_result[key]:
                                        result.append(item)
                    else:
                        result.append(query_result)
                else:
                    print(f"\t{str(response)}{response.text}", file=sys.stderr)
                    return False

                current_page += 1

        return result

    # wrapper for api Gets
    def get(self, target_endpoint, params={}):
        return self.cupi_api(target_endpoint, data=params)

    # wrapper for api PUT
    def put(self, target_endpoint, put_data):
        return self.cupi_api(target_endpoint, method='PUT', data=put_data)

    # wrapper for api POST
    def post(self, target_endpoint, post_data):
        return self.cupi_api(target_endpoint, method='POST', data=post_data)

    # wrapper for api DELETE
    def delete(self, target_endpoint):
        return self.cupi_api(target_endpoint, method='DELETE')

    def get_prompt(self, greeting_stream_file_uri, filename="greeting.wav"):
        try:
            folder = greeting_stream_file_uri.split("/")[4]
            try:
                print(f"Creating folder {folder}...")
                os.mkdir(folder, 0o0775)
            except Exception as err:
                if not str(err).find('already exists') > -1:
                    print(f"Could not create directory - {err}", file=sys.stderr)

            prompt_file = open(f"{folder}{os.sep}{filename}", "wb")
            wav_content = requests.get(f"https://{self.ipaddr}{greeting_stream_file_uri}/audio",
                                       auth=self.auth, verify=False)
            prompt_file.write(wav_content.content)
            prompt_file.close()

        except Exception as err:
            print(f"Could not download prompt - {err}", file=sys.stderr)

        else:
            return filename

    def get_all_prompts(self, search):
        print(f"Searching for User extension {search}")
        users = self.cupi_api(f"users?query=(%20DtmfAccessId%20is%20{search}%20)")
        if users and len(users) == 0:
            print(f"Searching for User Alias {search}")
            users = self.cupi_api(f"users?query=(%20Alias%20is%20{search}%20)")
        if users and len(users) == 0:
            print(f"Searching for User Display Name {search}")
            users = self.cupi_api(f"users?query=(%20DisplayName%20is%20{search}%20)")

        if users and len(users) > 0:
            ch = self.cupi_api(users[0]['CallhandlerURI'])
            greetings = self.cupi_api(ch[0]['GreetingsURI'])
            for greeting in greetings:
                prompt = self.cupi_api(greeting['GreetingStreamFilesURI'])
                if len(prompt) > 0:
                    prompt_name = prompt[0]['GreetingStreamFileLanguageURI'].split("/")[6]
                    print(f"\tDownloading Prompt {prompt_name}")
                    self.get_prompt(prompt[0]['GreetingStreamFileLanguageURI'], f"{prompt_name}.wav")
            return True

        else:
            print(f"Couldnt find User {search} by extension, searching by name..", file=sys.stderr)
            handlers = self.cupi_api(f"handlers")
            greetings = False
            for handler in handlers:
                if handler['DisplayName'] == search or ('DtmfAccessId' in handler.keys() and handler["DtmfAccessId"] == search):
                    call_handler = self.cupi_api(handler['URI'])
                    if len(call_handler) > 0:
                        greetings = self.cupi_api(call_handler[0]['GreetingsURI'])
                    break
            if not greetings:
                print(f"Couldnt find {search} by name, searching Call Handlers by extension..", file=sys.stderr)
                handlers = self.cupi_api(f"handlers/callhandlers")
                greetings = False
                for handler in handlers:
                    if handler['DisplayName'] == search or ('DtmfAccessId' in handler.keys() and handler["DtmfAccessId"] == search):
                        call_handler = self.cupi_api(handler['URI'])
                        if len(call_handler) > 0:
                            greetings = self.cupi_api(call_handler[0]['GreetingsURI'])
                        break

            if greetings and len(greetings) > 0:
                print(f"Found Call Handler for {search}")
                for greeting in greetings:
                    prompt = self.cupi_api(greeting['GreetingStreamFilesURI'])
                    if len(prompt) > 0:
                        prompt_name = prompt[0]['GreetingStreamFileLanguageURI'].split("/")[6]
                        print(f"\tDownloading {prompt_name}")
                        self.get_prompt(prompt[0]['GreetingStreamFileLanguageURI'], f"{prompt_name}.wav")
                return True
            else:
                print("... and I stiiiiill havent fouuuund what Im looking foooor..")
                return False

import requests
import xmltodict
from requests.auth import HTTPBasicAuth
import sys
import re
import json
import urllib

requests.packages.urllib3.disable_warnings()


class Connect:

    # initialize object set system type and build DB connectors as needed
    def __init__(self,
                 ipaddr=None,
                 username=None,
                 passwd=None,
                 db=False,
                 server_name=None
                 ):

            self.system_type = "UCCX"
            self.ipaddr = ipaddr

            # if type= cucm then set username/password for AXL connection
            if ipaddr is  None or passwd is None or username is None:
                print(f'Usage: CollabConnector.UCCX.Connect("ipaddr", "admin", "password", db=False)',
                      file=sys.stderr)
            else:
                self.username = username
                self.auth = HTTPBasicAuth(username, passwd)

                # if type = uccx-db then set the informixConnection variable for the connector
                if db:
                    try:
                        import IfxPy
                    except:
                        print("""
                            IfxPy module failed to load. If you intend to connect to an Informix DB check the linux enviroment
                            << pip3 install IfxPy >>
                            export INFORMIXDIR=/opt/IBM/Informix_Client-SDK/  
                            export CSDK_HOME=$INFORMIXDIR
                            export LIBPATH=${INFORMIXDIR}/lib:${INFORMIXDIR}/lib/cli:${INFORMIXDIR}/lib/esql:${INFORMIXDIR}/lib:${INFORMIXDIR}/bin:${INFORMIXDIR}/etc:${LIBPATH}
                            export LD_LIBRARY_PATH=$INFORMIXDIR/lib:$INFORMIXDIR/lib/cli:$INFORMIXDIR/lib/esql
                            """, file=sys.stderr)
                        self.INFORMIX = False
                    else:
                        connection_string = f"SERVER={server_name};DATABASE=db_cra;HOST={ipaddr};SERVICE=5104;UID=uccxhruser;PWD={passwd};DB_LOCALE=en_US.utf8;"
                        try:
                            self.informixConnector = IfxPy.connect(connection_string, "", "")
                        except Exception as err:
                            print(f'INFORMIX connection failed. {err}', file=sys.stderr)
                            self.INFORMIX = False
                        else:
                            self.INFORMIX = True
                else:
                    self.INFORMIX = False
                    print("Informix Drivers not correctly initialized.  Try again or use the API", file=sys.stderr)

    # Function query SQL via direct Informix connector
    def informix_query(self, sql_statement):
        if self.INFORMIX is False:
            print("Not connected to INFORMIX DB. Use db=True.", file=sys.stderr)
            return False

        result = []
        if re.search("select", sql_statement.lower()) and not re.search('select.*limit .*from', sql_statement.lower()):
            selectCount = re.sub("[sS][eE][lL][eE][cC][tT] .* [fF][rR][oO][mM] ", "SELECT COUNT(*) AS qty FROM ",
                                 sql_statement)
            stmt = IfxPy.exec_immediate(self.informixConnector, selectCount)
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

    # REST Wrapper for UCCX
    def uccx_api(self, target_uri, method='GET', data={}):
        if target_uri.find("adminapi/") > -1:
            target_uri = target_uri
        else:
            if target_uri.find('/') == 0:
                target_uri = target_uri[1:]
            target_uri = f"https://{self.ipaddr}:8443/adminapi/{target_uri}"

        if len(data) > 0:
            target_uri += f"?{urllib.parse.urlencode(data)}"
        print(target_uri)
        attempt = 0
        while attempt < 2:
            try:
                # send API request
                response = requests.request(method, target_uri, auth=self.auth,
                                            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
                                            data=json.dumps(data), verify=False)
            except Exception as err:
                print(f"Error requesting API: {err}", file=sys.stderr)
                attempt += 1
            else:
                # format response into result array
                try:
                    result = json.loads(response.text)
                except Exception as err:
                    return [response.text]
                else:
                    if "apiError" in result.keys():
                        print(f"Error requesting CCX API: {response.text}", file=sys.stderr)
                        return False

                    elif isinstance(result, dict):
                        if target_uri in result:
                            if isinstance(result[target_uri], list):
                                return result[target_uri]
                            else:
                                return [result[target_uri]]
                        else:
                            if isinstance(result, list):
                                return result
                            else:
                                return [result]
                    else:
                        return [result]
        return False

    # wrapper for api Gets
    def get(self, target_endpoint, params={}):
        return self.uccx_api(target_endpoint, data=params)

    # wrapper for api PUT
    def put(self, target_endpoint, put_data):
        return self.uccx_api(target_endpoint, method='PUT', data=put_data)

    # wrapper for api POST
    def post(self, target_endpoint, post_data):
        return self.uccx_api(target_endpoint, method='POST', data=post_data)

    # wrapper for api DELETE
    def delete(self, target_endpoint):
        return self.uccx_api(target_endpoint, method='DELETE')

    # wrapper for api PATCH
    def patch(self, target_endpoint, patch_data):
        return self.uccx_api(target_endpoint, method='PATCH', data=patch_data)

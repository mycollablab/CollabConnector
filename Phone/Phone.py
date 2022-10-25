from urllib.request import urlopen
import xmltodict
import requests
import re
import sys
import ssl
import time
import html
import os

requests.packages.urllib3.disable_warnings()


class Connect():
    device_html = None
    network_html = None
    port_html = None
    ip = None
    _username = None
    _dn = None
    _passwd = None
    _serial = None
    _mac = None
    _model = None
    _name = None
    _timezone = None
    _dhcpServer = None
    _bootpserver = None
    _domain = None
    _subnet = None
    _dns = [None, None, None, None, None]
    _gateway = None
    _cm_list = [None, None, None, None, None]
    _tftp = [None, None]
    _voice_vlan = None
    _data_vlan = None
    _alternate_tftp = None
    _dhcp = None
    _secure = None
    _user_locale = None
    _network_locale = None
    _idle_url = None
    _directory_url = None
    _auth_url = None
    _services_url = None
    _headset = None
    _pc_port = None
    _video = None
    _itl = None
    _ctl = None
    _lldp_neighbor = None
    _cdp_neighbor = None
    _stream = None
    _tvs = None

    def __init__(self, ip_addr, username=None, passwd=None):
        self.ip = ip_addr
        if username is not None: self._username = username
        if passwd is not None: self._passwd = passwd
        self.base_url = f"http://{self.ip}"
        try:
            self.device_html = urlopen(f"{self.base_url}", context=ssl.SSLContext(), timeout=1).read().decode("utf-8")
            self.network_html = urlopen(f"{self.base_url}/NetworkConfiguration", timeout=1).read().decode("utf-8")
            self.port_html = urlopen(f"{self.base_url}/PortInformation?1", timeout=1).read().decode("utf-8")

        except Exception as err1:
            self.base_url = f"https://{self.ip}"
            try:
                self.device_html = urlopen(f"{self.base_url}", context=ssl.SSLContext(), timeout=1).read().decode(
                    "utf-8")
                self.network_html = urlopen(f"{self.base_url}/NetworkConfiguration", context=ssl.SSLContext(),
                                            timeout=1).read().decode("utf-8")
                self.port_html = urlopen(f"{self.base_url}/PortInformation?1", context=ssl.SSLContext(),
                                         timeout=1).read().decode("utf-8")

            except Exception as err2:
                print(f"{ip_addr} - Unable to connect to phone Web Page. Check that its enabled: {err1} - {err2}",
                      file=sys.stderr)

    def details(self):
        result = {}
        result['ip'] = self.ip
        result['serial'] = self.serial()
        result['mac'] = self.mac()
        result['name'] = self.name()
        result['dn'] = self.dn()
        result['model'] = self.model()
        result['mwi'] = self.mwi()
        result['timezone'] = self.timezone()
        result['dhcpserver'] = self.dhcpserver()
        result['domain'] = self.domain()
        result['subnet'] = self.subnet()
        result['bootpserver'] = self.bootpserver()
        result['dns'] = self.dns()
        result['gateway'] = self.gateway()
        result['cm_list'] = self.cm_list()
        result['tvs'] = self.tvs()
        result['tftp'] = self.tftp()
        result['voice_vlan'] = self.voice_vlan()
        result['data_vlan'] = self.data_vlan()
        result['alternate_tftp'] = self.alternate_tftp()
        result['dhcp'] = self.dhcp()
        result['secure'] = self.secure()
        result['user_locale'] = self.user_locale()
        result['network_locale'] = self.network_locale()
        result['idle_url'] = self.idle_url()
        result['directories_url'] = self.directories_url()
        result['auth_url'] = self.auth_url()
        result['services_url'] = self.services_url()
        result['headset'] = self.headset()
        result['itl'] = self.itl()
        result['ctl'] = self.ctl()
        result['pc_port'] = self.pc_port()
        result['video'] = self.video()
        result['cdp_neighbor'] = self.cdp_neighbor()
        result['lldp_neighbor'] = self.lldp_neighbor()
        if self._username is not None and self._passwd is not None:
            result['API'] = self.check_auth()
        return result

    def check_creds(self, username, passwd):
        # check that username is set somewhere
        if username is not None: self._username = username
        if passwd is not None: self._passwd = passwd

        if self._username is None and self._passwd is None:
            print("You must pass 'username' and passwd' for phone access!", file=sys.stderr)
            return False

        return True

    def scrape_html_data(self, html_data, search_string):
        if html_data is None:
            return None
        else:
            try:
                search_string = html_data[html_data.lower().find(search_string.lower()):]
                search_string = search_string[search_string.find("<TD>"):]
                search_string = search_string[search_string.find("<TD>"):search_string.find("</TD>")]
                search_string = re.sub("<[^>]*>", "", search_string).strip()
                if isinstance(search_string, str):
                    search_string = html.unescape(search_string)

            except Exception as err:
                print(f"Error parsing HTML: {err}", file=sys.stderr)
                return False

            else:
                return search_string

    def screenshot(self, screenshot_file=None, username=None, passwd=None, raw=False):
        # check that username is set somewhere
        if not self.check_creds(username, passwd):
            return False

        # send request for screenshot
        try:
            screenshot = requests.get(f"http://{self.ip}/CGI/Screenshot", auth=(self._username, self._passwd))

        except Exception as err:
            print(f"{self.ip} - Unable to take Screenshot - {err}", file=sys.stderr)

        else:
            # confirm that response is an image based on header
            if screenshot.headers['Content-Type'].find("image") > -1:
                if raw:
                    return screenshot.content

                else:
                    # if file destination is not set then set it
                    if screenshot_file is None:
                        base_dir = "./PhoneScreenshots/"
                        screenshot_file = f"{base_dir}{self.name()}-{int(time.time())}.png"
                        try:
                            os.mkdir(base_dir, 0o0775)

                        except Exception as err:
                            # print(f"Screenshot folder exists...", file=sys.stderr)
                            pass

                    try:
                        # write the response to file
                        with open(screenshot_file, "wb") as image:
                            image.write(screenshot.content)

                    except Exception as err:
                        print(f"{self.ip} - Error saving Image - {err}", file=sys.stderr)

                    else:
                        # return the screenshot filename
                        return screenshot_file

            else:
                print(f"{self.ip} - Screenshot not valid", file=sys.stderr)
                return False

    # not Working!!!!!!!!
    def play(self, file, username=None, passwd=None):
        # check that username is set somewhere
        if not self.check_creds(username, passwd):
            return False

        # xml = f"""<CiscoIPPhoneExecute><ExecuteItem Priority=”0” URL=”Play:chime.raw”/><ExecuteItem Priority=”1” URL=”http://server/textmessage.xml”/></CiscoIPPhoneExecute>"""
        xml = f"""<CiscoIPPhoneExecute><ExecuteItem Priority=”0” URL=”Play:{file}”/></CiscoIPPhoneExecute>"""

        # send command to phone and xml decode response
        try:
            response = xmltodict.parse(
                requests.post(f"http://{self.ip}/CGI/Execute", auth=(self._username, self._passwd),
                              headers={'Content-Type': 'application/xml'}, data={'XML': xml}).content,
                dict_constructor=dict)
        except Exception as err:
            print(f"Error sending command to phone - {err}", file=sys.stderr)
        else:
            # check that response code was sucessful - 0 - or return False as a list with the reason
            if 'CiscoIPPhoneResponse' in response and response['CiscoIPPhoneResponse']['ResponseItem'][
                '@Status'] == "0":
                return True
            elif 'CiscoIPPhoneError' in response and response['CiscoIPPhoneError']['@Number'] == "4":
                return [False, "unauthorized"]
            else:
                return [False, response]

    # open audio stream to endpoint
    ######!!!!!Not working!!!
    def stream(self, stream, username=None, passwd=None):
        # check that username is set somewhere
        if not self.check_creds(username, passwd):
            return False

        if stream.lower() == "stop" and self._stream is None:
            stream = f"""<stopMedia><mediaStream id=”{self._stream}”/></stopMedia>"""
            self._stream = None

        else:
            stream = f"""<startMedia><mediaStream receiveVolume=”50”><type>audio</type><codec>G.711ULAW</codec><mode>sendReceive</mode><address>{stream.split(":")[0]}</address><port>{stream.split(":")[1]}</port></mediaStream></startMedia>"""

        # send command to phone and xml decode response
        try:
            response = xmltodict.parse(
                requests.post(f"http://{self.ip}/CGI/Execute", auth=(self._username, self._passwd),
                              headers={'Content-Type': 'application/xml'}, data={'XML': stream}).content,
                dict_constructor=dict)
        except Exception as err:
            print(f"Error sending command to phone - {err}", file=sys.stderr)
            return False
        else:
            self._stream = response['mediaStream']['id']
            return True

    def press(self, commands, username=None, passwd=None, delay=0.2):
        # check that username is set somewhere
        if not self.check_creds(username, passwd):
            return False

        if not isinstance(commands, list):
            commands = [commands]

        for command in commands:
            # send command to phone and xml decode response
            try:
                button = self.build_xml(str(command))

                if button:
                    response = xmltodict.parse(
                        requests.post(f"http://{self.ip}/CGI/Execute", auth=(self._username, self._passwd),
                                      headers={'Content-Type': 'application/xml'}, data=button).content,
                        dict_constructor=dict)
                else:
                    return [False, "Button not valid"]

            except Exception as err:
                print(f"Error sending command to phone - {err}", file=sys.stderr)
                return [False, err]

            else:
                # check that response code was sucessful - 0 - or return False as a list with the reason
                if 'CiscoIPPhoneError' in response and response['CiscoIPPhoneError']['@Number'] == "4":
                    return [False, "unauthorized"]

                elif 'CiscoIPPhoneResponse' in response and response['CiscoIPPhoneResponse']['ResponseItem'][
                    '@Status'] == "0":
                    pass
                else:
                    return [False, response]

            time.sleep(delay)

        return True

    def check_auth(self, username=None, passwd=None):
        # check that username is set somewhere
        if not self.check_creds(username, passwd):
            return False

        try:
            response = xmltodict.parse(
                requests.get(f"http://{self.ip}/CGI/Execute", auth=(self._username, self._passwd)).content,
                dict_constructor=dict)

        except Exception as err:
            print(f"{self.ip} - Error sending command to phone - {err}", file=sys.stderr)
            return False

        else:
            # check that response code was sucessful - 0 - or return False as a list with the reason
            if 'CiscoIPPhoneError' in response and response['CiscoIPPhoneError']['@Number'] == "4":
                return False

            else:
                return True

    # Builds the XML associated with the availble commands
    def build_xml(self, button):
        button = button.lower()
        if button in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            phone_url = f"Key:KeyPad{button}"
        elif button == "*":
            phone_url = f"Key:KeyPadStar"
        elif button == "#":
            phone_url = f"Key:KeyPadPound"
        elif button == "end":
            phone_url = "Key:Release"
        elif button == "hold":
            phone_url = "Key:Hold"
        elif button.find("fixedfeature") > -1:
            phone_url = f"Key:FixedFeature{re.sub('fixedfeature', '', button)}"
        elif button.find("feature") > -1:
            phone_url = f"Key:Feature{re.sub('feature', '', button)}"
        elif button.find("softkey") > -1:
            phone_url = f"Key:Soft{re.sub('softkey', '', button)}"
        elif button.find("session") > -1:
            phone_url = f"Key:Session{re.sub('session', '', button)}"
        elif button.find("line") > -1:
            phone_url = f"Key:Line{re.sub('line', '', button)}"
        elif button in ["apps", "applications", "app", "application"]:
            phone_url = f"Key:Applications"
        elif button == "contacts":
            phone_url = f"Key:Contacts"
        elif button == "settings":
            phone_url = f"Key:Settings"
        elif button == "services":
            phone_url = f"Key:Services"
        elif button in ["directory", "directories", "dir"]:
            phone_url = f"Key:Directories"
        elif button in ['messages', 'vm', 'voicemail']:
            phone_url = f"Messages:"
        elif button == "mute":
            phone_url = f"Key:Mute"
        elif button == "speaker":
            phone_url = f"Key:Speaker"
        elif button == "headset":
            phone_url = f"Key:Headset"
        elif button == "select":
            phone_url = f"Key:NavSelect"
        elif button == "up":
            phone_url = f"Key:NavUp"
        elif button == "down":
            phone_url = f"Key:NavDown"
        elif button == "left":
            phone_url = f"Key:NavLeft"
        elif button == "right":
            phone_url = f"Key:NavRight"
        elif button in ["volume-up", "volumeup"]:
            phone_url = f"Key:VolUp"
        elif button in ["volume-down", "volumedown"]:
            phone_url = f"Key:VolDwn"
        elif button in ["info", "question", "?"]:
            phone_url = f"Key:Info"
        elif button == "exit":
            phone_url = f"Key:Exit"

        else:
            print(f"Send button '{button}' not supported.", file=sys.stderr)
            return False

        # return formated XML
        return {'XML': f'<CiscoIPPhoneExecute><ExecuteItem Priority="0" URL="{phone_url}"/></CiscoIPPhoneExecute>'}

    def ip(self):
        if self.ip is None:
            print("Phone class not initialized yet.", file=sys.stderr)

        return self.ip

    def dn(self):
        if self._dn is None:
            self._dn = self.scrape_html_data(self.device_html, "Phone DN")
        return self._dn

    def serial(self):
        if self._serial is None:
            self._serial = self.scrape_html_data(self.device_html, "Serial Number")

        return self._serial

    def mac(self):
        if self._mac is None:
            self._mac = self.scrape_html_data(self.network_html, "MAC Address")

        return self._mac

    def name(self):
        if self._name is None:
            self._name = self.scrape_html_data(self.device_html, "Host Name")

        return self._name

    def model(self):
        if self._model is None:
            self._model = self.scrape_html_data(self.device_html, "Model Number")

        return self._model

    def mwi(self):
        try:
            if self.scrape_html_data(
                    urlopen(f"{self.base_url}", context=ssl.SSLContext(), timeout=1).read().decode("utf-8"),
                    "Message Waiting") == "Yes":
                return True
            else:
                return False
        except:
            return None

    def timezone(self):
        if self._timezone is None:
            self._timezone = self.scrape_html_data(self.device_html, "Time Zone")

        return self._timezone

    def dhcpserver(self):
        if self._dhcpServer is None:
            self._dhcpServer = self.scrape_html_data(self.network_html, "DHCP Server")

        return self._dhcpServer

    def domain(self):
        if self._domain is None:
            self._domain = self.scrape_html_data(self.network_html, "Domain Name")

        return self._domain

    def subnet(self):
        if self._subnet is None:
            self._subnet = self.scrape_html_data(self.network_html, "Subnet Mask")

        return self._subnet

    def bootpserver(self):
        if self._bootpserver is None:
            if self.scrape_html_data(self.network_html, "BOOTP Server") == "Yes":
                self._bootpserver = True
            else:
                self._bootpserver = False

        return self._bootpserver

    def dns(self):
        if self._dns[0] is None:
            x = 1
            while x <= len(self._dns):
                self._dns[x - 1] = self.scrape_html_data(self.network_html, f"DNS Server {x}")
                if self._dns[x - 1] == '':
                    self._dns[x - 1] = None
                x += 1

        return self._dns

    def gateway(self):
        if self._gateway is None:
            self._gateway = self.scrape_html_data(self.network_html, f"Default Router 1")
            if self._gateway == '':
                self._gateway = self.scrape_html_data(self.network_html, f"Default Router")

        return self._gateway

    def tvs(self):
        if self._tvs is None:
            self._tvs = self.scrape_html_data(self.network_html, f"TVS")

        return self._tvs

    def cm_list(self):
        if self._cm_list[0] is None:
            x = 1
            while x <= len(self._cm_list):
                if self.scrape_html_data(self.network_html, f"Unified CM {x}") is not None:
                    self._cm_list[x - 1] = self.scrape_html_data(self.network_html, f"Unified CM {x}").split()
                if self._cm_list[x - 1] == []:
                    self._cm_list[x - 1] = None
                x += 1
            if self._cm_list[0] == None:
                x = 1
                while x <= len(self._cm_list):
                    if self.scrape_html_data(self.network_html, f"CUCM server{x}") is not None:
                        self._cm_list[x - 1] = self.scrape_html_data(self.network_html, f"CUCM server{x}").split()
                    if self._cm_list[x - 1] == []:
                        self._cm_list[x - 1] = None
                    x += 1

        return self._cm_list

    def tftp(self):
        if self._tftp[0] is None:
            x = 1
            while x <= len(self._tftp):
                self._tftp[x - 1] = self.scrape_html_data(self.network_html, f"TFTP Server {x}")
                if self._tftp[x - 1] == '':
                    self._tftp[x - 1] = None
                x += 1

        return self._tftp

    def voice_vlan(self):
        if self._voice_vlan is None:
            self._voice_vlan = self.scrape_html_data(self.network_html, "Operational VLAN Id")

        return self._voice_vlan

    def data_vlan(self):
        if self._data_vlan is None:
            self._data_vlan = self.scrape_html_data(self.network_html, "Admin. VLAN Id")

        return self._data_vlan

    def alternate_tftp(self):
        if self._alternate_tftp is None:
            if self.scrape_html_data(self.network_html, "Alternate TFTP") == "Yes":
                self._alternate_tftp = True
            else:
                self._alternate_tftp = False

        return self._alternate_tftp

    def dhcp(self):
        if self._dhcp is None:
            if self.scrape_html_data(self.network_html, "DHCP<") == "Yes":
                self._dhcp = True
            else:
                self._dhcp = False

        return self._dhcp

    def secure(self):
        if self._secure is None:
            self._secure = self.scrape_html_data(self.network_html, "Security Mode")

        return self._secure

    def user_locale(self):
        if self._user_locale is None:
            self._user_locale = self.scrape_html_data(self.network_html, "User Locale<")

            if self._user_locale == "":
                self._user_locale = False

        return self._user_locale

    def network_locale(self):
        if self._network_locale is None:
            self._network_locale = self.scrape_html_data(self.network_html, "Network Locale<")

        return self._network_locale

    def idle_url(self):
        if self._idle_url is None:
            self._idle_url = self.scrape_html_data(self.network_html, "Idle URL<")

        return self._idle_url

    def directories_url(self):
        if self._directory_url is None:
            self._directory_url = self.scrape_html_data(self.network_html, "Directories URL<")

        return self._directory_url

    def auth_url(self):
        if self._auth_url is None:
            self._auth_url = self.scrape_html_data(self.network_html, "Authentication URL<")

        return self._auth_url

    def services_url(self):
        if self._services_url is None:
            self._services_url = self.scrape_html_data(self.network_html, "Services URL<")

        return self._services_url

    def itl(self):
        if self._itl is None:
            self._itl = [self.scrape_html_data(self.network_html, "ITL file<"),
                         self.scrape_html_data(self.network_html, "ITL signature<")]

        return self._itl

    def ctl(self):
        if self._ctl is None:
            self._ctl = [self.scrape_html_data(self.network_html, "CTL file<"),
                         self.scrape_html_data(self.network_html, "CTL signature<")]

        return self._ctl

    def headset(self):
        if self._headset is None:
            if self.scrape_html_data(self.network_html, "Headset Enabled<") == "Yes":
                self._headset = True
            else:
                self._headset = False

        return self._headset

    def pc_port(self):
        if self._pc_port is None:
            if self.scrape_html_data(self.network_html, "PC Port Disabled<") == "Yes":
                self._pc_port = False
            else:
                self._pc_port = True

        return self._pc_port

    def video(self):
        if self._video is None:
            if self.scrape_html_data(self.network_html, "Video Capability Enabled<") == "Yes":
                self._video = True
            else:
                self._video = False

        return self._video

    def cdp_neighbor(self):
        if self._cdp_neighbor is None:
            self._cdp_neighbor = {}
            self._cdp_neighbor['device'] = self.scrape_html_data(self.port_html, "CDP Neighbor Device ID")
            self._cdp_neighbor['ip'] = self.scrape_html_data(self.port_html, "CDP Neighbor IP Address")
            if self._cdp_neighbor['ip'] == '':
                self._cdp_neighbor['ip'] = self.scrape_html_data(self.port_html, "CDP Neighbor IPv4 Address")
            self._cdp_neighbor['ipv6'] = self.scrape_html_data(self.port_html, "CDP Neighbor IPv6 Address")
            self._cdp_neighbor['port'] = self.scrape_html_data(self.port_html, "CDP Neighbor Port")

        return self._cdp_neighbor

    def lldp_neighbor(self):
        if self._lldp_neighbor is None:
            self._lldp_neighbor = {}
            self._lldp_neighbor['device'] = self.scrape_html_data(self.port_html, "LLDP Neighbor Device ID")
            self._lldp_neighbor['ip'] = self.scrape_html_data(self.port_html, "LLDP Neighbor IP Address")
            self._lldp_neighbor['ipv6'] = self.scrape_html_data(self.port_html, "LLDP Neighbor IPv6 Address")
            self._lldp_neighbor['port'] = self.scrape_html_data(self.port_html, "LLDP Neighbor Port")

        return self._lldp_neighbor

    def status_messages(self):
        try:
            html = urlopen(f"{self.base_url}/CGI/Java/Serviceability?adapter=device.settings.status.messages",
                           context=ssl.SSLContext(), timeout=1).read().decode("utf-8")

        except:
            try:
                html = urlopen(f"{self.base_url}/stat.html", context=ssl.SSLContext(), timeout=1).read().decode("utf-8")
            except:
                return False

        html = html[
               html.find('<td VALIGN=top><DIV ALIGN=center>\n<TABLE BORDER="0" CELLSPACING="10" CELLPADDING="0">'):]
        html = re.sub("<[^>]*>", "\n", html).split('\n')

        logs = []
        for line in html:
            if not line == '':
                logs.append(line)

        return logs

    def debug(self):
        try:
            html = urlopen(f"{self.base_url}/CGI/Java/Serviceability?adapter=device.trace.display.alarm",
                           context=ssl.SSLContext(), timeout=1).read().decode("utf-8")
        except:
            try:
                html = urlopen(f"{self.base_url}/debug.html", context=ssl.SSLContext(), timeout=1).read().decode(
                    "utf-8")
            except:
                return False

        logs = []
        while html.find('<?xml version="1.0" encoding="UTF-8"?>') >= 0:
            html = html[html.find('<?xml version="1.0" encoding="UTF-8"?>') - 9:]
            log_date = html[:9]
            html = html[9:]
            xml_length = html.find('</x-cisco-alarm>') + 16

            logs.append([log_date, xmltodict.parse(html[:xml_length], dict_constructor=dict)])

            html = html[xml_length:]

        return logs

    def parse_streams(self, streamNumber):
        try:
            html = urlopen(
                f"{self.base_url}/CGI/Java/Serviceability?adapter=device.statistics.streaming.{streamNumber - 1}",
                context=ssl.SSLContext(),
                timeout=1).read().decode("utf-8")
        except:
            try:
                html = urlopen(f"{self.base_url}/StreamingStatistics?{streamNumber}",
                               context=ssl.SSLContext(),
                               timeout=1).read().decode("utf-8")
            except:
                return False

        stream = {}
        stream['Remote Address'] = self.scrape_html_data(html, "Remote Address").split('/')
        stream['Local Address'] = self.scrape_html_data(html, "Local Address<").split('/')
        stream['Start Time'] = self.scrape_html_data(html, "Start Time<")
        if self.scrape_html_data(html, "Is video") == "True":
            stream['video'] = True
        else:
            stream['video'] = False
        stream['Rcvr resolution'] = self.scrape_html_data(html, "Rcvr resolution<")
        stream['Sender resolution'] = self.scrape_html_data(html, "Sender resolution")
        stream['Stream Status'] = self.scrape_html_data(html, "Stream Status<")
        stream['Sender Packets'] = self.scrape_html_data(html, "Sender Packets<")
        stream['Sender Codec'] = self.scrape_html_data(html, "Sender Codec<")
        stream['Sender Reports Sent'] = self.scrape_html_data(html, "Sender Reports Sent<")
        stream['Sender Report Time Sent'] = self.scrape_html_data(html, "Sender Report Time Sent<")
        stream['Rcvr Lost Packets'] = self.scrape_html_data(html, "Rcvr Lost Packets<")
        stream['Avg Jitter'] = self.scrape_html_data(html, "Avg Jitter<")
        stream['Rcvr Codec'] = self.scrape_html_data(html, "Rcvr Codec<")
        if stream['Rcvr Codec'] == '':
            stream['Rcvr Codec'] = self.scrape_html_data(html, "Receiver Codec")
        stream['Rcvr Reports Sent'] = self.scrape_html_data(html, "Rcvr Reports Sent<")
        if stream['Rcvr Reports Sent'] == '':
            stream['Rcvr Reports Sent'] = self.scrape_html_data(html, "Receiver Reports Sent<")
        stream['Rcvr Report Time Sent'] = self.scrape_html_data(html, "Rcvr Report Time Sent<")
        if stream['Rcvr Report Time Sent'] == '':
            stream['Rcvr Report Time Sent'] = self.scrape_html_data(html, "Receiver Report Time Sent<")
        stream['Rcvr Packets'] = self.scrape_html_data(html, "Rcvr Packets<")
        if stream['Rcvr Packets'] == '':
            stream['Rcvr Packets'] = self.scrape_html_data(html, "Receiver Packets<")
        stream['MOS LQK'] = self.scrape_html_data(html, "MOS LQK<")
        stream['Avg MOS LQK'] = self.scrape_html_data(html, "Avg MOS LQK<")
        stream['Min MOS LQK'] = self.scrape_html_data(html, "Min MOS LQK<")
        stream['Max MOS LQK'] = self.scrape_html_data(html, "Max MOS LQK<")
        stream['Latency'] = self.scrape_html_data(html, "Latency<")
        stream['Max Jitter'] = self.scrape_html_data(html, "Max Jitter<")
        stream['Sender Size'] = self.scrape_html_data(html, "Sender Size<")
        stream['Sender Reports Received'] = self.scrape_html_data(html, "Sender Reports Received<")
        stream['Sender Report Time Received'] = self.scrape_html_data(html, "Sender Report Time Received<")
        stream['Rcvr Size'] = self.scrape_html_data(html, "Rcvr Size<")
        stream['Rcvr Discarded'] = self.scrape_html_data(html, "Rcvr Discarded<")
        stream['Rcvr Reports Received'] = self.scrape_html_data(html, "Rcvr Reports Received<")
        if stream['Rcvr Reports Received'] == '':
            stream['Rcvr Reports Received'] = self.scrape_html_data(html, "Receiver Reports Received<")
        stream['Rcvr Report Time Received'] = self.scrape_html_data(html, "Rcvr Report Time Received<")
        if stream['Rcvr Report Time Received'] == '':
            stream['Rcvr Report Time Received'] = self.scrape_html_data(html, "Receiver Report Time Received<")

        return stream

    def media_stream(self, stream):
        return self.parse_streams(stream)


"""

phoneList = ['172.20.130.254','172.20.130.253']
phones = []
for phone in phoneList:
	phones.append(Connect(phone))

for phone in phones:
	print(phone.details())
"""
# phone = Connect("172.20.130.254")
# print(phone.serial())
# print(phone.mwi())
# print(phone.timezone())
# print(phone.dhcpserver())
# print(phone.bootpserver())
# print(phone.dns())
# print(phone.cm_list())
# print(phone.tftp())
# print(phone.debug())
# print(phone.cdp_neighbor())
# print(phone.stream1())
# print(phone.detail())

class Status:
    def __init__(self, device):
        self.device = device

    def sccp(self) -> dict:
        status = self.device.exec("show sccp").splitlines()
        if status[0] != "SCCP Admin State: UP":
            return { "status": False }

        else:
            return_status = {
                "status": True,
                "interface": status[1].split(": ")[1].strip(),
                "ip": status[2].split(": ")[1].strip(),
                "port": status[3].split(": ")[1].strip(),
                "callmanager": [],
                "ports": []
            }
            i = 4
            while status[i].strip() != "":
                if "Call Manager:" in status[i]:
                    return_status['callmanager'].append(
                        {
                            "node": status[i].split(":")[1].split(",")[0].strip(),
                            "port": status[i].split(":")[2].strip(),
                            "priority": status[i+1].split(":")[1].split(",")[0].strip(),
                            "version": status[i+1].split(":")[2].split(",")[0].strip(),
                            "identifier": status[i+1].split(":")[3].strip()
                        }
                    )
                    i += 1

            i += 1
            while i <= len(status):
                port_info = {'codec'}
                while status[i].strip() != "":
                    if "Alg_Phone Oper State" in status[i]:
                        port_info['state'] = status[i].split(" ")[1].strip()
                        port_info['reason'] = status[i].split(" ")[-1].strip()
                        i += 1
                    if "Active Call Manager" in status[i]:
                        port_info['node']: status[i].split(":")[1].split(",")[0].strip()
                        port_info['port']: status[i].split(":")[2].strip()
                        i += 1
                    if "TCP Link Status" in status[i]:
                        port_info['link'] = status[i].split(":")[1].split(",")[0].strip()
                        port_info['device']: status[i].split(":")[2].strip()
                        i =+ 1
                    if "Reported Max Streams" in status[i]:
                        port_info['streams'] = {
                            "max": status[i].split(":")[1].split(",")[0].strip(),
                            "oss": status[i].split(":")[2].strip()
                        }
                        i += 1
                    if "Supported Codec" in status[i]:
                        port_info['codec'].append(
                            {
                                "codec": status[i].split(":")[1].split(",")[0].strip(),
                                "size": status[i].split(":")[2].strip()
                            }
                        )
                        i += 1
                return_status['ports'].append(port_info)

        return return_status

    def mgcp(self) -> dict:
        status = self.device.exec("show ccm-manager").splitlines()
        if "% Call Manager Application is not enabled" in status[0]:
            return { "status": False }
        else:
            return_status = {}

        return return_status
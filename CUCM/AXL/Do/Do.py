from zeep.helpers import serialize_object
from zeep.exceptions import Fault
import sys


class Do:
    def __init__(self, soap_client):
        self.client = soap_client

    def LdapSync(self, uuid):
        """
        Do LDAP Sync
        :param uuid: uuid
        :return: result dictionary
        """
        try:
            return self.client.doLdapSync(uuid=uuid, sync=True)
        except Fault as e:
            return e

    def ChangeDndStatus(self, **args):
        """
        Do Change DND Status
        :param userID:
        :param status:
        :return: result dictionary
        """
        try:
            return self.client.doChangeDNDStatus(**args)
        except Fault as e:
            return e

    def DeviceLogin(self, **args):
        """
        Do Device Login
        :param deviceName:
        :param userId:
        :param profileName:
        :return: result dictionary
        """
        try:
            return self.client.doDeviceLogin(**args)
        except Fault as e:
            return e

    def DeviceLogout(self, **args):
        """
        Do Device Logout
        :param device:
        :param userId:
        :return: result dictionary
        """
        try:
            return self.client.doDeviceLogout(**args)
        except Fault as e:
            return e

    def DeviceReset(self, name="", uuid=""):
        """
        Do Device Reset
        :param name: device name
        :param uuid: device uuid
        :return: result dictionary
        """
        if name != "" and uuid == "":
            try:
                return self.client.doDeviceReset(deviceName=name, isHardReset=True)
            except Fault as e:
                return e
        elif name == "" and uuid != "":
            try:
                return self.client.doDeviceReset(uuid=uuid, isHardReset=True)
            except Fault as e:
                return e

    def ResetSipTrunk(self, name="", uuid=""):
        """
        Reset SIP Trunk
        :param name: device name
        :param uuid: device uuid
        :return: result dictionary
        """
        if name != "" and uuid == "":
            try:
                return self.client.resetSipTrunk(name=name)
            except Fault as e:
                return e
        elif name == "" and uuid != "":
            try:
                return self.client.resetSipTrunk(uuid=uuid)
            except Fault as e:
                return e

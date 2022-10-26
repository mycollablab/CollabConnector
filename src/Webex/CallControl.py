import json
import requests
import sys
import time


class CallControl():
    access_token = None

    def __init__(self, access_token=None):
        if access_token is None:
            raise Exception("Must specify access token!")
        else:
            self.access_token = access_token

    def webex_rest(self, method="GET", uri="", data=None):
        headers = { "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.access_token}"}
        while True:
            try:
                if method in ["GET", "DELETE"]:
                    response = requests.request(method, f"https://webexapis.com/v1/telephony/calls/{uri}", headers=headers, params=data, verify=False)

                else:
                    response = requests.request(method, f"https://webexapis.com/v1/telephony/calls/{uri}", headers=headers, data=json.dumps(data), verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST GET - {err}")

            else:
                if response.status_code == 426:
                    print("API Throttling...", file=sys.stderr)
                    time.sleep(response.headers['Retry-After'])

                elif response.status_code == 204:
                    return True

                elif response.headers['Content-Type'].find("json") > -1 and 'errors' not in json.loads(response.text).keys():
                    return json.loads(response.text)

                else:
                    print(f"Error sending POST to Webex - {response.text}", file=sys.stderr)
                    return False

    def list_calls(self):
        return self.webex_rest()

    def call_details(self, call_id):
        return self.webex_rest("GET", data={'callId': call_id})

    def history(self, call_type=None):
        return self.webex_rest("GET", "history", data={'type': call_type})

    def dial(self, number):
        return self.webex_rest("POST", "dial", {'destination': number})

    def answer(self, call_id):
        return self.webex_rest("POST", "answer", {'callId': call_id})

    def reject(self, call_id):
        return self.webex_rest("POST", "reject", {'callId': call_id})

    def hangup(self, call_id):
        return self.webex_rest("POST", "hangup", {'callId': call_id})

    def hold(self, call_id):
        return self.webex_rest("POST", "hold", {'callId': call_id})

    def resume(self, call_id):
        return self.webex_rest("POST", "resume", {'callId': call_id})

    def divert(self, call_id, destination=None, to_voicemail=True):
        return self.webex_rest("POST", "divert", {'callId': call_id, 'destination': destination, 'toVoicemail': to_voicemail})

    def transfer(self, call_id_1, call_id_2):
        return self.webex_rest("POST", "transfer", {'callId1': call_id_1, 'callId2': call_id_2})

    def park(self, call_id, destination=None, is_group_park=True):
        return self.webex_rest("POST", "park", {'callId': call_id, 'destination': destination, 'isGroupPark': is_group_park})

    def retrieve(self, destination):
        return self.webex_rest("POST", "destination", {'destination': destination})


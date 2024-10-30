import time


class WhatsApp:
    def __init__(self, parent):
        self.parent = parent

    def send(self,
             app_id: str = "",
             destination: str = "",
             message: str = "",
             attachments: list = []
             ) -> dict:
        for attachment in attachments:
            payload = {
                "deliverychannel": "whatsapp",
                "channels": {"OTT-Messaging": {"wa": {
                    "type": attachment['type'],
                    "image": {"url": attachment['url']}
                }}},
                "destination": [{"waid": [destination]}],
                "appid": app_id
            }
            self.parent.rest.post("/resources/v1/messaging/", payload)

        payload = {
            "deliverychannel": "whatsapp",
            "channels": {"OTT-Messaging": {"wa": {
                "type": "text",
                "text": {"body": message}
            }}},
            "destination": [{"waid": [destination]}],
            "appid": app_id
        }

        return self.parent.rest.post("/resources/v1/messaging/", payload)

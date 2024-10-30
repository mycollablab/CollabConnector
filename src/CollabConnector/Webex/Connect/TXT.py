import time


class TXT:
    def __init__(self, parent):
        self.parent = parent

    def mms(self, destination: str,
            service_number: str,
            attachment: str,
            trans_id: str = "",
            message: str = "Be The match attempted to send an attachment",
            attachment_type: str = "image"
            ) -> dict:
        if attachment.lower().split(".")[-1] in ['gif', 'jpg', 'png', 'jpeg']:
            attachment_type = "image"
        elif attachment.lower().split(".")[-1] in ["vcf", "vcard"]:
            attachment_type = "contact"
        elif attachment.lower().split(".")[-1] in ["mp4"]:
            attachment_type = "video"
        elif attachment.lower().split(".")[-1] in ["mp3", "wav", "acc"]:
            attachment_type = "audio"
        elif attachment.lower().split(".")[-1] in ["pdf"]:
            attachment_type = "pdf"

        mms_body = {
                        "channel": "mms",
                        "from": service_number,
                        "to": [
                        {
                            "msisdn": [
                                destination
                            ],
                            "correlationId": trans_id
                        }],
                        "content":
                        {
                            "fallbacktext": "MMS attempt failed",
                            "attachments": [
                            {
                                "type": attachment_type,
                                "messageText": message,
                                "mediaUrl": attachment,
                                "duration": 5
                            }]
                        }
                    }
        try:
            connect_response = self.parent.rest.post("/v2/messages", data=mms_body)
        except Exception as err:
            raise Exception(f"Error sending MMS: {err}")
        else:
            return connect_response

    def sms(self, destination: str,
            service_number: str,
            message: str = "",
            trans_id: str = ""
            ) -> dict:

        sms_body = {
                        "channel": "sms",
                        "from": service_number,
                        "to": [
                        {
                            "msisdn": [
                                destination
                            ],
                            "correlationId": trans_id
                        }],
                        "content":
                        {
                            "text": message,
                            "type": "text"
                        }
                    }
        try:
            connect_response = self.parent.rest.post("/v2/messages", data=sms_body)
        except Exception as err:
            raise Exception(f"Error sending SMS: {err}")
        else:
            return connect_response

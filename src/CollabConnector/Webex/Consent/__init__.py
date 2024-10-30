from .REST import REST
import sys
import urllib.parse


class Connect:
    def __init__(self, key: str, group_id: str, base_url: str = "https://contactpolicy-us.imiconnect.io"):
        self.rest = REST(key)
        self.key = key
        self.group_id = group_id
        self.base_url = base_url

    def check(self, number) -> bool:
        try:
            consent = self.rest.get(f"/v1/groups/{self.group_id}/members?address={urllib.parse.quote_plus(number)}")[0]
        except Exception as err:
            print(f"Error obtaining consent: {err}", file=sys.stderr)
            return False
        else:
            if consent['consent'] is True:
                return True
            else:
                return False

    def list(self) -> list:
        try:
            consent = self.rest.get(f"/v1/groups/{self.group_id}/members")
        except Exception as err:
            print(f"Error obtaining consent: {err}", file=sys.stderr)
            return []
        else:
            return consent

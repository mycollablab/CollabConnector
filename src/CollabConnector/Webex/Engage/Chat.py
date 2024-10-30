import sys
from datetime import datetime


class Chat:
    def __init__(self, parent):
        self.parent = parent

    def list(self, team_id: int = None, status: str = "all") -> dict:
        if status.lower() == "all":
            if chats := self.parent.rest.get(f"/v3.0/chats",
                                             headers={"teamid": str(team_id if team_id else self.parent.team.id)}
                                             ):
                return chats['chats']
        elif status:
            return self.search(search_params={
                "condition": "AND",
                "rules": [
                    {
                        "param_name": "status",
                        "operator": "eq",
                        "param_value": status.lower()
                    }
                ]
            },
                team_id=team_id)
        return {}

    def get(self, chat_id: str, team_id: int = None) -> dict:
        if chat := self.parent.rest.get(f"/v3.0/chats/{chat_id}",
                                        headers={"teamid": str(team_id if team_id else self.parent.team.id)}
                                        ):
            return chat

        print(f"Error getting chat: {chat_id}", file=sys.stderr)
        return {}

    def search(self, search_params: dict = {}, team_id: int = None) -> dict:
        """
        search_params = {
                "condition": "AND",
                "rules": [
                    {
                        "condition": "OR",
                        "rules": [
                            {
                                "param_name": "mobile",
                                "operator": "eq",
                                "param_value": "44739273721"
                            },
                            {
                                "param_name": "facebook_psid",
                                "operator": "eq",
                                "param_value": "12983719823712"
                            }
                        ]
                    },
                    {
                        "param_name": "status",
                        "operator": "not_eq",
                        "param_value": "closed"
                    }
                ]
            }
        """
        if chat := self.parent.rest.post(f"/v3.0/chats/search",
                                         data=search_params
                                         # headers={"teamid": str(team_id if team_id else self.parent.team.id)}
                                         ):
            return chat
        print("Chats not found", file=sys.stderr)
        return {}

    def close(self, chat_id: str, outcome: str = "", team_id: int = None) -> bool:
        if chat := self.parent.rest.patch(f"/v3.0/chats/{chat_id}",
                                          headers={"teamid": str(team_id if team_id else self.parent.team.id)},
                                          params={"status": "closed",
                                                  "outcome": outcome}):
            if chat['status'] == "closed":
                return True

        print(f"Error closing chat: {chat_id}", file=sys.stderr)
        return False

    def onhold(self, chat_id: str, team_id: int = None) -> bool:
        if chat := self.parent.rest.patch(f"/v3.0/chats/{chat_id}",
                                          headers={"teamid": str(team_id if team_id else self.parent.team.id)},
                                          params={"status": "onhold"}):
            if chat['status'] == "onhold":
                return True

        print(f"Error holding chat: {chat_id}", file=sys.stderr)
        return False

    def queued(self, chat_id: str, team_id: int = None) -> bool:
        if chat := self.parent.rest.patch(f"/v3.0/chats/{chat_id}",
                                          headers={"teamid": str(team_id if team_id else self.parent.team.id)},
                                          params={"status": "queued"}):
            if chat['status'] == "queued":
                return True

        print(f"Error queuing chat: {chat_id}", file=sys.stderr)
        return False

    def picked(self, chat_id: str, agent_id: str, team_id: int = None) -> bool:
        if chat := self.parent.rest.patch(f"/v3.0/chats/{chat_id}",
                                          headers={"teamid": str(team_id if team_id else self.parent.team.id)},
                                          params={"status": "picked",
                                                  "assigned": agent_id}):
            if chat['status'] == "picked":
                return True

        print(f"Error assigning chat: {chat_id}", file=sys.stderr)
        return False

    def update(self, chat_id: str, update_data: dict = {}, team_id: int = None) -> dict:
        if chat := self.parent.rest.patch(f"/v3.0/chats/{chat_id}",
                                          headers={"teamid": str(team_id if team_id else self.parent.team.id)},
                                          params=update_data):
            return chat

        print(f"Error updating chat: {chat_id}", file=sys.stderr)
        return {}

    def alias(self, chat_id: str, alias: str, team_id: int = None) -> dict:
        if chat := self.parent.rest.patch(f"/v3.0/chats/{chat_id}",
                                          headers={"teamid": str(team_id if team_id else self.parent.team.id)},
                                          params={"alias_id": alias}):
            return chat

        print(f"Error updating chat alias_id: {chat_id}", file=sys.stderr)
        return {}

    def tag(self, chat_id: str, tags: list = [], team_id: int = None) -> dict:
        if chat := self.parent.rest.patch(f"/v3.0/chats/{chat_id}",
                                          headers={"teamid": str(team_id if team_id else self.parent.team.id)},
                                          params={"tags": tags if isinstance(tags, list) else [tags]}):
            return chat

        print(f"Error updating chat tags: {chat_id}", file=sys.stderr)
        return {}

    def create(self, chat: dict = {}, team_id: int = None, channel: str = "", asset_id: str = "", destination_id: str = "") -> dict:
        if chat or (team_id and channel and asset_id and destination_id):
            if not chat:
                chat = {
                    "channel": channel,
                    "asset_id": asset_id,
                    "destination_id": destination_id
                }

            try:
                chat = self.parent.rest.post(f"/v3.0/chats/{chat_id}",
                                             headers={"teamid": str(team_id if team_id else self.parent.team.id)},
                                             data={"tags": tags if isinstance(tags, list) else [tags]})
            except Exception as err:
                print(f"Error creating chat: {err}", file=sys.stderr)
            else:
                return chat
        else:
            print(f"Must supply team_id, channel, asset_id and destination_id", file=sys.stderr)
        return {}

    def append(self, chat_id: str,
               direction: str = "inbound",
               text: str = "",
               attachment: dict = {},
               timestamp: datetime = None,
               delivery_details: dict = {}
               ) -> dict:
        if timestamp and not isinstance(timestamp, datetime):
            raise Exception("Timestamp must be in `datetime.datetime` format")

        if timestamp is None:
            timestamp = f"{datetime.utcnow().isoformat(sep='T', timespec='milliseconds')}Z"
        message = {
            "type": direction,
            "text": text,
            "timestamp": str(timestamp)
        }

        if attachment:
            message['attachment'] = attachment
        if delivery_details:
            message['delivery_details'] = delivery_details

        if chat := self.parent.rest.post(f"/v3.0/chats/{chat_id}/messages",
                                         headers={},
                                         data=[message]):
            return chat

        print(f"Error appending chat message: {chat_id}", file=sys.stderr)
        return {}

import sys


class User:
    def __init__(self, parent):
        self.parent = parent

    def list(self, team: int = None) -> dict:
        if team and isinstance(team, str) and not team.isnumeric():
            team = self.parent.team.find(team)

        if users := self.parent.rest.get("/v3.0/users",
                                         headers={"teamid": str(team if team else self.parent.team.id)}
                                         ):
            return users['users']
        print(f"Error listing Users: team - {team}", file=sys.stderr)
        return {}

    def find(self, user: str = None, team: int = None) -> dict:
        if user is None:
            return self.list(team)

        for agent in self.list(team):
            if user.lower() == agent['email_id'].lower() or user.lower() == agent['login_id'].lower():
                return agent
        print(f"User not found: {user}", file=sys.stderr)
        return {}

    def get(self, user_id: str) -> dict:
        if user := self.parent.rest.get(f"/v3.0/users/{user_id}"):
            return user

        print(f"Error getting user: {user_id}", file=sys.stderr)
        return {}

    def create(self,
               user: dict = {},
               email: str = "",
               team: int = None,
               first_name: str = "",
               last_name: str = "",
               passwd: str = "P@ssw0rd!",
               role: str = "Team Agent",
               custom_attributes: dict = {},
               skill_attributes: dict = {},
               job_description: str = "Agent",
               login_using_email: bool = True,
               privileges: list = None,
               accepting_chats: list = None
               ) -> dict:
        if not user:
            user = {
                "first_name": first_name,
                "last_name": last_name,
                "login_id": email,
                "email_id": email,
                "password": passwd,
                "login_using_email": login_using_email,
                "job_description": job_description,
                "accepting_chats": [
                    {
                        "teamid": int(team if team else self.parent.team.id),
                        "value": "True"
                    }
                ],
                "privileges": [
                    {
                        "team_id": int(team),
                        "role": role  # Team Manager, Team Agent, Team Analyst
                    }
                ],
                "custom_attributes": custom_attributes,
                "skill_attributes": skill_attributes
            }
            if privileges:
                user['privileges'] = privileges
            if accepting_chats:
                user['accepting_chats'] = accepting_chats

        if user := self.parent.rest.post("/v3.0/users", data=user):
            return user
        else:
            print(f"Error creating user: {email}", file=sys.stderr)
            return {}

    def update(self,
               user_id: str,
               first_name: str = None,
               last_name: str = None,
               status: str = None,  # active/inactive
               custom_attributes: dict = None,
               skill_attributes: dict = None,
               job_description: str = None,
               login_using_email: bool = None
               ) -> dict:
        user = self.get(user_id)
        user_update = {}
        if first_name:
            user_update['first_name'] = first_name
        else:
            user_update['first_name'] = user['first_name']
        if last_name:
            user_update['last_name'] = last_name
        else:
            user_update['last_name'] = user['last_name']
        if status:
            user_update['status'] = status
        else:
            user_update['status'] = user['status']
        if custom_attributes:
            user_update['custom_attributes'] = custom_attributes
        else:
            user_update['custom_attributes'] = user['custom_attributes']
        if skill_attributes:
            user_update['skill_attributes'] = skill_attributes
        else:
            user_update['skill_attributes'] = user['skill_attributes']
        if job_description:
            user_update['job_description'] = job_description
        else:
            user_update['job_description'] = user['job_description']
        if login_using_email is not None:
            user_update['login_using_email'] = login_using_email
        else:
            user_update['login_using_email'] = user['login_using_email']

        if user_update := self.parent.rest.patch(f"/v3.0/users/{user_id}", params=user_update):
            return user_update
        else:
            print(f"Error updating user: {user_id}", file=sys.stderr)
            return {}

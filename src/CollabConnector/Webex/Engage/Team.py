import sys


class Team:
    def __init__(self, parent, default_team="Default"):
        self.parent = parent
        try:
            self.id, self.name = list(self.find(default_team).values())
        except:
            self.id, self.name = [0, 0]

    def set(self, team) -> bool:
        if isinstance(team, int) or team.isnumeric():
            team = self.get(int(team))
            self.id = team['id']
            self.name = team['name']
        else:
            self.id, self.name = list(self.find(team).values())
        return True

    def list(self) -> list:
        if teams := self.parent.rest.get(f"/v3.0/teams"):
            return teams['teams']
        return teams

    def find(self, name: str) -> dict:
        teams = self.parent.rest.get(f"/v3.0/teams")
        if teams and 'teams' in teams.keys():
            teams = teams['teams']
        if name is None:
            return teams

        for team in self.parent.rest.get(f"/v3.0/teams")['teams']:
            if name.lower() == team['name'].lower():
                return team
        print(f"Team not found: {name}", file=sys.stderr)
        return {}

    def get(self, team_id: int) -> dict:
        if team := self.parent.rest.get(f"/v3.0/teams/{team_id}"):
            return team

        print(f"Error getting team: {team_id}", file=sys.stderr)
        return {}

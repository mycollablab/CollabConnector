from .REST import REST
from .User import User
from .Team import Team
from .Chat import Chat


class Connect:
    def __init__(self, key=None, domain=None, default_team="Default"):
        self.rest = REST(key, domain)
        self.user = User(self)
        self.team = Team(self, default_team=default_team)
        self.chat = Chat(self)

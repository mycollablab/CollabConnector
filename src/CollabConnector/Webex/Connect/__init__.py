from .TXT import TXT
from .REST import REST
from .WhatsApp import WhatsApp


class Connect:
    def __init__(self, key=None):
        self.rest = REST(key)
        self.txt = TXT(self)
        self.whatsapp = WhatsApp(self)

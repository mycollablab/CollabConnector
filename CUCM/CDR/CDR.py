from .CDROnDemand import *


class CDR:
    def __init__(self, ipaddr, username, passwd):
        self.on_demand = CDROnDemand(ipaddr, username, passwd)


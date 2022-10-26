# CollabConnector
 Cisco Collab Connector Library

This library is made to try and be a single source for all Cisco Collab APIs (which can be lots). The goal is to unify requests and responces across different REST and SOAP APIs availble to make connecting to and scripting Collab tasks easier.  Hopefully.  Maybe.

Install:
```
pip3 install CollabConnector
```

Usage:
```commandline
from CollabConnector import CUCM
from CollabConnector import CUCX
from CollabConnector import UCCX
from CollabConnector.Webex import Webex

cucm = CUCM.Connect("10.10.10.10", "admin", "P@ssw0rd")
cucm.query("select count(*) from enduser")
[{'count': '5'}]
cucm.get.Phone(name="SEPAAAABBBBCCCC")
[{'name': 'SEP3C08F67A9618', 'description': 'Auto 1000', 'product': 'Cisco 7841', 'mod... }]

unity = CUCX.Connect("10.10.10.20", "admin", "P@ssw0rd")
unity.get("users")
[{'URI': '/vmrest/users/a151...123', 'ObjectId': 'a151...123', 'Alias': 'undeliverablemess... }]

ccx = UCCX.Connect("10.10.10.40", "admin", "P@ssw0rd")
ccx.get("application")
[{'@type': 'applicationXMLList', 'application': []}]

wbx = Webex.Connect(token)
wbx.get("/v1/people/me")
{'id': 'Y2l...mYTg', 'emails': ['jsn....com'], 'phoneNumbers': [{'type': 'work', 'value': '2001'}, ...}]
```
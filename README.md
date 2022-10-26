# CollabConnector
 Cisco Collab Connector Library

This library is made to try and be a single source for all Cisco Collab APIs (which can be lots). The goal is to unify requests and responces across different REST and SOAP APIs availble to make connecting to and scripting Collab tasks easier.  Hopefully.  Maybe.

```commandline
from CollabConnector import CUCM
from CollabConnector import CUCX
from CollabConnector import UCCX
from CollabConnector.Webex import ContactCenter

cucm = CUCM.Connect("10.10.10.10", "admin", "P@ssw0rd")
cucm.query("select count(*) from enduser")
cucm.get.Phone(name="SEPAAAABBBBCCCC")

unity = CUCX.Connect("10.10.10.20", "admin", "P@ssw0rd")
unity.get("users")

ccx = UCCX.Connect("10.10.10.40", "admin", "P@ssw0rd")
ccx.get("applications")

wbx = ContactCenter.Connect(token)
wbx.get("EntryPoints")
```
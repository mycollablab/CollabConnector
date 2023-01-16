# CollabConnector
 Cisco Collab Connector Library

This library is made to try and be a single source for all Cisco Collab APIs (which can be lots). The goal is to unify requests and responses across different REST and SOAP APIs availble to make connecting to and scripting Collab tasks easier.  Hopefully.  Maybe.

Install:
```
pip3 install CollabConnector
```

Usage:
```commandline
>>> from CollabConnector import CUCM
>>> from CollabConnector import CUCX
>>> from CollabConnector import UCCX
>>> from CollabConnector.Webex import Webex

>>> cucm = CUCM.Connect("10.10.10.10", "admin", "P@ssw0rd")
>>> cucm.query("select count(*) from enduser")
[{'count': '5'}]
>>> cucm.get.Phone(name="SEP3C08F67A9618")
[{'name': 'SEP3C08F67A9618', 'description': 'Auto 1000', 'product': 'Cisco 7841', 'mod... }]
>>> cucm.uds.get("version")
{'@uri': 'https://10.10.10.10:8443/cucm-uds/version', '@version': '12.5.1', 'version': '12.5.1', 'capabil... }]
>>> cucm.ast.cluster
{'cluster_name': 'StandAloneCluster', 'nodes': ['cucm-01.lab-01.mycollablab.org', 'cucm-02.lab-01.mycollablab.org'], 'service...}]
>>> cucm.serviceability.status("Cisco Tftp")
{'cucm-01.lab-01.mycollablab.org': {'Cisco Tftp': {'ServiceName': 'Cisco Tftp', 'ServiceStatus': 'Started', 'ReasonCode': -1, 'Rea...}]
>>> cucm.registration_status("SEP3C08F67A9618")
{'SEP3C08F67A9618': {'name': 'SEP3C08F67A9618', 'node': ..., 'firmware': 'sip78xx.12-7-1-0001-393', 'IPAddress': ..., 'dirn': '1000', 'status': 'Registered'}}

>>> unity = CUCX.Connect("10.10.10.20", "admin", "P@ssw0rd")
>>> unity.get("users")
[{'URI': '/vmrest/users/a151...123', 'ObjectId': 'a151...123', 'Alias': 'undeliverablemess... }]
>>> unity.get("/vmrest/users", DtmfAccessId="10*", sort="DtmfAccessId")
[{'URI': ..., 'ObjectId': ..., 'FirstName': '', 'LastName': '', 'Alias': '1000', 'DisplayName': '1000', 'EmailAddress': '', ... }]

>>> ccx = UCCX.Connect("10.10.10.40", "admin", "P@ssw0rd")
>>> ccx.get("application")
[{'@type': 'applicationXMLList', 'application': []}]

>>> wbx = Webex.Connect(token)
>>> wbx.get("/v1/people/me")
{'id': 'Y2l...mYTg', 'emails': ['jsn....com'], 'phoneNumbers': [{'type': 'work', 'value': '2001'}, ...}]
```

Notes:
The AXL SOAP API was generated based on the version 14 WSDL files and may not be complete or function depending on version. A version specific SOAP client is built at CollabConnector.CUCM.axl and can be leveraged as a backup as needed, however no post call treatment is made so soap responses will need to be sterilized etc if used.
```commandline
>>> from CollabConnector import CUCM

>>> cucm = CUCM.Connect("10.10.10.10", "admin", "P@ssw0rd")
>>> cucm.axl.getPhone(name="SEPAAAABBBBCCCC")
[{'name': 'SEP3C08F67A9618', 'description': 'Auto 1000', 'product': 'Cisco 7841', 'mod... }]
```
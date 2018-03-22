#!/usr/bin/env python

import json
from napalm import get_network_driver
ios_driver = get_network_driver('ios')
HOST = ios_driver('192.168.122.1','dilraj','dilraj')
HOST.open()

output = HOST.get_facts()
print (json.dumps(output, indent=4))

output = HOST.get_interfaces()
print (json.dumps(output, sort_keys=True, indent=4))

output = HOST.get_interfaces_counters()
print (json.dumps(output, sort_keys=True,  indent=4))

HOST.close()

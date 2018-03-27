#!/usr/bin/env python

from netmiko import ConnectHandler

SW1 = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.200',
    'username':'dilraj',
    'password':'dilraj'
    }

SW2 = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.201',
    'username':'dilraj',
    'password':'dilraj'
    }

SW3 = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.202',
    'username':'dilraj',
    'password':'dilraj'
    }

all_devices = [SW1,SW2,SW3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range(2,11):
        output = net_connect.send_config_set('no vlan ' + str(n))
        print output

#!/usr/bin/env python

from netmiko import ConnectHandler

ios = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.200',
    'username':'dilraj',
    'password':'dilraj'
    }

net_connect = ConnectHandler(**ios)
print ('Connected ', ios['ip'], ' via SSH')
output = net_connect.send_command('sh ip int brief')
print output

config_commands = ['int loop 1', 'ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print output

for n in range (2,11):
    config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output

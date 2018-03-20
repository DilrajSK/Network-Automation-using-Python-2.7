#!/usr/bin/env python

import sys
import getpass
import telnetlib

username = raw_input ('Enter the Telnet username: ')
password=getpass.getpass()

f=open('myswitches')

for line in f:
    HOST = line

    tn=telnetlib.Telnet(HOST)

    tn.read_until('Username: ')
    tn.write(username + '\n')

    if password:
        tn.read_until('Password: ')
        tn.write(password + '\n')

    tn.write('conf t\n')

    for i in range(2,11):
        tn.write('vlan ' + str(i) + '\n')
        tn.write('name PythonVLAN_' + str(i) + '\n')
    
    tn.write('exit\n')
    tn.write('banner motd & ************* WELCOME *********** &\n')
    tn.write('end\n')
    tn.write('write\n')
    tn.write('exit\n')

    print tn.read_all()

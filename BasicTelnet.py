#!/usr/bin/env python

import getpass
import sys
import telnetlib

HOST='192.168.1.200'
user=raw_input('Enter username: ')
password=getpass.getpass()

tel=telnetlib.Telnet(HOST)

tel.read_until('Username: ')
tel.write(user + '\n')

if password:
	tel.read_until('Password: ')
	tel.write(password + '\n')

tel.write('enable')
tel.write('cisco\n')
tel.write('conf t\n')
tel.write('banner motd @ **Welcome** @\n')
tel.write('end\n')
tel.write('wr\n')
tel.write('exit\n')

print tel.read_all()
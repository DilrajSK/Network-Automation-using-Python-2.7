#! /usr/bin/env python

import telnetlib
import getpass

user = raw_input ('Enter Username: ')
password = getpass.getpass()

f = open('myswitches')

for line in f:
    print 'Getting running-config for ' + line
    HOST = line.strip()
    tel=telnetlib.Telnet(HOST)

    tel.read_until('Username: ')
    tel.write(user + '\n')
    if password:
        tel.read_until('Password: ')
        tel.write(password + '\n')

    tel.write('enable\n')
    tel.write('terminal length 0\n')
    tel.write('show run\n')
    tel.write('exit\n')

    readoutput = tel.read_all()
    saveoutput = open('Switch' + HOST , 'w')
    saveoutput.write(readoutput)
    saveoutput.close

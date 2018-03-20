#!/usr/bin/env python

import paramiko
import time
import getpass

HOST = '192.168.1.200'
username = raw_input ('Enter username: ')
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST, username=username, password=password)

print 'Successful SSH Connection ',HOST

remote_connection = ssh_client.invoke_shell()

remote_connection.send('conf t\n')

for n in range (2,11):
    remote_connection.send('vlan ' + str (n) + '\n')
    remote_connection.send('name Python_VLAN_' + str (n) + '\n')
    time.sleep(0.5)

remote_connection.send('end\n')

time.sleep(1)
print remote_connection.recv(65535)

ssh_client.close

#!/usr/bin/env python

import os

ssh_list = []
ssh_list_counter = 0
ssh_hosts = {}

#logins file needs this syntax: name login ip
#each record on separarate line

logins = open('logins')
#readlines
x = logins.readlines()
for i in range(len(x)):
    a = x[i].split()
    name = a[0]
    login = a[1]
    ip = a[2]
    ssh_hosts[name] = login, ip

#create a list from ssh_hosts keys
for k in ssh_hosts.keys():
    ssh_list.append(k)

ssh_list = sorted(ssh_list)

print '\n', ' SSH MANAGER '.center(25, '~'), '\n'

#use above list to print out all hosts
for i in ssh_list:
    x = ssh_hosts.get(i)
    print str(ssh_list_counter) + '. ' + i + ' - ' + x[1]
    ssh_list_counter += 1

try:
    index = int(raw_input('\nSelect host to login [0 - %s]: ' % (len(ssh_list) -
                                                           1)))

#create var 'v' that is a value - list - of key (ssh_list[index])
    v =  ssh_hosts.get(ssh_list[index])

#create string for ssh login
    login = 'ssh ' + v[0] + '@' + v[1]

    print '\nConnecting to', ssh_list[index], ' \n'
    os.system('date')

#initiate ssh login
    os.system(login)

except KeyboardInterrupt:
    print '\n\nCTRL + C > Exiting\n'

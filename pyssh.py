#!/usr/bin/env python

import os

ssh_list = []
ssh_list_counter = 0

'''Put the 'hostname'(printed name):['login', 'ip_address'] in ssh_hosts
dictionary.''' #

ssh_hosts = {'my_own':['tns', '127.0.0.1'],
             'my_own_2':['tns', '128.0.0.1']
            }

#create a list from ssh_hosts keys
for k in ssh_hosts.keys():
    ssh_list.append(k)

print '\nSelect host to ssh to:\n'

#use above list to print out all hosts
for i in ssh_list:
    print str(ssh_list_counter) + '. ' + i
    ssh_list_counter += 1

index = int(raw_input('\nSelect host to login [0 - %s]: ' % (len(ssh_list) -
                                                           1)))

#create var 'v' that is a value - list - of key (ssh_list[index]) 
v =  ssh_hosts.get(ssh_list[index]) 

#create string for ssh login
login = 'ssh ' + v[0] + '@' + v[1]

print '\nLogging to', ssh_list[index], ' \n'
os.system('date')

#initiate ssh login
os.system(login)

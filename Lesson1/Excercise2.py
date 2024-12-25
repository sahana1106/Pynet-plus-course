#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

devices = [

{
    "host":'nxos1.lasthop.io',
    "username":'pyclass',
    "password":getpass(), 
    "device_type":'cisco_nxos'
},

{
    "host":'nxos2.lasthop.io',
    "username":'pyclass',
    "password":getpass(),
    "device_type":'cisco_nxos'
}
]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())


from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
}

nxos2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
}

for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file(config_file='my_changes.txt')
    print(output)
    net_connect.save_config()
    net_connect.disconnect()



#net_connect = ConnectHandler(**device1)
#print(net_connect.find_prompt())

#output = net_connect.send_config_from_file(config_file='my_changes.txt')
#print(output)

#net_connect = ConnectHandler(**device2)
#print(net_connect.find_prompt())

#output = net_connect.send_config_from_file(config_file='my_changes.txt')
#print(output)



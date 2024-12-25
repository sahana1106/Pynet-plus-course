from netmiko import ConnectHandler
from getpass import getpass


device = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',

}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("\n" "show version", use_textfsm=True)
out_lldp = net_connect.send_command("\n" "show lldp neighbors", use_textfsm=True)

print(output)
print(out_lldp)
data = type(out_lldp)
print(data)

neighbor = out_lldp[0]['neighbor_interface']
print(neighbor)

net_connect.disconnect()


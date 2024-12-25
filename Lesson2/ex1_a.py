from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios'
    
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())


command = "ping"
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
#print("Output after sending ping command:")
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)

print(output)

net_connect.disconnect()



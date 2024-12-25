from netmiko import ConnectHandler
from getpass import getpass
import time


password = getpass()

device = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "secret": password,
    "device_type": 'cisco_ios',
    "session_log": 'session_log.txt',
}

net_connect = ConnectHandler(**device)
output = net_connect.find_prompt()
print(output)


output = net_connect.config_mode()
#output += net_connect.find_prompt()
print(output)

output = net_connect.exit_config_mode()
#output += net_connect.find_prompt()
print(output)

output = net_connect.write_channel("disable\n")
time.sleep(2)
output = net_connect.read_channel()
print(output)

output = net_connect.enable()
output = net_connect.find_prompt()
print(output)


net_connect.disconnect()
print()

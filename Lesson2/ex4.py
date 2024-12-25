from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "fast_cli": False,    
}

start_time = datetime.now()
print(f"the process starts now: {start_time}")
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
]

output = net_connect.send_config_set(cfg)
print(output)
end_time = datetime.now()
print(f"the process ends now: {end_time}")
execution_time = end_time - start_time
print(f"the execution time for adding the config without fast cli: {execution_time}")

ping = net_connect.send_command("ping google.com")
print(ping)

net_connect.disconnect()


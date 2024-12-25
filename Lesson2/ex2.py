from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "global_delay_factor": 2,
    "fast_cli": False,
}

start_time = datetime.now()
print(f"the following starts now: {start_time}")


net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

output = net_connect.send_command("show lldp neighbors detail", use_textfsm=True)

print(output)
end_time = datetime.now()
print(f"this command without delay factor finished now: {end_time}")
execution_time = end_time - start_time
print(f"Execution time is :{execution_time}")


start_time = datetime.now()
print(f"The beginning of the command: {start_time}")
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
print(output)

end_time = datetime.now()
print(f"The operations command with delay factor ends now: {end_time}")

execution_time = end_time - start_time
print(f"Execution time: {execution_time}")

net_connect.disconnect()

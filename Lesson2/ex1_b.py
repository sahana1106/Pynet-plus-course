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
output = net_connect.send_command(command, expect_string=r"Protocol")
#print("Output after sending ping command:")
output += net_connect.send_command("ip", expect_string=r"Target IP address")
output += net_connect.send_command("8.8.8.8", expect_string=r"Repeat count")
output += net_connect.send_command("5", expect_string=r"Datagram size")
output += net_connect.send_command("100", expect_string=r"Timeout in seconds")
output += net_connect.send_command("2", expect_string=r"Extended commands")
output += net_connect.send_command("n", expect_string=r"Sweep range of sizes")
output += net_connect.send_command("n", expect_string=r"Type escape sequence to abort")

print(output)

net_connect.disconnect()



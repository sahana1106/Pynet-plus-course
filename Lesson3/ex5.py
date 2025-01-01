import yaml
from netmiko import ConnectHandler
from os import path

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    out_file = yaml.load(f, Loader=yaml.SafeLoader)

device = out_file["cisco3"]

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

import pyeapi
from getpass import getpass
from pprint import pprint


connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable(["show arp"])
output = output[0]['result']['ipV4Neighbors']

for arp_entry in output:
    mac_address = arp_entry["hwAddress"]
    ip_address = arp_entry["address"]
    pprint("{:^15}{:^5}{:^15}".format(ip_address, "-->", mac_address))

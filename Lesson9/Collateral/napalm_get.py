#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cisco3 = dict(
    hostname = "cisco3.lasthop.io",
    device_type = "ios",
    username = "pyclass",
    password = getpass(),
    optional_args = {},
)

nxos1 = dict(
    hostname = "nxos1.lasthop.io",
    device_type = "nxos1",
    username = "pyclass",
    password = getpass(),
    optional_args = {"port": 8443},
)

eos1 = dict(
    hostname = "arista1.lasthop.io",
    device_type = "eos",
    username = "pyclass",
    password = getpass(),
)

my_device = cisco3

device_type = my_device.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**my_device)

print()
device.open()
print()

output = device.get_facts()
# output = device.get_interfaces()
# output = device.get_lldp_neighbors()
pprint(output)
print()

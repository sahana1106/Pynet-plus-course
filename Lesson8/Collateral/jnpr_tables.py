import os
from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from getpass import getpass

# from pprint import pprint
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

a_device = Device(host="srx2.lasthop.io", user="pyclass", password=password)
a_device.open()

arp_entries = ArpTable(a_device)
arp_entries.get()



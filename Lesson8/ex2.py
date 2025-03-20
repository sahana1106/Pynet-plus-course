from pprint import pprint
import sys

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

from jnpr_devices import srx2

def check_connected(device):
    print("\n\n")
    if device.connected:
        print(f"Device {device.hostname} is connected!")
    else:
        print(f"Device {device.hostname} failed to connect :(.")
        sys.exit(1)

def gather_routes(device):
    routes = RouteTable(device)
    routes.get()
    return routes


def gather_arp_table(device):
    arp = ArpTable(device)
    arp.get()
    return arp


def print_output(dev, routes, arp):
    print()
    print("Print out desired output from device, route and arp information")
    device = {}
    device["hostname"] = dev.hostname
    device["connected_port"] = dev.port
    device["connected_user"] = dev.user
    device["route_table"] = routes.items()
    device["arp_table"] = arp.items()
    pprint(device)
    print()

if __name__ == "__main__":
    
    device = Device(**srx2)
    device.open()

    check_connected(device)
    routes = gather_routes(device)
    arp = gather_arp_table(device)

    print_output(device, routes, arp)

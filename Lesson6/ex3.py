import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices, output_printer
from pprint import pprint

def main():

    devices = yaml_load_devices()
    password = getpass()

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        pprint(output)
        

if __name__ == "__main__":
    main()

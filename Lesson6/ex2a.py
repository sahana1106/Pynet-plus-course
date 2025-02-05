import pyeapi
import yaml
from getpass import getpass
from pprint import pprint

def load_devices(filename="arista_devices.yml"):
    with open(filename) as f:
        return yaml.safe_load(f)


def main():

    devices = load_devices("arista_devices.yml")
    device_dict = devices['arista4']
    device_dict['password'] = getpass()

    connection = pyeapi.client.connect(**device_dict)

    device = pyeapi.client.Node(connection)

    output = device.enable("show ip arp")

    arp_table = output[0]['result']['ipV4Neighbors']

    print("\nIP Address to MAC Address mappings:")
    print("-" * 50)

    for entry in arp_table:
        print(f"IP: {entry['address']:<15} -> MAC: {entry['hwAddress']}")

if __name__ == "__main__":
    main()

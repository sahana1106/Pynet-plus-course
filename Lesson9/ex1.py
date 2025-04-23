from napalm import get_network_driver
from pprint import pprint
from my_devices import network_devices

def open_napalm_connection(device):
    """Function to open napalm connection and return connection object"""
    # Copy dictionary to ensure original object is not modified.
    device = device.copy()
    platform = device.pop("platform")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn

if __name__ == "__main__": 
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    print("\n\n")
    print("Print facts for all devices in connections list")
    for conn in connections:
        print()
        print(conn)
        print("{} facts:". format(conn.platform))
        print(conn.get_facts())
        conn.close()
    print("\n\n")


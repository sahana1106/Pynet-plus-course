from pprint import pprint
from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup


if __name__ == "__main__":
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    print("\n\n")
    print("Print arp table of all devices")
    for conn in connections:
        pprint(conn.get_arp_table())


    print("\n\n")
    print("Print NTP peers if available")
    for conn in connections:
        try:
            pprint(conn.get_ntp_peers())
        except NotImplementedError:
            print(
                "NTP Peers Getter not implemented for device type {}".format(conn.platform)
            )

    print("\n\n")
    print("Capture and write backups to disk")
    for conn in connections:
        create_backup(conn)
        conn.close()
    print("\n\n")


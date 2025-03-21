import yaml

def yaml_load_devices(filename="arista_devices.yml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)

def output_printer(arp_list):
    print()
    for arp_entry in arp_list:
        mac_address = arp_entry["hwAddress"]
        ip_address = arp_entry["address"]
        print("{:^15}{:^5}{:^15}".format(ip_address, "--->", mac_address))
    print()

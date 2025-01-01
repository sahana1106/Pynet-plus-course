import json

filename = input("Enter a filename: ")
with open(filename) as f:
    out_file = json.load(f)

arp_dict = {}

arp_entries = out_file["ipV4Neighbors"]

for entry in arp_entries:
    ip_addr = entry['address']
    mac_addr = entry['hwAddress']
    arp_dict[ip_addr] = mac_addr

print(arp_dict)

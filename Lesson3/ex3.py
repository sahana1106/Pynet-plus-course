import json
from pprint import pprint


filename = input("Please enter a filename: ")
with open(filename) as f:
    out_file = json.load(f)

ipv4_list = []

ipv6_list = []

for intf, ipaddr in out_file.items():
    for ipv4_or_ipv6, addr_info in ipaddr.items():
        for ip_addr, prefix_dict in addr_info.items():
            prefix_length = prefix_dict["prefix_length"]
            if ipv4_or_ipv6 == "ipv4":
                ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
            elif ipv4_or_ipv6 == "ipv6":
                ipv6_list.append("{}/{}".format(ip_addr, prefix_length))


print("IPv4 Addresses: {}\n".format(ipv4_list))
print("IPv6 Addresses: {}\n".format(ipv6_list))




from pprint import pprint

arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

arp_list = []

lines = arp_data.strip().splitlines()

for line in lines[1:]:
    parts = line.split()
    arp_entry = {
        "ip_addr": parts[1],
        "mac_addr": parts[3],
        "interface": parts[5],
    }

    arp_list.append(arp_entry)

pprint(arp_list)

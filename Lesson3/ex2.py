import yaml
from pprint import pprint


cisco3 = {"device": "cisco3", "hostname": "cisco3.lasthop.io"}

cisco4 = {"device": "cisco4", "hostname": "cisco4.lasthop.io"}

nexus01 = {"device": "nexus01", "hostname": "nxos1.lasthop.io"}

nexus02 ={"device": "nexus02", "hostname": "nxos2.lasthop.io"}

devices = [cisco3, cisco4, nexus01, nexus02]

for device in devices:
    device["username"] = "cisco"
    device["password"]= "cisco123"

print()
pprint(devices)
print()


filename = "outfile.yml"
with open(filename, "w") as f:
    yaml.dump(devices, f, default_flow_style=False)



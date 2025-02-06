from __future__ import unicode_literals, print_function
from pprint import pprint
import xmltodict

with open("show_security_zones.xml") as file:
    show_security_zones = xmltodict.parse(file.read())

print("Print the new variable and its type")
pprint(show_security_zones)
print(type(show_security_zones))

print("Print out index and name of the security zones")
zones = show_security_zones["zones-information"]["zones-security"]

for index, zone in enumerate(zones):
    print(f"Security Zone #{index + 1}: {zone['zones-security-zonename']}")

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

interface_vars = {
    "interface_name_nxos1": "Ethernet1/1",
    "ip_address_nxos1": "10.1.100.1",
    "netmask_nxos1": 24,
    "interface_name_nxos2": "Ethernet1/1",
    "ip_address_nxos2": "10.1.100.2",
    "netmask_nxos2": 24,
}

template_file = "int_conf.j2"
template = env.get_template(template_file)
output = template.render(**interface_vars)
print(output)

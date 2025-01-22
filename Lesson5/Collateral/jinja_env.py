from __future__ import unicode_literals, print_function
from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined

#env = Environment()
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./templates/'])
#env.loader = FileSystemLoader('.')

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "10.20.30.1",
}

template_file = 'bgp_config.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

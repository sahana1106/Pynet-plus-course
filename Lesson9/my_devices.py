import os
from getpass import getpass

username = "pyclass"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "platform": "ios",
}

arista1 = {
    "hostname": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "eos",
}


nxos1 = {
    "hostname": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "eos",
}

network_devices = [cisco3, arista1]


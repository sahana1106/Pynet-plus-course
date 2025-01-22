from getpass import getpass

password = getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
    "timeout": 120,
    "fast_cli": False,
    "read_timeout_override": 90,
}
nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
    "timeout": 120,
    "fast_cli": False,    
    "read_timeout_override": 90,
}

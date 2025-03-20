from jnpr.junos import Device
from lxml import etree
from jnpr_devices import srx2

dev = Device(**srx2)
dev.open()

print()
print("Gather show version information using rpc: print output")
sh_ver_xml = dev.rpc.get_software_information()
print(etree.tostring(sh_ver_xml, encoding="unicode"))

print()
print("Get terse show interface information from rpc call; print output")
sh_int_terse = dev.rpc.get_interface_information(terse=True)
print(etree.tostring(sh_int_terse, encoding="unicode"))

print()
print("Get terse show interface info for fe-0/0/7; pretty print output")
sh_int_terse_fe007 = dev.rpc.get_interface_information(
    interface_name="fe-0/0/7", terse=True, normalize=True
)

print(etree.tostring(sh_int_terse_fe007, pretty_print=True, encoding="unicode"))
print()


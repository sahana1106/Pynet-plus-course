Value MAC_ADDRESS ([0-9a-f:]+)
Value IP_ADDRESS (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value NAME (\S+)
Value INTERFACE (\S+)

Start
  ^MAC Address.*Flags.*$$ -> ARPTable

ARPTable
  ^${MAC_ADDRESS}\s+${IP_ADDRESS}\s+${NAME}\s+${INTERFACE}\s+ -> Record





#MAC Address       Address         Name                      Interface           Flags
#00:62:ec:29:70:fe 10.220.88.1     10.220.88.1               vlan.0              none
#c8:9c:1d:ea:0e:b6 10.220.88.20    10.220.88.20              vlan.0              none
#52:54:ab:a8:9a:ea 10.220.88.28    10.220.88.28              vlan.0              none
#52:54:ab:be:5b:7b 10.220.88.29    10.220.88.29              vlan.0              none
#52:54:ab:71:e1:19 10.220.88.30    10.220.88.30              vlan.0              none
#64:64:9b:e8:08:c8 10.220.88.39    10.220.88.39              vlan.0              none
#Total entries: 6

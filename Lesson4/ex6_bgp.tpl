Value Filldown BGP_ROUTER_ID (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value Filldown LOCAL_AS (\d+)
Value PEER_IP (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value REMOTE_AS (\d{4,6})
Value UP_DOWN (\S+)
Value STATE_PFXRCD (\S+)


Start
  ^BGP router identifier ${BGP_ROUTER_ID}, local AS number ${LOCAL_AS}\s*$$
  ^Neighbor.*State.PfxRcd.*$$ -> BGPTable

BGPTable
  ^${PEER_IP}\s+4\s+${REMOTE_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${STATE_PFXRCD} -> Record


EOF












#BGP router identifier 128.223.51.103, local AS number 6447
#BGP table version is 24508298, main routing table version 24508298
#776391 network entries using 192544968 bytes of memory
#24595707 path entries using 2951484840 bytes of memory
#3679950/131072 BGP path/bestpath attribute entries using 912627600 bytes of memory
#3388736 BGP AS-PATH entries using 170415118 bytes of memory
#3 BGP ATTR_SET entries using 120 bytes of memory
#121765 BGP community entries using 14715500 bytes of memory
#1074 BGP extended community entries using 67730 bytes of memory
#0 BGP route-map cache entries using 0 bytes of memory
#0 BGP filter-list cache entries using 0 bytes of memory
#BGP using 4241855756 total bytes of memory
#BGP activity 1842235/998824 prefixes, 95031319/69222218 paths, scan interval 60 secs
#
#Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
#4.69.184.193    4         3356 942101852   70242 24508270    0    0 4w5d       720787
#5.101.110.2     4        14061       0       0        1    0    0 never    Active
#12.0.1.63       4         7018 20129803   53213 24508270    0    0 4w5d       722337
#37.139.139.0    4        57866 21976076  103582 24508270    0    0 4w4d       723278
#64.71.137.241   4         6939 7493759   53210 24508270    0    0 4w5d       748249
#66.59.190.221   4         6539       0       0        1    0    0 never    Active
#66.110.0.86     4         6453       0       0        1    0    0 never    Idle
#66.185.128.48   4         1668       0       0        1    0    0 never    Active
#69.31.111.244   4         4436       0       0        1    0    0 never    Active
#80.241.176.31   4        20771       0       0        1    0    0 never    Active
#89.149.178.10   4         3257 4554910   10722 24508270    0    0 4w5d       721998
#91.218.184.60   4        49788 11604600   40029 24508270    0    0 4w5d       724514
#94.142.247.3    4         8283 59677087   36962 24508270    0    0 4w3d       723358

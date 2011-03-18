import re
from time import struct_time

maintStart = 0040
maintStop = 0115

now = time.struct_time(3,4)
maintStart = 0045
maintStop = 0105

print now

if re.search('threshold of Relay Position Change', evt.summary):
    repDelay = device.getRRDValue('check_mysql_slave_time')
    if repDelay > 0:
        evt._action = "drop"
    elif now >= maintStart and now <= maintStop:
        evt.severity = 3
                                


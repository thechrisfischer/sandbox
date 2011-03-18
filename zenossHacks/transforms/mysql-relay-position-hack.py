import re
from time import strftime, localtime

now = strftime("%H%M", localtime())
maintStart = 0045
maintStop = 0105

if re.search('threshold of Relay Position Change', evt.summary):
    repDelay = device.getRRDValue('check_mysql_slave_time')
    if repDelay > 0:
        evt._action = "drop"
    elif now >= maintStart and now <= maintStop:
        evt.severity = 3
                                


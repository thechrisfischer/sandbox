#!/usr/bin/env python

import sys

user_options = sys.argv[1]
shares_outstanding = 48000000

user_percent = float(user_options) * 100 / shares_outstanding
user_bps = float(user_percent) * 100 
print "percent " + str(user_percent) + "\n"
print "basis points " + str(user_bps) 


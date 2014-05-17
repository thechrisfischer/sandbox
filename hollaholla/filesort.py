#!/usr/bin/env python

#TODO - make the check for directories work vs check for file or dir

import os
import re
import string

cur_dir = os.getcwd()
shows = ['vikings', 'castle', 'archer']

def show_match(show, showdir):
  for dirpath, dirname, filenames in  os.walk(cur_dir, followlinks = True):
    for name in filenames:
      fullname = os.path.join(dirpath, name)
      m = re.search(show, name)
      if m:
        os.rename(fullname, showdir + "/" + name)
        print "moved ", fullname, "to ", showdir
  return


for show in shows:
  showdir = cur_dir + "/" + show
  if not os.access(showdir, os.F_OK):
    os.mkdir(show)
  show_match(show, showdir)


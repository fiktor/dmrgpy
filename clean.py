#!/usr/bin/python
        
# SPDX-License-Identifier: GPL-3.0-or-later


import os


pwd = os.getcwd()
for d in os.walk("."): # loop over subdirectories
  os.chdir(d[0])
  os.system("rm -rf .mpsfolder")
  os.system("rm -f ERROR")
  os.system("rm -f *.OUT")
  os.system("rm -rf .pychainfolder")
  os.system("rm -rf .dmrgfolder")
  os.chdir(pwd)


#!/usr/bin/env python

import os
import sys
import time

for ID in open(sys.argv[1], 'r'):
	ID = ID.replace("\n","")
	print(ID + " is operating !")
	try:
		os.system("python goodinfo.py " + ID)
		time.sleep(300)
	except:
		print("We Got Some Error!")
		continue
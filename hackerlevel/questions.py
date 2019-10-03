#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys

flagfile= open('/home/hackerlevel/flag.txt', 'r')
ctf_flag = flagfile.readline()

#print("\nhint: A true hacker uses pwn too\n")

#print("The flag looks like FLAG{...} \n")

total=0
for i in range(0,10000):
	x = random.randrange(0,1000)
	y = str(x).encode('base64')
	y = y[:-1]
	y+='=='
	print str(y)
	sys.stdout.flush()
	ans = raw_input()
	if str(ans) == str(x):
		total+=1

if total == 10000:
		print "You are a true hacker, you hacker level is over 9k. Here is your prize.\n"
		sys.stdout.flush()
		print ctf_flag
		sys.stdout.flush()
else:
		print "Nope"
		sys.stdout.flush()


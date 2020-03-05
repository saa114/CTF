import os

flagfile = open("/home/escape/flag.txt", "r")
ctf_flag = flagfile.readline().strip()

print "\nCan you break out of jail? nc 127.0.0.1 17777"
print "Hint: You might get out early, based on your evaluation. \n"
print ("\nThe flag looks like FLAG{...} \n")




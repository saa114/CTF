import os

flagfile = open("/home/stolen-pw/flag.txt", "r")
ctf_flag = flagfile.readline().strip()

print "\nCan you crack a password for me, if I can log on I will give you the flag. Connect here: nc 127.0.0.1 20202\n"
print "Hint: Luckily these 5 MaD people weren't salty. \n"
print ("\nThe flag looks like FLAG{...} \n")




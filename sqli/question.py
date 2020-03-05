import os

flagfile = open('/home/sqli/flag.txt','r')
ctf_flag = flagfile.readline().strip()

print "\nCan you log into the system? http://127.0.0.1:10811/ \n"
print "Hint:  There is a databse storing login information, maybe it can be injected.\n "

while True:
    user_flag = raw_input("\nThe flag looks like FLAG{...} \nInsert here:")

    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;

    else:
        print "Nope. Try again \n"



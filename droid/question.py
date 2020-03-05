import os

flagfile = open("/home/droid/flag.txt", "r")
ctf_flag = flagfile.readline().strip()

print "\nCan you find the flag in this file: http://localhost:60000/ReverseMe.apk ?"
print "You might need this tool: http://localhost:60000/tools.zip \n"
print "Hint: Tools are helpful. \n"

while True:
    user_flag = raw_input("\nThe flag looks like FLAG{...} \nInsert here: ")

    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;
    
    else:
        print "Nope. Try again \n"




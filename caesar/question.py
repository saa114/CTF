import os

flagfile = open("/home/caesar/flag.txt", "r")
ctf_flag = flagfile.readline().strip()

print "\nCan you find the flag in http://localhost:45000/file.enc "
print "Hint: There are two ingredients in this salad.\n"

while True:
    user_flag = raw_input("\nThe flag looks like FLAG{...} \nInsert here: ")

    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;
    
    else:
        print "Nope. Try again \n"




import os

flagfile = open('/home/php/flag.txt','r')
ctf_flag = flagfile.readline().strip()

print "Go here:  http://localhost:10800"
print "Hint: Make the buffers flow."

while True:
    user_flag = raw_input("\nThe flag looks like FLAG{...} \nInsert here:")

    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;

    else:
        print "Nope. Try again \n"



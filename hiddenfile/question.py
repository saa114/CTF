import os

flagfile = open("/home/hiddenfile/flag.txt", "r")
ctf_flag = flagfile.readline().strip()

print "\nSometimes a file is used to hide other files. Go to http://localhost:50000/Spurs.jpg and seeif there is anything in this image?\n"
print "Hint: Try comparing it to the original\n"

while True:
    user_flag = raw_input("\nThe flag looks like FLAG{...} \nInsert here: ")

    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;
    
    else:
        print "Nope. Try again \n"




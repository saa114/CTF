import os

flagfile = open("/home/messy-aes/flag.txt", "r")
ctf_flag = flagfile.readline().strip()

print "\nWe were playing around with AES encryption and lost our flag in http://localhost:63000/textfiles/given.txt \n"
print "This is all we know: e220eb994c8fc16388dbd60a969d4953f042fc0bce25dbef573cf522636a1ba3fafa1a7c21ff824a5824c5dc4a376e75 \n"
print "Hint: Block."

while True:
    user_flag = raw_input("\nThe flag looks like FLAG{...} \nInsert here: ")

    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;
    
    else:
        print "Nope. Try again \n"




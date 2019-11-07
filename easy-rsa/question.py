import os

flagfile = open("/home/easy-rsa/flag.txt", "r")
ctf_flag = flagfile.readline().strip()

print "\nWe encrypted the flag with rsa. Can you crack it? The file is in localhost:55000/easy-rsa.tar.gz \n"
print "Hint: Short public key. \n"

while True:
    user_flag = raw_input("\nThe flag looks like FLAG{...} \nInsert here: ")

    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;
    
    else:
        print "Nope. Try again \n"




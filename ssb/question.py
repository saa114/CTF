import os

flagfile = open('flag.txt','r')
ctfflag = flagfile.readlines()

print "\nGO TO http://localhost:65000/textfiles/catchthemall.txt \n"
print "Can you find the flag in the textfile?"
print "Hint: That is a lot of text, maybe a script would help."

while True:
    user_flag = raw_input("\nThe flag looks like FLAG{...} \nInsert here:")

    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;

    else:
        print "Nope. Try again \n"



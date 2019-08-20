import os

ctf_flag = "FLAG{THIS_IS_AN_EASY_CODING_PROBLEM}"

print "Can you find the flag in the textfile?"
print "Hint: That is a lot of text, maybe a script would help."

while True:
    user_flag = raw_input("The flag looks like FLAG{...} \n")
    
    if ctf_flag in user_flag:
        print "Correct!! \n"
        break;
    
    else:
        print "Nope. Try again \n"




import os

ctf_flag =  "FLAG{3nCod1nG_4nD_d3c0D1nG}"
final_flag = ''

print "Can you turn this string into a flag? 464c41477b336e436f64316e475f346e445f6433633044316e477d. "

user_flag = raw_input("The flag looks like this FLAG{...}. \n")

for i in user_flag:
    if i != ' ':
        final_flag += i

if final_flag == ctf_flag:
    print "Correct!"

else:
    print "Try again"



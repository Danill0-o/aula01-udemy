print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
both = name1 + name2
count_t  = both.count("t")
count_r  = both.count("r")
count_u  = both.count("u")
count_e  = both.count("e")
count_l  = both.count("l")
count_o  = both.count("o")
count_v  = both.count("v")
count_e2 = both.count("e")

true = str(count_t + count_r + count_u + count_e)
love = str(count_l + count_o + count_v + count_e2)
percentage = int(true + love)

if percentage < 10 or percentage > 90:
    print(f"Your score is {percentage}, you go together like coke and mentos.")
elif percentage >= 40 and percentage <= 50:
    print(f"Your score is {percentage}, you are alright together.")        
else:
    print(f"Your score is {percentage}.")
import random
logo = """
   ___                     _                                             _                _ 
  / _ \_   _  ___  ___ ___(_)_ __   __ _    __ _   _ __  _   _ _ __ ___ | |__   ___ _ __ / \\
 / /_\/ | | |/ _ \/ __/ __| | '_ \ / _` |  / _` | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/  /
/ /_\\| |_| |  __/\__ \__ \ | | | | (_| | | (_| | | | | | |_| | | | | | | |_) |  __/ | /\_/ 
\____/ \__,_|\___||___/___/_|_| |_|\__, |  \__,_| |_| |_|\__,_|_| |_| |_|_.__/ \___|_| \/   
                                   |___/                                                    """
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm guessing a number between 1 and 100.")
difficult = input("Choose a difficulty:\n 1 - Easy\n 2 - Medium\n 3 - Hard\n")
def rand_number():
    rdn_num = random.randint(1,100)
    return rdn_num
def loop(life):
     lives = life 
     while True:
        if lives == 0:
            print("You've run out of attempts. You lose!")
            break      
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > rdn_num:
            print("Too high!")
            lives -= 1
        elif guess < rdn_num:
            print("Too low!")
            lives -= 1
        else:
            print(f"You got it! The answer was {rdn_num}")
            break   
life = 0
if difficult == "1":
    rdn_num = rand_number()    
    print("You choose 'Easy'\n")     
    life = 10
    loop(life)       

elif difficult == "2":
    rdn_num = rand_number()    
    print("You choose 'Medium'\n")
    life = 7  
    loop(life)       
elif difficult == "3":
    rdn_num = rand_number()    
    print("You choose 'Hard'\n")
    life = 5 
    loop(life)
else:
    print("The games explodes!")
        
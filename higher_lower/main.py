from art import logo, vs
#from game_data import data
from game_data import data
import random

print(logo)
def grab_data():
    compareA = data[random.randint(0,len(data) -1)]
    compareB = data[random.randint(0,len(data) -1)]

    while compareA == compareB:
        compareB = data[random.randint(0,len(data) -1)]
    return compareA, compareB
score = 0
while True:
    compareA, compareB = grab_data()
    print(f"Compare A: {compareA['name']}, a {compareA['description']} from {compareA['country']}.")

    print(vs)

    print(f"Compare B: {compareB['name']}, a {compareB['description']} from {compareB['country']}.")
    guess = input("Who has more followers? 'A' or 'B'\n")

    
    if guess == 'A':
        if compareA['follower_count'] > compareB['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            print(f"\nYou're wrong! You lose!\n Final score: {score}.")
            break    
    if guess == 'B':
        if compareA['follower_count'] < compareB['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            print(f"\nYou're wrong! You lose!\n Final score: {score}.")
            break    
    print(f"{compareA['name']} has {compareA['follower_count']} millions followers!")
    print(f"{compareB['name']} has {compareB['follower_count']} millions followers!\n")
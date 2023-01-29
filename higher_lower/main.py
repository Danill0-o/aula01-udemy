from art import logo, vs
from game_data import data
import random

print(logo)
def grab_data():
    grab_name = data[random.randint(0,len(data) -1)]
    return grab_name

score = 0
loop_list = []
loop_list.append(grab_data()) 
while True:
    loop_list.append(grab_data())
    while loop_list[0] == loop_list[1]:
        loop_list.pop(1)
        loop_list.append(grab_data())
    print(f"Compare A: {loop_list[0]['name']}, a {loop_list[0]['description']} from {loop_list[0]['country']}.")

    print(vs)

    print(f"Compare B: {loop_list[1]['name']}, a {loop_list[1]['description']} from {loop_list[1]['country']}.")
    print(loop_list[0]['follower_count'], loop_list[1]['follower_count'])
    guess = input("Who has more followers? 'A' or 'B'\n")
    
    if guess == 'A':
        if loop_list[0]['follower_count'] > loop_list[1]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.\n")
            print(f"{loop_list[0]['name']} has {loop_list[0]['follower_count']} millions followers!")
            print(f"{loop_list[1]['name']} has {loop_list[1]['follower_count']} millions followers!\n")
            loop_list.pop(1)
        else:
            print(f"\nYou're wrong! You lose!\n Final score: {score}.")
            break    
    if guess == 'B':
        if loop_list[0]['follower_count'] < loop_list[1]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.\n")
            print(f"{loop_list[0]['name']} has {loop_list[0]['follower_count']} millions followers!")
            print(f"{loop_list[1]['name']} has {loop_list[1]['follower_count']} millions followers!\n")
            loop_list.pop(0)
        else:
            print(f"\nYou're wrong! You lose!\n Final score: {score}.")
            break    
    
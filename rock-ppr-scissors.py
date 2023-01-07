import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
wpn = [rock, paper, scissors]
wrd = ["Rock", "Paper", "Scissors"]
print("Welcome to the international Rock, Paper and Scissors Championship!")
choice = int(input("\nRock, paper and scissors, shoot!\n\n  1 - Rock\n  2 - Paper\n  3 - Scissors\n"))
choice -= 1
pc_choice = random.randint(0,2)
print(f"\nYou chose {wrd[choice]}.")
print(wpn[choice])
print(f"\nYour opponent chose {wrd[pc_choice]}.")
print(wpn[pc_choice])
if choice == pc_choice:
    print("\nDraw...")
elif choice == 0 and pc_choice == 1:
    print("\nYou lose!")
elif choice == 0 and pc_choice == 2:
    print("\nYou win!")
elif choice == 1 and pc_choice == 0:  
    print("\nYou win!")
elif choice == 1 and pc_choice == 2:  
    print("\nYou lose!")
elif choice == 2 and pc_choice == 0:
    print("\nYou lose!")
elif choice == 2 and pc_choice == 1:  
    print("\nYou Win!") 
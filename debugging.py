############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# num1 = 0
# num2 = 0
# num3 = 0
# num4 = 0
# num5 = 0
# num6 = 0
# for i in range(1000):
#   dice_imgs = ["1", "2", "3", "4", "5", "6"]
#   dice_num = randint(0,5)
#   #print(dice_imgs[dice_num])
#   if dice_num == 0:
#     num1 += 1
#   if dice_num == 1:
#     num2 += 1
#   if dice_num == 2:
#     num3 += 1
#   if dice_num == 3:
#     num4 += 1
#   if dice_num == 4:
#     num5 += 1
#   if dice_num == 5:
#     num6 += 1
# print(num1, num2, num3, num4, num5, num6)
# Play Computer
# year = int(input("What's your year of birth?\n"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# else:
#   print("You are old!")
# # Fix the Errors
# age = int(input("How old are you?"))
# if age >= 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
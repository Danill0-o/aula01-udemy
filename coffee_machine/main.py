from functions import *

choice = check_flavor()
if choice != False or choice == 0:
    check_money(choice)
#keep = input("Do you want to try another one?\n 1 - YES\n 2 - NO")
#if keep == '1':
    #check_flavor()
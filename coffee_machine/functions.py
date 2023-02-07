from lists_and_dicts import *
import datetime
import getpass
def check_flavor():
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        print("Good morning.")
    elif current_time < datetime.time(19):
        print("Good afternoon.")
    else:
        print("Good night.")        
    
    count = 0
    out_stock = []
    out_stock_index = []
    flavor_names2 = flavor_names.copy()
    for i in flavor_list:    
        for key in tank:
            if tank[key] < i[key]:
                out_stock.append(flavor_names.pop(count))
                count -= 1
                break
        count += 1
    
    for y in out_stock:
        out_stock_index += str(flavor_names2.index(y) +1)
    
    print(f"The available flavors are: {flavor_display}")
    #print(out_stock_index)
    if out_stock != []:
        print(f"Flavors out of stock: {', '.join(out_stock)}")
    if flavor_names == []:
        print("There is no flavors available, sorry.")
        return False
    while True:
        choice = input("Choose the flavor that you want: ")
        if choice == '256':
            check_tank()
        elif choice in out_stock_index:
            print("This flavor is out of stock for now, choose another one.")
        elif choice not in "1, 2, 3, 4, 5":
            print("There is no such option.")
        else: 
            break  
    choice = int(choice) - 1      
    print(f"You choose: {flavor_names2[choice]}. It will cost you ${flavor_list[choice]['price']}")
    tank_update(choice)
    return choice    

def tank_update(choice):
    tank2 = {}
    for z in tank:
        tank2[z] = tank[z] - flavor_list[choice][z]
    print(tank2)
    return tank2

def check_tank(tank2):
    print("Admin mode")
    password = getpass.getpass(prompt='Enter your password: ', stream=None)
    if password == '1234':
        print("Access granted!")
        print(f"Here is the report of the supplies: {tank2}")
        refil = input("Do you want refil it? \n 1 - YES\n 2 - NO")
        if refil == '1':
            tank2 = tank
        else:
            print("Leaving the Admin Mode...")    
    else:
        print("Access denied!")    

def check_money(choice):
    print(choice)
    print("Insert the coins below! ($1,00 and $0,50 only)")
    print(coin_display)
    value = int(input("How many coins of $1? "))
    value += 0.5 * int(input("How many coins of $0,50? "))
    print("Your inserted: ${:.2f}".format(value))  

    if value > flavor_list[choice]['price']:
        change = value - flavor_list[choice]['price']
        print("Here is your change: ${:.2f}".format(change))
        print("Enjoy your drink!")
    elif value < flavor_list[choice]['price']:
        change = value - flavor_list[choice]['price']
        print("It is missing: ${:.2f}, please insert the difference.".format(change))        
    else:
        print("Enjoy your drink!")

def tank_track(tank):
    import os
    tanks =[]
    tanks.append(tank)
    if not os.path.isfile('coffee_machine/tank_track.txt'):
        open('coffee_machine/tank_track.txt', 'w').close()
    with open('coffee_machine/tank_track.txt', 'r+') as f:
        for tank in tanks:
            f.write(f"milk: {tank['milk']}\n")
            f.write(f"water: {tank['water']}\n")
            f.write(f"coffee: {tank['coffee']}")

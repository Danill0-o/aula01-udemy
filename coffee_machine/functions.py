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
    #colocar essa parte dentro de uma função pra poder limpar o out_stock_index após abastecer com o Admin
    tank_updated = read_tank_track()
    for i in flavor_list: #Checa se tem todos os ingredientes, se não tiver qqr ingrediente, insere na lista out_stock e pára.   
        for key in tank_updated:
            if tank_updated[key] < i[key]:
                out_stock.append(flavor_names[count])#tirei o .pop(count)
                #count -= 1
                break
        count += 1
    
    for y in out_stock:
        out_stock_index += str(flavor_names2.index(y) +1)
    
    print(f"The available flavors are: {flavor_display}")
    if out_stock != []:
        print(f"Flavors out of stock: {', '.join(out_stock)}")
    if flavor_names == []:
        print("There is no flavors available, sorry.")
        #return False
    while True:
        choice = input("Choose the flavor that you want: ")
        if choice == '256':
            tank_updated = tank_admin_access(tank_updated)
        elif choice in out_stock_index:
            print("This flavor is out of stock for now, choose another one.")
        elif choice not in "1, 2, 3, 4, 5":
            print("There is no such option.")
        else: 
            break  
    choice = int(choice) - 1      
    print(f"You choose: {flavor_names2[choice]}. It will cost you ${flavor_list[choice]['price']}")
    tank_updated = tank_update(choice, tank_updated)
    print(tank_updated, "maça")
    tank_track(tank_updated)
    print(tank_updated, "banana")
    return choice    

def tank_update(choice, tank_updated):
    for z in tank:
        tank_updated[z] = tank_updated[z] - flavor_list[choice][z]
    print(tank_updated,"vermifugo")
    return tank_updated

#acessa o tanque em modo Admim para ver o status e reabastecer.
def tank_admin_access(tank_updated):
    print("Admin mode")
    password = getpass.getpass(prompt='Enter your password: ', stream=None)
    if password == '1234':
        print("Access granted!")
        print(f"Here is the report of the supplies: {tank_updated}")
        refil = input("Do you want refil it? \n 1 - YES\n 2 - NO\n")
        if refil == '1':
            tank_updated = tank
            tank_track(tank_updated)
            print("The tank is full", tank_updated)
            return tank_updated
        else:
            print("Leaving the Admin Mode...")    
    else:
        print("Access denied!")    

def check_money(choice):
    #print(choice)
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

def tank_track(tank_updated):#cria um arquivo txt e armazena os dados do tanque.
    import os
    tanks =[]
    tanks.append(tank_updated)
    if not os.path.isfile('coffee_machine/tank_track.txt'):
        open('coffee_machine/tank_track.txt', 'w').close()
    with open('coffee_machine/tank_track.txt', 'r+') as f:
        for tank_updated in tanks:
            f.write(f"milk: {tank_updated['milk']}\n")
            f.write(f"water: {tank_updated['water']}\n")
            f.write(f"coffee: {tank_updated['coffee']}")

def read_tank_track():# transforma os dados do arquivo txt de volta para um dict.
    tank_updated = {}
    with open('coffee_machine/tank_track.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            tank_updated[key] = int(value)
        print(tank_updated,"macarrao")    
    return tank_updated



from lists_and_dicts import *
import datetime
import getpass
def check_flavor():
    """Inicializa a máquina de café."""
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
                out_stock.append(flavor_names[count])
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
            tank_updated, out_stock, out_stock_index = tank_admin_access(tank_updated)
        elif choice in out_stock_index:
            print("This flavor is out of stock for now, choose another one.")
        elif choice not in "1, 2, 3, 4, 5":
            print("There is no such option.")
        else: 
            break  
    choice = int(choice) - 1      
    print(f"You choose: {flavor_names2[choice]}. It will cost you ${flavor_list[choice]['price']}")
    tank_updated = tank_update(choice, tank_updated)
    tank_track(tank_updated)
    return choice    

def tank_update(choice, tank_updated):
    """Atualiza o tanque de suprimentos após o uso."""
    for z in tank:
        tank_updated[z] = tank_updated[z] - flavor_list[choice][z]
    #print(tank_updated)
    return tank_updated

def tank_admin_access(tank_updated):
    """Acessa o tanque em modo Admim para ver o status e reabastecer."""
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
            out_stock = []
            out_stock_index = []
            return tank_updated, out_stock_index, out_stock
        else:
            print("Leaving the Admin Mode...")    
    else:
        print("Access denied!")    

def check_money(choice):
    """Confere o valor inserido, devolve o troco ou pede pela diferença, se o caso."""
    print("Insert the coins below! ($1,00 and $0,50 only)")
    print(coin_display)
    value = 0
    value = int(input("How many coins of $1? "))
    value += 0.5 * int(input("How many coins of $0,50? "))
    print("Your inserted: ${:.2f}".format(value))  
    change = value - flavor_list[choice]['price']
    
    if value > flavor_list[choice]['price']:
        print("Here is your change: ${:.2f}".format(change))
        print("Enjoy your drink!")
    elif value < flavor_list[choice]['price']:
        print("It is missing: ${:.2f}, please insert the difference.".format(change))
        more_money(change)
    else:
        print("Enjoy your drink!")

def more_money(change):
    """Pede pra inserir mais dinheiro em caso de o valor inserido ser menor do que o valor do produto."""
    print(coin_display)
    value = int(input("How many coins of $1? "))
    value += 0.5 * int(input("How many coins of $0,50? "))
    print("Your inserted: ${:.2f}".format(value))
    change = value + change  

    if change > 0:
        print("Here is your change: ${:.2f}".format(change))
        return print("Enjoy your drink!")
    elif value == 0 or change < 0:
        print("It is missing: ${:.2f}, please insert the difference.".format(change))
        return more_money(change)
    else:
        return print("Enjoy your drink!")

def tank_track(tank_updated):
    """Cria um arquivo txt e armazena os dados do tanque."""
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

def read_tank_track():
    """Transforma os dados do arquivo txt de volta para um dict."""
    tank_updated = {}
    with open('coffee_machine/tank_track.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            tank_updated[key] = int(value)
    return tank_updated



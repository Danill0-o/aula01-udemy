from flavors import *
import datetime
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
    print(out_stock_index)
    if out_stock != []:
        print(f"Flavors out of stock: {', '.join(out_stock)}")    
    while True:
        choice = int(input("Choose the flavor that you want: "))
        if choice in out_stock_index:
            print("This flavor is out of stock for now, choose another one.")
        elif choice not in [1, 2, 3, 4, 5]:
            print("There is no such flavor.")
        else: 
            break    
    print(f"You choose: {flavor_names2[choice -1]}")    

    #falta transformar o out_stock_index em INT para o IF funcionar
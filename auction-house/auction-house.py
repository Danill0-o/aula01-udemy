from logo import logo
import os

print(logo)

#gera um contador fora do arquivo.
def add_counter():
    if not os.path.isfile('counter.txt'):
        open('counter.txt', 'w').close()
    with open('counter.txt', 'r+') as f:
        counter = int(f.read() or 0) + 1
        f.seek(0)
        f.write(str(counter))
        f.truncate()
    return counter

def auction_list(name_inside, bid_inside):
    players ={}
    players["id"] = add_counter()
    players["name"] = name_inside
    players["bid"] = bid_inside
    jogadores.append(players)

jogadores = []
keep_going = 1
while keep_going == 1:
    
    name = input("What is your name, good sir?: ")
    bid = int(input("What is your bid: $"))
    auction_list(name_inside = name, bid_inside = bid)
    #print(jogadores)
    keep_going = int(input("Are there any other bidders?\n 1 - Yes\n 2 - No \n "))
    os.system('cls')
max_bid = 0
max_bid_index = 0
max_bid_name = ""
for i in range(len(jogadores)):
    if jogadores[i]["bid"] > max_bid:
        max_bid = jogadores[i]["bid"]
        max_bid_index = i
        max_bid_name = jogadores[i]["name"]
print(logo)
print(f"The winner is: {max_bid_name}, bid ${max_bid}!")
# jogadores = [{
#      "id": idd,
#      "name": name,
#      "bid": bid,
# }]
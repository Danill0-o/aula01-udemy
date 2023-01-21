import random
#ouro = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#copas = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#paus = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#espadas = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
baralho = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

naipes = ["Ouro", "Copas", "Paus", "Espadas"]

letras = {
    "K" : 10,
    "Q" : 10,
    "J" : 10,
    "Ás" : 1
}
num = 0
def compra():    
    player_hand_naipe = random.choice(naipes)
    player_hand = random.choice(baralho)
    carta = f" {player_hand} de {player_hand_naipe}"
    if player_hand in letras:
        player_hand = int(letras[player_hand])
    return carta
  
print(f"Your cards are: {compra()} and {compra()}")
print(f"The Dealer's first card is: {compra()}")
answer = input("Do you want to get another card? \n 1 - Yes\n 2 - No\n")
print(num)
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

player_hand_naipe = random.choice(naipes)
player_hand = random.choice(baralho)
print(f" {player_hand} de {player_hand_naipe}")
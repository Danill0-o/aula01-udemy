import random
#ouro = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#copas = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#paus = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#espadas = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
baralho = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

naipes = ["Diamonds", "Hearts", "Clubs", "Spades"]

letras = {
    "K" : 10,
    "Q" : 10,
    "J" : 10,
    "Ace" : 1
}
num = 0

def compra():    
    player_hand_naipe = random.choice(naipes)
    player_hand = random.choice(baralho)
    carta = f" {player_hand} of {player_hand_naipe}"
    if player_hand in letras:
        player_hand = int(letras[player_hand])
    return carta, player_hand

carta1, card1 = compra()
carta2, card2 = compra()
dealers_carta1, dealers_card1 = compra()
dealers_carta2, dealers_card2 = compra()
print(f"Your cards are: {carta1} and {carta2}")
print(f"You got: {card1 + card2}")
print(f"The Dealer's first card is: {dealers_carta1}")
answer = input("Do you want to get another card? \n 1 - Yes\n 2 - No\n")
dealers_hand = dealers_card1 + dealers_card2
card3 = 0
total = card1 + card2
if answer == "1":
    carta3, card3 = compra() 
    total += card3    
    print(f"You got a: {carta3}\n Total: {total}")
    print(f"Your hand: {carta1}, {carta2} and {carta3}")
    
if answer == "2":
    print(f"You got: {carta1} and {carta2}")
           
print(f"The Dealer got: {dealers_carta1} and {dealers_carta2}")
if total > dealers_hand and total <= 21:
    print("You win!")
elif total == dealers_hand:
    print("Draw")
else:
    print("You lose!")        
print(f"Your hand: {total}\nDealer's hand: {dealers_hand}")
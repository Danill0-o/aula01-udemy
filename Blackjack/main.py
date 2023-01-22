import random
baralho = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
naipes = ["Diamonds", "Hearts", "Clubs", "Spades"]
letras = {
    "K" : 10,
    "Q" : 10,
    "J" : 10,
    "Ace" : 11
}

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

# check if player has only two cards and one of them is an Ace
if card1 == 11 and card2 != 11:
    if card2 + 11 <= 21:
        card1 = 11
    else:
        card1 = 1
elif card2 == 11 and card1 != 11:
    if card1 + 11 <= 21:
        card2 = 11
    else:
        card2 = 1
elif card1 == 11 and card2 == 11:
    card1 = 1        
if dealers_card1 == 11 and dealers_card2 != 11:
    if dealers_card2 + 11 <= 21:
        dealers_card1 = 11
    else:
        dealers_card1 = 1
elif dealers_card2 == 11 and dealers_card1 != 11:
    if card1 + 11 <= 21:
        dealers_card2 = 11
    else:
        dealers_card2 = 1
elif dealers_card1 == 11 and dealers_card2 == 11:
    dealers_card1 = 1        
total = card1 + card2
dealers_hand = dealers_card1 + dealers_card2

print(f"You got: {total}")
print(f"The Dealer's first card is: {dealers_carta1}")
answer = input("Do you want to get another card? \n 1 - Yes\n 2 - No\n")

# check if player chooses to buy a third card
if answer == "1":
    carta3, card3 = compra() 
    
    if card3 == 11:
        if total + 11 <= 21:
            card3 = 11
            total += 11
        else:
            card3 = 1
            total += card3
    elif total > 21:
        print("You lose!")  
    total += card3          
    print(f"You got a: {carta3}\nTotal: {total}")
    print(f"Your hand: {carta1}, {carta2} and {carta3}")

# if player doesn't choose to buy a third card
if answer == "2":
    print(f"You got: {carta1} and {carta2}")


if dealers_hand < 17:
    dealers_carta3, dealers_card3 = compra()
    print(f"The Dealer got: {dealers_carta1}, {dealers_carta2} and {dealers_carta3}.")
    dealers_hand += dealers_card3    
else:
    print(f"The Dealer got: {dealers_carta1} and {dealers_carta2}")

if total > dealers_hand and total <= 21:
    print("You win!")
elif total == dealers_hand:
    print("Draw")
else:
    print("You lose!")        
print(f"Your hand: {total}\nDealer's hand: {dealers_hand}")
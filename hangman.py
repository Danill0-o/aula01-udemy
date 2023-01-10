import random
nouns = ["cat", "dog", "bird", "fish", "tree", "flower", "sky", "sun", "moon", "star", "sea", "beach", "desk", "chair", "table", "computer", "phone", "television", "book", "pen", "pencil", "paper", "notebook", "couch", "bed", "pillow", "blanket", "carpet", "door", "window", "ceiling", "floor", "wall", "house", "apartment", "building", "school", "office", "store", "museum", "library", "theater", "cinema", "concert", "art", "music", "dance", "theatre", "play", "movie", "television show", "sport", "game", "toy", "guitar", "piano", "violin", "drums", "singer", "actor", "actress", "director", "producer", "writer", "artist", "painter", "sculptor", "photographer", "chef", "waiter", "waitress", "bartender", "doctor", "nurse", "pharmacist", "dentist", "veterinarian", "lawyer", "judge", "police officer", "firefighter", "teacher", "student", "professor", "researcher", "scientist", "engineer", "architect", "accountant", "businessman", "businesswoman", "salesperson", "customer", "client", "partner", "colleague", "boss", "employee", "freelancer", "contractor", "intern", "apprentice"]

word = random.choice(nouns) #pega uma palavra da lista acima.
lenword = int(len(word))#mede o qts caracteres essa palavra têm.
letter_list = list(word)#transforma a palavra em uma lista de letras.
underline = list("_" * lenword)#cria uma lista de "_" de tamanho correpondente.

print(letter_list)
print(underline)


#while "_" in underline:
top   = [' ╠═══╦']
base2 = [' ║ ']
base1 = [' ║ ']
base  = ['_║_']
while "_" in underline:
    guess = input("Guess a letter.")
    num = -1
    for i in letter_list:
        num += 1
        if guess == i:
            underline[num] = guess
            print(underline)
    if guess not in letter_list:
        for not_in_list in range(6):
            print(top)
            print(base2)
            print(base1)
            print(base)
#print(letter_list)
#print(underline)
#print('''  ╠═══╦  
#           ║   o
#           ║  /|\
#          _║_ / \    ''')
import random
import os
nouns = ["cat", "dog", "bird", "fish", "tree", "flower", "sky", "sun", "moon", "star", "sea", "beach", "desk", "chair", "table", "computer", "phone", "television", "book", "pen", "pencil", "paper", "notebook", "couch", "bed", "pillow", "blanket", "carpet", "door", "window", "ceiling", "floor", "wall", "house", "apartment", "building", "school", "office", "store", "museum", "library", "theater", "cinema", "concert", "art", "music", "dance", "theatre", "play", "movie", "television show", "sport", "game", "toy", "guitar", "piano", "violin", "drums", "singer", "actor", "actress", "director", "producer", "writer", "artist", "painter", "sculptor", "photographer", "chef", "waiter", "waitress", "bartender", "doctor", "nurse", "pharmacist", "dentist", "veterinarian", "lawyer", "judge", "police", "officer", "firefighter", "teacher", "student", "professor", "researcher", "scientist", "engineer", "architect", "accountant", "businessman", "businesswoman", "salesperson", "customer", "client", "partner", "colleague", "boss", "employee", "freelancer", "contractor", "intern", "apprentice"]

word = random.choice(nouns) #pega uma palavra da lista acima.
lenword = int(len(word))#mede o qts caracteres essa palavra têm.
letter_list = list(word)#transforma a palavra em uma lista de letras.
underline = list("_" * lenword)#cria uma lista de "_" de tamanho correpondente.
stages = ["""  ╠═══╦  
  ║   o
  ║  
 _║_     ""","""  ╠═══╦  
  ║   o
  ║   |
 _║_     ""","""  ╠═══╦  
  ║   o
  ║  /|
 _║_     ""","""  ╠═══╦  
  ║   o
  ║  /|\\
 _║_     ""","""  ╠═══╦  
  ║   o
  ║  /|\\
 _║_ /     ""","""  ╠═══╦  
  ║   o
  ║  /|\\
 _║_ / \    """]
#print(letter_list)
print(" ".join(underline))

count = 0
guess_list =[]
while count < 6 and "_" in underline:
    guess = input("\nGuess a letter.").lower()
    os.system('cls')#limpa o terminal
    if guess in guess_list:
        print(stages[count - 1])
        print("\nYou already tried this one.")
    else:      
        if guess in letter_list:
            num = -1
            for i in letter_list:
                num += 1
                if guess == i:
                    underline[num] = guess
            print(stages[count - 1])
            print(" ".join(underline))
        else:
            count += 1
           
            if count == 1:
                print(stages[count - 1])
                print(" ".join(underline))
            if count == 2:
                print(stages[count - 1])
                print(" ".join(underline))
            if count == 3:
                print(stages[count - 1])
                print(" ".join(underline))
            if count == 4:
                print(stages[count - 1])
                print(" ".join(underline))
            if count == 5:
                print(stages[count - 1])
                print(" ".join(underline))
            if count == 6:
                print(stages[count - 1])
                print("You lose!")
                print(" ".join(underline))
                print(" ".join(letter_list))
    guess_list += guess
    #print(guess_list)
if count < 6:
    print("You Win!")

#print('''  ╠═══╦  
#           ║   o
#           ║  /|\
#          _║_ / \    ''')
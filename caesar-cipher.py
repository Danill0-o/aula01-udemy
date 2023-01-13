alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

plain_text = list(text)
num_list = []
num_list_soma = []
texto = ""
#transforma palavra em índice.
def word_index():
    
    for i in plain_text:
        num_list.append(alphabet.index(i))

#soma o número de troca ao índice.
def shift():
    
    for soma in num_list:
        soma += shift
        num_list_soma.append(soma)

#transforma índice em palavra.
def index_word():
    
    for x in num_list_soma:
        texto += alphabet[x]




print(plain_text, num_list, texto, num_list_soma)
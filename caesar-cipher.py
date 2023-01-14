alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

plain_text = list(text)
num_list = []
num_list_soma = []
texto_encripitado = ""
if direction == "encode":    
    #transforma palavra em índice.
    for i in plain_text:
        num_list.append(alphabet.index(i))

    #soma o número de troca ao índice.
    for soma in num_list:
        soma += shift
        if soma > len(alphabet):
            soma = (soma - len(alphabet))       
        num_list_soma.append(soma)

    #transforma índice em palavra.
    for x in num_list_soma:
        texto_encripitado += alphabet[x]

if direction == "decode":
    #transforma palavra em índice.
    for i in plain_text:
        num_list.append(alphabet.index(i))

    #soma o número de troca ao índice.
    for subtracao in num_list:
        subtracao -= shift
        num_list_soma.append(subtracao)

    #transforma índice em palavra.
    for x in num_list_soma:
        texto_encripitado += alphabet[x]    

print(plain_text, num_list, texto_encripitado, num_list_soma)
print(f"The encoded text is {texto_encripitado}")
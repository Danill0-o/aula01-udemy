#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Desta forma a senha é criada sem repetir caracteres, porém ela pode ficar mais curta do que o esperado, ainda não descobri como manter o loop caso um caracter se repita.
# ltr = []
# for l in range(0, nr_letters + 1):
#     nl = letters[random.randint(0, len(letters)-1)]
#     if nl not in ltr:
#         ltr.insert(l, nl)
# print(ltr)
# smbl = []
# for s in range(0, nr_symbols + 1):
#     ns = symbols[random.randint(0, len(symbols)-1)]
#     if ns not in smbl:
#         smbl.insert(s, ns)
# print(smbl)
# num = []
# for n in range(0, nr_numbers + 1):
#     nn = numbers[random.randint(0, len(numbers)-1)]
#     if nn not in num:
#         num.insert(n, nn)
# print(num)
# pass_lenght = nr_letters + nr_numbers + nr_symbols
# sum_list = ltr + smbl + num
# print(sum_list)


# random.shuffle(sum_list)
# final = "".join(sum_list)

# print(f"Your motherfucker password is: {final}")

#Esse é o jeito mais fácil.
password = []
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
for char in range(1, nr_symbols +1):
    password += random.choice(symbols)

random.shuffle(password)

pswrd = ""
for char in password:
    pswrd += char
print(f"Your password is: {pswrd}")
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rdn_name = names[random.randint(0,len(names))] #a função len() garante que o tamanho da lista será respeitado
print(f"{rdn_name} is going to buy the meal today!")
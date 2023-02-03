from flavors import *

count = 0
remove_lista = []
for i in flavor_list:    
    #num = str(flavor_names[count])
    #print(f"{num} = {flavor_list[count]}")
    
    for key in tank:
        if tank[key] < i[key]:
            remove_lista.append(flavor_names.pop(count))
            count -= 1
            break
    count += 1

# for index in remove_lista:
#         #index = int(index)
#         flavor_names.remove(index)    
print(f"The available flavors are: {', '.join(flavor_names)}\nFlavors out of stock: {', '.join(remove_lista)}")    


#print(flavor['1'])
#tem que tirar o item da lista so depois de correr todo o loop, senão o loop para antes.
#talvez add o indice a uma outra lista e ao fim do loop remover tais itens da lista de sabores
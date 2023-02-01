from flavors import *

count = 0
for i in flavor_list:    
    num = str(flavor_names[count])
    #print(f"{num} = {flavor_list[count]}")
    
    for key in tank:
        if tank[key] < flavor_list[count][key]:
            flavor_list.pop(count)
            flavor_names.pop(count)
       
    count += 1
print(f"The available flavors are: {flavor_names}")    
#print(flavor['1'])

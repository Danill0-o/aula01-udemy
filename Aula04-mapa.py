# ð¨ Don't change the code below ð
row1 = ["â¬ï¸","ï¸â¬ï¸","ï¸â¬ï¸"]
row2 = ["â¬ï¸","â¬ï¸","ï¸â¬ï¸"]
row3 = ["â¬ï¸ï¸","â¬ï¸ï¸","â¬ï¸ï¸"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ð¨ Don't change the code above ð

#Write your code below this row ð
pos_list = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
if position not in pos_list:
    print("Escolha um valor vÃ¡lido.")
else:    
    col = int(position[0])
    rw = int(position[1])
    col -= 1
    rw -= 1
    map[rw] [col] = "X"
#Write your code above this row ð

# ð¨ Don't change the code below ð
print(f"{row1}\n{row2}\n{row3}")
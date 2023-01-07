# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
pos_list = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
if position not in pos_list:
    print("Escolha um valor válido.")
else:    
    col = int(position[0])
    rw = int(position[1])
    col -= 1
    rw -= 1
    map[rw] [col] = "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
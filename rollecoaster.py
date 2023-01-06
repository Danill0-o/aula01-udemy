height = float(input("What is your height? "))
height = int(height * 100)
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Teenager ticket is $7.")
    else:
        bill = 12
        print("Adult ticket is $12.")
    photo = input("Do you want a photo? (Y/N) ")
    if photo == "Y" or photo == "y":
       bill += 3
    print(f"Your final bill is ${bill}!")    
else:
    print("Sorry. You have to grow taller to ride.")
#Write your code below this line ๐

def prime_checker(number):
    if number % 2 == 1 and number % 3 == 1:
        print("It's a prime number.")
    elif number % 2 == 1 and number % 3 == 2 and number % 5 != 0:
        print("It's a prime number.")
    elif number == 2:
        print("It's a prime number.")    
    else:
        print("It's not a prime number.")        





#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)

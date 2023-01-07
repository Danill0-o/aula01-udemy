import random
heads = 0
tails = 0
for i in range(1000):
        coin = random.randint(0,1)
        if coin == 1:
                #print("Heads")
                heads += 1
        else:
                #print("Tails")        
                tails += 1
print(heads)
print(tails) 
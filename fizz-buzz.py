num = 0
for i in range(1,101):
       
    if i % 3 == 0 and i % 5 == 0:#vai inprimir somente os numeros divisíveis por 3 E por 5.
        print("FizzBuzz")
    else:    
        if i % 3 == 0:#substitui os nº divisíveis por 3 por "Fizz".
            print("Fizz")    
        if i % 5 == 0:#substitui os nº divisíveis por 5 por "Buzz".
            print("Buzz")
        if i % 3 != 0 and i % 5 != 0: # vai imprimir todos os números que não sejam divisíveis por 3 e por 5.
            print(i)
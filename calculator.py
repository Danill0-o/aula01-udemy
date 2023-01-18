def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2 

def multiply(n1, n2):
  return n1 * n2

operators = {
  "+" : add,
  "-" : subtract,
  "/" : divide,
  "*" : multiply,
}

num1 = int(input("What's the first number?: "))
list_key = ""
for key in operators:
  list_key += key
list_key = " ".join(list_key)
print(f"\n{list_key}\n")
print(type(list_key))
operator_symbol = input("Pick one of the operators above: ")
num2 = int(input("What's the second number?: "))
function = operators[operator_symbol]
answer = function(num1, num2)
print(f"{num1} {operator_symbol} {num2} = {answer}")

while True:
    keep = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if keep == 'y':
        
        operator_symbol = input("Pick an operator: ")
        num3 = int(input("What's the next number?: "))
        function = operators[operator_symbol]
        answer2 = function(answer, num3)
        print(f"{answer} {operator_symbol} {num3} = {answer2}")
        answer = answer2
    else:
        break

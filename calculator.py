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
answer = function(n1 = num1, n2 = num2)
print(f"{num1} {operator_symbol} {num2} = {answer}")
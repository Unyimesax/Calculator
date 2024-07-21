#Addition
def add(n1, n2):
    return n1+n2

#Subtraction
def subtract(n1, n2):
    return n1 - n2

#Multiplication
def multiply(n1, n2):
    return n1*n2

#Division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    
}

num1 = int(input("What's the first number?: \n"))

for symbol in operations:
    print(symbol)

operation_symbol = input("choose an operation from the line above: \n ")

num2 = int(input("What's the second number?: \n"))

calculation_function = operations[operation_symbol]

answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")


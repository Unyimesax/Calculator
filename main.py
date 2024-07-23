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

def calculator():
    num1 = float(input("What's the first number?: \n"))
    
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        
        operation_symbol = input("choose an operation: \n ")
        
        num2 = float(input("What's the next number?: \n"))
        
        calculation_function = operations[operation_symbol]
        
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        continue_calc = input(f"Type 'y' to continue calculating with {answer} or type 'n' to restart :\n")
        if continue_calc == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
    
calculator()    
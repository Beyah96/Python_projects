import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

Operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}
should_continue = True
first_number = float(input("What's the first number?:"))
while should_continue :
    for symbol in Operations :
        print(symbol)
    operation = input("Pick an operation : ")
    second_number = float(input("What's the second number?:"))
    result = Operations[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    continuation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ").lower()
    if continuation == 'y' :
        first_number = result
    else :
        first_number = float(input("What's the first number?:"))


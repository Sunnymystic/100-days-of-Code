from calculator_project import logo
print(logo)
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
repeat = 'n'
while repeat == 'n' or repeat == 'y':
    if repeat == 'n':
        first_num = float(input("What's the first number? "))
    else:
        first_num = float(result)
    ops = list(operations.keys())
    print(ops[0])
    print(ops[1])
    print(ops[2])
    print(ops[3])
    operation = input("Pick an operation: ")
    if operation not in ops:
        print("Invalid opeation")
        exit()
    second_num = float(input("What's the next number?: "))
    if operation == "+":
        result = operations["+"](first_num,second_num)
    elif operation == "-":
        result = operations["-"](first_num,second_num)
    elif operation == "*":
        result = operations["*"](first_num,second_num)
    elif operation == "/":
        result = operations["/"](first_num,second_num)
    print(f"{first_num} {operation} {second_num} = {result}")        
    repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

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
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_num = float(input("What's the first number? "))
while True:
    for operation in operations:
        print(operation)

    operation = input("Pick an operation: ")
    if operation not in operations:
        print("Invalid operation")
        continue

    second_num = float(input("What's the next number?: "))
    if operation == "/" and second_num == 0:
        print("Error: division by zero is not allowed.")
        continue

    result = operations[operation](first_num, second_num)
    print(f"{first_num} {operation} {second_num} = {result}")

    next_step = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if next_step == "y":
        first_num = result
    elif next_step == "n":
        first_num = float(input("What's the first number? "))
    else:
        print("Invalid choice. Exiting.")
        break

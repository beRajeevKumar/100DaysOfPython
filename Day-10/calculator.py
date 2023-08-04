from art import logo
print(logo)


def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid Operator!"


def calculator_main():
    first_number = float(input("What's the first number?: "))
    operations = ["+", "-", "*", "/"]
    for operator in operations:
        print(operator)

    not_end = True
    while not_end:
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        result = calculator(first_number, next_number, operation)
        print(f"{first_number} {operation} {next_number} = {result}")

        next_operation = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if next_operation == 'y':
            first_number = result
        else:
            not_end = False
            calculator_main()


calculator_main()

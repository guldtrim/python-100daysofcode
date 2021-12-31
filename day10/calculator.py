from art import logo

def add(a1, a2):
    return a1 + a2

def subtract(s1, s2):
    return s1 - s2

def multiply(m1, m2):
    return m1 * m2

def divide(s1, s2):
    return s1 / s2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("Whats the first number?: "))

    while should_continue:
        for i in operations:
            print(i)
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("Whats the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.")

        if continue_calc == "y":
            num1 = answer
        else:
            should_continue = False

calculator()
print("Thanks for calculating")
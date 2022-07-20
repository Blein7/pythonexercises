
# Add function
def add(n1, n2):
    return n1 + n2


# Subtract function
def sub(n1, n2):
    return n1 - n2


# Multiply function
def multiply(n1, n2):
    return n1 * n2


# Divide function
def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": sub,
              "*": multiply,
              "/": divide
              }


def calculator():
    num1 = float(input("Enter the first number:"))

    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        chosen_operator = input("Choose operation:")
        num2 = float(input("Enter the next number:"))
        function = operations[chosen_operator]
        answer = function(num1, num2)
        print(f"{num1} {chosen_operator} {num2} = {answer}")

        choice_continue = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculator.:").lower()
        if choice_continue == 'y':
            num1 = answer

        elif choice_continue == 'n':
            should_continue = False
            calculator()


calculator()

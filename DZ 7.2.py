def checker(function):
    def checker_1(*args, **kwards):
        try:
            result = function(*args, **kwards)
        except Exception as exc:
            print(f'We have problems {exc}')
        else:
            print(result)
    return checker_1

def calculate(expression):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Operation: +, -, *, /")
    select = input("Select operations: ")

    if select == "+":
        print(num1, "+", num2, "=", num1 + num2)

    elif select == "-":
        print(num1, "-", num2, "=", num1 - num2)

    elif select == "*":
        print(num1, "*", num2, "=", num1 * num2)

    elif select == "/":
        print(num1, "/", num2, "=", num1 / num2)
    return eval(expression)

calculate = checker(calculate)
calculate("calculate")
print("Program 2")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def floor(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 // num2

def modulo(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 % num2

def exponent(num1, num2):
    return num1 ** num2


def main():
    print("Calculator")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    choice = int(input("""
Enter your choice:
1) +
2) -
3) *
4) /
5) //
6) %
7) **
Choice: """))

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    elif choice == 5:
        result = floor(num1, num2)
    elif choice == 6:
        result = modulo(num1, num2)
    elif choice == 7:
        result = exponent(num1, num2)
    else:
        print("Invalid choice")
        return

    print(f"Result: {result}")


main()

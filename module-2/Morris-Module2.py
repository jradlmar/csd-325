# Jared Morris
# Module 2 Assignment

def add(num1, num2):
    return num1 + num2

def main():
    print("Simple Calculator")

    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))

    answer = add(first, second)

    print(f"The answer is {answer}")

main()
# Please write a program which asks the user for an integer number. The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.
# Sample output

# Please type in a number: 2020
# Sample output

# Please type in a number: 1984
# Orwell
num = int(input("Give me a number"))

if num == 1984:
    print("Orwell")


# Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.
num1 = input ("give me a first number")
num2 = input("give me a second number")
operation = input("what math op do you want?")

num1 = int(num1)
num2 = int(num2)

if operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
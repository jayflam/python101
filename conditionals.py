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


# Write your solution here
temp = int(input("Temperature"))
rain = input("Will it rain?")

# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

# Some examples of expected behaviour:

if temp>20:
    print("Wear jeans and a T-shirt")
if 20>temp>10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
if 10>temp>5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
if 5>temp:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget an umbrella!")

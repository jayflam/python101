input_str = input("Which year were you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2021: {2021 - year}" )


# Please write a program which asks the user for a number. The program then prints out the number multiplied by five.

# The program should function as follows:
# Sample output

# Please type in a number: 3
# 3 times 5 is 15
number = int(input("Give me a number!"))
print(f"{number} times 5 is {number*5}")

# Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:
# Sample output

# What is your name? Frances Fictitious
# Which year were you born? 1990
# Hi Frances Fictitious, you will be 31 years old at the end of the year 2021

# Write your solution here
name = input("what is your name?") 
dob = int(input("what is your DOB?"))

print(f"Hi {name}, you will be {2021-dob} at the end of the year 2021")


# Please write a program which estimates a user's typical food expenditure.

# The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

# The program should function as follows:
# Sample output

# How many times a week do you eat at the student cafeteria? 4
# The price of a typical student lunch? 2.5
# How much money do you spend on groceries in a week? 28.5

# Average food expenditure:
# Daily: 5.5 euros
# Weekly: 38.5 euros

# Write your solution here

times_cafe = int(input("How many times do you eat at the cafeteria?"))
price_meal = float(input("what is the price of a meal?"))
price_grocery = float(input("How much do you spend on groceries?"))

daily = ((times_cafe*price_meal)+price_grocery)/7
weekly = ((times_cafe*price_meal)+price_grocery)

print(f"How many times a week do you eat at the student cafeteria? {times_cafe}")
print(f"The price of a typical student lunch? {price_meal}")
print(f"How much money do you spend on groceries in a week? {price_grocery}")

print(f"Average food expenditure:\nDaily: {daily} euros\nWeekly: {weekly} euros")

# Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

# If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.
# Sample output

# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2
# Sample output

# How many students on the course? 11
# Desired group size? 3
# Number of groups formed: 4

# Hint: the integer division operator // could come in handy here.

# Write your solution here
class_size = int(input("Class size"))
group_size = int(input("group size"))

group_formed = -(-class_size//group_size)

# print(f"How many students on the course? {class_size}")
# print(f"Desired group size? {group_size}")
print(f"Number of groups formed: {group_formed}")
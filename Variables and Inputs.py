print("Hello world! <:-)")
print("I love python!")
print("python is the greatest language eva!!!")

print(2+5)
print(5%4)


#number of minutes in a year
print(365*24*60)

#printing out quotes:
print('print("Hello there!")')

name = input("what is your name? ")
print("Hi there, " + name)
print(name)
print (name)

name = input("what is your name?")
print("hi " + name)
print(name + " is quite a nice name")

# Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:
# Sample output

# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

first_name = input("Name?")
last_name = input("Last Name?")
address = input("Addy?")
city_zip = input("city and zip code?")

print (first_name + " " + last_name)
print(address)
print (city_zip)



# Please write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.
name = input("Please type in a name: ")
year = input("Please type in a year: ")


print(f"{name} is a valiant knight, born in the year {year}. One morning {name} woke up to an awful racket: a dragon was approaching the village. Only {name} could save the village's residents.")



#F string and new line exercise:

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")


# Write your solution here
x = 27
y = 15

print(f"{x} + {y} =", x+y)
print(f"{x} - {y} =", x-y)
print(f"{x} * {y} =", x*y)
print(f"{x} / {y} =", x/y)

#end="", prevent print from creating a new line:
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)

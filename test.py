# Write your solution here

year = int(input("Give me a year"))
nextleap = year

while nextleap % 4 != 0 and nextleap % 400 != 0 and nextleap % 100 == 0:
    nextleap = year+1
    # if year % 4 == 0  and year % 100  == 0 and year % 400 != 0:
    #     nextleap += 4
    # elif year % 4 == 0
    
print(f"The next leap year after {year} is {nextleap}")
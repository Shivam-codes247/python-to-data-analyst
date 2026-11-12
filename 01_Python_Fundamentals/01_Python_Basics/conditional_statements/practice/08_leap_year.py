# Problem

# Write a Python program to check whether a given year is a leap year or not.

# Rules for a Leap Year

# A year is a leap year if:

# It is divisible by 400, OR
# It is divisible by 4 but not divisible by 100.

n = int(input("enter the year : "))

if n%400==0 :
    print(f"{n} is a leap year")
elif n % 100 == 0:
    print(f"{n} is not a leap year")
elif n % 4 == 0:
    print(f"{n} is a leap year")

# we  can also do this as because every century year is not a leap year 
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    
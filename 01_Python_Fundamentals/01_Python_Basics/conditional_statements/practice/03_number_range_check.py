# Check whether a number falls within the inclusive range from 1 to 100.

# Read the number and convert it from text to an integer.
n = int(input("enter the number : "))

# Both conditions must be true for the number to be within the range.
if n>=1 and n<=100:
    print("Within Range")
else:
    print("Out of range")
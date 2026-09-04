# Check whether a user-provided number is evenly divisible by 7.

# Convert the text entered by the user into an integer.
a = int(input("enter the number : "))

# A remainder of zero means the number is a multiple of 7.
if (a % 7 == 0):
    print(f"{a} is multiple of 7")
else:
    print(f"{a} is not a multiple of 7")
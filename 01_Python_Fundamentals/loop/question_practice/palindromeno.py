# Palindrome Number

n = int(input("Enter the number: "))

# Store a copy because 'temp' will be modified
temp = n

# Store the original number for comparison at the end
original = n

# Variable to build the reversed number
rev = 0

# Loop until all digits of the number are processed
while temp > 0:

    # % 10 extracts the last digit
    last = temp % 10

    # Shift existing digits left and add the last digit
    rev = rev * 10 + last

    # // 10 removes the last digit
    temp = temp // 10

# A palindrome remains the same when reversed
if rev == original:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
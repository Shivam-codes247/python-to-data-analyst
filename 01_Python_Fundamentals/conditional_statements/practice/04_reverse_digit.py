# Read an integer and print its digits in reverse order.

# Convert the user's text input into an integer.
n = int(input("enter the number :" ))

# Store the sign separately so negative numbers remain negative after reversal.
sign = -1 if n<0 else 1
n = abs(n)

# Build the reversed number one digit at a time.
rev = 0

while(n>0):
    # Take the last digit, append it to the reversed number, then remove it.
    temp = n%10
    rev = (rev * 10) + temp
    n = n//10

print(sign * rev)
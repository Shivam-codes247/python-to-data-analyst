# Print the complete input if it is short; otherwise print its first four characters.

# Read a string from the user.
a = input("enter the string : ")

# Strings shorter than three characters are displayed unchanged.
if len(a)<3:
    print(a)
else:
    # Slice from the beginning up to, but not including, index 4.
    print(a[:4])
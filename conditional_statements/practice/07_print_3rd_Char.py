# Print the third character of the user's string when it exists.

# Read a string from the user.
a = input("enter the string : ")

# Python uses zero-based indexing, so the third character is at index 2.
if len(a)<3:
    print("not enough character")
else:
    print(a[2])
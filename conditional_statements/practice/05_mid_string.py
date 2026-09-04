# Print the middle character of a user-provided string.
# For an even-length string, print the character immediately before the center.

# Read the string to inspect.
a = input("enter the string : ")

# Handle the special case represented by a single space.
if a == " ":
    print("empty string")

else:
    # Integer division gives the center index for an odd-length string.
    mid = len(a) // 2
    if len(a)%2 == 0:
        # For even lengths, move one position left from the right middle index.
        print(a[mid-1])
    else:
        print(a[mid])

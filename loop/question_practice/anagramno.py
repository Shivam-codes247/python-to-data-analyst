# Anagram Number
# Two numbers are anagrams if they contain the same digits
# with the same frequency, regardless of their order.

s1 = input("Enter the first number: ")
s2 = input("Enter the second number: ")

# If the lengths are different, they cannot contain
# the same number of digits.
if len(s1) != len(s2):
    print("Not an anagram number")
else:
    # Check each digit of the first number
    for ch in s1:
        # count() returns how many times the digit
        # appears in each number.
        if s1.count(ch) != s2.count(ch):
            print("Not an anagram number")
            # Stop the loop as soon as a mismatch is found.
            break
    # The 'else' belongs to the for loop.
    # It runs only when the loop finishes without 'break'.
    else:
        print("Anagram number")
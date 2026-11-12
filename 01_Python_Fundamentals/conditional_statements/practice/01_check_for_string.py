# Check whether the letter "a" appears in the user's input.

# Read a word or sentence from the user.
user_input = input("enter the word : ")

# Count every occurrence of the letter "a" before displaying the result.
count = user_input.count('a')

# Test membership with `in` and report whether the letter was found.
if 'a' in user_input:
    print(f"A is found {count} times")
else:
    print("A is not found")
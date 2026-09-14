# ==========================================
# PYTHON LOOPS
# ==========================================
# Loops are used to execute a block of code repeatedly based on a given condition or sequence.
# ------------------------------------------
# 1. FOR LOOP
# ------------------------------------------
# A for loop is used to iterate over a sequence such as a string, list, tuple, or range.

for i in range(1, 6):
    print(i)

# ------------------------------------------
# 2. ITERATING OVER A STRING
# ------------------------------------------

name = "Shivam"

for character in name:
    print(character)

# ------------------------------------------
# 3. RANGE() FUNCTION
# ------------------------------------------
# range(start, stop, step)

for i in range(1, 11):
    print(i)

# Printing even numbers
for i in range(2, 11, 2):
    print(i)

# ------------------------------------------
# 4. WHILE LOOP
# ------------------------------------------
# A while loop executes as long as the given condition is True.

i = 1

while i <= 5:
    print(i)
    i += 1

# ------------------------------------------
# 5. BREAK STATEMENT
# ------------------------------------------
# break is used to immediately stop a loop.

for i in range(1, 11):
    if i == 6:
        break

    print(i)

# ------------------------------------------
# 6. CONTINUE STATEMENT
# ------------------------------------------
# continue skips the current iteration and moves to the next iteration.

for i in range(1, 11):
    if i == 5:
        continue

    print(i)

# ------------------------------------------
# 7. NESTED LOOPS
# ------------------------------------------
# A loop inside another loop is called a nested loop.

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# This program prints an inverted triangle pattern using nested `for` loops.

n = int(input("enter the number: "))

# The outer loop controls the number of rows.
# range(n, 0, -1) decreases the row size.
for i in range(n,0,-1):

    # The inner loop controls the number of stars in each row.
    for j in range(1,i):
        # print("*", end=" ") keeps the stars on the same line.
        print("*",end=" ")
    # print() moves to the next line.
    print()
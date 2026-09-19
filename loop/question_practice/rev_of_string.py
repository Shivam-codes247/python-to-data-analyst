# Write a Python program to reverse a given string without using the 
# built-in reversed() function or slicing.

n = input("enter a string : ")

rev = ""
for i in range(len(n)-1,-1,-1):
    rev = rev + n[i]

print(rev)
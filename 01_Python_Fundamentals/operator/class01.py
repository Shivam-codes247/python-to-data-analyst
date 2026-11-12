# Python Operators - Class 01

# 1. Arithmetic Operators

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# 2. Comparison Operators

x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# 3. Assignment Operators

num = 10

num += 5
print("After += :", num)

num -= 3
print("After -= :", num)

num *= 2
print("After *= :", num)

num /= 4
print("After /= :", num)


# 4. Logical Operators

p = True
q = False

print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)


# 5. Membership Operators

name = "Shivam"

print("v" in name)
print("z" in name)
print("z" not in name)


# 6. Identity Operators

a = 10
b = 10

print(a is b)
print(a is not b)
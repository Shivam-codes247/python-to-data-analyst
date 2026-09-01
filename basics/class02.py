# ==========================================
# CLASS 02 - STRINGS & TYPE CONVERSION
# ==========================================

# Strings

name = "shivam kumar" 
print(name)

#string indexing
print(name[0])  #s
print(name[5])  #m

#string slicing
print(name[1:6])    #hivam

#string concatination
first_name = "shivam"
second_name = "kumar"

full_name = first_name + " " + second_name
print(full_name)

#type conversion 
age = "23"
age_modified = int(age)

print(type(age))
print(type(age_modified))

# Integer to Float
marks = 90
marks = float(marks)

print(marks)
print(type(marks))


# Integer to String
number = 100
number = str(number)

print(number)
print(type(number))


# Float to Integer
price = 99.99
price = int(price)

print(price)
print(type(price))
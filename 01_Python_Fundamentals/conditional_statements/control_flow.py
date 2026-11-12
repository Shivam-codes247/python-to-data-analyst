# Control Flow in Python
# ======================
# 1. Control flow determines the order in which Python statements are executed.

# 2. The if statement is used to execute code only when a condition is True.

# 3. else executes when the if condition is False.

# 4. elif means “else if” and is used to check multiple conditions.

# 5. You can use multiple elif statements, but only one else is allowed at the end.

# 6. Python uses indentation to define blocks of code. Incorrect indentation can cause an IndentationError.

# 7. Comparison operators such as `>`, `<`, `==`, `!=`, `>=`, and `<=` are commonly used in conditions.

# 8. Logical operators `and`, `or`, and `not` are used to combine or modify conditions.

# 9. Nested `if` statements are used when one condition needs to be checked inside another condition.

# 10. Conditions always evaluate to True or False, which determines which block of code will execute.


# 1. if statement
print("1st question")
age = 18

if age >= 18:
    print("You are eligible to vote.")


# 2. if-else statement
print("2nd question")
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3. if-elif-else statement
print("3rd question")
marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# 4. Nested if statement
print("4th question")
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID is required.")
else:
    print("Entry not allowed.")


# 5. Comparison operators
print("5th question")
a = 10
b = 20

if a < b:
    print("a is smaller than b")


# 6. Logical AND operator
print("6th question")
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")


# 7. Logical OR operator
print("7th question")
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend.")


# 8. Logical NOT operator
print("8th question")
is_raining = False

if not is_raining:
    print("You don't need an umbrella.")


# 9. Check positive, negative or zero
print("9th question")
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 10. Find the greater number
print("10th question")
a = 45
b = 32

if a > b:
    print(f"{a} is greater.")
elif b > a:
    print(f"{b} is greater.")
else:
    print("Both numbers are equal.")


# 11. Check voting eligibility
print("11th question")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 12. Simple calculator using control flow
print("12th question")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")


# 13. Check leap year
print("13th question")
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 14. Password check
print("14th question")
password = input("Enter password: ")

if password == "python123":
    print("Login successful.")
else:
    print("Incorrect password.")


# 15. Temperature check
print("15th question")
temperature = float(input("Enter temperature: "))

if temperature >= 35:
    print("It's very hot.")
elif temperature >= 25:
    print("The weather is warm.")
elif temperature >= 15:
    print("The weather is pleasant.")
else:
    print("It's cold.")



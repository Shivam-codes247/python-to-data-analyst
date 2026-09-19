# Prime Number Checker
# --------------------
# A prime number is a number greater than 1
# that is divisible only by 1 and itself.

n = int(input("enter the number : "))

# 2 is the smallest prime number
if n<2: 
    print(f"{n} is not a prime no")
else:
    for i in range (2,n):
        if n%i == 0:
            print(f"{n} is not a prime no")
            break
    else :
        print(f"{n} is a prime no")
        
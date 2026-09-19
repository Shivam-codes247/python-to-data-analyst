n = int(input("enter the number : "))

temp = n
original = n
rev = 0

while(temp>0):
    last = temp%10
    rev = rev * 10 + last
    temp = temp // 10

if rev == original:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
    
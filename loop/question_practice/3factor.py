# Print all numbers up to n that have exactly 3 factors.

n = int(input("enter the number : "))

# A number has exactly 3 factors if and only if it is the square of a prime number.
for x in range(2,int(n**0.5)+1):
    count = 0

    for i in range(1,x+1):
        if x%i == 0:
            count+=1
    if count == 2:
        print(x*x,end=" ")
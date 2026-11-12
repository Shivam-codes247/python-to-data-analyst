n = input("give the input : ")

upper = 0
lower = 0

for ch in n:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1

print(f"number of upper case letters are {upper} \n and number of lower case letters are {lower}")
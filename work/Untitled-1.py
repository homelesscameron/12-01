import os
os.system('cls')

num = int(input("first number: "))
secondnum = int(input("second number: "))

x = pow(num, secondnum)

print()
print(x, "is the power of both numbers")
print()
print(max(num, secondnum), "is greater")
print()
print(min(num, secondnum), "is lesser")
print()
print("thank you for this maths calculator")
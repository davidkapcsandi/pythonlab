i = int(input("Please insert a number for factorials: "))

x = 1
y = 1

while y <= i:
    x *= y
    y +=1
print("The factorial of", i, "is : ", x)
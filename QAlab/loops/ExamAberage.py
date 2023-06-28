
mark1 = float(input("English mark: "))
mark2 = float(input("Math mark: "))
mark3 = float(input("ICT mark: "))

while not (0 <= mark1 <= 100) or not (0 <= mark2 <= 100) or not (0 <= mark3 <= 100):
    print("Please insert valid marks between 0 and 100.")
    mark1 = float(input("English mark: "))
    mark2 = float(input("Math mark: "))
    mark3 = float(input("ICT mark: "))

average = (mark1 + mark2 + mark3) / 3

if average >= 65:
    print("Pass, your average is:", average)
else:
    print("Fail, your average is:", average)

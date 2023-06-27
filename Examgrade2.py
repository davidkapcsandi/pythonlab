mark = int(input("Enter the exam mark: "))
level = int(input("Enter the student level (1 or 2): "))

if mark < 1 or mark > 100:
    print("Error: marks must be between 1 and 100")
elif level == 1:
    if mark < 50:
        print("Grade: Fail")
    elif mark <= 60:
        print("Grade: Pass")
    elif mark <= 70:
        print("Grade: Merit")
    else:
        print("Grade: Distinction")
elif level == 2:
    if mark < 40:
        print("Grade: Fail")
    elif mark <= 50:
        print("Grade: Pass")
    elif mark <= 65:
        print("Grade: Merit")
    else:
        print("Grade: Distinction")
else:
    print("Invalid level selection.")

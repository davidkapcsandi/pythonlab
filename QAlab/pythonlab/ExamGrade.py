score = int(input("Enter the exam score: "))

if score < 1 or score > 100:
    print("Error, score must be between 1 and 100")
elif score > 70:
    print("Disctinction")
elif score > 60:
    print("Merit")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
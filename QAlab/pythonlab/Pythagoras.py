print("1. Calculate side A")
print("2. Calculate side B")
print("3. Calculate side C")

choice = input("Enter your choice: ")

if choice == "1":
    side_b = float(input("Enter length of side B: "))
    side_c = float(input("Enter length of side C: "))
    side_a = (side_c**2 - side_b**2)**0.5
    print("Length of side A is", side_a)
elif choice == "2":
    side_a = float(input("Enter length of side A: "))
    side_c = float(input("Enter length of side C: "))
    side_b = (side_c**2 - side_a**2)**0.5
    print("Length of side B is", side_b)
elif choice == "3":
    side_a = float(input("Enter length of side A: "))
    side_b = float(input("Enter length of side B: "))
    side_c = (side_a**2 + side_b**2)**0.5
    print("Length of side C is", side_c)
else:
    print("Invalid choice, please enter 1, 2, or 3.")
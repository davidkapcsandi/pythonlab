while True:
    num1 = int(input("Choose your first number: "))
    num2 = int(input("Choose your second number: "))

    print("Calculator Menu:")
    print("Add (+)")
    print("Subtract (-)")
    print("Multiply (*)")
    print("Divide (/)")
    print("Square (s)")
    operation = input("Choose an operation(For example: *):")

    if operation == "+":
        result = num1 + num2
        print("Result:", result)
    elif operation == "-":
        result = num1 - num2
        print("Result:", result)
    elif operation == "*":
        result = num1 * num2
        print("Result:", result)
    elif operation == "/":
        result = num1 / num2
        print("Result:", result)
    elif operation == "s":
        result1 = num1 ** 2
        result2 = num2 ** 2
        print("Square of num1:", result1)
        print("Square of num2:", result2)
    else:
        print("Invalid selection.")
    x = input("Do you want to do it again? Type (y/n): ")
    if x != "y":
            input("Are you sure?(y/n)")
            if input != "n":
                    print("You are trapped in a loop, alright just joking, Goodbye"'\U0001F600')
            break



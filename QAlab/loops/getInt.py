min_value = 1
max_value = 100
attempts = 0

while attempts <3:
    value = int(input(f"enter an integer between {min_value} and {max_value}: "))
    if min_value <= value <= max_value:
        print(f"valid value entered: {value}")
        break
    else:
        print("invalid integer- try again!")
    attempts += 1
if attempts == 3:
    print("None")
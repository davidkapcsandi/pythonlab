def password_checker():
    common_passwords = ["123456798", "qwerty", "123465", "password", "00000"]

    guest = input("Please enter your password: ")

    if guest in common_passwords:
        print(f"Use a safer password {guest} is compromised")

    else:
        print("password is safe")

print(password_checker())
# write an application that checks the strength of a password.
# Requirements:
# 
# Write a class that has a method that checks the password strength.
# Use factors like length, upper/lower case and if it has a number and special character.
# ratings hould be very weak - weak - moderate - strong - very strong 
# Check against a list of common passwords 10-20 common password = very weak
# User input that loops until the user quits
# A dictionary that returns a history of passwords/strengths whilst in the loop.
common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "admin", "123456789", "password1", "welcome", "12345678", "test"]
class PasswordChecker:

    def __init__(self):
        self.password_history = {}
     
    def check_strength(self, password):

     
        strength = 0

        if len(password) >= 8:
            strength += 1

        if any(char.islower() for char in password) and any(char.isupper() for char in password):
            strength += 1

        if any(char.isdigit() for char in password):
            strength += 1

        if any(not char.isalnum() for char in password):
            strength += 1
        if password in common_passwords:
            strength = 0

        if strength == 0:
            return "very weak"
        elif strength == 1:
            return "weak"
        elif strength == 2:
            return "moderate"
        elif strength == 3:
            return "strong"
        else:
            return "very strong"
        
def run():
        checker = PasswordChecker()
        while True:
            
            password = input("Enter a password(or type q to exit): ")
            if password.lower() == "q":
                print("GoodBye.")
                break
            strength = checker.check_strength(password)
            checker.password_history[password] = strength
            print(f"Password strength: {strength}\n")

        print("Password history: ")
        for password, strength in checker.password_history.items():
            print(f"Password: {password}, Strength: {strength}")

run()
            
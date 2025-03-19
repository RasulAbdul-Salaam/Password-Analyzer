import re

def check_password(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 8 characters.")

    # Check for uppercase, lowercase, digits, and special characters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Add at least one number.")
    
    if re.search(r'[\W_]', password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Check if password is common (you could add a list of common passwords)
    common_passwords = ["123456", "password", "qwerty", "0000"]
    if password in common_passwords:
        suggestions.append("Avoid using common passwords.")

    return score, suggestions

# Example usage
password = input("Enter your password: ")
score, suggestions = check_password(password)
print(f"Password Strength Score: {score}")
if suggestions:
    print("\nSuggestions to improve your password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("Your password is strong!")

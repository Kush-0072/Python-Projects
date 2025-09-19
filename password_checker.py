def password_strength_checker():
    password = input("Enter a password to check its strength: ")
    strength = 0
    
    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()_+" for c in password):
        strength += 1

    if strength <= 2:
        print("Weak password")
    elif strength == 3 or strength == 4:
        print("Moderate password")
    else:
        print("Strong password")

password_strength_checker()

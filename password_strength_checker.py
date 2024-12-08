def check_strength(password: str):
    strength = 0
    
    if any(char.isdigit() for char in password):
        strength += 1

    if any(char.isupper() for char in password):
        strength += 1

    if any(char.islower() for char in password):
        strength += 1

    if any(char in "!@#$%^&*()-+?_=,<>/" for char in password):
        strength += 1

    if len(password) >= 8:
        strength += 1

    if strength <= 1:
        return "Very Weak"
    elif strength == 2:
        return "Weak"
    elif strength == 3:
        return "Medium"
    elif strength == 4:
        return "Strong"
    else:
        return "Very Strong"

def main():
    password = input("Enter a password: ")

    strength = check_strength(password)

    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
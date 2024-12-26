import string
import random

def password_generator(length: int, uppercase: bool, numbers: bool, special: bool):
    if length < (uppercase + numbers + special):
        raise ValueError("password is too short")
    
    password = list()
    allowed_characters = string.ascii_lowercase

    if uppercase:
        password.append(random.choice(string.ascii_uppercase))
        allowed_characters += string.ascii_uppercase
    if numbers:
        password.append(random.choice(string.digits))
        allowed_characters += string.digits
    if special:
        password.append(random.choice(string.punctuation))
        allowed_characters += string.punctuation

    password += [random.choice(allowed_characters) for _ in range(length - len(password))]

    random.shuffle(password)

    return "".join(password)

def get_strength(data: str):
    while True:
        ans = input(f"Include {data}? (y/n): ").lower()

        if ans not in ["y", "n"]:
            print("Please enter y or n")
            continue

        return ans


def get_password_length() -> int:
    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 1:
                raise ValueError()
            
            return length
        except ValueError:
            print("Please enter a valid number")
            continue

def main():
    length = get_password_length()

    uppercase = get_strength("uppercase letters").lower() == "y"
    numbers = get_strength("numbers").lower() == "y"
    special = get_strength("special characters").lower() == "y"

    try:
        password = password_generator(length, uppercase, numbers,special)
        print(password)

    except ValueError as e:
        print(e)

        
if __name__ == "__main__":
    main()
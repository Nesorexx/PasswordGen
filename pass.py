import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    if length <= 0:
        raise ValueError("Password length must be a positive integer")

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid password length. Please enter a positive integer.")

    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
        print("Generated password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

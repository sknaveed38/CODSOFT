import random
import string

def generate_password(length):
    """Generates a random password of a specified length."""
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    # Define the character sets to use
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password with a random mix of all characters
    all_chars = lower + upper + digits + symbols
    password += [random.choice(all_chars) for _ in range(length - 4)]

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a number.")

import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure at least one character from each set
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest with random choices from all sets combined
    all_chars = lowercase + uppercase + digits + special_chars
    password_chars += random.choices(all_chars, k=length - 4)

    # Shuffle to randomize the order
    random.shuffle(password_chars)

    # Convert list to string
    password = ''.join(password_chars)
    return password

# Get user input for password length
try:
    password_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(password_length)
    if generated_password:
        print(f"\nGenerated Password: {generated_password}")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Get user input for password length
try:
    length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Generate and display the password
if length > 0:
    password = generate_password(length)
    print("Generated Password:", password)
else:
    print("Password length should be greater than 0.")

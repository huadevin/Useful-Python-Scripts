import random
import string

# Define the character sets
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_chars = string.punctuation

# Ask the user for input
password_length = int(input("How many characters do you want your password to be?: "))
include_uppercase = input("Include uppercase letters? (y/n): ")
include_lowercase = input("Include lowercase letters? (y/n): ")
include_digits = input("Include numbers? (y/n): ")
include_special_chars = input("Include special characters? (y/n): ")

# Build the list of character sets to include
char_sets = []
if include_uppercase.lower() == 'y':
    char_sets.append(uppercase_letters)
if include_lowercase.lower() == 'y':
    char_sets.append(lowercase_letters)
if include_digits.lower() == 'y':
    char_sets.append(digits)
if include_special_chars.lower() == 'y':
    char_sets.append(special_chars)

# Generate the password
password = ''
while len(password) < password_length:
    char_set = random.choice(char_sets)
    char = random.choice(char_set)
    password += char

# Print the password to the console
print("Your password is:", password)
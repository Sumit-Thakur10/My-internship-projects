import random  # Import the random module for generating random numbers....
import string  # Import the string module for working with strings.......

def generate_password(length=8):
    # Define a string containing all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly choosing characters from the defined string
    password = ''.join(random.choice(characters) for _ in range(length))
    return password  # Return the generated password

def generate_passwords(num_passwords, length=8):
    # Generate multiple passwords by calling the generate_password function multiple times
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords  # Return the list of generated passwords

if __name__ == "__main__":
    # Ask the user to input the number of passwords to generate
    num_passwords = int(input("Enter the number of passwords to generate: "))
    # Ask the user to input the length of each password
    length = int(input("Enter the length of each password: "))
    
    # Generate the specified number of passwords with the specified length
    passwords = generate_passwords(num_passwords, length)
    
    # Print the generated passwords
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

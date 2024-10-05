#Password Generator

import random
import string


def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter any  positive  length of the password: "))

        if length > 0:
            password = generate_password(length)
            print(f"Generated password: {password}")
        else:
            print("Please enter a length greater than 0.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        print("\nPassword Generator")
        print("1. Generate Password")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
                length = int(input("Enter the password length: "))
                use_letters = input("Include letters? (yes/no): ").lower() == "yes"
                use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
                use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

                password = generate_password(length, use_letters, use_numbers, use_symbols)
                print(f"Generated password: {password}")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
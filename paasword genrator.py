import secrets
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Create a pool of characters based on user preferences
    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    # Ensure the character pool is not empty
    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get password length from user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get character type preferences from user
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    try:
        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

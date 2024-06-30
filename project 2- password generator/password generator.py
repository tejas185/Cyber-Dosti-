import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generates a random password based on the specified criteria.
    
    Parameters:
    - length (int): Length of the password (default is 12).
    - use_uppercase (bool): Include uppercase letters (default is True).
    - use_lowercase (bool): Include lowercase letters (default is True).
    - use_digits (bool): Include digits (default is True).
    - use_special (bool): Include special characters (default is True).
    
    Returns:
    - str: The generated password.
    """
    
    # Create the character pool based on the criteria
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    # Ensure there's at least one type of character to choose from
    if not character_pool:
        raise ValueError("At least one character type must be selected")
    
    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

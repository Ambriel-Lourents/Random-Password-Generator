# user preferences
# - length
# - should contain uppercase
# - should contain special characters
# - should contain numbers

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of each type

import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() 
    include_special = input("Include special characters? (yes/no): ").strip().lower() 
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() 

# Validate input
    if length < 4:
        print("Password length must be at least 4.")
        return
    
    # include lowercase letters
    lower = string.ascii_lowercase

    # include uppercase letters if specified
    uppercase = string.ascii_uppercase if include_uppercase == 'yes' else ''
    # include special characters if specified
    special = string.punctuation if include_special == 'yes' else ''
    # include numbers if specified
    numbers = string.digits if include_numbers == 'yes' else ''
    # adds all characters together
    all_characters = lower + uppercase + special + numbers


    required_characters = []
    # chooses a random uppercase character
    if include_uppercase == 'yes':
        required_characters.append(random.choice(special))
    # chooses a random special character
    if include_special == 'yes':
        required_characters.append(random.choice(special))
    # chooses a random number
    if include_numbers == 'yes':
        required_characters.append(random.choice(numbers))

    # 
        remaining_length = length - len(required_characters)
        password = required_characters

        # runs the loop for the remaining amount of characters that have to be picked
        for _ in range(remaining_length):
            # picks one from all the valid characters
            character = random.choice(all_characters)
            password.append(character)
        
        # shuffles the generated characters
        random.shuffle(password)

        # combine all values in list to a string
        str_password = ''.join(password)
        return str_password

password = generate_password()
print(password)
# Generate a random password and require letters, numbers and special characters if needed.
import random
import string

def generate_strong_password(length: int, numbers: bool, special: bool):

    letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    specials = list('!?=+-()#')

    required =[random.choice(letters)]
    
    char_pool = letters.copy()

    if numbers:
        char_pool += digits
        required.append(random.choice(digits))

    if special:
        char_pool += specials
        required.append(random.choice(specials))
    
    remaining_length = length - len(required)

    if remaining_length > 0:
        required += random.choices(char_pool, k=remaining_length)

    random.shuffle(required)

    return ''.join(required)


    

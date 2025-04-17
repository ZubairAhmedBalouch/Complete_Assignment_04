import string
import random


# Generate a random password generator
def password_generator(length,use_digit=True):
    character = string.ascii_letters

    if use_digit:
        character +=string.digits
    
    
    return "".join(random.choice(character) for i in range(length))

password = password_generator(10,use_digit=True)
print(password)
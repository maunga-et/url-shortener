import string
import random

def generate_id():
    unique_id = ''

    while len(unique_id) < 7:
        characters = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [i for i in range(9)]
        random.shuffle(characters)
        generated_random_char = characters[random.randint(0, 36)]
        unique_id += str(generated_random_char)

    return unique_id

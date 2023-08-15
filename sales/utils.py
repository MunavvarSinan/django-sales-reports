import string
import random

def generate_code():
    code_length = 8
    characters = string.ascii_letters + string.digits
    return "tid_" + ''.join(random.choice(characters) for _ in range(code_length)) 
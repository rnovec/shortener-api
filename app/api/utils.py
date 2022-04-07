import random
import string


def generate_code(size=4):
    """Generate a user friendly code string"""
    str = string.ascii_letters
    return "".join(random.choice(str) for _ in range(size))

from random import choices
from string import ascii_lowercase


def generator_random_string(length):
    rand_str = choices(ascii_lowercase, k=length)
    return ' '.join(rand_str)

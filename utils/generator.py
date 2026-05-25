import random
import string

def generate_password(length, letters, numbers, symbols, exclude_similar):
    characters = ""

    if letters:
        characters += string.ascii_letters

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if exclude_similar:
        similar = "il1Lo0O"
        characters = ''.join(c for c in characters if c not in similar)

    if not characters:
        return "Select character types"

    password = ''.join(random.choice(characters) for _ in range(length))

    return password
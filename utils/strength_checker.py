import string

def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(c.islower() for c in password):
        strength += 1

    if any(c.isupper() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

    if any(c in string.punctuation for c in password):
        strength += 1

    if strength <= 2:
        return "Weak"

    elif strength <= 4:
        return "Medium"

    else:
        return "Strong"
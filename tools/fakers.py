import random

def random_email() -> str:
    return f"mike{random.randrange(1, 10000)}@gmail.com"

print(random_email())
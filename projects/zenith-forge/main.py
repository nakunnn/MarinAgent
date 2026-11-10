import secrets
import string
import math

def generate_password(length: int = 18) -> str:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*-_=+"
    return "".join(secrets.choice(alphabet) for _ in range(length))

def calculate_entropy(pwd: str) -> float:
    pool = 0
    if any(c in string.ascii_lowercase for c in pwd): pool += 26
    if any(c in string.ascii_uppercase for c in pwd): pool += 26
    if any(c in string.digits for c in pwd): pool += 10
    if any(c in "!@#$%^&*-_=+" for c in pwd): pool += 13
    return len(pwd) * math.log2(pool) if pool else 0.0

if __name__ == "__main__":
    p = generate_password()
    ent = calculate_entropy(p)
    print(f"Generated Password: {p} (Entropy: {ent:.2f} bits)")
    assert len(p) == 18

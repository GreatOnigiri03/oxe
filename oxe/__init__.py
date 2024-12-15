import random
from string import ascii_letters as letters, digits, punctuation

__characters = letters + digits + punctuation

def generate(__size: int) -> str:
    return str().join(random.SystemRandom().choice(__characters) for _ in range(__size))

def encrypt(__data: str, __key) -> str:
    return str().join([chr(ord(a) ^ ord(b)) for (a, b) in zip(__data, __key)])

def decrypt(__data: str, __key) -> str:
    return encrypt(__data, __key)

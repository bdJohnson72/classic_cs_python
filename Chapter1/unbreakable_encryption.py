from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    # convert bytes into bit string and return
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode();
    print(original_bytes)
    dummy: int = random_key(len(original_bytes))
    print(dummy)
    original_key: int = int.from_bytes(original_bytes, "big")
    print(original_key)
    encrypted_data: int = original_key ^ dummy
    print(encrypted_data)
    return dummy, encrypted_data


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return temp.decode()


key1, key2 = encrypt("Hello world")
decypted = decrypt(key1, key2)
print(decypted)
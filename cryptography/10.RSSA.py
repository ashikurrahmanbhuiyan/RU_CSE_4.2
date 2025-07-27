import math

# ---------- Helper Functions ----------

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    # Extended Euclidean Algorithm
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# ---------- RSA Key Generation ----------

def generate_keys():
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 17  # Common choice for e
    while gcd(e, phi) != 1:
        e += 2

    d = modinv(e, phi)
    
    return ((e, n), (d, n))  # public, private

# ---------- Encryption & Decryption ----------

def encrypt_integer(plaintext, pub_key):
    e, n = pub_key
    return pow(plaintext, e, n)

def decrypt_integer(ciphertext, priv_key):
    d, n = priv_key
    return pow(ciphertext, d, n)

def encrypt_string(plaintext, pub_key):
    return [encrypt_integer(ord(ch), pub_key) for ch in plaintext]

def decrypt_string(cipher_list, priv_key):
    return ''.join([chr(decrypt_integer(c, priv_key)) for c in cipher_list])

# ---------- Main ----------

def main():
    public_key, private_key = generate_keys()

    # Encrypt Integer
    int_message = 42
    encrypted_int = encrypt_integer(int_message, public_key)
    decrypted_int = decrypt_integer(encrypted_int, private_key)
    print("Original Integer:", int_message)
    print("Encrypted Integer:", encrypted_int)
    print("Decrypted Integer:", decrypted_int)

    # Encrypt String
    str_message = "Hello"
    encrypted_str = encrypt_string(str_message, public_key)
    decrypted_str = decrypt_string(encrypted_str, private_key)
    print("\nOriginal String:", str_message)
    print("Encrypted String:", encrypted_str)
    print("Decrypted String:", decrypted_str)

if __name__ == "__main__":
    main()

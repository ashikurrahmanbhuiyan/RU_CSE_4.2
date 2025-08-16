import math

def encrypt_transposition(plaintext, width):
    cleaned = plaintext.replace(" ", "").upper()
    while len(cleaned) % width != 0:
        cleaned += 'X'
    rows = [cleaned[i:i+width] for i in range(0, len(cleaned), width)]
    ciphertext = ''
    for col in range(width):
        for row in rows:
            ciphertext += row[col]
    return ciphertext, cleaned

def decrypt_transposition(ciphertext, width):
    num_rows = len(ciphertext) // width
    columns = [ciphertext[i*num_rows:(i+1)*num_rows] for i in range(width)]
    plaintext = ''
    for i in range(num_rows):
        for col in columns:
            plaintext += col[i]
    return plaintext.rstrip('X')

# ======================
# DOUBLE TRANSPOSITION
# ======================

# Original Plaintext
plaintext = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLOGY UNIVERSITY OF RAJSHAHI BANGLADESH"

# Transposition widths
width1 = 8
width2 = 5

# First transposition
first_cipher, cleaned1 = encrypt_transposition(plaintext, width1)

# Second transposition on the result of first
second_cipher, _ = encrypt_transposition(first_cipher, width2)

# Decrypt: reverse second then first
first_decryption = decrypt_transposition(second_cipher, width2)
final_decryption = decrypt_transposition(first_decryption, width1)

# Output
print("Original (no space):", cleaned1)
print("After 1st Transposition:", first_cipher)
print("Final Cipher (Double):", second_cipher)
print("Decrypted Text:", final_decryption)

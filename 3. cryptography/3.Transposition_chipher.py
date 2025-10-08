
def encrypt_transposition(plaintext, width):
    # Step 1: Remove spaces (optional)
    cleaned = plaintext.replace(" ", "").upper()
    
    # Step 2: Pad to make length a multiple of width
    while len(cleaned) % width != 0:
        cleaned += 'X'
    
    # Step 3: Form the matrix row-wise
    rows = [cleaned[i:i+width] for i in range(0, len(cleaned), width)]
    
    # Step 4: Read column-wise to get ciphertext
    ciphertext = ''
    for col in range(width):
        for row in rows:
            ciphertext += row[col]
    
    return ciphertext, cleaned  # return cleaned version for comparison

def decrypt_transposition(ciphertext, width):
    num_rows = len(ciphertext) // width
    # Step 1: Break into columns
    columns = [ciphertext[i*num_rows:(i+1)*num_rows] for i in range(width)]
    
    # Step 2: Reconstruct original row-wise text
    plaintext = ''
    for i in range(num_rows):
        for col in columns:
            plaintext += col[i]
    
    return plaintext.rstrip('X')  # remove padding


# =======================
# MAIN EXECUTION
# =======================

plaintext = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLOGY UNIVERSITY OF RAJSHAHI BANGLADESH"
width = int(input("Enter transposition width: "))

ciphertext, cleaned_plaintext = encrypt_transposition(plaintext, width)
decrypted_text = decrypt_transposition(ciphertext, width)

# Output
print("Original (no space):", cleaned_plaintext)
print("Ciphertext:          ", ciphertext)
print("Decrypted:           ", decrypted_text)

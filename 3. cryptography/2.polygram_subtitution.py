def chunk_text(text, size):
    return [text[i:i+size] for i in range(0, len(text), size)]

# Sample plaintext
plaintext = "HELLOWORLD"

# Block size
block_size = 3

# Step 1: Break into 3-letter blocks
blocks = chunk_text(plaintext, block_size)

# Step 2: Define substitution mapping (for demo purposes)
substitution_map = {
    'HEL': 'QWE',
    'LOW': 'RTY',
    'ORL': 'UIO',
    'D': 'P' 
}

# Create reverse mapping for decryption
reverse_map = {v: k for k, v in substitution_map.items()}

# Step 3: Encrypt
cipher_blocks = [substitution_map.get(block, '???') for block in blocks]
ciphertext = ''.join(cipher_blocks)

# Step 4: Decrypt
decrypted_blocks = [reverse_map.get(block, '???') for block in cipher_blocks]
decrypted_text = ''.join(decrypted_blocks)

# Output
print("Plaintext:     ", plaintext)
print("Blocks:        ", blocks)
print("Cipher Blocks: ", cipher_blocks)
print("Ciphertext:    ", ciphertext)
print("Decrypted:     ", decrypted_text)

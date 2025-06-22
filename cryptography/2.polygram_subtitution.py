import random
import string

def chunk_text(text, size):
    # Pad with spaces to make text divisible by block size
    while len(text) % size != 0:
        text += ' '
    return [text[i:i+size] for i in range(0, len(text), size)]

def generate_dynamic_mapping(blocks):
    unique_blocks = set(blocks)
    shuffled = list(unique_blocks)
    random.shuffle(shuffled)

    mapping = dict(zip(unique_blocks, shuffled))
    return mapping

def polygram_encrypt(text, block_size=3):
    blocks = chunk_text(text.lower(), block_size)
    mapping = generate_dynamic_mapping(blocks)
    cipher_blocks = [mapping[block] for block in blocks]
    cipher_text = ''.join(cipher_blocks)
    return cipher_text, mapping  # return mapping to use for decryption

def polygram_decrypt(cipher_text, mapping, block_size=3):
    reverse_mapping = {v: k for k, v in mapping.items()}
    blocks = chunk_text(cipher_text, block_size)
    original_blocks = [reverse_mapping[block] for block in blocks]
    return ''.join(original_blocks).strip()

# 🧪 Example
plaintext = "i love you"
ciphertext, mapping = polygram_encrypt(plaintext, block_size=3)
recovered = polygram_decrypt(ciphertext, mapping, block_size=3)

print("Plaintext   :", plaintext)
print("Ciphertext  :", ciphertext)
print("Decrypted   :", recovered)
print("Mapping     :", mapping)

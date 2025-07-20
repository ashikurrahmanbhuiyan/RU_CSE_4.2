
def read_key_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            key = file.read()
            return key
    except FileNotFoundError:
        print("Key file not found.")




def encrypt(message, key):
    encrypted = ''.join([chr((ord(m) + k-ord('A')+1)) for m, k in zip(message, key)])
    return encrypted

def decrypt(ciphertext, key):
    decrypted = ''.join([chr(ord(c) - k + ord('A')-1) for c, k in zip(ciphertext, key)])
    return decrypted


message = "HELLOZ"
print("Original Message:", message)

key1 = read_key_from_file('cryptography/encrypt_key.txt')
key2 = read_key_from_file('cryptography/decrypt_key.txt')


ciphertext = encrypt(message, key1)
print("Encrypted Message :", ciphertext)


decrypted_message = decrypt(ciphertext, key2)
print("Decrypted Message:", decrypted_message)

def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def caesar_decrypt(cipher_text, shift=3):
    return caesar_encrypt(cipher_text, -shift)


plaintext = "2kzcbkwh"
ciphered = caesar_encrypt(plaintext)
deciphered = caesar_decrypt(ciphered)

print("Original Plaintext: ", plaintext)
print("Caesar Ciphered   : ", ciphered)
print("Decrypted Back    : ", deciphered)

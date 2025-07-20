import hashlib

def md5_hash(input_string):
    # Create MD5 hash object
    md5 = hashlib.md5()
    
    # Update the hash with the input string encoded to bytes
    md5.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal digest
    return md5.hexdigest()

if __name__ == "__main__":
    user_input = input("Hello, sweety! Enter a string to hash: ")
    print("MD5 Hash:", md5_hash(user_input))

import hashlib

def md5_hash(input_string):
    md5 = hashlib.md5()
    
    md5.update(input_string.encode('utf-8'))
    return md5.hexdigest()

if __name__ == "__main__":

    user_input = "Ashikur Rahman"
    print("Input String:", user_input)
    print("MD5 Hash:", md5_hash(user_input))

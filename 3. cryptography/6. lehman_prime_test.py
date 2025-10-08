# import random

# def lehmer_test(n, iterations=100):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     if n < 100:
#         for i in range(3, int(n**0.5) + 1, 2):
#             if n % i == 0:
#                 return False
#         return True
    
#     for _ in range(iterations):
#         a = random.randint(2, n - 2)
        
#         if pow(a, n - 1, n) != 1:
#             return False
#     return True

# for n in [3, 79, 70000009, 15, 37, 101, 221, 561, 1021, 2047]:
#     print(f"{n}: {'Prime' if lehmer_test(n) else 'Not Prime'}")



import random

def lehmann_primality_test(n, k=10):
    if n <= 2:
        return n == 2
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        r = pow(a, (n - 1) // 2, n)

        if r != 1 and r != n - 1:
            return False

    return True


num = 10085476457653
if lehmann_primality_test(num):
    print(f"{num} is probably prime.")
else:
    print(f"{num} is composite.")

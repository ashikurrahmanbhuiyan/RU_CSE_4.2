import random

def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Step 1: Write n-1 as 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Step 2: Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # Composite

    return True  # Probably Prime

# Test values
for n in [3, 79, 70000009, 15, 37, 101, 221, 561, 1021, 2047]:
    print(f"{n}: {'Prime' if is_prime(n) else 'Not Prime'}")

def sieve_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, limit + 1, p):
                sieve[i] = False
    for p in range(int(limit**0.5) + 1, limit + 1):
        if sieve[p]:
            primes.append(p)
    return primes

def is_prime_eratosthenes(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def calculate_modulo(M, e, p):
    result = M ** e % p
    return result

M = 8
e = 5
p = 269

result = calculate_modulo(M, e, p)

if is_prime_eratosthenes(p):
    print(f"{p} is a prime number.")
    print(f"{M}^{e} mod {p} is {result}")

else:
    print(f"{p} is not a prime number.")
    print(f"{M}^{e} mod {p} is {result}")



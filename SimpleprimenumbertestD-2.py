import math
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    candidate = 5
    while candidate <= sqrt_n:
        if n % candidate == 0 or n % (candidate + 2) == 0:
            return False
        candidate += 6
    return True
def generate_primes_up_to(limit):
    prime_list = []
    for number in range(2, limit + 1):
        if is_prime(number):
            prime_list.append(number)
    return prime_list
limit = 1000
prime_numbers = generate_primes_up_to(limit)
print(prime_numbers)

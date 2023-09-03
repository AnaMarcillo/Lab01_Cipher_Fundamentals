def linear_congruential_random(a, seed, c, m, n):
    random_numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        random_numbers.append(x)
    return random_numbers

a = 21
seed = 35
c = 31
m = 100
n = 5 # Number of random numbers to generate

random_numbers = linear_congruential_random(a, seed, c, m, n)
print("Generated Random Numbers:")
for num in random_numbers:
    print(num)

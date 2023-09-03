"""Write a Python program to determine the
GCD for the following:
4105 and 10:
4539 and 6:"""
def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
ans1 = euclidean_gcd(4105,10)
ans2 = euclidean_gcd(4539, 6)
print(f"4105 and 10: {ans1}\n4539 and 6: {ans2}")
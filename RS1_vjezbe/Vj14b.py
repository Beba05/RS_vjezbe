def isPrime(broj):
    if broj <= 1:
        return False
    for i in range(2, int(broj**0.5) + 1):
        if broj % i == 0:
            return False
    return True


def primes_in_range(start, end):
    prosti = []
    for broj in range(start, end + 1):
        if isPrime(broj):
            prosti.append(broj)
    return prosti


# Primjer upotrebe:
print(primes_in_range(1, 10))   # [2, 3, 5, 7]
print(primes_in_range(10, 30))  # [11, 13, 17, 19, 23, 29]

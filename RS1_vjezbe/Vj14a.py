def isPrime(broj):
    if broj <= 1:
        return False  # prosti brojevi su samo > 1

    for i in range(2, broj):
        if broj % i == 0:  # ako se dijeli bez ostatka
            return False
    return True


# Primjeri:
print(isPrime(7))   # True
print(isPrime(10))  # False
print(isPrime(1))   # False
print(isPrime(2))   # True
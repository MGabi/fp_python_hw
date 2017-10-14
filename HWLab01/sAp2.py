from math import sqrt, ceil


def isPrime(n):
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(ceil(sqrt(n)))+1):
        if n % i == 0:
            return False

    return True

def primeSum(n):

    if n < 4:
        return "There are no prime numbers p1, p2 such that p1 + p2 = n"

    primes = []

    for i in range(2, n):
        if isPrime(i):
            primes.append(i)

    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            if primes[i] + primes[j] == n:
                print(primes[i], " ", primes[j])

    return ""


def main():
    n = int(input("Enter a number to find two\nprime numbers p1 and p2 such that N = p1 + p2: "))
    print(primeSum(n))


main()
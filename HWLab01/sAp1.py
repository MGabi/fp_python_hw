from math import sqrt


def isPrime(x):
    """
    Checking if a number is prime
    :param x: number to be checked
    :return: True if prime, False if not
    """
    if x < 2 or x % 2 == 0:
        return False

    for i in range(3, int(sqrt(x))+1):
        if x % i == 0:
            return False

    return True

def nextPrime(x):
    """
    Calculates the lowest prime number greater than X
    :param x: reference number
    :return: the lowest prime number greater than X
    """
    if x < 0:
        print("That's not a natural number")
        return ""

    x += 1
    while not isPrime(x):
        x += 1

    return x

def firstPrimeNumber():
    """
    Calculates the first prime number greater than a given X number
    :return: nothing
    """
    x = int(input("Enter a number to calculate the first prime number greater than it: "))
    #for x in range(1, 400, 23):
    print(nextPrime(x))

def main():
    firstPrimeNumber()

main()
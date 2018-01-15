"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/14/2018 23:18
"""
from datetime import datetime
from math import sqrt

from bkt import BacktrackingAlgorithm

def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def getFirstElement():
    return 2


def isConsistent(x, n):
    s = 0
    for el in x:
        s += el
    return s <= n


def isSolution(x, n):
    s = 0
    for el in x:
        s += el
    return s == n


def getSolution(x):
    return x


def getNextElement(x, n):
    if x[len(x) - 1] > n:
        return None
    el = x[len(x)-1] + 1

    while not isPrime(el):
        el += 1
    return el


def back_rec(x, n):
    el = getFirstElement()
    x.append(el)
    while el != None:
        x[len(x) - 1] = el
        if isConsistent(x, n):
            if isSolution(x, n):
                yield getSolution(x)
            else:
                yield from back_rec(x[:], n)
        el = getNextElement(x, n)


def back_iter(n):
    x = [getFirstElement()]
    while len(x) > 0:
        el = getNextElement(x, n)
        while el != None:
            x[len(x) - 1] = el
            if isConsistent(x, n):
                if isSolution(x, n):
                    yield getSolution(x)
                else:
                    x.append(getFirstElement())
                    break
            el = getNextElement(x, n)
        if el is None: x = x[:-1]

def main():
    time1 = datetime.now()
    res = back_rec([], 30)
    # res = back_iter(11)
    for sol in res:
        print(*sol)
    time2 = datetime.now()
    print(time2-time1)

main()
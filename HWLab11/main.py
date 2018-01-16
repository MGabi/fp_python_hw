"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/13/2018 15:08

     Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two
solutions: (()) and ()().
"""
from bkt import BacktrackingAlgorithm


def first(x):
    return 0


def consistent(x, n):
    z, u = 0, 0
    for e in x:
        if e == 0: z += 1
        if e == 1: u += 1
    if z > n // 2: return False
    return True if z >= u else False


def is_solution(x, n):
    return len(x) == n


def get_solution(x):
    s = ("(" if e == 0 else ")" for e in x)
    s = "".join(s)
    return s


def next_elem(x):
    if x[len(x) - 1] == 1:
        return None
    return x[len(x) - 1] + 1


def initial_value():
    return -1


def main():
    bkt = BacktrackingAlgorithm(first, consistent, is_solution, get_solution, next_elem, initial_value)
    res = bkt.back_iter(6)
    # res = bkt.back_rec([], 6)

    for sol in res:
        print(sol)

main()
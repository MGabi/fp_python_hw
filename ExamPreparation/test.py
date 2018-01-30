"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/28/2018 14:59
"""
from random import randint
from time import time

from copy import deepcopy

from searches import SearchAlgorithms
from sorting_algorithms import SortingAlgorithms

# random array generator
def generate_random_array(n):
    a = []
    for i in range(n):
        a.append(randint(1, 10000))
    return a


unsorted_list = generate_random_array(50)


print(*unsorted_list)
start3 = time()
sort = SortingAlgorithms.sort_insertionSort
sort(unsorted_list)
end3 = time() - start3

print(sort.__name__, "ends in", end3, " seconds.")
print(*unsorted_list)

# searchList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# start = time()
# search = SearchAlgorithms.binarySearch
# rez = search(searchList, 9)
# end = time()
# print(search.__name__, "finished in", end-start, "with result", rez)

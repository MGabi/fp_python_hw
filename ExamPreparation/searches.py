"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/28/2018 15:42
"""
class SearchAlgorithms(object):

    def __init__(self):
        pass

    @staticmethod
    def binarySearch(l, n):
        if len(l) == 0:
            return False
        if len(l) == 1:
            return l[0] == n

        mid = len(l) // 2

        if l[mid] > n:
            return SearchAlgorithms.binarySearch(l[:mid], n)
        return SearchAlgorithms.binarySearch(l[mid:], n)

    @staticmethod
    def seqSearch(l, n):
        for el in l:
            if el == n:
                return True

        return False
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/28/2018 14:26
"""
class SortingAlgorithms(object):

    def __init__(self):
        pass


    @staticmethod
    def sort_mergeSort(l):
        if len(l) > 1:
            mid = len(l) // 2

            left = l[:mid]
            right = l[mid:]

            i = 0
            j = 0
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    l[k] = left[i]
                    i += 1
                else:
                    l[k] = right[j]
                    j += 1

                k+=1

            while i < len(left):
                l[k] = left[i]
                i, k = i+1, k+1

            while j < len(right):
                l[k] = right[j]
                j, k = j+1, k+1

    @staticmethod
    def sort_insertionSort(l):

        for index in range(1, len(l)):
            curVal = l[index]
            pos = index

            while pos > 0 and l[pos-1] > curVal:
                l[pos] = l[pos - 1]
                pos -= 1

            l[pos] = curVal



    @staticmethod
    def sort_bubbleSort(l):
        n = len(l)
        done = False
        while not done:
            done = True
            for i in range(0, n - 1):
                if l[i] < l[i + 1]:
                    done = False
                    l[i], l[i + 1] = l[i + 1], l[i]

            n -= 1
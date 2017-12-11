"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/11/2017 18:51
"""
from collections import OrderedDict

from copy import deepcopy


class MyDict(dict):
    def __init__(self):
        super(MyDict, self).__init__()

    # GNOME SORT
    def sort(self, func, lst):
        poz = 0
        listLen = len(lst)
        while poz < listLen:
            # if i and lst[i] < lst[i - 1]:
            if poz > 0 and func(lst[poz], lst[poz-1]):
                lst[poz], lst[poz - 1] = lst[poz - 1], lst[poz]
                poz -= 1
            else:
                poz += 1
        return lst

    def bongoSort(self, fun, lst):
        pass

    def filter(self, func):
        finalList = []

        for k, elem in self.items():

            if func(elem, finalList):
                finalList.append(elem)
        return finalList
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/11/2017 18:51
"""
import random
from collections import OrderedDict

from copy import deepcopy


class MyDict(dict):

    def __init__(self):
        super(MyDict, self).__init__()

    def __setitem__(self, key, value):
        super(MyDict, self).__setitem__(key, value)

    def __delitem__(self, key):
        super(MyDict, self).__delitem__(key)

    def __next__(self):
        super(MyDict, self).__next__()

    def __iter__(self):
        super(MyDict, self).__iter__()

    # GNOME SORT
    # def sort(self, func, lst):
    #     poz = 0
    #     listLen = len(lst)
    #     while poz < listLen:
    #         # if i and lst[i] < lst[i - 1]:
    #         if poz > 0 and func(lst[poz], lst[poz-1]):
    #             lst[poz], lst[poz - 1] = lst[poz - 1], lst[poz]
    #             poz -= 1
    #         else:
    #             poz += 1
    #     return lst

    @staticmethod
    def sort(func, collection):
        """Pure implementation of the bogosort algorithm in Python
        :param collection: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
        """
        def isSorted(collection):
            if len(collection) < 2:
                return True
            for i in range(len(collection) - 1):
                if func(collection[i+1], collection[i]):
                #if collection[i] > collection[i + 1]:
                    return False
            return True

        while not isSorted(collection):
            random.shuffle(collection)
        return collection

    def filter(self, func):
        finalList = []

        for k, elem in self.items():

            if func(elem, finalList):
                finalList.append(elem)
        return finalList
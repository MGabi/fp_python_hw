"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/14/2018 19:34
"""
class BacktrackingAlgorithm(object):

    def __init__(self, getFirstElement, isConsistent, isSolution, getSolution, getNextElement, getInitialValue):
        self.__getFirstElement = getFirstElement
        self.__isConsistent = isConsistent
        self.__isSolution = isSolution
        self.__getSolution = getSolution
        self.__getNextElement = getNextElement
        self.__getInitialValue = getInitialValue

    def back_rec(self, x, n):
        el = self.__getFirstElement(x)
        x.append(el)
        while el != None:
            x[len(x) - 1] = el
            if self.__isConsistent(x, n):
                if self.__isSolution(x, n):
                    yield self.__getSolution(x)
                else:
                    #                     for s in self.back_rec(x[:], n):
                    #                         yield s
                    yield from self.back_rec(x[:], n)
            el = self.__getNextElement(x)


    def back_iter(self, n):
        x = [self.__getInitialValue()]
        while len(x) > 0:
            el = self.__getNextElement(x)
            while el != None:
                x[len(x) - 1] = el
                if self.__isConsistent(x, n):
                    if self.__isSolution(x, n):
                        yield self.__getSolution(x)
                    else:
                        x.append(self.__getInitialValue())
                        break
                el = self.__getNextElement(x)
            if el is None: x = x[:-1]

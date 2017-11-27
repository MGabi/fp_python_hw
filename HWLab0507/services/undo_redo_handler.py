"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/26/2017 16:42
"""
from zope.interface import interface


class Operation(object):
    def __init__(self, service, oldFunc, reverseFunc, *params):
        self.__service = service
        self.__oldFunc = oldFunc
        self.__reverseFunc = reverseFunc
        self.__params = params

    @property
    def service(self):
        return self.__service

    @property
    def oldFunc(self):
        return self.__oldFunc

    @property
    def reverseFunc(self):
        return self.__reverseFunc

    @property
    def params(self):
        return self.__params

    def __str__(self):
        s = str(self.service) + "\n" + str(self.oldFunc) + "\n" + str(self.reverseFunc) + "\n" + str(self.params)
        return s

class UndoHandler(object):

    def __init__(self):
        self.__operations = []
        self.__operationsIndex = -1

    def registerOperation(self, service, oldFunc, reverseFunc, *params):
        self.opList.append(Operation(service, oldFunc, reverseFunc, params))
        self.opIndex = len(self.opList) - 1

    def deleteLastOperation(self):
        self.opList.pop()

    @property
    def opList(self):
        return self.__operations

    @property
    def opIndex(self):
        return self.__operationsIndex

    @opIndex.setter
    def opIndex(self, index):
        self.__operationsIndex = index

    def undo(self):
        if len(self.opList) < 1:
            raise Exception("You have nothing to undo!")

        op = self.opList.pop()
        op.reverseFunc(*op.params)



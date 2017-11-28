"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/26/2017 16:42
"""

class Operation(object):
    def __init__(self, reverseFunc, *params):
        self.__reverseFunc = reverseFunc
        self.__params = params

    @property
    def reverseFunc(self):
        return self.__reverseFunc

    @property
    def params(self):
        return self.__params

    def __str__(self):
        s = str(self.reverseFunc) + "\n" + str(self.params)
        return s

class UndoHandler(object):

    def __init__(self):
        self.__operationsUndo = []
        self.__operationsRedo = []
        self.__listIndex = -1

    def registerOperationUndo(self, reverseFunc, *params):
        self.deleteAfterActions()
        self.opListUndo.append(Operation(reverseFunc, params))
        self.listIndex = len(self.opListUndo) - 1

    def registerOperationRedo(self, reverseFunc, *params):
        self.opListRedo.append(Operation(reverseFunc, *params))

    @property
    def opListUndo(self):
        return self.__operationsUndo

    @property
    def opListRedo(self):
        return self.__operationsRedo

    @property
    def listIndex(self):
        return self.__listIndex

    @listIndex.setter
    def listIndex(self, index):
        self.__listIndex = index

    def undo(self):
        if self.listIndex < 0:
            raise Exception("You have nothing to undo!")

        op = self.opListUndo[self.listIndex]
        op.reverseFunc(*op.params)
        self.listIndex -= 1

    def redo(self):
        if self.listIndex+1 > len(self.__operationsRedo)-1:
            raise Exception("You have nothing to redo!")

        op = self.opListRedo[self.listIndex+1]
        op.reverseFunc(*op.params)
        self.listIndex += 1

    def deleteAfterActions(self):
        l = len(self.opListRedo)
        for i in range(1, l - self.listIndex):
            self.opListRedo.pop()
            self.opListUndo.pop()


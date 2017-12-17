"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 13:30
"""
class Player(object):

    def __init__(self, playerType):
        self.__playerType = playerType
        self.__dots = []

    @property
    def playerType(self):
        return self.__playerType

    @property
    def dots(self):
        return self.__dots

    def addDot(self, dot):
        self.dots.append(dot)
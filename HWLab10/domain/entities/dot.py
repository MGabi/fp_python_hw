"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 13:37
"""
class Dot(object):

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    def applyColor(self, color):
        if color == 0:
            return str(color)
        if color == 1:
            return "\033[31m" + str(color) + "\033[0m"
        if color == 2:
            return "\033[34m" + str(color) + "\033[0m"

    def __str__(self):
        return self.applyColor(self.__color)
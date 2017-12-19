"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/19/2017 12:16
"""
class Driver(object):

    def __init__(self, name, dx, dy):
        self.__name = name
        self.__dx = dx
        self.__dy = dy

    @property
    def name(self):
        return self.__name

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    def __str__(self):
        return self.name + "," + str(self.dx) + "," + str(self.dy) + "\n"

    @staticmethod
    def fromStrToObj(obj):
        return Driver(obj[0], int(obj[1]), int(obj[2]))
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/19/2017 12:13
"""
class Address(object):

    def __init__(self, id, address, dx, dy):
        self.__id = id
        self.__address = address
        self.__dx = dx
        self.__dy = dy

    @property
    def id(self):
        return self.__id

    @property
    def address(self):
        return self.__address

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    def __str__(self):
        return str(self.id) + "," + self.address + "," + str(self.dx) + "," + str(self.dy) + " \n"

    @staticmethod
    def fromStrToObj(obj):
        return Address(int(obj[0]), obj[1], int(obj[2]), (obj[3]))
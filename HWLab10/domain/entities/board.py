"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 13:16
"""
from random import randint

from domain.entities.dot import Dot


class Board(object):
    """
    Board objects where the game
    will be played
    0 - empty
    1 - user
    2 - computer
    """
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__table = [[Dot(0) for i in range(self.__width)] for j in range(self.__height)]

    @property
    def table(self):
        return self.__table

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def __str__(self):
        brd = "\n\033[31mTable:\033[0m\n\n"
        for line in self.__table:
            for dot in line:
                brd += str(dot) + " "
            brd += "\n"
        return brd

    def isAnyDotAvaiable(self,column):
        for line in self.table:
            if line[column].color is 0:
                return True
        return False

    def makeMove(self, column, dot):
        for i in range(self.__height-1, -1, -1):
            if self.__table[i][column].color == 0:
                self.__table[i][column] = dot
                return

    def isGroupOk(self, dot1, dot2, dot3, dot4):
        return dot1.color == dot2.color == dot3.color == dot4.color and dot1.color != 0
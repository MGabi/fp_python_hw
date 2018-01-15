"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/19/2017 19:03
"""
from tkinter import Tk, ttk, Frame, Button


class UiHandler(object):

    def __init__(self, root):
        self.__root = root
        self.__frame = Frame(self.__root)
        self.__frame.pack_propagate(0)
        self.__dots = [[None for x in range(7)] for x in range(6)]

    @property
    def root(self):
        return self.__root

    @property
    def frame(self):
        return self.__frame

    @property
    def dots(self):
        return self.__dots

    def openUi(self):
        self.root.title("Connect Four")
        self.frame.grid(row=6, column=7)

        for x in range(6):
            for y in range(7):
                self.dots[x][y] = Button(self.frame, text= str(0))
                self.dots[x][y].grid(column=x, row=y, command = self.setColor("red", x, y))

    def setColor(self, color, x, y):
        self.dots[x][y].config(bg=color)
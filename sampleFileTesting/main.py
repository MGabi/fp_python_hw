"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/29/2017 16:52
"""
import pickle

import os
from random import randint


class TestObj(object):

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def ID(self):
        return self.__id

    @ID.setter
    def ID(self, id):
        self.__id = id

    @property
    def NAME(self):
        return self.__name

    @NAME.setter
    def NAME(self, name):
        self.NAME = name

    def __str__(self):
        return "ID: " + str(self.__id) + " Name: " + self.__name

    def strForFile(self):
        return str(self.ID) + ";" + self.NAME + "\n"

def readFromBinaryFile(fileName):
    result = []
    try:
        f = open(fileName, "r")
        line = f.readline().strip()
        while len(line)>0:
            try:
                line = line.split(";")
                result.append(TestObj(line[0], line[1]))
                line = f.readline().strip()
            except EOFError:
                break
        f.close()
    except EOFError:
        print("The file is empty")
        return []
    except IOError as ioe:
        print("IO error:", str(ioe))
        return []
    f.close()
    return result

def writeToBinaryFile(fileName, object):
    f = open(fileName, "a")
    f.write(object.strForFile())
    f.close()

def main():

    writeToBinaryFile("testfile", TestObj(randint(1, 15), "Name" + str(randint(1, 15))))
    l = readFromBinaryFile("testfile")
    for el in l:
        print(el)
main()
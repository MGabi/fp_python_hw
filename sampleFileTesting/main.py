"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/29/2017 16:52
"""
import json
import pickle

import os
import sqlite3
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

    def toJson(self):
        return {"id": self.ID, "name": self.NAME}

def readAll(fileName):
    with open(fileName, "r") as jsonFile:
        try:
            return json.load(jsonFile)
        except Exception as ex:
            print(str(ex))
        return {}

def writeAll(fileName, data):
    with open(fileName, "w") as out:
        json.dump(data, out)

def save(fileName, node, obj):
    data = readAll(fileName)
    if node not in data.keys():
        data[node] = {}
    data[node][str(obj.ID)] = obj.toJson()
    writeAll(fileName, data)

def update(fileName, node, object):
    data = readAll(fileName)
    data[node][str(object.ID)] = object.toJson()
    writeAll(fileName, data)

def delete(fileName, node, ID):
    data = readAll(fileName)
    data[node].pop(str(ID))
    writeAll(fileName, data)


def main():
    fileName = "testFileJSON"
    f = open(fileName, "a")
    f.close()
    save(fileName, "test", TestObj(3, "Name3"))
    save(fileName, "test", TestObj(5, "Name5"))
    save(fileName, "test", TestObj(4, "Name4"))
    print("")
    print(readAll(fileName))
    print("")
    update(fileName, "test", TestObj(3, "333"))
    delete(fileName, "test", 5)
    print("")
    print(readAll(fileName))
    print("")
    #output : 3 5 4
    # 3, 333
    # 4, Name4

main()

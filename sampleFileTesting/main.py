"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/29/2017 16:52
"""
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

def readFromDB(fileName):
    conn = sqlite3.connect(fileName)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM testobj")
    l = cursor.fetchall()
    conn.close()
    return l

def setupDB(fileName):
    conn = sqlite3.connect(fileName)
    cursor = conn.cursor()
    sql_cmd = """
    CREATE TABLE IF NOT EXISTS testobj (
      id INTEGER PRIMARY KEY,
      name VARCHAR(30)
    )
    """
    cursor.execute(sql_cmd)
    conn.commit()
    conn.close()

def save(fileName, obj):
    try:
        conn = sqlite3.connect(fileName)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO testobj VALUES (?, ?)", (obj.ID, obj.NAME, ))
        conn.commit()
        conn.close()
    except Exception as ex:
        print(str(ex))

def update(fileName, object):
    conn = sqlite3.connect(fileName)
    cursor = conn.cursor()
    cursor.execute("UPDATE testobj SET id=?, name=? WHERE id=?", (object.ID, object.NAME, object.ID,))
    conn.commit()
    conn.close()

def delete(fileName, ID):
    conn = sqlite3.connect(fileName)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM testobj WHERE id=?", (ID,))
    conn.commit()
    conn.close()

def main():

    fileName = "testFileSQL.db"
    setupDB(fileName)
    save(fileName, TestObj(5, "Jhon"))
    save(fileName, TestObj(3, "Marry"))
    save(fileName, TestObj(5, "Alex"))
    save(fileName, TestObj(9, "Roland"))
    update(fileName, TestObj(3, "Martin"))
    delete(fileName, 9)
    #output: 5, Jhon / 3, Martin /

    # l = readFromDB(fileName)
    # for el in l:
    #     print(type(el))
    #     print(el)
    print(tuple(TestObj(55, "JHONNY")))
main()
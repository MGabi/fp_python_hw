"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/6/2017 23:40
"""
from _datetime import datetime
from random import randint

from domain.entities.client import Client
from domain.entities.movie import Movie
from domain.entities.rental import Rental


def dateFromStr(date):
    """
    Returns a timestamp from a given date
    :param date: date to create timestamp
    :return: timestamp as float
    """
    return datetime.strptime(date, "%d/%m/%Y").timestamp()

def getSecFromDays(days):
    """
    Returns the seconds contained in a number of days
    :param days: number of days
    :return: seconds in a given number of days
    """
    return days*24*60*60

def addElements(store):
    for i in range(1, 10):
        store.addToList(1, Client(i, "Name" + str(i)))
        store.addToList(2, Movie(i, "Title" + str(i), "Desc" + str(i), "Genre" + str(i)))

    for i in range(0, 6):
        store.addToList(3, Rental(i, randint(1, 10), randint(1, 10), dateFromStr(str(randint(1, 12)) + "/" + str(randint(1, 12)) + "/" + str(randint(2015, 2017))), datetime.now().timestamp(), None))

def getNextIndex(entityList, keyword):
    return entityList[len(entityList)-1].getAttrs()[keyword] + 1
"""
    MOVIE RENTAL Application

    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   10/31/2017 13:08
"""
from domain.entities.movie import Movie
from domain.entities.client import Client
from domain.entities.store import *
from services.option_handler import *
from ui.menu import *


def addElements(store):
    store.addMovie(Movie(1, "Title1", "Desc1", "Genre1"))
    store.addMovie(Movie(2, "Title2", "Desc2", "Genre2"))
    store.addMovie(Movie(3, "Title3", "Desc3", "Genre3"))
    store.addClient(Client(1, "Name1"))
    store.addClient(Client(2, "Name2"))
    store.addClient(Client(3, "Name3"))
    store.addClient(Client(4, "Name4"))

def startup():
    store = Store()

    printMenu()
    addElements(store)
    while True:
        printOptions()
        selectedOption, resultOption = readOption(optionsLen)

        if resultOption and selectedOption in range(1, 5):
            resultList = False

            while not resultList:
                printChooseList()
                selectedList, resultList = readOption(availableListsLen)

                if resultList:
                    options[selectedOption](store, selectedList)

startup()
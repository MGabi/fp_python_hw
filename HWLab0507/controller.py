"""
    MOVIE RENTAL Application

    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   10/31/2017 13:08
"""
from domain.entities.store import *
from services.option_handler import *
from ui.menu import *
from services.utils import *
from random import randint

def addElements(store):
    for i in range(1, 10):
        store.addMovie(Movie(i, "Title" + str(i), "Desc" + str(i), "Genre" + str(i)))
        store.addClient(Client(i, "Name" + str(i)))

    for i in range(0, 6):
        store.addRental(Rental(i, randint(1, 10), randint(1, 10), dateFromStr(str(randint(1, 12)) + "/" + str(randint(1, 12)) + "/" + str(randint(2015, 2018))), datetime.now().timestamp(), None))


def startup():
    """
    Main method for the program
    Initialize the store object and
    starts to read user options
    :return: nothing
    """
    store = Store()

    printMenu()
    addElements(store)
    while True:
        printOptions()
        selectedOption, resultOption = readOption(optionsLen)

        if resultOption:
            if selectedOption in range(1, 5):
                resultList = False

                while not resultList:
                    printChooseList()
                    selectedList, resultList = readOption(availableListsLen)

                    if resultList:
                        options[selectedOption](store, selectedList)

            elif selectedOption in [5, 6]:
                options[selectedOption](store)

startup()
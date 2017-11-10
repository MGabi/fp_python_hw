"""
    MOVIE RENTAL Application

    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   10/31/2017 13:08
"""
from domain.entities.store import *
from domain.validators.tests import test_all
from services.option_handler import *
from ui.menu import *
from services.utils import *

def startup():
    """
    Main method for the program
    Initialize the store object and
    starts to read user options
    :return: nothing
    """
    store = Store()
    addElements(store)
    #test_all(store)
    printMenu()
    while True:
        printOptions()
        selectedOption, resultOption = readOption(optionsLen)
        if selectedOption == 0:
            printByeBye()
            return
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
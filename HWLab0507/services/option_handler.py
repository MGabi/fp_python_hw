"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/3/2017 13:35
"""
from domain.validators.input_validation import *
from services.read_user_input import *
from ui.console_output import *
from ui.menu import *

optionsLen = 8
availableListsLen = 2

def optionAdd(store, listNumber):
    if listNumber == 1:
        store.addClient(getNewClientFromConsole())
    elif listNumber == 2:
        store.addMovie(getNewMovieFromConsole())

def optionRemove(store, listNumber):
    if listNumber == 1:
        store.removeClient(getIndexFromConsole(len(store.clientsList), inputPromptForRemovalIndex(len(store.clientsList))))
    elif listNumber == 2:
        store.removeMovie(getIndexFromConsole(len(store.moviesList), inputPromptForRemovalIndex(len(store.moviesList))))

def optionUpdate(store, listNumber):
    if listNumber == 1:
        index = getIndexFromConsole(len(store.clientsList), inputPromptForUpdateIndex(len(store.clientsList)))
        store.clientsList[index] = getNewClientFromConsole()
    elif listNumber == 2:
        index = getIndexFromConsole(len(store.moviesList), inputPromptForUpdateIndex(len(store.moviesList)))
        store.moviesList[index] = getNewMovieFromConsole()

def optionList(store, listNumber):
    printListOfEntities(store.lists[listNumber](store))

def optionRent(store, listNumber):



options = {1: optionAdd,
           2: optionRemove,
           3: optionUpdate,
           4: optionList,
           5: optionRent}

def readOption(opLen):
    op = input("\033[31m>>> \033[0m")
    if validateOption(op, opLen):
        return int(op), True
    return 0, False
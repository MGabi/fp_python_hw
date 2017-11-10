"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/3/2017 13:35
"""
from domain.entities.rental import Rental
from services.utils import *
from services.read_user_input import *
from ui.console_output import *
from ui.menu import *
from _datetime import datetime

#optionsLen = len(options)
optionsLen = 10
availableListsLen = 3

def optionAdd(store, listNumber):
    """
    Handle the add feature on both clients and movies list
    Get a new client/movie and it will append it to the specific store list
    :param store: store object to work with
    :param listNumber: 1 for clients list, 2 for movies list
    :return: nothing
    """
    if listNumber == 1:
        store.addToList(1, getNewClientFromConsole())
    elif listNumber == 2:
        store.addToList(2, getNewMovieFromConsole())


def optionRemove(store, listNumber):
    """
    Handle the remove feature on both clients and movies list
    Get a index for removing a movie/object and removes the
    specific index from the movie/object list
    :param store: store object to work with
    :param listNumber: 1 for clients list, 2 for movies list
    :return: nothing
    """
    if listNumber == 1:
        store.removeFromList(1, getIndexFromConsole(len(store.clientsList),inputPromptForRemovalIndex(len(store.clientsList))))
    elif listNumber == 2:
        store.removeFromList(2, getIndexFromConsole(len(store.moviesList), inputPromptForRemovalIndex(len(store.moviesList))))

def optionUpdate(store, listNumber):
    """
    Handle the update feature on both clients and movies list
    Will get the new data for updating a client/movie
    :param store: store object to work with
    :param listNumber: 1 for clients list, 2 for movies list
    :return:
    """
    if listNumber == 1:
        index = getIndexFromConsole(len(store.getClientsList()), inputPromptForUpdateIndex(len(store.getClientsList())))
        store.updateList(1, getNewClientFromConsole(), index)
    elif listNumber == 2:
        index = getIndexFromConsole(len(store.getMoviesList()), inputPromptForUpdateIndex(len(store.getMoviesList())))
        store.updateList(2, getNewMovieFromConsole(), index)

def optionList(store, listNumber):
    """
    Handle the list feature on both clients and movies list
    :param store: store object to work with
    :param listNumber: 1 for clients list, 2 for movies list
    :return: nothing
    """
    printListOfEntities(store.lists[listNumber](store))


def optionRent(store):
    """
    Handle the renting feature for the store.
    After getting the user for a new rent, will
    receive a movie to create a new rental
    with a period of 14 DAYS
    :param store: store object to work with
    :return: nothing
    """
    index, clientID = getUserIndexForRental(store.getClientsList())

    if validateUserRentalStatus(clientID, store.getRentalsList()):
        movie = getDesiredMovieForRent(store.getMoviesList())
        currTime = datetime.now().timestamp()
        newRentID = getNextIndex(store.getRentalsList(), KEYWORDS.rental_id)
        store.addToList(3, Rental(newRentID, movie.getMovieID(), clientID, currTime, currTime + getSecFromDays(14), None))
        printListOfEntities(store.getRentalsList())

def optionReturn(store):
    print("in opReturn")
    pass

options = {1: optionAdd,
           2: optionRemove,
           3: optionUpdate,
           4: optionList,
           5: optionRent,
           6: optionReturn}

def readOption(opLen):
    """
    Reads a menu option from console
    :param opLen: the lenght of possible options
    :return: the operation index
    """
    op = input("\033[31m>>> \033[0m")
    if validateInRange(op, opLen):
        return int(op), True
    return 0, False
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/3/2017 13:40
"""
from domain.entities.errors import *
from ui.error_messages import *
from _datetime import datetime
import domain.entities.keywords as KEYWORDS

def validateClient(clientID, clientName):
    """
    Validate input data for a new Client
    :param clientID: ID for a new client
    :param clientName: name for a new client
    :return: True if all conditions are aquired, False if not
    """
    #TODO: Make validation for client
    return True

def validateMovie(movieID, movieTitle, movieDescription, movieGenre):
    """
    Validate input data for a new Movie
    :param movieID: ID for a new movie
    :param movieTitle: title for a new movie
    :param movieDescription: description for a new movie
    :param movieGenre: genre for a new movie
    :return: True if all conditions are aquired, False if not
    """
    #TODO: Make validation for movie
    return True

def validateInRange(index, listLen):
    """
    Validate the fact that a given index fits
    in a certain lenght of a list
    :param index: index that need validation
    :param listLen: lenght of the list
    :return: True if the index is in the listLen, False if n
    """
    try:
        index = int(index)
        if index not in range(0, listLen):
            raise OutOfRangeError
        return True
    except ValueError as ve:
        notIntErrorMsg()
        return False
    except OutOfRangeError as oor:
        notInRangeErrorMsg()
        return False


def verifyDueDate(dueDate):
    print(dueDate)
    print(datetime.now().timestamp())
    print(dueDate > datetime.now().timestamp())
    return dueDate > datetime.now().timestamp()


def validateUserRentalStatus(clientID, rentalsList):
    """
    Checks if a user can make a rental
    :param index: index of client in clientList
    :param clientID: clientID which will make the rent
    :param rentalsList: the list of all rentals which store made
    :return: True if user has no rented movies that passed
             their due date for return
    """
    for rental in rentalsList:
        rentalAttrs = rental.getAttrs()
        if rentalAttrs[KEYWORDS.client_id] == clientID:
            if not verifyDueDate(rentalAttrs[KEYWORDS.due_date]):
                clientCannotRent()
                return False
    return True

def validateInt(value):
    """
    Validates if a value is an int
    :param value: value that needs to be checked
    :return: True if it's an int, false if not
    """
    try:
        value = int(value)
        return True
    except ValueError as ve:
        notIntErrorMsg()
        return False
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/3/2017 13:40
"""
from domain.entities.errors import OutOfRangeError
from ui.error_messages import *

def validateOption(option, opLen):
    try:
        option = int(option)
        if option in range(1, opLen + 1):
            return True
        else:
            raise OutOfRangeError
    except ValueError as ve:
        notIntErrorMsg()
        return False
    except OutOfRangeError as oor:
        notInRangeErrorMsg()
        return False

def validateClient(clientID, clientName):
    #TODO: Make validation for client
    return True

def validateMovie(movieID, movieTitle, movieDescription, movieGenre):
    #TODO: Make validation for movie
    return True

def validateInRange(index, listLen):
    try:
        index = int(index)
        if index not in range(1, listLen+1):
            raise OutOfRangeError
        return index
    except ValueError as ve:
        notIntErrorMsg()
    except OutOfRangeError as oor:
        notInRangeErrorMsg()
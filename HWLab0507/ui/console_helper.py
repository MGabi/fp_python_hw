"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 15:36
"""
from domain.validators.option_validator import OptionValidator
from services.utils import *

class ConsoleHelper(object):

    @staticmethod
    def readCommand(len, min=0):
        op = input("\033[91m>>>\033[0m")
        OptionValidator.validate(op, min, len)
        return int(op)

    @staticmethod
    def readID():
        rID = input("ID: ")
        rID = int(rID)
        return rID

    @staticmethod
    def readClient():
        cID = input("Client ID:")
        cID = int(cID)
        name = input("Client name:")
        return {Utils.CLIENT_ID: cID, Utils.CLIENT_NAME: name}

    @staticmethod
    def readMovie():
        mID = input("Movie ID:")
        mID = int(mID)
        title = input("Movie title:")
        desc = input("Movie description:")
        genre = input("Movie genre:")
        return {Utils.MOVIE_ID: mID,
                Utils.MOVIE_TITLE: title,
                Utils.MOVIE_DESCRIPTION: desc,
                Utils.MOVIE_GENRE: genre}

    @staticmethod
    def readRental():
        rID = input("Rental ID:")
        rID = int(rID)
        movieID = input("Movie ID:")
        clientID = input("client ID:")
        rentedDate = 0
        dueDate = 0
        returnedDate = None

        return {Utils.RENTAL_ID: rID,
                Utils.MOVIE_ID: movieID,
                Utils.CLIENT_ID: clientID,
                Utils.RENTED_DATE: rentedDate,
                Utils.DUE_DATE: dueDate,
                Utils.RETURNED_DATE: returnedDate}

    @staticmethod
    def printError(args):
        print("\n\033[31m   ", args, "\033[0m\n")

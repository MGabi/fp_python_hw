"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 15:36
"""
from domain.validators.option_validator import OptionValidator
from services.utils import *

class ConsoleHelper(object):

    @staticmethod
    def readCommand(max, min=0):
        """
        Reads a command from console
        for a given interval
        OptionException will be raised if validation fails
        :param max: max element for current option
        :param min: min element for current option
        :return: the option as an int
        """
        op = input("\033[91m>>>\033[0m")
        OptionValidator.validate(op, min, max)
        return int(op)

    @staticmethod
    def readID():
        """
        Reads an ID for removing/updating a list
        ValueError will be raised if the ID is not an int
        :return: the ID as an int
        """
        rID = input("ID: ")
        rID = int(rID)
        return rID

    @staticmethod
    def readClient():
        """
        Reads the data for a new client
        or for updating an existing client
        ValueError will be raised if the ID is not an int
        :return: client attributes as a dictionary
        """
        cID = input("Client ID:")
        cID = int(cID)
        name = input("Client name:")
        return {Utils.CLIENT_ID: cID, Utils.CLIENT_NAME: name}

    @staticmethod
    def readMovie():
        """
        Reads the data for a new movie
        or for updating an existing movie
        ValueError will be raised if the ID is not an int
        :return: movie attributes as a dictionary
        """
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
        """
        Reads the data for a new rental
        ValueError will be raised if the ID is not an int
        :return: rental attributes as a dictionary
        """
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
        """
        Prints an error with color/format
        :param args: the error text
        :return: nothing
        """
        print("\n\033[31m   ", args, "\033[0m\n")

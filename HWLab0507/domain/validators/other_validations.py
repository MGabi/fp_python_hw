"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/13/2017 12:56
"""
from services.utils import Utils
from datetime import datetime

class ValidateException(Exception):
    pass

class ValidateUserRentalStatus(object):
    @staticmethod
    def validate(clientID, rentals, movieID):
        for rent in rentals.values():
            if rent.clientID == clientID:
                if rent.dueDATE < datetime.now().timestamp():
                    raise ValidateException("Client {0} can't rent because he has\nother rents with due date passed!".format(clientID))
                if rent.movieID == movieID:
                    raise ValidateException("Client {0} already rented movie with ID {1}".format(clientID, movieID))

class ValidateMovieCanBeRented(object):
    @staticmethod
    def validate(movieID, movies):
        if movieID not in movies.keys():
            raise ValidateException("The movie with ID {0} does not exist!".format(movieID))
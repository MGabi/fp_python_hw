"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:42
"""
class RentalException(Exception):
    pass

class RentalValidator(object):

    @staticmethod
    def validate(rental):
        if type(rental.ID) is not int:
            raise RentalException("ID {0} is not an int!".format(rental.ID))
        if type(rental.movieID) is not int:
            raise RentalException("Movie ID {0} is not an int!".format(rental.movieID))
        if type(rental.clientID) is not int:
            raise RentalException("Client ID {0} is not an int!".format(rental.clientID))
        if rental.ID < 1:
            raise RentalException("Rental ID {0} should be strictly greater than 0!".format(rental.ID))
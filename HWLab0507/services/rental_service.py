"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:53
"""
from domain.entities.rental import Rental
from services.utils import *


class RentalService(object):

    def __init__(self, manager):
        self.__rentalManager = manager

    # def addRental(self, rentalID, movieID, clientID, rentedDate, dueDate, returnedDate):
    #     rental = Rental(rentalID, movieID, clientID, rentedDate, dueDate, returnedDate)
    #     self.__rentalManager.saveEntity(rental)

    def addRental(self, attrs):
        rental = Rental(attrs[Utils.RENTAL_ID], attrs[Utils.MOVIE_ID], attrs[Utils.CLIENT_ID], attrs[Utils.RENTED_DATE], attrs[Utils.DUE_DATE], attrs[Utils.RETURNED_DATE])
        self.__rentalManager.saveEntity(rental)

    def getAllRentals(self):
        return self.__rentalManager.getEntities()

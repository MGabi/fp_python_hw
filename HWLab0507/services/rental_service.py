"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:53
"""
import operator

from domain.entities.my_dict import MyDict
from domain.entities.rental import Rental
from services.utils import *


class RentalService(object):

    def __init__(self, manager):
        self.__rentalManager = manager

    def addRental(self, rental):
        """
        Create a new rental with given attributes
        and save it to the storage
        :param attrs: attributes of the rental
        :return: nothing
        """
        self.__rentalManager.saveEntity(rental)

    def updateRental(self, rental):
        if isinstance(rental, tuple):
            rental = rental[0]
        self.__rentalManager.updateEntity(rental.ID, rental)

    def finishRental(self, rental):
        rental.returnedDATE = datetime.now().timestamp()
        self.__rentalManager.updateEntity(rental.ID, rental)

    def getRentalWithIDs(self, clientID, movieID):
        for rental in self.getAllRentals().values():
            if rental.clientID == clientID and rental.movieID == movieID:
                return rental
        return None

    def getRental(self, id):
        return self.__rentalManager.getEntityById(id)

    def getAllRentals(self):
        """
        Returns all existing rentals
        :return: all rentals as a list
        """
        return self.__rentalManager.getEntities()

    def getMostRentedMovies(self):
        """
        Creates a list with all movies
        sorted decreasingly by the
        number of times a movie was rented
        :return: a list of tuples like (x, y) -> x is the movie ID
        and the y is the number of times it was rented
        """
        movies = MyDict()
        for rental in self.getAllRentals().values():
            if rental.movieID in movies:
                movies[rental.movieID] += 1
            else:
                movies[rental.movieID] = 1

        finals = []
        for k, days in movies.items():
            finals.append(tuple([k, days]))

        return movies.sort(self.isHigher, finals)
       # return sorted(movies.items(), key = operator.itemgetter(1), reverse = True)

    def getMostActiveClients(self):
        """
        Creates a list with all clients
        sorted decreasingly by the number of
        days their movies were rented
        :return: a list of tuples like (x, y) -> x is the client ID
        and the y is the number of days of all its rentals
        """
        clients = MyDict()
        for rental in self.getAllRentals().values():
            if rental.clientID in clients:
                clients[rental.clientID] += 14
            else:
                clients[rental.clientID] = 14

        finals = []
        for k, days in clients.items():
            finals.append(tuple([k, days]))

        return clients.sort(self.isHigher, finals)
        #return sorted(clients.items(), key = operator.itemgetter(1), reverse = True)

    def getAllRentedMovies(self):
        """
        Creates a list with IDs of all movies
        actively rented by clients
        :return: a list with all IDs of rented movies
        """
        rentalsMap = self.__rentalManager.getEntities().filter(self.isMovieRented)
        movs = []
        for rental in rentalsMap:
            movs.append(rental.movieID)

        #return sorted(movs, reverse = True)
        return self.__rentalManager.getEntities().sort(self.haveMoreMovies, movs)

    @staticmethod
    def haveMoreMovies(c1, c2):
        return c1 > c2

    @staticmethod
    def isMovieRented(rent, finalList):
        return rent.movieID not in finalList and rent.returnedDATE is None

    def getLateRentals(self):
        """
        Creates a list with IDs of all
        late rentals, sorted decreasingly by the
        number of delayed days
        :return: a list of tuples like (x, y) -> x is the rental ID
        and the y is the number of days for the delay of late rental
        """
        lateRents = self.__rentalManager.getEntities().filter(self.isLateRental)
        finalRents = MyDict()
        for rent in lateRents:
            finalRents[rent.ID] = int(Utils.rentalDelay(rent)/60/60/60)

        finals = []
        for k, days in finalRents.items():
            finals.append(tuple([k, days]))

        return finalRents.sort(self.isHigher, finals)

    @staticmethod
    def isLateRental(rental, finalList):
        return Utils.rentalDelay(rental) > 0

    @staticmethod
    def isHigher(v1, v2):
        return v1[1] > v2[1]


    def removeRental(self, id):
        if isinstance(id, tuple):
            id = id[0]
        self.__rentalManager.deleteEntityById(id)

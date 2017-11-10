"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:37
"""
from domain.entities.entity_list import EntityList


class Store:
    """
    This is the main class for the program
    Holds the lists for the clients and movies
    owned by the store
    Contains getters, setters and other base methods
    @moviesList : list of Movie objects
    @clientsList : list of Client objects
    @rentalsList : list of Rental objects
    """
    def __init__(self):
        self.__moviesList = EntityList()
        self.__clientsList = EntityList()
        self.__rentalsList = EntityList()

    def getMoviesList(self):
        return self.__moviesList

    def getClientsList(self):
        return self.__clientsList

    def getRentalsList(self):
        return self.__rentalsList

    lists = {1: getClientsList,
             2: getMoviesList,
             3: getRentalsList}

    def addToList(self, listID, entity):
        self.lists[listID](self).addEntity(entity)

    def removeFromList(self, listID, index):
        self.lists[listID](self).removeEntity(index)

    def updateList(self, listID, entity, index):
        self.lists[listID](self).update(entity, index)
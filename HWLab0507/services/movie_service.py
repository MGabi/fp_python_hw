"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:53
"""
from domain.entities.movie import Movie
from services.utils import *


class MovieService(object):

    def __init__(self, manager):
        self.__movieManager = manager

    def addMovie(self, movie):
        """
        Create a new movie with given attributes
        and save it to the storage
        :param attrs: attributes of the movie
        :return: nothing
        """
        if isinstance(movie, tuple):
            movie = movie[0]
        self.__movieManager.saveEntity(movie)

    def updateMovie(self, movie):
        """
        Updates a certain movie having mID
        Attrs can contain a new ID for the movie
        but it will not be passed forward to data
        manager because the ID isn't supposed to be modified
        :param mID: the ID for the movie which will be updated
        :param attrs: new attributes of the movie
        :return: nothing
        """
        if isinstance(movie, tuple):
            movie = movie[0]
        self.__movieManager.updateEntity(movie.ID, movie)

    def removeMovie(self, id):
        """
        Removes a movie having a certain ID
        :param id: the ID for the movie which will be deleted
        :return: nothing
        """
        if isinstance(id, tuple):
            id = id[0]
        self.__movieManager.deleteEntityById(id)

    def getAllMovies(self):
        """
        Returns all existing movies
        :return: all movies as a list
        """
        return self.__movieManager.getEntities()

    def getMovie(self, id):
        """
        Returns a movie with given ID
        :param id: id for the movie
        :return: a movie with this ID
        """
        return self.__movieManager.getEntityById(id)
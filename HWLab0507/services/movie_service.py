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

    # def addMovie(self, id, title, description, genre):
    #     movie = Movie(id, title, description, genre)
    #     self.__movieManager.saveEntity(movie)

    def addMovie(self, attrs):
        movie = Movie(attrs[Utils.MOVIE_ID], attrs[Utils.MOVIE_TITLE], attrs[Utils.MOVIE_DESCRIPTION], attrs[Utils.MOVIE_GENRE])
        self.__movieManager.saveEntity(movie)

    def updateMovie(self, mID, attrs):
        movie = Movie(mID, attrs[Utils.MOVIE_TITLE], attrs[Utils.MOVIE_DESCRIPTION], attrs[Utils.MOVIE_GENRE])
        self.__movieManager.updateEntity(mID, movie)

    def removeMovie(self, id):
        self.__movieManager.deleteEntityById(id)

    def getAllMovies(self):
        return self.__movieManager.getEntities()
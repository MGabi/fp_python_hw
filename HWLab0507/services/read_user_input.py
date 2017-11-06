"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/6/2017 10:29
"""
from domain.entities.client import Client
from domain.entities.movie import Movie
from domain.validators.input_validation import *

def getNewClientFromConsole():
    """
    Reads a new user from console and returns
    it after validation
    :return: a new Client
    """
    while True:
        clientID = input("Client ID: ")
        clientName = input("Client name: ")
        if validateClient(clientID, clientName):
            return Client(clientID, clientName)

def getNewMovieFromConsole():
    """
    Reads a new movie from console and returns
    it after validation
    :return: a new Movie
    """
    while True:
        movieID = input("Movie ID: ")
        movieTitle = input("Movie title: ")
        movieDescription = input("Movie description: ")
        movieGenre = input("Movie genre: ")
        if validateMovie(movieID, movieTitle, movieDescription, movieGenre):
            return Movie(movieID, movieTitle, movieDescription, movieGenre)

def getIndexFromConsole(listLen, prompt):
    """
    Reads an index from console and will return
    it if the validation succeeds
    :param listLen: the lenght of the list where the index need to fit
    :param prompt: prompt message for reading
    :return: the index
    """
    while True:
        index = input(prompt)
        if validateInRange(index, listLen):
            return int(index)-1

def getUserIndexForRental(clientList):
    """
    Read the userID for which is wanted to make a rental and
    returns the index in client list and the clientID
    :param clientList: list of clients
    :return: index of client in list and clientID
    """
    while True:
        clientID = input("Enter a client ID in order to make a rental: ")
        if validateInt(clientID):
            clientID = int(clientID)
        else:
            continue

        for client in clientList:
            if client.getClientId() == clientID:
                return clientList.index(client), clientID

        clientNotExist()

def getDesiredMovieForRent(movieList):
    """
    Read the desired movieID and returns the specified movie
    for a new rental
    :param movieList: list of movies
    :return: the movie that will be rented
    """
    while True:
        movieID = input("Enter a movieID for renting: ")
        if validateInt(movieID):
            movieID = int(movieID)
        else:
            continue

        for movie in movieList:
            if movie.getAttrs()[KEYWORDS.movie_id] == movieID:
                return movie
        noSuchMovie()
    pass
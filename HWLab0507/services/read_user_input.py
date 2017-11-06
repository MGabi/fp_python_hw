"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/6/2017 10:29
"""
from domain.entities.client import Client
from domain.entities.movie import Movie
from domain.validators.input_validation import *

def getNewClientFromConsole():
    while True:
        clientID = input("Client ID: ")
        clientName = input("Client name: ")
        if validateClient(clientID, clientName):
            return Client(clientID, clientName)

def getNewMovieFromConsole():
    while True:
        movieID = input("Movie ID: ")
        movieTitle = input("Movie title: ")
        movieDescription = input("Movie description: ")
        movieGenre = input("Movie genre: ")
        if validateMovie(movieID, movieTitle, movieDescription, movieGenre):
            return Movie(movieID, movieTitle, movieDescription, movieGenre)

def getIndexFromConsole(listLen, prompt):
    while True:
        index = input(prompt)
        if validateInRange(index, listLen):
            return int(index)-1

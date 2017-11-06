"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:37
"""
class Store:

    def __init__(self):
        self.moviesList = []
        self.clientsList = []
        self.__rentalsList = []

    def getMoviesList(self):
        return self.moviesList

    def addMovie(self, movie):
        self.moviesList.append(movie)

    def removeMovie(self, index):
        self.moviesList.__delitem__(index)

    def getClientsList(self):
        return self.clientsList

    def addClient(self, client):
        self.clientsList.append(client)

    def removeClient(self, index):
        self.clientsList.__delitem__(index)

    def getRemtalsList(self):
        return self.__rentalsList

    def addRental(self, rental):
        self.__rentalsList.append(rental)


    lists = {1: getClientsList,
             2: getMoviesList}
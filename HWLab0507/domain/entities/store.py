"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:37
"""
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
        self.moviesList = []
        self.clientsList = []
        self.rentalsList = []

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


    def getRentalsList(self):
        return self.rentalsList

    def addRental(self, rental):
        self.rentalsList.append(rental)

    lists = {1: getClientsList,
             2: getMoviesList}
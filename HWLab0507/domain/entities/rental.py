"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:18
"""
import domain.entities.keywords as KEYWORDS

class Rental:
    """
    This class holds data for a certain rental from the store
    @__rentalID : INT
    @__movieID : INT
    @__clientID : INT
    @__rentedDate : FLOAT (timestamp)
    @__dueDate : FLOAT (timestamp)
    @__returnedDate : FLOAT (timestamp)
    """
    def __init__(self, rentalID, movieID, clientID, rentedDate, dueDate, returnedDate):
        self.__rentalID = rentalID
        self.__movieID = movieID
        self.__clientID = clientID
        self.__rentedDate = rentedDate
        self.__dueDate = dueDate
        self.__returnedDate = returnedDate

    def getRentalID(self):
        return self.__rentalID

    def setRentalID(self, rentalID):
        self.__rentalID = rentalID


    def getMovieID(self):
        return self.__movieID

    def setMovieID(self, movieID):
        self.__movieID = movieID


    def getClientID(self):
        return self.__clientID

    def setClientID(self, clientID):
        self.__clientID = clientID


    def getRentedDate(self):
        return self.__rentedDate

    def setRentedDate(self, rentedDate):
        self.__rentedDate = rentedDate


    def getDueDate(self):
        return self.__dueDate

    def setDueDate(self, dueDate):
        self.__dueDate = dueDate


    def getReturnedDate(self):
        return self.__returnedDate

    def setReturnedDate(self, returnedDate):
        self.__returnedDate = returnedDate


    def getAttrs(self):
        attrs = {KEYWORDS.rental_id: self.getRentalID(),
                KEYWORDS.movie_id: self.getMovieID(),
                KEYWORDS.client_id: self.getClientID(),
                KEYWORDS.rented_date: self.getRentedDate(),
                KEYWORDS.due_date: self.getDueDate(),
                KEYWORDS.returned_date: self.getReturnedDate()}
        return attrs
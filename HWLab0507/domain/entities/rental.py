"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 12:50
"""
from services.utils import Utils


class Rental(object):
    """
    This class holds data
    for a rental object
    """

    # def __init__(self, rentalID, movieID, clientID, rentedDATE, dueDATE, returnedDATE):
    #     self.__rentalID = rentalID
    #     self.__movieID = movieID
    #     self.__clientID = clientID
    #     self.__rentedDATE = rentedDATE
    #     self.__dueDATE = dueDATE
    #     self.__returnedDATE = returnedDATE

    def __init__(self, *args):
        self.__rentalID = args[0]
        self.__movieID = args[1]
        self.__clientID = args[2]
        self.__rentedDATE = args[3]
        self.__dueDATE = args[4]
        self.__returnedDATE = args[5]


    @property
    def ID(self):
        return self.__rentalID

    @ID.setter
    def ID(self, ID):
        self.__rentalID = ID

    @property
    def movieID(self):
        return self.__movieID

    @movieID.setter
    def movieID(self, movieID):
        self.__movieID = movieID

    @property
    def clientID(self):
        return self.__clientID

    @clientID.setter
    def clientID(self, clientID):
        self.__clientID = clientID

    @property
    def rentedDATE(self):
        return self.__rentedDATE

    @rentedDATE.setter
    def rentedDATE(self, rentedDATE):
        self.__rentedDATE = rentedDATE

    @property
    def dueDATE(self):
        return self.__dueDATE

    @dueDATE.setter
    def dueDATE(self, dueDATE):
        self.__dueDATE = dueDATE

    @property
    def returnedDATE(self):
        return self.__returnedDATE

    @returnedDATE.setter
    def returnedDATE(self, returnedDATE):
        self.__returnedDATE = returnedDATE

    @property
    def attrs(self):
        return {Utils.RENTAL_ID: self.ID, Utils.MOVIE_ID: self.movieID, Utils.CLIENT_ID: self.clientID, Utils.RENTED_DATE: self.rentedDATE, Utils.DUE_DATE: self.dueDATE, Utils.RETURNED_DATE: self.returnedDATE}

    def toTxt(self):
        return str(self.ID) + ";" + str(self.movieID) + ";" + str(self.clientID) + ";" + str(self.rentedDATE) + ";" + str(self.dueDATE) + ";" + str(self.returnedDATE) + "\n"
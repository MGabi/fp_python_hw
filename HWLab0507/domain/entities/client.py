"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 12:48
"""
from services.utils import Utils


class Client(object):
    """
    This class holds data
    for a client object
    """
    def __init__(self, clientID, clientNAME):
        self.__clientID = clientID
        self.__clientNAME = clientNAME

    @property
    def ID(self):
        return self.__clientID

    @ID.setter
    def ID(self, clientID):
        self.__clientID = clientID

    @property
    def clientNAME(self):
        return self.__clientNAME

    @clientNAME.setter
    def clientNAME(self, clientNAME):
        self.__clientNAME = clientNAME

    @property
    def attrs(self):
        return {Utils.CLIENT_ID: self.__clientID, Utils.CLIENT_NAME: self.__clientNAME}
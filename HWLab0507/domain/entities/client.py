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
    def __init__(self, *args):
        self.__clientID = args[0]
        self.__clientNAME = args[1]

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

    def toTxt(self):
        return str(self.ID) + ";" + self.clientNAME + "\n"

    def toJson(self):
        return {"id": self.ID, Utils.CLIENT_NAME: self.clientNAME}

    @staticmethod
    def makeFromJson(dictData):
        return Client(dictData["id"], dictData[Utils.CLIENT_NAME])

    @staticmethod
    def createTableQuery():
        return """CREATE TABLE IF NOT EXISTS clients
                (id INTEGER PRIMARY KEY,
                clientName VARCHAR(50))"""

    def getTuple(self):
        return tuple([self.ID, self.clientNAME])

    def getUpdateQuery(self):
        return "UPDATE clients SET id=?, clientName='{0}' WHERE id=?".format(self.clientNAME)


"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:15
"""
import domain.entities.keywords as KEYWORDS
class Client:
    """
    This class holds data for a certain client from the store
    @__clientID : INT
    @__clientName: String
    """
    def __init__(self, clientID, clientName):
        self.__clientID = clientID
        self.__clientName = clientName

    def getClientId(self):
        return self.__clientID

    def setClientId(self, clientID):
        self.__clientID = clientID


    def getClientName(self):
        return self.__clientName

    def setClientName(self, clientName):
        self.__clientName = clientName

    def getAttrs(self):
        return {KEYWORDS.client_id: self.getClientId(),
                KEYWORDS.client_name: self.getClientName()}
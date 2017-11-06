"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:15
"""
class Client:

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
        attrs = []
        attrs.append(self.getClientId())
        attrs.append(self.getClientName())
        return attrs
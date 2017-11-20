"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:53
"""
from domain.entities.client import Client
from services.utils import *

class ClientService(object):
    """
    Operations on client list
    """
    def __init__(self, manager):
        self.__clientManager = manager

    def addClient(self, attrs):
        """
        Create a new client with given attributes
        and save it to the storage
        :param attrs: attributes of the client
        :return: nothing
        """
        client = Client(attrs[Utils.CLIENT_ID], attrs[Utils.CLIENT_NAME])
        self.__clientManager.saveEntity(client)

    def updateClient(self, cID, attrs):
        """
        Updates a certain client having cID
        Attrs can contain a new ID for the client
        but it will not be passed forward to data
        manager because the ID isn't supposed to be modified
        :param mID: the ID for the client which will be updated
        :param attrs: new attributes of the client
        :return: nothing
        """
        client = Client(cID, attrs[Utils.CLIENT_NAME])
        self.__clientManager.updateEntity(cID, client)

    def removeClient(self, id):
        """
        Removes a client having a certain ID
        :param id: the ID for the client which will be deleted
        :return: nothing
        """
        self.__clientManager.deleteEntityById(id)

    def getAllClients(self):
        """
        Returns all existing clients
        :return: all clients as a list
        """
        return self.__clientManager.getEntities()

    def getClient(self, id):
        """
        Returns a client with given ID
        :param id: id for the client
        :return: a client with this ID
        """
        return self.__clientManager.getEntityById(id)
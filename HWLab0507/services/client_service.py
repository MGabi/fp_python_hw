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

    # def addClient(self, id, name):
    #     client = Client(id, name)
    #     self.__clientManager.saveEntity(client)

    def addClient(self, attrs):
        client = Client(attrs[Utils.CLIENT_ID], attrs[Utils.CLIENT_NAME])
        self.__clientManager.saveEntity(client)

    def updateClient(self, cID, attrs):
        client = Client(cID, attrs[Utils.CLIENT_NAME])
        self.__clientManager.updateEntity(cID, client)

    def removeClient(self, id):
        self.__clientManager.deleteEntityById(id)

    def getAllClients(self):
        return self.__clientManager.getEntities()
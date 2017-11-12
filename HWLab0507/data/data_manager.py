"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:00
"""
import traceback
class DataManagerException(Exception):
    pass

class DataManager(object):

    def __init__(self, entityValidator):
        self.__entityValidator = entityValidator
        self.__entities = {}

    def getEntityById(self, entityID):
        if entityID in self.__entities.keys():
            return self.__entities[entityID]
        else:
            return None

    def saveEntity(self, entity):
        if not self.entityExists(entity.ID):
            self.__entityValidator.validate(entity)
            self.__entities[entity.ID] = entity
        else:
            raise DataManagerException("ID {0} already exists!".format(entity.ID))

    def updateEntity(self, entityID, entity):
        if self.entityExists(entityID):
            self.__entityValidator.validate(entity)
            self.__entities[entityID] = entity
        else:
            raise DataManagerException("ID {0} is not present in the list!".format(entityID))

    def deleteEntityById(self, entityID):
        if self.entityExists(entityID):
            self.__entities.__delitem__(entityID)
        else:
            raise DataManagerException("ID {0} is not present in the list!".format(entityID))

    def entityExists(self, entityID):
        return entityID in self.__entities.keys()

    def getEntities(self):
        return self.__entities
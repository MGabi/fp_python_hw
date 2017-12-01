"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:00
"""
import traceback

class DataManagerException(Exception):
    pass

class DataManager(object):
    """
    This class is the manager of all existing entities
    Proceeds CRUD operations on the existing data
    """
    def __init__(self, entityValidator):
        self.__entityValidator = entityValidator
        self.__entities = {}

    def getEntityById(self, entityID):
        """
        Returns the entity having entityID
        :param entityID: id for searching the entity
        :return: the entity itself or None if there's
                no entity with the given id
        """
        if entityID in self.__entities.keys():
            return self.__entities[entityID]
        else:
            return None

    def saveEntity(self, entity):
        """
        Saves the entity to the storage
        Raise DataManagerSqlException if another entity
        with the same ID exists
        :param entity: entity that need to be stored
        :return: nothing
        """
        if not self.entityExists(entity.ID):
            self.__entityValidator.validate(entity)
            self.__entities[entity.ID] = entity
        else:
            raise DataManagerException("ID {0} already exists!".format(entity.ID))

    def updateEntity(self, entityID, entity):
        """
        Update an entity with id entityID
        Raise DataManagerSqlException if another entity
        with the same ID exists
        Raise DataManagerSqlException if there's
        no entity with given id for update
        :param entityID: id for updating
        :param entity: an object with new attributes
        :return: nothing
        """
        if self.entityExists(entityID):
            self.__entityValidator.validate(entity)
            self.__entities[entityID] = entity
        else:
            raise DataManagerException("ID {0} is not present in the list!".format(entityID))

    def deleteEntityById(self, entityID):
        """
        Deletes the entity with
        id entityID
        Raise DataManagerSqlException if there's
        no entity with given id for deleting
        :param entityID: id for deleting
        :return: nothing
        """
        if self.entityExists(entityID):
            self.__entities.__delitem__(entityID)
        else:
            raise DataManagerException("ID {0} is not present in the list!".format(entityID))

    def entityExists(self, entityID):
        """
        Checks if there's an entity
        with given ID
        :param entityID: id for checking
        :return: True if exists, False if not
        """
        return entityID in self.__entities.keys()

    def getEntities(self):
        """
        Return all entities
        :return: the list of entities
        """
        return self.__entities
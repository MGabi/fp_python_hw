"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/29/2017 16:42
"""
import pickle

class DataManagerPickleException(Exception):
    pass

class DataManagerPickle(object):
    """
        This class is the manager of all existing entities
        Proceeds CRUD operations on the existing data
        """

    def __init__(self, entityValidator, fileName):
        self.__entityValidator = entityValidator
        self.__filename = fileName
        f = open(fileName, "ab")
        f.close()

    def getEntityById(self, entityID):
        """
        Returns the entity having entityID
        :param entityID: id for searching the entity
        :return: the entity itself or None if there's
                no entity with the given id
        """
        entities = self.getEntities()
        if entityID in entities.keys():
            return entities[entityID]
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
            f = open(self.__filename, "ab")
            pickle.dump(entity, f)
            f.close()
        else:
            raise DataManagerPickleException("ID {0} already exists!".format(entity.ID))

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
            entities = self.getEntities()
            entities[entityID] = entity
            self.dumpAll(entities)
        else:
            raise DataManagerPickleException("ID {0} is not present in the list!".format(entityID))

    def dumpAll(self, entities):
        f = open(self.__filename, "wb")
        for el in entities.values():
            pickle.dump(el, f)
        f.close()


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
            entities = self.getEntities()
            entities.__delitem__(entityID)
            self.dumpAll(entities)
        else:
            raise DataManagerPickleException("ID {0} is not present in the list!".format(entityID))

    def entityExists(self, entityID):
        """
        Checks if there's an entity
        with given ID
        :param entityID: id for checking
        :return: True if exists, False if not
        """
        return entityID in self.getEntities().keys()

    def getEntities(self):
        """
        Return all entities
        :return: the dict of entities
        """
        #return self.__entities
        objects = {}
        try:
            f = open(self.__filename, "rb")
            while True:
                try:
                    obj = pickle.load(f)
                    objects[obj.ID] = obj
                except EOFError:
                    break
            f.close()
        except EOFError as eof:
            print("The file {0} is empty!".format(self.__filename))
            raise eof
        except IOError as io:
            print("IO Error:", str(io))
        f.close()
        return objects

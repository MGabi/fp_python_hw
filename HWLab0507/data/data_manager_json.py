"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/3/2017 17:51
"""
import json
import traceback

class DataManagerJsonException(Exception):
    pass

class DataManagerJson(object):
    """
    This class is the manager of all existing entities
    Proceeds CRUD operations on the existing data
    """
    def __init__(self, entityValidator, fileName, node, objClass):
        self.__entityValidator = entityValidator
        self.__fileName = fileName
        self.__node = node
        self.__objClass = objClass
        with open(fileName, "a") as js:
            js.close()

        with open(fileName, "r") as jsonFile:
            try:
                data = json.load(jsonFile)
                if self.__node not in data.keys():
                    data[node] = {}
                    self.writeAll(data)
            except Exception as ex:
                self.writeAll({self.__node: {}})
            jsonFile.close()

    def readAll(self):
        with open(self.__fileName, "r") as jsonFile:
            try:
                return json.load(jsonFile)
            except Exception as ex:
                print(str(ex))
            return {}

    def writeAll(self, data):
        with open(self.__fileName, "w") as out:
            json.dump(data, out)

    def getEntityById(self, entityID):
        """
        Returns the entity having entityID
        :param entityID: id for searching the entity
        :return: the entity itself or None if there's
                no entity with the given id
        """
        l = self.getEntities()
        if entityID in l.keys():
            return l[entityID]
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
            data = self.readAll()
            data[self.__node][str(entity.ID)] = entity.toJson()
            self.writeAll(data)
        else:
            raise DataManagerJsonException("ID {0} already exists!".format(entity.ID))

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
            data = self.readAll()
            data[self.__node][str(entityID)] = entity.toJson()
            self.writeAll(data)
        else:
            raise DataManagerJsonException("ID {0} is not present in the list!".format(entityID))

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
            data = self.readAll()
            data[self.__node].pop(str(entityID))
            self.writeAll(data)
        else:
            raise DataManagerJsonException("ID {0} is not present in the list!".format(entityID))

    def entityExists(self, entityID):
        """
        Checks if there's an entity
        with given ID
        :param entityID: id for checking
        :return: True if exists, False if not
        """
        return str(entityID) in self.readAll()[self.__node].keys()

    def getEntities(self):
        """
        Return all entities
        :return: the list of entities
        """
        data = self.readAll()
        entities = {}
        for el in data[self.__node].values():
            entities[el["id"]] = self.__objClass.makeFromJson(el)
        return entities
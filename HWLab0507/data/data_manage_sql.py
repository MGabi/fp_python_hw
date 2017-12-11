"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/30/2017 16:53
"""
import sqlite3

from domain.entities.my_dict import MyDict
from domain.entities.rental import Rental

"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:00
"""

class DataManagerSqlException(Exception):
    pass

class DataManagerSql(object):
    """
    This class is the manager of all existing entities
    Proceeds CRUD operations on the existing data
    """
    def __init__(self, entityValidator, filename, tablename, entityClass):
        self.__entityValidator = entityValidator
        self.__fileName = filename
        self.__tableName = tablename
        self.__entityClass = entityClass
        try:
            conn = sqlite3.connect(filename)
            cursor = conn.cursor()
            #cursor.execute("DROP TABLE {0}".format(self.__tableName))
            cursor.execute(entityClass.createTableQuery())
            conn.commit()
            conn.close()
        except Exception as ex:
            raise ex

    def getCursor(self):
        conn = sqlite3.connect(self.__fileName)
        cursor = conn.cursor()
        return conn, cursor

    def getEntityById(self, entityID):
        """
        Returns the entity having entityID
        :param entityID: id for searching the entity
        :return: the entity itself or None if there's
                no entity with the given id
        """
        if entityID in self.getEntities().keys():
            return self.getEntities()[entityID]
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
            conn, cursor = self.getCursor()
            cursor.execute("INSERT INTO {0} VALUES {1}".format(self.__tableName, entity.getTuple()))
            conn.commit()
            conn.close()
        else:
            raise DataManagerSqlException("ID {0} already exists!".format(entity.ID))

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
            conn, cursor = self.getCursor()
            query = entity.getUpdateQuery()
            cursor.execute(query, (entityID, entityID,))
            conn.commit()
            conn.close()
        else:
            raise DataManagerSqlException("ID {0} is not present in the list!".format(entityID))

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
            conn, cursor = self.getCursor()
            cursor.execute("DELETE FROM {0} WHERE id=?".format(self.__tableName), (entityID,))
            conn.commit()
            conn.close()
        else:
            raise DataManagerSqlException("ID {0} is not present in the list!".format(entityID))

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
        :return: the list of entities
        """
        entities = MyDict()
        conn, cursor = self.getCursor()
        cursor.execute("SELECT * FROM {0}".format(self.__tableName))
        l = cursor.fetchall()
        conn.close()
        for el in l:
            el = list(el)
            if self.__entityClass == Rental:
                if el[len(el)-1] == "None":
                    el[len(el)-1] = None
            obj = self.__entityClass(*el)
            entities[obj.ID] = obj

        return entities

    def dropTable(self):
        conn, cursor = self.getCursor()
        cursor.execute("DELETE FROM {0}".format(self.__tableName))
        conn.commit()
        conn.close()
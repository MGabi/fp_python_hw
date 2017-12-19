"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/19/2017 12:31
"""
class Repository(object):

    def __init__(self, fileName, classType):
        self.__fileName = fileName
        self.__classType = classType

    def getAll(self):
        """
        Creates a list with all entities from file fileName
        :return: a list with objects of type classType
        """
        objects = []
        with open(self.__fileName, "r") as f:
            try:
                for line in f.readlines():
                    line = line.split("\n")[0]
                    line = line.split(",")
                    objects.append(self.__classType.fromStrToObj(line))
            except EOFError as eof:
                return objects
        return objects

    def saveEntity(self, entity):
        """
        Saves the entity to fileName file
        :param entity: entity to be saved
        :return: nothing
        """
        with open(self.__fileName, "a") as f:
            f.write(str(entity))
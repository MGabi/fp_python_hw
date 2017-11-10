"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/9/2017 17:24
"""
class EntityList(list):

    def __init__(self):
        super().__init__()

    def update(self, entity, poz):
        self[poz] = entity

    def addEntity(self, entity):
        self.append(entity)

    def removeEntity(self, index):
        self.__delitem__(index)

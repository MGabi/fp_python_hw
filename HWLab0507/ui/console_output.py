"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/6/2017 10:23
"""
def printListOfEntities(listEntities):
    print("The list is:")
    for el in listEntities:
        print(*el.getAttrs())
    print("")
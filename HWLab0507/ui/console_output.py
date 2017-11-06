"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/6/2017 10:23
"""
def printListOfEntities(listEntities):
    """
    Prints the list of clients/movies
    :param listEntities: list that need to be printed
    :return: nothing
    """
    print("The list is:")
    for el in listEntities:
        #print(*el.getAttrs().values())
        for k, v in el.getAttrs().items():
            print(k, ":", v)
        print("")
    print("")


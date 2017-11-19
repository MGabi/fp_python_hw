"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/14/2017 12:10
"""
import ui as UI
import operations as OPS
import sys
from random import randint

from tests import test_all


def populateWarehouse(warehouse):
    """
    Adds few items to the warehouse
    :param warehouse:
    :return:
    """
    for i in range(1, 11):
        OPS.addItem(warehouse, "prod" + str(i), i, i)


def startApplication():
    """
    This is the core method for the application
    Calls the desired method (add, remove, list) after receiving
    data from the user throudh UI module
    """
    warehouse = []
    populateWarehouse(warehouse)
    #test_all(warehouse)
    while True:
        UI.printMenu()
        cmd, args = UI.getCmd()
        if cmd == "exit":
            sys.exit()
        #print(args)
        OPS.dict_operations[cmd](warehouse, args)

startApplication()
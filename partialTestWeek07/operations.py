"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/14/2017 12:14
"""
import ui as UI
import validate as VALIDATE

#keywords
#these are keywords for accesing a product's data
KEY_NAME = "product_name"
KEY_QUANTITY = "product_quantity"
KEY_ITEM_PRICE = "product_price"

def getNewItem(name, quantity, price):
    """
    Create a new dictionary with item attributes
    :param name: name of the product
    :param quantity: quantity of the product
    :param price: price of the product
    :return: a dictionary with product attributes
    """
    return {KEY_NAME: name, KEY_QUANTITY: quantity, KEY_ITEM_PRICE: price}


def addItem(warehouse, name, quantity, price):
    """
    Creates and appends a new item to the warehouse
    :param warehouse: the list of the products
    :param name: name of the new product
    :param quantity: quantity of the new product
    :param price: price of the new product
    :return: nothing
    """
    item = getNewItem(name, quantity, price)
    warehouse.append(item)

def addItemFunc(warehouse, *args):
    """
    Handles the add feature
    Verifies the data and then proceed to
    the appending of the new item to the warehouse
    :param warehouse: list of the products
    :param args: arguments received from console
    :return: nothing
    """
    args = args[0]
    if len(args) == 3:
        name = args[0]
        quantity = args[1]
        price = args[2]
        try:
            quantity = int(quantity)
            price = int(price)
        except Exception as ex:
            UI.printError("The quantity/price is not an integer!")
            return

        if VALIDATE.validateNewItemData(name, quantity, price):
            addItem(warehouse, name, quantity, price)
        else:
            UI.printError("The quantity/price is an int but the value is probably negative or 0!")
    else:
        UI.printError("Invalid number of arguments!")


def removeItemFromList(warehouse, key):
    """
    Removes the item at the position `key` from the list
    :param warehouse: the list of items
    :param key: key that needs to be deleted
    :return: nothing
    """
    #del warehouse[key]
    warehouse.__delitem__(key)

def removeItemFunc(warehouse, *args):
    """
    Handles the remove feature
    Validate the data and then proceed to
    deleting the item with the desired name
    from the list
    :param warehouse: list of items
    :param args: arguments received from console
    :return: nothing
    """
    args = args[0]
    if len(args) == 1:
        key = findItemInList(warehouse, args[0])
        if key is not None:
            #print("key", key)
            removeItemFromList(warehouse, key)
        else:
            UI.printError("This product does not exist in the warehouse items!")
    else:
        UI.printError("Invalid number of arguments!")


def getTotalValue(warehouse):
    total = 0
    for el in warehouse:
        total = total + el["product_quantity"] * el["product_price"]
    return total

def listItemsFunc(warehouse, *args):
    """
    Handles the list feature
    Validates the data and then
    proceed to the UI module to print
    the list/total to the user
    :param warehouse: list of items
    :param args: arguments received from console
    :return: nothing
    """
    args = args[0]
    if len(args) == 1:
        if args[0] == "all":
            UI.printAllItems(warehouse)
        elif args[0] == "total":
            total = getTotalValue(warehouse)
            UI.printTotal(total)
        else:
            UI.printError("{0} is not a valid argument for this function".format(args[0]))
    else:
        UI.printError("Invalid number of arguments!")

def findItemInList(warehouse, name):
    """
    Finds an item in list and returns the index
    :param warehouse: list of items
    :param name: name for searching in list
    :return:
    """
    for i in range(0, len(warehouse)):
        if warehouse[i][KEY_NAME] == name:
            return i
    return None

dict_operations = {"add": addItemFunc,
                   "remove": removeItemFunc,
                   "list": listItemsFunc}
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/14/2017 12:12
"""
def printMenu():
    """
    Prints the menu to the console
    :return: nothing
    """
    print("The available commands for managing the warehouse items are:")
    print("add <product_name> <quantity> <item_price>")
    print("remove <product_name>")
    print("list all")
    print("list total\n")

def getCmd():
    """
    Reads a command from console
    :return: command and arguments as a string
    e.g. : "add", ["name", "1", "2"]
    """
    cmdString = input(">>> ")
    args = cmdString.split()
    cmd = args[0]
    cmd = cmd.lstrip()
    return cmd, args[1:]

def printError(message):
    """
    Prints an error message formatted
    :param message: error text
    :return: nothing
    """
    print("\n\033[91m", message, "\033[0m\n")
    return None


def printAllItems(warehouse):
    """
    Prints all the items in the warehouse, detailed
    :param warehouse: list of items
    :return: nothing
    """
    for el in warehouse:
        print("Prod name: ", el["product_name"])
        print("Prod quantity: ", el["product_quantity"])
        print("Prod price: ", el["product_price"], "\n")


def printTotal(total):
    """
    Prints the total value of items from the warehouse
    :param total: total value of items
    :return: nothing
    """
    print("The total value of the items in warehouse is: ", total)
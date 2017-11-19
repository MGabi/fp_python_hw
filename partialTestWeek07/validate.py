"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/14/2017 12:30
"""
def validateNewItemData(name, quantity, price):
    """
    Validates if the data received from console
    is ok for appending a new product to the list
    :param name: name of the product
    :param quantity: quantity of the product
    :param price: price of the product
    :return: True if all conditions are aquired, False if not
    """
    return len(name) > 1 and quantity > 0 and price > 0
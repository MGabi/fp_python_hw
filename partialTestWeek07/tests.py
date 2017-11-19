"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/14/2017 13:10
"""
from operations import *


def test_all(warehouse):
    test_getNewItem()
    test_addItem(warehouse)
    test_addItemFunc(warehouse)
    test_removeItemFromList(warehouse)
    test_removeItemFunc(warehouse)
    test_getTotalValue(warehouse)
    test_findItemInList(warehouse)

def test_getNewItem():
    item = getNewItem("NameX", 5, 9)
    assert item[KEY_NAME] == "NameX" and item[KEY_QUANTITY] == 5 and item[KEY_ITEM_PRICE] == 9, "getNewItem assert error"

def test_addItem(warehouse):
    l = len(warehouse)
    addItem(warehouse, "NameX", 5, 9)
    assert len(warehouse) == l+1 and warehouse[l][KEY_NAME] == "NameX" and warehouse[l][KEY_QUANTITY] == 5 and warehouse[l][KEY_ITEM_PRICE] == 9

def test_addItemFunc(warehouse):
    l = len(warehouse)
    addItemFunc(warehouse, (["1", "2"]))
    assert len(warehouse) == l

    addItemFunc(warehouse, (["NameX", "1", "2"]))
    assert len(warehouse) == l+1

def test_removeItemFromList(warehouse):
    l = len(warehouse)
    removeItemFromList(warehouse, 2)
    assert len(warehouse) == l-1

def test_removeItemFunc(warehouse):
    l = len(warehouse)
    removeItemFunc(warehouse, (["prodsxxc"]))
    assert l == len(warehouse)
    removeItemFunc(warehouse, (["prod1"]))
    assert len(warehouse) == l-1

def test_getTotalValue(warehouse):
    total = 0
    for el in warehouse:
        total = total + el["product_quantity"]*el["product_price"]
    assert getTotalValue(warehouse) == total

def test_findItemInList(warehouse):
    assert findItemInList(warehouse, "asfawgaegea") == None
    p = findItemInList(warehouse, "prod10")
    assert p == 7

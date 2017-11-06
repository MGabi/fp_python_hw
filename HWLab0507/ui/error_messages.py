"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/3/2017 13:46
"""

def printError(message):
    print("\033[31m", message, "\033[0m")

def notIntErrorMsg():
    printError("\nThe current input is not an integer!\n")

def notInRangeErrorMsg():
    printError("\nThe index is out of range!\n")

def clientNotExist():
    printError("\nThere is no client with that clientID!\n")

def clientCannotRent():
    printError("\nThe selected client can't rent any movie!\n")

def noSuchMovie():
    printError("\nThere is no movie with given ID!\n")
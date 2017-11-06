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
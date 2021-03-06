import _operator
import random

from copy import deepcopy

"""
Mathematical operators for filtering a list
"""
operators = {
    "=": _operator.eq,
    "<": _operator.lt,
    ">": _operator.gt
}

ops = ["<", "=", ">"]


def raiseException(exception):
    raise exception

def removeEl(argList, el):
    """
    Remove an unsued element from an argument list
    :param argList: list of arguments
    :param el: unused argument
    :return: nothing
    """
    if el in argList:
        argList.remove(el)
    elif el == "to":
        pass
    else:
        raiseException(TypeError)

def compareWithOperator(scorePair, comparator, value):
    """
    Return boolean value of the expression below:
    averageScore(scorePair) 'comparator' 'value'
    ex: 4.56 < 5
    :param scorePair: pair of 3 scores obtained by a participant
    :param comparator: < or = or >
    :param value: value which needs
    :return: boolean value of the above arithmetic expression
    """
    return operators[comparator](averageScore(scorePair), float(value))

def averageScore(scorePair):
    """
    Return the average real value of the scores obtained by a contestant
    :param scorePair: the pair which consists of 3 scores ( s1, s2, s3 )
    :return: the average of s1, s2, s3
    """
    #return (scorePair[0] + scorePair[1] + scorePair[2]) / 3
    s = 0
    for el in scorePair:
        s += el

    return s / len(scorePair)

def checkRange(score):
    """
    Checks if a score is in the correct range
    :param score: score that needs approval
    :return: nothing, raise and error if something's wrong
    """
    if score not in range(0, 101):
        raise ValueError

def getNewScore(s1, s2, s3):
    """
    Create a new score pair object
    :param s1: score for #1 problem
    :param s2: score for #2 problem
    :param s3: score for #3 problem
    :return: a list of those 3 scores
    """
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    checkRange(s1)
    checkRange(s2)
    checkRange(s3)
    return [s1, s2, s3]

def newRand():
    return random.randint(10, 100)

def resetScore(score):
    """
    Resets the score for a participant to 0
    :param score: score that need to be reseted
    :return: nothing
    """
    score[0] = 0
    score[1] = 0
    score[2] = 0

def checkAllNumeric(positions):
    """
    Checks if all positions are integers
    raise an exception if something's wrong
    :param positions:
    :return: nothing
    """
    for i in range(len(positions)):
        positions[i] = int(positions[i])

def sortList(l, type):
    l.sort(key = lambda x: averageScore(x), reverse = type)

def sortListWithIndex(l, type, pIndex):
    l.sort(key = lambda x: x[pIndex-1], reverse = type)

def checkInList(scoreList, topN):
    if topN not in range(1, len(scoreList) + 1):
        raise TypeError

def checkPIndex(pIndex):

    if pIndex not in range(1, 4):
        raise TypeError

def makeBackup(scoreList, backupList):
    backupList.append(deepcopy(scoreList))

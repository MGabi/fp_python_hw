import _operator
import random

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
    return (scorePair[0] + scorePair[1] + scorePair[2]) / 3


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
    return [s1, s2, s3]

def newRand():
    return random.randint(10, 100)
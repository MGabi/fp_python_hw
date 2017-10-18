import _operator

operators = {
    "=": _operator.eq,
    "<": _operator.lt,
    ">": _operator.gt
}

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
    return (scorePair[0] + scorePair[1] + scorePair[2]) / 3
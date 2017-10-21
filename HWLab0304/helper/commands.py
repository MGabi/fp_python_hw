import helper.utils as UTILS

def addScoreToList(scoreList, s1, s2, s3):
    """
    Add a score pair to list
    :param scoreList: list of scores
    :param score: score pair to be added
    :return: nothing
    """
    try:
        scoreList.append(UTILS.getNewScore(s1, s2, s3))
    except BaseException as be:
        print(be.args)
        print("Scores are invalid")

def insertScoreToList(scoreList, s1, s2, s3, position):
    """
    Insert a score pair at a given position in list
    :param scoreList: list of scores
    :param score: score pair to be added
    :param position: position where it needs to be added
    :return: nothing
    """
    try:
        position = int(position)
        if position < 1:
            raise BaseException
        scoreList.insert(position - 1, UTILS.getNewScore(s1, s2, s3))
    except BaseException as be:
        print("Invalid position or score.")

def removeScore(scoreList, posStart, posEnd = None):
    """
    Remove the score pairs in a given range,
    or at a certain position if posEnd is not specified
    :param scoreList: list of scores
    :param posStart: start position for removing
    :param posEnd: end position for removing
    :return: nothing
    """
    try:
        posStart = int(posStart)
        if posEnd == None:

            if posStart > len(scoreList):
                raise IndexError

            posEnd = posStart

        posEnd = int(posEnd)

        if posStart < 0 or posStart > posEnd:
            raise TypeError

        if posEnd > len(scoreList):
            print("Since the end position is higher than the size of the list\
                  \nthe entire list was deleted")
            del scoreList
            return

        for i in range(posEnd - posStart + 1):
            del scoreList[posStart - 1]

    except TypeError as te:
        print("Invalid position")
    except IndexError as ie:
        print("The index of the score is out of range.\
                        \nCurrently, the list contains only", len(scoreList), "elements.\
                        \nNo changes have been made to the list.")
    except BaseException as be:
        print(be.args)

def replaceScore(scoreList, participant, problemIndex, newScore):
    """
    Replace the score obtained by `participant` at the problem
    `problemIndex`
    :param scoreList: list of scores
    :param participant: the participant whose note needs to be modified
    :param problemIndex: the problem which needs to be modified
    :param newScore: the new score of the problem
    :return: nothing
    """

    if len(problemIndex) != 2:
        raise TypeError

    participant = int(participant)
    problemIndex = int(problemIndex[1])
    newScore = int(newScore)

    if participant not in range(0, len(scoreList)) or problemIndex not in range(0, 4):
        raise IndexError

    scoreList[participant - 1][problemIndex - 1] = newScore

def printList(scoreList, type=None, comparator=None, value=None):
    """
    Prints the list
    :param scoreList: list of scores
    :param type: 0 - normal printing,
                 sorted - sorted decreasing by average,
                 1 - with criteria
    :param comparator:
    :param value:
    :return: nothing
    """
    #normal printing
    if type == None:
        print(*scoreList)

    #sorted in decreasing order and printed
    elif type == "sorted":

        if comparator != None or value != None:
            UTILS.raiseException(KeyError)

        l = scoreList[:]
        l.sort(key = lambda x: (x[0] + x[1] + x[2]) / 3, reverse=True)

        print(*l)
        del l

    #printed with a given criteria
    elif type == 1:
        l = [el for el in scoreList if UTILS.compareWithOperator(el, comparator, value)]
        if len(l) == 0:
            print("There are no scores with given criteria")
            return
        print(l)
        del l

    else:
        UTILS.raiseException(KeyError)

commandsDictionary = {"add" : addScoreToList,
            "insert" : insertScoreToList,
            "remove" : removeScore,
            "replace" : replaceScore,
            "list" : printList}

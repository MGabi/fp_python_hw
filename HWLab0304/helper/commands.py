import os

import helper.utils as UTILS

##TASK 1
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
        if position > len(scoreList - 1):
            print("The score will be inserted at the end of the list\
            \nsince the position is higher than the size of the list.")
    except BaseException as be:
        print("Invalid position or score.")

##TASK 2
def removeScore(scoreList, posStart, posEnd = None):
    """
    Remove the score pairs in a given range,
    or at a certain position if posEnd is not specified
    :param scoreList: list of scores
    :param posStart: start position for removing
    :param posEnd: end position for removing
    :return: nothing
    """
    if validateForRange(scoreList, posStart, posEnd):
        posStart = int(posStart)
        if posEnd == None:
            posEnd = posStart

        posEnd = int(posEnd)

        for i in range(posStart - 1, posEnd):
            UTILS.resetScore(scoreList[i])

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

    if participant not in range(1, len(scoreList)+1) or problemIndex not in range(1, 4):
        raise IndexError
    try:
        UTILS.checkRange(newScore)
        scoreList[participant - 1][problemIndex - 1] = newScore
    except ValueError:
        print("Score is invalid. Try again")

##TASK 3
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
        l.sort(key = lambda x: UTILS.averageScore(x), reverse=True)

        print(*l)
        del l

    #printed with a given criteria
    elif type == 1:
        l = [el for el in scoreList if UTILS.compareWithOperator(el, comparator, value)]
        if len(l) == 0:
            print("There are no scores with given criteria")
            return
        print(*l)
        del l

    else:
        UTILS.raiseException(KeyError)

#TASK 4
def validateForRange(scoreList, posStart, posEnd):
    try:
        posStart = int(posStart)
        if posEnd != None:
            posEnd = int(posEnd)
        else:
            posEnd = posStart
        if posStart < 1 or posStart > posEnd or posEnd > len(scoreList) or posStart > len(scoreList) or posEnd < 1:
            raise IndexError

        return True
    except IndexError as ie:
        print("The index of the score is out of range.\
                        \nCurrently, the list contains only", len(scoreList), "elements.\
                        \nNo changes have been made to the list.")
        return False

    except BaseException as be:
        print(be.__cause__)
        return False

def avgList(scoreList, posStart, posEnd):
    posStart = int(posStart)
    posEnd = int(posEnd)
    if validateForRange(scoreList, posStart, posEnd):

        s = 0
        for i in range(posStart-1, posEnd):
            s += UTILS.averageScore(scoreList[i])
            print(UTILS.averageScore(scoreList[i]))

        s = s / len(scoreList)
        print(s)

def minList(scoreList, posStart, posEnd):
    posStart = int(posStart)
    posEnd = int(posEnd)
    if validateForRange(scoreList, posStart, posEnd):

        minAvgValue = UTILS.averageScore(scoreList[posStart-1])
        for i in range(posStart, posEnd):
            currVal = UTILS.averageScore(scoreList[i])

            if currVal < minAvgValue:
                minAvgValue = currVal

        print(minAvgValue)

commandsDictionary = {"add" : addScoreToList,
            "insert" : insertScoreToList,
            "remove" : removeScore,
            "replace" : replaceScore,
            "list" : printList,
            "avg": avgList,
            "min": minList}

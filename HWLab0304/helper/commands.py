import helper.ui_functions as UI
import helper.utils as UTILS

##TASK 1
def addScoreToList(scoreList, *scores):
    """
    Add a score pair to list
    :param scoreList: list of scores
    :param score: score pair to be added
    :return: nothing
    """
    # try:
    #     scoreList.append(UTILS.getNewScore(s1, s2, s3))
    # except BaseException as be:
    #     UI.invalidScores()

    try:
        if not len(scores) % 3 == 0:
            raise AttributeError
        for i in range(0, len(scores), 3):
            scoreList.append(UTILS.getNewScore(scores[i], scores[i+1], scores[i+2]))

    except AttributeError as ae:
        UI.invalidNumberOrArgs()
    except BaseException as be:
        UI.invalidScores()

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
        if position > len(scoreList) - 1:
            print("The score will be inserted at the end of the list\
            \nsince the position is higher than the size of the list.")
    except BaseException as be:
        print("Invalid position or score.")

##TASK 2

def removeScore(scoreList, *positions):
    """
    Remove the score pairs in a given range,
    or at a certain position if posEnd is not specified
    :param scoreList: list of scores
    :param positions: positions that needs to be reseted
    :return: nothing
    """
    posStart = 0
    posEnd = None
    positions = list(positions)
    try:
        if positions[0] not in UTILS.ops:
            UTILS.checkAllNumeric(positions)
    except ValueError as ve:
        UI.invalidIndex()
        return

    if positions[0] in UTILS.ops:
        if len(positions) == 2:
            score = int(positions[1])
            UTILS.checkRange(score)
            for i in range(len(scoreList)):
                if UTILS.compareWithOperator(scoreList[i], positions[0], score):
                    UTILS.resetScore(scoreList[i])
        else:
            raise KeyError

    elif len(positions) == 1:
        posStart = positions[0]
        posStart = int(posStart)
        if validateForRange(scoreList, posStart, posEnd):
            UTILS.resetScore(scoreList[posStart - 1])

    elif len(positions) == 2:
        posStart = positions[0]
        posEnd = positions[1]
        if validateForRange(scoreList, posStart, posEnd):
            posStart = int(posStart)
            if posEnd == None:
                posEnd = posStart

            posEnd = int(posEnd)

            for i in range(posStart - 1, posEnd):
                UTILS.resetScore(scoreList[i])
    else:
        for s in positions:
            posStart = int(s)
            if validateForRange(scoreList, posStart, posEnd):
                UTILS.resetScore(scoreList[posStart - 1])

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
        UI.invalidScores()

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
        UI.printListOnScreen(scoreList)

    #sorted in decreasing order and printed
    elif type == "sorted":

        if comparator != None or value != None:
            UTILS.raiseException(KeyError)

        l = scoreList[:]
        UTILS.sortList(l, True)
        UI.printListOnScreen(l)
        del l

    #printed with a given criteria
    elif type == 1:
        l = [el for el in scoreList if UTILS.compareWithOperator(el, comparator, value)]
        if len(l) == 0:
            UI.noCriteria()
            return
        UI.printListOnScreen(l)
        del l

    else:
        UTILS.raiseException(KeyError)

#TASK 4
def validateForRange(scoreList, posStart, posEnd):
    """
    Validates the fact that start position and end position
    fits in the scoreList size and if they are properly transmitted
    for a certain operation ( e.g. removing from a given range )
    :param scoreList: score list
    :param posStart: start position
    :param posEnd: end position
    :return: true if the positions fit the above criterias, false if not
    """
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
        UI.indexOutOfRange(scoreList)
        return False

    except BaseException as be:
        print(type(be))
        return False

def avgList(scoreList, posStart, posEnd):
    """
    Calculate the average value of scores from 2 positions in list
    :param scoreList: scores list
    :param posStart: start position
    :param posEnd: end position
    :return: average value of scores
    """
    posStart = int(posStart)
    posEnd = int(posEnd)
    if validateForRange(scoreList, posStart, posEnd):

        s = 0
        for i in range(posStart-1, posEnd):
            s += UTILS.averageScore(scoreList[i])
            #print(UTILS.averageScore(scoreList[i]))

        s = s / posEnd - posStart + 1
        print(s)

def minList(scoreList, posStart, posEnd):
    """
    Calculate the minimum average value of participants scores
    from a given range in scores list
    :param scoreList: scores list
    :param posStart: start position
    :param posEnd: end position
    :return: minimum value from a given range
    """
    posStart = int(posStart)
    posEnd = int(posEnd)
    if validateForRange(scoreList, posStart, posEnd):

        minAvgValue = UTILS.averageScore(scoreList[posStart-1])
        for i in range(posStart, posEnd):
            currVal = UTILS.averageScore(scoreList[i])

            if currVal < minAvgValue:
                minAvgValue = currVal

        print(minAvgValue)

#TASK 5
def topList(scoreList, topN, problem = None):
    topN = int(topN)
    index = 0
    l = scoreList[:]
    UTILS.checkInList(scoreList, topN)
    if problem != None:
        index = int(problem[1])
        UTILS.checkPIndex(index)
        UTILS.sortListWithIndex(l, True, index)
    else:
        UTILS.sortList(l, True)

    UI.printListOnScreen(l, topN)
    del l

#TASK 6
def undoFunc(scoreList, backupList):
    if len(backupList) != 0:
        scoreList[:] = backupList.pop()[:]
    else:
        UI.cantUndo()


"""
A dictionary containing references to
certain functions based on user input
"""
commandsDictionary = {"add" : addScoreToList,
            "insert" : insertScoreToList,
            "remove" : removeScore,
            "replace" : replaceScore,
            "list" : printList,
            "avg": avgList,
            "min": minList,
            "top": topList,
            "undo": undoFunc}
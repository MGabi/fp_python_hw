import helper.utils as UTILS

def addScoreToList(scoreList, score):
    """
    Add a score pair to list
    :param scoreList: list of scores
    :param score: score pair to be added
    :return: nothing
    """
    scoreList.append(score)

def insert(scoreList, score, position):
    """
    Insert a score pair at a given position in list
    :param scoreList: list of scores
    :param score: score pair to be added
    :param position: position where it needs to be added
    :return: nothing
    """
    scoreList.insert(position, score)

def removeScore(scoreList, position):
    """
    Remove a score pair at a given position
    :param scoreList: list of scores
    :param position: position where the score pair needs to be removed
    :return: nothing
    """
    scoreList.remove(position)

def removeScoreInRange(scoreList, posStart, posEnd):
    """
    Remove the score pairs in a given range
    :param scoreList: list of scores
    :param posStart: start position for removing
    :param posEnd: end position for removing
    :return: nothing
    """
    l = scoreList[:posStart - 1]
    l.append(scoreList[posEnd:])
    scoreList.clear()
    scoreList.append(l)
    del l


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
    scoreList[participant - 1][problemIndex - 1] = newScore


def printList(scoreList, type=None, comparator=None, value=None):
    """
    Prints the list
    :param scoreList: list of scores
    :param type: 0 - normal printing, 1 - sorted decreasing by average, 2 - with criteria
    :param comparator:
    :param value:
    :return: nothing
    """
    if type == None:
        print(scoreList)

    elif type == 0:
        l = scoreList
        l.sort(key = lambda x: (x[0] + x[1] + x[2]) / 3, reverse=True)
        print(l)
        del l

    elif type == 1:
        l = [el for el in scoreList if UTILS.compareWithOperator(el, comparator, value)]
        print(l)
        del l

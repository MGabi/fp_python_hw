"""
#################
#               #
#   CONTEST     #
#               #
#################
    During a programming contest for students, each contestant had to solve 3 problems (named P1, P2
and P3). Afterwards, an evaluation committee graded the solution to each of the problems solved by
the contestants using integers between 0 and 10. The committee needs a program that will allow
managing the list of scores and establishing the winners.

@author : Gabi
@email : ytgabi98@gmail.com
"""
import helper.ui_functions as UI
import helper.commands as CMDS
import helper.utils as UTILS

def getNewScore(s1, s2, s3):
    """
    Create a new score pair object
    :param s1: score for #1 problem
    :param s2: score for #2 problem
    :param s3: score for #3 problem
    :return: a list of those 3 scores
    """
    return [s1, s2, s3]

def generateScoreList(scoreList):
    #for i in range(0, 10):
    #    addScoreToList(getNewScore(i+1, i+1, i+1), scoreList)
    CMDS.addScoreToList(getNewScore(1, 5, 10), scoreList)
    CMDS.addScoreToList(getNewScore(2, 1, 1), scoreList)
    CMDS.addScoreToList(getNewScore(10, 9, 7), scoreList)


def parseCommand(cmd):
    pass

def main():
    UI.printAvailableCommands()
    UI.needCommand()
    scoreList = []
    generateScoreList(scoreList)
    CMDS.insert()
    print(scoreList)
    '''
    while True:
        cmd = input(">>> ")
        parseCommand(cmd)
    '''
main()
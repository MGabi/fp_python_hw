
def printAvailableCommands():
    print("")
    print("\033[91m###############################")
    print("\033[91m######  CONTEST MANAGER  ######")
    print("\033[91m###############################\033[0m")
    print("")
    print("Currently available commands for\
    \nmanaging contestants list are:")
    print("")
    print("  \033[32madd\033[0m <P1 score> <P2 score> <P3 score>\
    \n  \033[32minsert\033[0m <P1 score> <P2 score> <P3 score> \033[32mat\033[0m <position>\
    \n  \033[32mremove\033[0m <position>\
    \n  \033[32mremove\033[0m <position1> <position2> <position3> <position4> ...\
    \n  \033[32mremove\033[0m <start position> \033[32mto\033[0m <end position>\
    \n  \033[32mremove\033[0m [ < / = / > ] <score>\
    \n  \033[32mreplace\033[0m <old score> <P1 / P2 / P3> \033[32mwith\033[0m <new score>\
    \n  \033[32mlist\033[0m\
    \n  \033[32mlist sorted\033[0m\
    \n  \033[32mlist\033[0m [ < / = / > ] <score>\
    \n  \033[32mavg\033[0m <start position> \033[32mto\033[0m <end position>\
    \n  \033[32mmin\033[0m <start position> \033[32mto\033[0m <end position>\
    \n  \033[32mtop\033[0m <number>\
    \n  \033[32mtop\033[0m <number> <P1 / P2 / P3>\
    \n  \033[32mundo\033[0m\
    \n\ntype \033[94mexit\033[0m for closing the program.")


def needCommand():
    print("\nYou can start using those commands by typing below:")


def indexOutOfRange(scoreList):
    print("The index of the score is out of range.\
                            \nCurrently, the list contains only", len(scoreList), "elements.\
                            \nNo changes have been made to the list.")

def noCriteria():
    print("There are no scores with given criteria")


def invalidScores():
    print("Score(s) is(are) invalid. Try again")


def noSuchCommand():
    print("There's no such command.")


def invalidIndex():
    print("Invalid index")


def invalidNumberOrArgs():
    print("Invalid number of arguments")

def invalidArgs():
    print("Invalid arguments")

def printListOnScreen(scoreList, firstN = None):
    if firstN == None:
        firstN = len(scoreList)
    for i in range(firstN):
        print("Participant:", i+1, ", scores: ", scoreList[i])


def cantUndo():
    print("You have nothing to undo")
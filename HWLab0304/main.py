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
import helper.utils as UTILS
import helper.commands as CMDS

def parseCommand(line):
    """
    Get the user input as a parameter and will
    separate the command and arguments,
    returning them
    :return: the command and arguments typed by user
    """
    line = line.lstrip(" ")
    pos = line.find(" ")

    if pos == -1:
        return line, []

    cmds = line[ : pos]
    args = line[pos+1 : ].split()

    return cmds, args

def generateScoreList(scoreList):
    """
    Generate a list of random scores
    for some participants
    :param scoreList:
    :return: nothing
    """
    for i in range(3):
       CMDS.addScoreToList(scoreList, UTILS.newRand(), UTILS.newRand(), UTILS.newRand())

def main():
    """
    The main functions.
    Handle the input of the user and
    call required methods based on user input
    :return: nothing
    """
    UI.printAvailableCommands()
    UI.needCommand()
    scoreList = []
    backupList = []
    generateScoreList(scoreList)

    while True:
        currentCommand, currentArgs = parseCommand(input("\033[96m>>> \033[0m"))

        if currentCommand == "exit":
            break

        try:
            currentCommand.lower()
            if currentCommand == "list" and len(currentArgs) > 1:
                if currentArgs[0] in UTILS.ops:
                    currentArgs.insert(0, 1)
                else:
                    raise TypeError

            if currentCommand == "insert":
                UTILS.removeEl(currentArgs, "at")

            if currentCommand == "remove":
                if len(currentArgs) > 1:
                    UTILS.removeEl(currentArgs, "to")

            if currentCommand == "replace":
                UTILS.removeEl(currentArgs, "with")

            if currentCommand in ["avg", "min"]:
                if len(currentArgs) == 3:
                    UTILS.removeEl(currentArgs, "to")

            if currentCommand not in ["list", "undo"]:
                UTILS.makeBackup(scoreList, backupList)

            if currentCommand == "undo":
                CMDS.commandsDictionary[currentCommand](scoreList, backupList)
            else:
                CMDS.commandsDictionary[currentCommand](scoreList, *currentArgs)

        except KeyError as ke:
            UI.noSuchCommand()
        except TypeError as te:
            UI.invalidNumberOrArgs()
        except IndexError as ie:
            UI.invalidIndex()
        except ValueError as ve:
            UI.invalidArgs()

main()
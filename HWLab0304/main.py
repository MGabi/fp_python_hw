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
import helper.commands
import helper.ui_functions as UI
import helper.utils as UTILS
import helper.commands as CMDS

def readCommand():
    line = input("\033[96m>>> \033[0m")
    pos = line.find(" ")

    if pos == -1:
        return line, []

    cmds = line[ : pos]
    args = line[pos+1 : ].split()

    return cmds, args

def generateScoreList(scoreList):
    for i in range(30):
       CMDS.addScoreToList(scoreList, UTILS.newRand(), UTILS.newRand(), UTILS.newRand())

def main():
    UI.printAvailableCommands()
    UI.needCommand()
    scoreList = []
    generateScoreList(scoreList)

    while True:
        currentCommand, currentArgs = readCommand()

        if currentCommand == "exit":
            break

        try:
            if currentCommand == "list" and len(currentArgs) > 1:
                if currentArgs[0] in UTILS.ops:
                    currentArgs.insert(0, 1)
                else:
                    raise TypeError

            if currentCommand == "insert":
                UTILS.removeEl(currentArgs, "at")

            if currentCommand == "remove" and len(currentArgs) > 1:
                UTILS.removeEl(currentArgs, "to")

            if currentCommand == "replace":
                UTILS.removeEl(currentArgs, "with")

            print(currentCommand, " ", currentArgs)
            CMDS.commandsDictionary[currentCommand.lower()](scoreList, *currentArgs)

        except KeyError as ke:
            print("There's no such command.\n")
        except TypeError as te:
            print("Invalid list of argument\n")
        except IndexError as ie:
            print("Invalid index")


main()
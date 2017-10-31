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
import helper.commands as CMDS
import helper.utils as UTILS
import ui.ui_functions as UI


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

def generateScoreList(scoreList, backupList):
    """
    Generate a list of random scores
    for some participants
    :param scoreList:
    :return: nothing
    """
    for i in range(12):
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
    generateScoreList(scoreList, backupList)

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


def test_parse():
    line = "add 1 2 3"
    cmds, args = parseCommand(line)
    assert cmds == "add" and args == ["1", "2", "3"], "Parsing error"

def test_add_score():
    list = [[2, 3, 4]]
    CMDS.addScoreToList(list, 1, 2, 3)
    assert len(list) == 2, "Add score error"

def test_insert_score():
    list = [[1, 2, 3]]
    CMDS.insertScoreToList(list, 4, 5, 6, 1)
    assert len(list) == 2 and list[0] == UTILS.getNewScore(4, 5, 6), "Insert error"

def test_remove_score():
    list = [[2, 5, 4], [8, 9, 11]]
    CMDS.removeScore(list, 1)
    assert list[0] == [0, 0, 0], "Remove error"

def test_replace_score():
    list = [[1, 2, 3], [4, 5, 6]]
    CMDS.replaceScore(list, 2, "P2", 50)
    assert list[1] == [4, 50, 6], "Replace error"

def test_validate_range():
    list = [1, 2, 3, 4]
    posS, posE = 2, 4
    assert CMDS.validateForRange(list, posS, posE), "Range validation error"

def test_undo():
    list = [1, 2, 3]
    bk = [[2, 3, 4], [5, 6, 8]]
    lastBk = [5, 6, 8]
    CMDS.undoFunc(list, bk)
    assert lastBk == list, "Undo error"

def test_remove_el_from_cmd():
    argList = ["1", "to", "2"]
    UTILS.removeEl(argList, "to")
    assert "to" not in argList, "Removing key element error"

def test_comp_operator():
    op = "<"
    scorePair = UTILS.getNewScore(1, 2, 3)
    assert UTILS.compareWithOperator(scorePair, op, 10) == (6 < 10), "Compare with operator error"

def test_get_new_score():
    assert UTILS.getNewScore(1, 2, 3) == [1, 2, 3], "New score error"

def test_reset_score():
    sc = UTILS.getNewScore(1, 2, 3)
    UTILS.resetScore(sc)
    assert sc == [0, 0, 0], "Reset score error"

def test_make_backup():
    scoreList = [1, 2, 3]
    bkList = [[9, 3, 9]]
    UTILS.makeBackup(scoreList, bkList)
    assert len(bkList) == 2 and bkList[1] == scoreList, "Making backup error"

def test_all():
    test_parse()
    test_add_score()
    test_insert_score()
    test_remove_score()
    test_replace_score()
    test_validate_range()
    test_undo()
    test_remove_el_from_cmd()
    test_comp_operator()
    test_get_new_score()
    test_reset_score()
    test_make_backup()

#test_all()
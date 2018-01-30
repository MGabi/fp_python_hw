"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/30/2018 11:34
"""
from controller.sentence_controller import SentenceController
from domain.entities.sentence import Sentence
from ui.ui import UI


class GameController(object):
    """
    The class which controls the entire game
    """

    def __init__(self, fileName):
        self.__fileName = fileName
        self.__sentenceController = SentenceController(self.__fileName)
        self.__cmdDict = {"add" : self.addSentence,
                          "start" : self.startGame,
                          "exit" : self.closeGame,
                          "help" : UI.printMenu}

    @property
    def sentenceController(self):
        """
        Returns the controller for the sentences
        :return: nothing
        """
        return self.__sentenceController

    def runProgram(self):
        """
        This method runs the command-based part of the game
        Receive commands from UI and execute them
        :return: nothing
        Catches any exceptions raised during the execution,
        mostly from UI
        """
        UI.printMenu([])
        while True:
            try:
                cmd, args = UI.getCommand()
                self.__cmdDict[cmd](args)
            except Exception as ex:
                UI.printException(ex)
                #raise ex

    def addSentence(self, words):
        """
        Add a sentence to file through sentence controller
        :param words: words of a sentence
        :return: nothing
        """
        self.sentenceController.addSentence(words)

    def startGame(self, args):
        """
        Starts the game as soon as the `start` command is entered to console
        :param args: not used, just for compatibility with cmdDict
        :return: True if the player wins, false if Not
        """
        sentence = self.sentenceController.getRandomSentence()
        hangman = "hangman"
        indexHangman = 0
        while indexHangman < 7:
            print(sentence.toHangMan() + " -> " + "\033[91m" + hangman[:indexHangman] + "\033[0m")
            char = ""

            try:
                char = UI.getChar()
            except Exception as ex:
                UI.printException(ex)

            if char in sentence.toTxt():
                if char not in sentence.chars:
                    sentence.chars.append(char)
                else:
                    indexHangman += 1
                    UI.printException(Exception("This character was already introduced!"))
            else:
                indexHangman += 1

            if "_" not in sentence.toHangMan():
                UI.printException(Exception("YOU WON!"))
                UI.printMenu([])
                return True

        if indexHangman == 7:
            print("\033[92m" + hangman[:indexHangman].upper() + "\033[0m")
            UI.printException(Exception("You lost!"))
            UI.printMenu([])
            return False



    def closeGame(self, args):
        """
        Close the entire program
        :param args: not used, just for compatibility with cmdDict
        :return: nothing
        """
        exit(0)

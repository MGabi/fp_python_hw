"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/30/2018 12:03
"""
from domain.data_manager import DataManager
from domain.entities.sentence import Sentence


class SentenceController(object):

    def __init__(self, fileName):

        self.__fileName = fileName
        self.__dataManager = DataManager(fileName)

    def addSentence(self, words):
        """
        Proceed to data manager to save the sentence
        :param words: words of a sentence
        :return: nothing
        """
        newSentence = Sentence(words)
        self.__dataManager.saveEntity(newSentence)

    def getRandomSentence(self):
        """
        Requests a random sentence from file via data manager
        :return: a random sentence from file
        """
        return self.__dataManager.getRandomEntity()

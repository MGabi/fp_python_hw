"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/30/2018 12:01
"""
from random import random, randint

from domain.entities.sentence import Sentence


class DataManager(object):

    def __init__(self, fileName):
        self.__fileName = fileName
        with open(fileName, "a") as f:
            pass

    @property
    def fileName(self):
        return self.__fileName

    def saveEntity(self, entity):
        """
        Saves an entity data to the file
        :param entity: entity to be saved
        :return: nothing
        Raises Exception when writing to file fails
        """
        if entity.toTxt() in self.getAllSentences():
            raise Exception("This sentence already exists!")
        try:
            with open(self.fileName, "a") as f:
                sentence = entity.toTxt()
                f.write(sentence + "\n")
        except Exception as ex:
            raise ex

    def getRandomEntity(self):
        """
        This method selects a random entity from the file
        :return: the selected entity as a Sentence object
        Raises Exception if the file if empty
        """
        sentences = self.getAllSentences()
        if sentences == []:
            raise Exception("The file is empty! Try to introduce a few sentences!")
        index = randint(0, len(sentences) - 1)
        sentence = Sentence(sentences[index].split())
        return sentence

    def getAllSentences(self):
        """
        Reads all sentences from the file, creating a list with all sentences separately
        :return: a list with all sentences
        Raises Exception if something went wrong with reading from file
        """
        sentences = []
        try:
            with open(self.fileName, "r") as f:
                try:

                    while True:
                        sentence = f.readline().strip()
                        if sentence == "":
                            raise EOFError()
                        sentences.append(sentence)
                except EOFError as eof:
                    f.close()
                    return sentences

        except Exception as ex:
            raise ex
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/30/2018 12:01
"""
class Sentence(object):

    def __init__(self, words):
        """
        Initialize a sentence and calculate the
        intial chars for every word in the sentence
        :param words: words for the sentence
        """
        self.__words = words
        self.__chars = []

        for word in words:

            if word[0] not in self.__chars:
                self.__chars.append(word[0])
            if word[len(word)-1] not in self.__chars:
                self.__chars.append(word[len(word)-1])

    @property
    def words(self):
        return self.__words

    @property
    def chars(self):
        return self.__chars

    def toHangMan(self):
        """
        This method formats the sentence to hangman style for easy printing
                example: "jhon has apples" will transform to "j__n has a____s"
        :return: the formatted hangman sentence
        """
        hangManStyle = ""
        for word in self.words:
            for char in word:
                if char in self.chars:
                    hangManStyle += char
                else:
                    hangManStyle += "_"
            hangManStyle += " "

        return hangManStyle

    def toTxt(self):
        """
        This method formats the sentence words to a proper style,
        preparing it for writing to a file
                example : ["jhon", "has", "apples"] will transform to "jhon has apples"
        :return: formated sentence
        """
        sentence = ""

        for i in range(len(self.words)):
            if i != len(self.words) - 1:
                sentence = sentence + self.words[i] + " "
            else:
                sentence = sentence + self.words[i]
        return sentence
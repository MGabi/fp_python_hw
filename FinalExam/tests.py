"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/30/2018 13:14
"""
from unittest import TestCase

from controller.game_controller import GameController
from controller.sentence_controller import SentenceController
from domain.entities.sentence import Sentence


class SentenceControllerTest(TestCase):

    def setUp(self):
        self.filename = "test_sentences.txt"
        self.controller = SentenceController(self.filename)
        with open(self.filename, "w") as f:
            pass

    def test_addSentence(self):
        sent_words = ["jhon", "has", "apples"]
        self.controller.addSentence(sent_words)
        with self.assertRaises(Exception):
            self.controller.addSentence(sent_words)
        sentence = self.controller.getRandomSentence()
        self.assertEqual(sent_words, sentence.words, "Adding error")

    def test_getRandomSentence(self):
        sent_words = ["jhon", "has", "apples"]
        sent_words2 = ["andy", "has", "nothing"]
        self.controller.addSentence(sent_words)
        self.controller.addSentence(sent_words2)
        sentence = self.controller.getRandomSentence()
        self.assertIn(sentence.words, [sent_words, sent_words2], "Getting random error")

    def test_empty(self):
        with open(self.filename, "w") as f:
            pass

        with self.assertRaises(Exception):
            self.controller.getRandomSentence()

class GameControllerTest(TestCase):

    def setUp(self):
        self.fileName = "test_sentences.txt"
        self.controller = GameController(self.fileName)

    def test_addSentence(self):
        with open(self.fileName, "w") as f:
            pass

        sent_words = ["jhon", "has", "apples"]
        self.controller.addSentence(sent_words)
        with self.assertRaises(Exception):
            self.controller.addSentence(sent_words)

class SentenceTest(TestCase):

    def test_words(self):
        sentence = Sentence(["jhon", "has", "apples"])
        self.assertEqual(sentence.words, ["jhon", "has", "apples"])

    def test_chars(self):
        sentence = Sentence(["jhon", "has", "apples"])
        self.assertEqual(sentence.chars, ["j", "n", "h", "s", "a"])

    def test_toHangMan(self):
        sentence = Sentence(["jhon", "has", "apples"])
        self.assertEqual(sentence.toHangMan(), "jh_n has a____s ")
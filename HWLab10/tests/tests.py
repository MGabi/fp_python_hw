"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 17:37
"""
from unittest import TestCase

from domain.entities.board import Board
from domain.entities.dot import Dot
from domain.entities.game import Game
from utils.utils import Utils


class TestGameWon(TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        self.game = Game(self.board)

    def test_checkLine(self):

        self.assertFalse(Utils.checkLine(self.board), "Error column checking")

        self.board.makeMove(1, Dot(1))
        self.board.makeMove(2, Dot(1))
        self.board.makeMove(3, Dot(1))
        self.board.makeMove(4, Dot(1))

        self.assertTrue(Utils.checkLine(self.board), "Error line checking")

    def test_checkColumn(self):

        self.assertFalse(Utils.checkColumn(self.board), "Error column checking")

        self.board.makeMove(1, Dot(1))
        self.board.makeMove(1, Dot(1))
        self.board.makeMove(1, Dot(1))
        self.board.makeMove(1, Dot(1))

        self.assertTrue(Utils.checkColumn(self.board), "Error column checking")

    def test_checkDiagonals(self):
        self.assertFalse(Utils.checkDiagonals(self.board), "Error diagonals checking")

        self.board.makeMove(0, Dot(1))
        self.board.makeMove(1, Dot(1))
        self.board.makeMove(1, Dot(1))
        self.board.makeMove(2, Dot(1))
        self.board.makeMove(2, Dot(1))
        self.board.makeMove(2, Dot(1))
        self.board.makeMove(3, Dot(1))
        self.board.makeMove(3, Dot(1))
        self.board.makeMove(3, Dot(1))
        self.board.makeMove(3, Dot(1))
        print(self.board)
        self.assertTrue(Utils.checkDiagonals(self.board), "Error diagonals checking")
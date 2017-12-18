"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 17:57
"""
from copy import deepcopy

from utils.alpha_beta_pruning import AlphaBetaSearch
from utils.min_max import MinMax


class AIComputer(object):

    def __init__(self, board):
        self.__board = board

    def computeMove(self):
        """
        AlphaBeta Pruning algorithm for computing move
        :return: the best move for current position
        """
        alphaBetaSearch = AlphaBetaSearch(deepcopy(self.board))
        return alphaBetaSearch.startAlphaBetaSearch()

    # def computeMove(self):
    #     """
    #     MinMax algorithm for computing move
    #     :return: the best move for current position
    #     """
    #     minMax = MinMax(deepcopy(self.board))
    #     return minMax.startMinMax()

    # def computeMove(self):
    #     """
    #     Random algorithm for computing move
    #     :return: a random move
    #     """
    #     if self.board.isAnyDotAvaiable(3):
    #         return 3
    #     for i in reversed(range(3)):
    #         if self.board.isAnyDotAvaiable(i):
    #             return i
    #         if self.board.isAnyDotAvaiable(self.board.width-i-1):
    #             return self.board.width-i-1
    #     return 3

    @property
    def board(self):
        return self.__board
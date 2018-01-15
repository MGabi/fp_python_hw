"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/18/2017 20:18
"""
from copy import deepcopy

from domain.entities.dot import Dot
from utils.utils import Utils


class AlphaBetaSearch(object):

    def __init__(self, board):
        self.__board = board
        self.__evalTable = [[3, 4, 5, 7, 5, 4, 3],
                            [4, 6, 8, 10, 8, 6, 4],
                            [5, 8, 11, 13, 11, 8, 5],
                            [5, 8, 11, 13, 11, 8, 5],
                            [4, 6, 8, 10, 8, 6, 4],
                            [3, 4, 5, 7, 5, 4, 3]]

    @property
    def evalTable(self):
        return self.__evalTable

    @property
    def board(self):
        return self.__board

    def startAlphaBetaSearch(self):
        depth = 5
        moves = self.board.getAvailableMoves()
        # moves = sorted(moves, key = lambda x : self.evalBoard(deepcopy(self.board).getNextState(x, Dot(2))), reverse=True)
        bestMove = moves[0]
        bestScore = float('-inf')
        beta = float('inf')

        for move in moves:

            clone = deepcopy(self.board).getNextState(move, Dot(2))
            score = self.minValue(clone, depth - 1, bestScore, beta)
            if score > bestScore:
                bestScore = score
                bestMove = move
            print("value:", score)

        return bestMove

    def minValue(self, board, depth, alpha, beta):
        if Utils.isGameFinished(board):
            return float('inf')
        if Utils.isGameDraw(board):
            return self.evalBoard(board)
            # return 0
        if depth == 0:
            return self.evalBoard(board)

        moves = board.getAvailableMoves()
        score = float('inf')

        for move in moves:
            clone = deepcopy(board).getNextState(move, Dot(1))
            score = min(score, self.maxValue(clone, depth - 1, alpha, beta))
            if score <= alpha:
                return score
            beta = min(beta, score)

        return score

    def maxValue(self, board, depth, alpha, beta):
        isLoosing = False
        if Utils.isGameFinished(board):
            isLoosing = True
        if Utils.isGameDraw(board):
            return 0
        if depth == 0:
            return self.evalBoard(board)

        moves = board.getAvailableMoves()
        score = float('-inf')

        for move in moves:
            clone = deepcopy(board).getNextState(move, Dot(2))
            score = max(score, self.minValue(clone, depth - 1, alpha, beta))
            if isLoosing is True:
                if score is float('inf'):
                    return float('inf')
            elif score >= beta:
                return score
            alpha = max(score, alpha)

        if isLoosing is True:
            return float('-inf')

        return score

    def evalBoard(self, board):
        half = 0
        sum = 0
        for i in range(len(board.table)):
            for j in range(len(board.table[i])):
                if board.table[i][j].color == 1:
                    sum -= self.evalTable[i][j]
                elif board.table[i][j].color == 2:
                    sum += self.evalTable[i][j]
        return half + sum

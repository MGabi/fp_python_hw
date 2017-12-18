"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 19:23
"""
from copy import deepcopy, copy

from domain.entities.dot import Dot
from utils.utils import Utils


class MinMax(object):
    global i
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

    def startMinMax(self):
        global i
        i = 0
        depth = 4
        moves = self.board.getAvailableMoves()
        bestMove = moves[0]
        bestScore = float('-inf')

        for move in moves:
            clone = deepcopy(self.board).getNextState(move, Dot(2))
            score = self.minPlay(clone, depth-1)
            if score > bestScore:
                bestMove = move
                bestScore = score
        print("i= ",i)
        return bestMove

    def minPlay(self, board, depth):
        if Utils.isGameFinished(board):
            return float('inf')
        if Utils.isGameDraw(board):
            return 0
        if depth == 0:
            return self.evalBoard(board)

        moves = board.getAvailableMoves()
        bestScore = float('inf')
        for move in moves:
            clone = deepcopy(board).getNextState(move, Dot(1))
            score = self.maxPlay(clone, depth-1)
            if score <= bestScore:
                bestScore = score

        return bestScore

    def maxPlay(self, board, depth):
        if Utils.isGameFinished(board):
            return float('-inf')
        if Utils.isGameDraw(board):
            return 0
        if depth == 0:
            return self.evalBoard(board)

        moves = board.getAvailableMoves()
        bestScore = float('-inf')
        for move in moves:
            clone = deepcopy(board).getNextState(move, Dot(2))
            score = self.minPlay(clone, depth-1)
            if score >= bestScore:
                bestScore = score
        return bestScore

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
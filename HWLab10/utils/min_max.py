"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 19:23
"""
from copy import deepcopy, copy

from domain.entities.dot import Dot
from utils.utils import Utils


class MinMax(object):

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
        moves = self.board.getAvailableMoves()
        bestMove = moves[0]
        bestScore = float('-inf')
        for move in moves:
            #clone = self.board.getNextState(move, Dot(2))
            clone = deepcopy(self.board).getNextState(move, Dot(2))
            clone
            print("#######")
            print("move: " + str(int(move)))
            score = self.minPlay(clone)
            print("next\n")
            #print("move:", move, "score:", score)
            if score > bestScore:
                bestMove = move
                bestScore = score
        #print("bestScore:" + str(bestScore))
        return bestMove

    def minPlay(self, board):
        print(board)
        if Utils.isGameFinished(board):
            return float('inf')
        if Utils.isGameDraw(board):
            return 0

        moves = board.getAvailableMoves()
        bestScore = float('inf')
        for move in moves:
            clone = board.getNextState(move, Dot(1))
            score = self.maxPlay(clone)
            if score <= bestScore:
                bestScore = score

        return bestScore

    def maxPlay(self, board):
        print(board)
        if Utils.isGameFinished(board):
            return self.evalBoard(board)
            #return float('-inf')
        if Utils.isGameDraw(board):
            return 0

        moves = board.getAvailableMoves()
        bestScore = float('-inf')
        for move in moves:
            clone = board.getNextState(move, Dot(2))
            score = self.minPlay(clone)
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
        # print(board)
        #print("sum", sum)
        #print(board)
        return half + sum
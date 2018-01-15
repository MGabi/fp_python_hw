"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/19/2017 17:56
"""
class NegaScout(object):

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

    def startNegaScout(self):
        pass

    def pvs(self, board, depth, alpha, beta, color):
        pass

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
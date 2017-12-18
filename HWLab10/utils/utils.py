"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 15:58
"""
class Utils(object):
    
    @staticmethod
    def checkLine(board):
        for i in range(board.height):
            for j in range(board.width - 3):
                if board.isGroupOk(board.table[i][j],
                                        board.table[i][j + 1],
                                        board.table[i][j + 2],
                                        board.table[i][j + 3]):
                    return True
        return False
    
    @staticmethod
    def checkColumn(board):
        for i in range(board.height-3):
            for j in range(board.width):
                if board.isGroupOk(board.table[i][j],
                             board.table[i+1][j],
                             board.table[i+2][j],
                             board.table[i+3][j]):
                    return True
        return False

    @staticmethod
    def checkDiagonals(board):
        for i in range(board.height):
            for j in range(board.width):
                result = False
                if i+3 < board.height and j+3 < board.width:
                    if board.isGroupOk(board.table[i][j],
                                       board.table[i+1][j+1],
                                       board.table[i+2][j+2],
                                       board.table[i+3][j+3]):
                        result = True
                if i+3 < board.height and j-3 >= 0:
                    if board.isGroupOk(board.table[i][j],
                                       board.table[i+1][j-1],
                                       board.table[i+2][j-2],
                                       board.table[i+3][j-3]):
                        result = True
                    return result
        return False

    @staticmethod
    def isGameFinished(board):
        res = False
        if Utils.checkLine(board):
            res = True
        if Utils.checkColumn(board):
            res = True
        if Utils.checkDiagonals(board):
            res =  True
        return res

    @staticmethod
    def isGameDraw(board):
        res = True
        for line in board.table:
            for dot in line:
                if dot.color == 0:
                    res = False
        return res
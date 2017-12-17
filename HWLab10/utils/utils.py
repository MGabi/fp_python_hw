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
                    if board.table[i][j].color == 1:
                        print("You won!")
                    else:
                        print("Computer won!")
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
                    if board.table[i][j].color == 1:
                        print("You won!")
                    else:
                        print("Computer won!")
                    return True
        return False

    @staticmethod
    def checkDiagonals(board):
        for i in range(3, board.height):
            for j in range(board.width):
                pass

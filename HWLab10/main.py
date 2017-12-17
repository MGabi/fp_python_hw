"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 13:13
"""
from domain.entities.board import Board
from domain.entities.game import Game


def main():
    board = Board(6, 7)
    game = Game(board)
    game.startGame()

main()
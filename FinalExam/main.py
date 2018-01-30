"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/30/2018 10:39
"""
from controller.game_controller import GameController


def main():
    """
    Main function of the program
    From there the game is initialized
    :return: nothing
    """
    gameController = GameController("sentences.txt")
    gameController.runProgram()


main()
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 14:06
"""
class UI(object):

    @staticmethod
    def readPlayerInput(max):
        while True:
            try:
                column = input("\033[93m   >>>\033[0m")
                column = int(column)

                if column < 1 or column > max:
                    raise Exception("Invalid column number")

                return column
            except ValueError as ve:
                print("Invalid arguments!")

            except Exception as ex:
                print(ex)

    @staticmethod
    def chooseUI():
        print("     1. Console")
        print("     2. GUI")
        op = input(" >> ")
        op = int(op)
        if op not in [1, 2]:
            raise Exception("There's no such option")
        return op
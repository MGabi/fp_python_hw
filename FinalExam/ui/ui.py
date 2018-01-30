"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   1/30/2018 11:37
"""
class UI(object):

    @staticmethod
    def printMenu(*args):
        """
        Prints the menu of the application
        """
        print("\033[96mAvailable commands:\033[0m")
        print("\033[91m     add \033[93m<sentence>\033[0m")
        print("\033[91m     start\033[0m")
        print("\033[91m     exit\033[0m")
        print("\033[91m     help\033[0m")


    @staticmethod
    def getCommand():
        """
        Reads a command and it's arguments from console
        :return: a tuple with the command and it's arguments
                    example : ("add", ["sentence", "for", "hangman"])
        Raises Exception when the command does not exist
                or the arguments are bad
                or the words of the sentences have less than 3 characters
        """
        cmd = input("\033[32m>>> \033[0m").lower()

        cmd = cmd.split()

        if cmd[0] not in ["add", "start", "exit", "help"]:
            raise Exception("Command error!")


        if cmd[0] == "add" and cmd[1:] == []:
            raise Exception("Argument error!")

        if cmd[0] == "add":
            for el in cmd[1:]:
                if len(el) < 3:
                    raise Exception("Invalid input. Words need to have at least 3 characters!\n    The bad word is '" + el + "'.")

        return cmd[0], cmd[1:]

    @staticmethod
    def printException(ex):
        """
        Prints an exception with format
        :param ex: exception to be printed
        :return: nothing
        """
        print("\n   \033[91m", ex, "\033[0m\n")

    @staticmethod
    def getChar():
        """
        Reads a character from the console for the hangman game
        :return: the character introduced by the user
        Raises ValueError when user introduces more than 1 characters
                or when the input is not a character
        """
        char = input("\033[32m>>> \033[0m").lower()
        if len(char) != 1:
            raise ValueError("You should insert only a character at a time!")

        if not char.isalpha():
            raise ValueError("Please introduce a character!")

        return char

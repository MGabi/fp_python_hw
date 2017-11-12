"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 14:08
"""
import traceback
from datetime import datetime
from random import randint
from services.utils import *
from ui.console_helper import ConsoleHelper


def dateFromStr(date):
    return datetime.strptime(date, "%d/%m/%Y").timestamp()


class Console(object):

    def __init__(self, clientService, movieService, rentalService):
        self.__clientService = clientService
        self.__movieService = movieService
        self.__rentalService = rentalService
        self.__cmdsDict = {0: self.opExit,
                           1: self.opAdd,
                           2: self.opRemove,
                           3: self.opUpdate,
                           4: self.opList,
                           5: self.opRentMovie,
                           6: self.opReturnMovie,
                           7: self.opSearch,
                           8: self.opStatistics,
                           9: self.opUndo}
        self.__consoleHelper = ConsoleHelper()

    def opExit(self):
        import sys
        sys.exit()

    def opAdd(self):
        self.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(3, 1)
            if l == 1:
                self.__clientService.addClient(self.__consoleHelper.readClient())
            if l == 2:
                self.__movieService.addMovie(self.__consoleHelper.readMovie())
            if l == 3:
                self.__rentalService.addRental(self.__consoleHelper.readRental())
        except Exception as ex:
            self.__consoleHelper.printError(*ex.args)

    def opRemove(self):
        self.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(2, 1)
            if l == 1:
                self.__clientService.removeClient(self.__consoleHelper.readID())
            if l == 2:
                self.__movieService.removeMovie(self.__consoleHelper.readID())
        except Exception as ex:
            self.__consoleHelper.printError(*ex.args)

    def opUpdate(self):
        self.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(2, 1)
            if l == 1:
                self.__clientService.updateClient(self.__consoleHelper.readID(), self.__consoleHelper.readClient())
            if l == 2:
                self.__movieService.updateMovie(self.__consoleHelper.readID(), self.__consoleHelper.readMovie())
        except Exception as ex:
            self.__consoleHelper.printError(*ex.args)

    def opList(self):
        self.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(3, 1)
            if l == 1:
                self.printAllOf("Clients", self.__clientService.getAllClients())
            if l == 2:
                self.printAllOf("Movies", self.__movieService.getAllMovies())
            if l == 3:
                self.printAllOf("Rentals", self.__rentalService.getAllRentals())
        except Exception as ex:
            self.__consoleHelper.printError(*ex.args)

    def opRentMovie(self):
        pass

    def opReturnMovie(self):
        pass

    def opSearch(self):
        pass

    def opStatistics(self):
        pass

    def opUndo(self):
        pass

    def startConsole(self):
        self.addClientsMoviesRentals()
        self.printHeader()
        consoleHelper = self.__consoleHelper
        while True:
            try:
                self.printOptions()
                option = consoleHelper.readCommand(9)
                self.__cmdsDict[option]()
            except Exception as ex:
                consoleHelper.printError(*ex.args)
                #traceback.print_exc()

        #TODO: menu things

    def printAllOf(self, type, elements):
        print(type, ":")
        for c in elements.values():
            print(c.attrs)
        print("")

    def printOptions(self):
        print("Choose one of the following options:")
        print("     \033[93m1\033[0m - \033[96mAdd\033[0m")
        print("     \033[93m2\033[0m - \033[96mRemove\033[0m")
        print("     \033[93m3\033[0m - \033[96mUpdate\033[0m")
        print("     \033[93m4\033[0m - \033[96mList\033[0m")
        print("     \033[93m5\033[0m - \033[96mRent a movie\033[0m")
        print("     \033[93m6\033[0m - \033[96mReturn a movie\033[0m")
        print("     \033[93m7\033[0m - \033[96mSearch users or movies\033[0m")
        print("     \033[93m8\033[0m - \033[96mCreate statistics\033[0m")
        print("     \033[93m9\033[0m - \033[96mUndo the last operation\033[0m")
        print("     \033[93m0\033[0m - \033[96mExit the program\033[0m")

    def printHeader(self):
        print("\033[91m##############################\033[0m")
        print("\033[91m######MOVIE RENTAL STORE######\033[0m")
        print("\033[91m##############################\033[0m")
        print("")
        print("Managing the list of clients and available movies")

    def printChooseList(self):
        print("Select a list:")
        print("     \033[93m1\033[0m - \033[96mClients\033[0m")
        print("     \033[93m2\033[0m - \033[96mMovies\033[0m")
        #print("     \033[93m3\033[0m - \033[96mRentals\033[0m")

    def addClientsMoviesRentals(self):
        for i in range(1, 10):
            self.__clientService.addClient({Utils.CLIENT_ID: i, Utils.CLIENT_NAME: "Name" + str(i)})
            self.__movieService.addMovie({Utils.MOVIE_ID: i, Utils.MOVIE_TITLE: "Title" + str(i), Utils.MOVIE_DESCRIPTION: "Desc" + str(i), Utils.MOVIE_GENRE: "Genre" + str(i)})

        for i in range(0, 6):
            self.__rentalService.addRental({Utils.RENTAL_ID: i, Utils.MOVIE_ID: randint(1, 10), Utils.CLIENT_ID: randint(1, 10), Utils.RENTED_DATE: dateFromStr(str(randint(1, 12)) + "/" + str(randint(1, 12)) + "/" + str(randint(2015, 2017))), Utils.DUE_DATE: datetime.now().timestamp(), Utils.RETURNED_DATE: None})

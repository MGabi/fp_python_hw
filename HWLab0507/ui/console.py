"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 14:08
"""
import traceback
from random import randint

from domain.entities.rental import Rental
from domain.validators.other_validations import *
from services.utils import *
from ui.console_helper import ConsoleHelper

class Console(object):
    """
    The main class which communicate with the user
    """
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
        """
        Close the application when called
        :return: nothing
        """
        import sys
        sys.exit()

    def opAdd(self):
        """
        This function will proceed to the service module for adding a new entity
        to the list after getting the object data from console
        :return: nothing
        """
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
            #self.__consoleHelper.printError(*ex.args)
            raise ex

    def opRemove(self):
        """
        This function will proceed to the service module for removing
        a certain entity with a given ID from the console
        :return: nothing
        """
        self.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(2, 1)
            if l == 1:
                self.__clientService.removeClient(self.__consoleHelper.readID())
            if l == 2:
                self.__movieService.removeMovie(self.__consoleHelper.readID())
        except Exception as ex:
            #self.__consoleHelper.printError(*ex.args)
            raise ex

    def opUpdate(self):
        """
        This function will proceed to the service module for an update on a
        given position for a client/movie after receiving data from console
        :return: nothing
        """
        self.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(2, 1)
            if l == 1:
                self.__clientService.updateClient(self.__consoleHelper.readID(), self.__consoleHelper.readClient())
            if l == 2:
                self.__movieService.updateMovie(self.__consoleHelper.readID(), self.__consoleHelper.readMovie())
        except Exception as ex:
            #self.__consoleHelper.printError(*ex.args)
            raise ex
    def opList(self):
        """
        This method will print the selected list after getting
        the ID from the console
        :return:
        """
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
            #self.__consoleHelper.printError(*ex.args)
            raise ex

    def opRentMovie(self):
        """
        Handle the rent operation
        Receive attributes for a new rental from console
        Performs validations on movie and client side
        Proceed to adding the rental if no exceptions were raised
        :return: nothing
        """
        try:
            rentalAttrs = self.__consoleHelper.readRental()
            ValidateUserRentalStatus.validate(rentalAttrs[Utils.CLIENT_ID], self.__rentalService.getAllRentals(), rentalAttrs[Utils.MOVIE_ID])
            ValidateMovieCanBeRented.validate(rentalAttrs[Utils.MOVIE_ID], self.__movieService.getAllMovies())
            self.__rentalService.addRental(rentalAttrs)
        except Exception as ex:
            #self.__consoleHelper.printError(*ex.args)
            raise ex

    def opReturnMovie(self):
        """
        Handle the return operation
        Receives the return data from console and then
        proceeds to finish the return of the movie
        :return: nothing
        """
        try:
            returnAttrs = self.__consoleHelper.getReturnData()
            rental = self.__rentalService.getRentalWithIDs(returnAttrs[Utils.CLIENT_ID], returnAttrs[Utils.MOVIE_ID])
            if rental is not None:
                if rental.returnedDATE is not None:
                    raise Exception("The rental with id {0} was already finished!".format(rental.ID))
                self.__rentalService.finishRental(rental)
            else:
                raise Exception("The rental with userID {0} and movieID {0} does not exist!".format(returnAttrs[Utils.CLIENT_ID], returnAttrs[Utils.MOVIE_ID]))
        except Exception as ex:
            #traceback.print_exc()
            #self.__consoleHelper.printError(*ex.args)
            raise ex

    def opSearch(self):
        """
        Handle the search operation
        Receives the list ID from console and then proceed to quering
        After getting the queried list, will proceed to printing
        :return: nothing
        """
        self.printChooseList()
        try:
            opList = self.__consoleHelper.readCommand(3, 1)
            query = self.__consoleHelper.readQuery()
            finalList = []
            if opList == 1:
                finalList = Utils.queryList(self.__clientService.getAllClients(), query)
            elif opList == 2:
                finalList = Utils.queryList(self.__movieService.getAllMovies(), query)
            elif opList == 3:
                finalList = Utils.queryList(self.__rentalService.getAllRentals(), query)
            self.printAllOf("Elements found: ", finalList)
            del finalList
        except Exception as ex:
            # self.__consoleHelper.printError(*ex.args)
            raise ex

    def opStatistics(self):
        self.printStatistics()
        try:
            cmd = self.__consoleHelper.readCommand(5, 1)
            l = {}
            if cmd == 1:
                l = self.__rentalService.getMostRentedMovies()
                self.printMostRented(l)
            elif cmd == 2:
                l = self.__rentalService.getMostActiveClients()
                self.printMostActiveClients(l)
            elif cmd == 3:
                self.printAllOf("Rentals", self.__rentalService.getAllRentals())
            elif cmd == 4:
                l = self.__rentalService.getAllRentedMovies()
                self.printAllCurrentRented(l)
            elif cmd == 5:
                l = self.__rentalService.getLateRentals()
                self.printLateRentals(l)
            del l

        except Exception as ex:
            raise ex

    def opUndo(self):
        pass

    def startConsole(self):
        """
        The start point of this class
        Prints the menu, reads every command
        and execute it as needed using a command dictionary
        :return:
        """
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
                traceback.print_exc()

    def printAllOf(self, type, elements):
        """
        Print a list of clients/movies/rentals
        :param type: the header of the printing: e.g. Clients / Movies / Rentals
        :param elements: the dictonary that will be printed
        :return: nothing
        """
        print(type, ":")
        for c in elements.values():
            for k, v in c.attrs.items():
                if k in [Utils.RENTED_DATE, Utils.DUE_DATE, Utils.RETURNED_DATE]:
                    if v is not None:
                        v = Utils.dateFromTimestamp(v)
                print(k, ":", v)
            print("")
        print("")

    def printMostRented(self, l):
        print("\n\033[92mThe most rented movies are: \033[0m")
        for el in l:
            print("     Movie\033[91m", self.__movieService.getMovie(el[0]).movieTITLE, "\033[0mwith\033[91m", el[1], "\033[0mrentings.")
        print("")

    def printMostActiveClients(self, l):
        print("\n\033[92mThe most active clients are: \033[0m")
        for el in l:
            print("     Client\033[91m", self.__clientService.getClient(el[0]).clientNAME, "\033[0mwith\033[91m", el[1], "\033[0mdays on rents.")
        print("")

    def printAllCurrentRented(self, l):
        print("\n\033[92mThe current rented movies are: \033[0m")
        for el in l:
            print("     Movie\033[91m", self.__movieService.getMovie(el).movieTITLE, "\033[0m")
        print("")

    def printLateRentals(self, l):
        print("\n\033[92mThe current late rentals are: \033[0m")
        for el in l:
            print("     Rental\033[91m", el[0], "\033[0mwith\033[91m", el[1], "\033[0m days of delay for returning.")
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

    def printStatistics(self):
        print("     \033[93m1\033[0m - \033[96mMost rented movies\033[0m")
        print("     \033[93m2\033[0m - \033[96mMost active clients\033[0m")
        print("     \033[93m3\033[0m - \033[96mAll rentals\033[0m")
        print("     \033[93m4\033[0m - \033[96mAll movies currently rented\033[0m")
        print("     \033[93m5\033[0m - \033[96mLate rentals\033[0m")

    def addClientsMoviesRentals(self):
        for i in range(1, 10):
            self.__clientService.addClient({Utils.CLIENT_ID: i,
                                            Utils.CLIENT_NAME: "Name" + str(i)})

            self.__movieService.addMovie({Utils.MOVIE_ID: i,
                                          Utils.MOVIE_TITLE: "Title" + str(i),
                                          Utils.MOVIE_DESCRIPTION: "Desc" + str(i),
                                          Utils.MOVIE_GENRE: "Genre" + str(i)})

        for i in range(1, 15):
            rDate = Utils.timestampFromDate(str(randint(1, 12)) + "/" + str(randint(1, 12)) + "/" + str(randint(2015, 2019)))
            self.__rentalService.addRental({Utils.RENTAL_ID: i,
                                            Utils.MOVIE_ID: randint(1, 9),
                                            Utils.CLIENT_ID: randint(1, 9),
                                            Utils.RENTED_DATE: rDate,
                                            Utils.DUE_DATE: rDate + Utils.CST_RENTAL_PERIOD,
                                            Utils.RETURNED_DATE: None})

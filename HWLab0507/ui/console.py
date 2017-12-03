"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 14:08
"""
import traceback
from random import randint
from copy import copy
from domain.entities.client import Client
from domain.entities.movie import Movie
from domain.entities.rental import Rental
from domain.validators.other_validations import *
from services.utils import *
from ui.console_helper import ConsoleHelper


class Console(object):
    """
    The main class which communicate with the user
    """
    def __init__(self, clientService, movieService, rentalService, undoRedoHandler):
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
                           9: self.opUndo,
                           10: self.opRedo}
        self.__consoleHelper = ConsoleHelper()
        self.__undoHandler = undoRedoHandler

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
        self.__consoleHelper.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(3, 1)
            if l == 1:
                client = self.__consoleHelper.readClient()
                self.__clientService.addClient(client)
                self.__undoHandler.registerOperationUndo(self.__clientService.removeClient, client.ID)
                self.__undoHandler.registerOperationRedo(self.__clientService.addClient, client)
            if l == 2:
                movie = self.__consoleHelper.readMovie()
                self.__movieService.addMovie(movie)
                self.__undoHandler.registerOperationUndo(self.__movieService.removeMovie, movie.ID)
                self.__undoHandler.registerOperationRedo(self.__movieService.addMovie, movie)
            if l == 3:
                rental = self.__consoleHelper.readRental()
                self.__rentalService.addRental(rental)
                self.__undoHandler.registerOperationUndo(self.__rentalService.removeRental, rental.ID)
                self.__undoHandler.registerOperationRedo(self.__rentalService.addRental, rental)
        except Exception as ex:
            #self.__consoleHelper.printError(*ex.args)
            raise ex

    def opRemove(self):
        """
        This function will proceed to the service module for removing
        a certain entity with a given ID from the console
        :return: nothing
        """
        self.__consoleHelper.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(2, 1)
            if l == 1:
                id = self.__consoleHelper.readID()
                client = self.__clientService.getClient(id)
                self.__clientService.removeClient(id)
                self.__undoHandler.registerOperationUndo(self.__clientService.addClient, client)
                self.__undoHandler.registerOperationRedo(self.__clientService.removeClient, client.ID)
            if l == 2:
                id = self.__consoleHelper.readID()
                movie = self.__movieService.getMovie(id)
                self.__movieService.removeMovie(id)
                self.__undoHandler.registerOperationUndo(self.__movieService.addMovie, movie)
                self.__undoHandler.registerOperationRedo(self.__movieService.removeMovie, movie.ID)
        except Exception as ex:
            #self.__consoleHelper.printError(*ex.args)
            raise ex

    def opUpdate(self):
        """
        This function will proceed to the service module for an update on a
        given position for a client/movie after receiving data from console
        :return: nothing
        """
        self.__consoleHelper.printChooseList()
        try:
            l = self.__consoleHelper.readCommand(2, 1)
            if l == 1:
                client = self.__consoleHelper.readClient()
                clientCopy = self.__clientService.getClient(client.ID)
                self.__clientService.updateClient(client)
                self.__undoHandler.registerOperationUndo(self.__clientService.updateClient, clientCopy)
                self.__undoHandler.registerOperationRedo(self.__clientService.updateClient, client)
            if l == 2:
                movie = self.__consoleHelper.readMovie()
                movieCopy = self.__movieService.getMovie(movie.ID)
                self.__movieService.updateMovie(movie)
                self.__undoHandler.registerOperationUndo(self.__movieService.updateMovie, movieCopy)
                self.__undoHandler.registerOperationRedo(self.__movieService.updateMovie, movie)
        except Exception as ex:
            #self.__consoleHelper.printError(*ex.args)
            raise ex

    def opList(self):
        """
        This method will print the selected list after getting
        the ID from the console
        :return:
        """
        self.__consoleHelper.printChooseList()
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
            rental = self.__consoleHelper.readRental()
            ValidateUserRentalStatus.validate(rental.clientID, self.__rentalService.getAllRentals(), rental.movieID)
            ValidateMovieCanBeRented.validate(rental.movieID, self.__movieService.getAllMovies())
            self.__rentalService.addRental(rental)
            self.__undoHandler.registerOperationUndo(self.__rentalService.removeRental, rental.ID)
            self.__undoHandler.registerOperationRedo(self.__rentalService.addRental, rental)
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
                rentalCpy = copy(rental)
                rentalCpy.returnedDATE = None
                self.__undoHandler.registerOperationUndo(self.__rentalService.updateRental, rentalCpy)
                self.__undoHandler.registerOperationRedo(self.__rentalService.updateRental, rental)
            else:
                raise Exception("The rental with userID {0} and movieID {1} does not exist!".format(returnAttrs[Utils.CLIENT_ID], returnAttrs[Utils.MOVIE_ID]))

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
        self.__consoleHelper.printChooseList()
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
        self.__consoleHelper.printStatistics()
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
        self.__undoHandler.undo()

    def opRedo(self):
        self.__undoHandler.redo()

    def startConsole(self):
        """
        The start point of this class
        Prints the menu, reads every command
        and execute it as needed using a command dictionary
        :return:
        """
        #self.addClientsMoviesRentals()
        self.__consoleHelper.printHeader()
        consoleHelper = self.__consoleHelper
        while True:
            try:
                self.__consoleHelper.printOptions()
                option = consoleHelper.readCommand(10)
                self.__cmdsDict[option]()
            except Exception as ex:
                #print("\nUP UP UP\n")
                consoleHelper.printError(*ex.args)
                traceback.print_exc()

    def printAllOf(self, headerType, elements):
        """
        Print a list of clients/movies/rentals
        :param headerType: the header of the printing: e.g. Clients / Movies / Rentals
        :param elements: the dictonary that will be printed
        :return: nothing
        """
        print(headerType, ":")
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


    def addClientsMoviesRentals(self):
        for i in range(1, 10):
            self.__clientService.addClient(Client(i, "Name" + str(i)))
            self.__movieService.addMovie(Movie(i, "Title" + str(i), "Desc" + str(i), "Genre" + str(i)))

        for i in range(1, 10):
            rDate = Utils.timestampFromDate(str(randint(1, 12)) + "/" + str(randint(1, 12)) + "/" + str(randint(2015, 2019)))
            self.__rentalService.addRental(Rental(i, randint(1, 9), randint(1, 9), rDate, rDate + Utils.CST_RENTAL_PERIOD, None))
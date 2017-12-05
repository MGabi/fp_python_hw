"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 12:40
"""
import traceback

from data.data_manage_sql import DataManagerSql
from data.data_manager import DataManager
from data.data_manager_json import DataManagerJson
from data.data_manager_pickle import DataManagerPickle
from data.data_manager_text import DataManagerText
from domain.entities.client import Client
from domain.entities.movie import Movie
from domain.entities.rental import Rental
from domain.validators.client_validator import ClientValidator
from domain.validators.movie_validator import MovieValidator
from domain.validators.rental_validator import RentalValidator
from services.client_service import ClientService
from services.movie_service import MovieService
from services.rental_service import RentalService
from services.settings import Settings
from services.undo_redo_handler import UndoHandler
from ui.console import Console


def run_application():
    """
    The main method of the application
    :return: nothing
    """
    try:
        undoRedoHandler = UndoHandler()
        dataManagerType = Settings.getDataManagerType()

        clientManager = None
        movieManager = None
        rentalManager = None

        if dataManagerType == "memory":
            # IN MEMORY
            clientManager = DataManager(ClientValidator)
            movieManager = DataManager(MovieValidator)
            rentalManager = DataManager(RentalValidator)
        elif dataManagerType == "pickle":
            # WITH PICKLE SERIALIZATION
            clientManager = DataManagerPickle(ClientValidator, "clients.pickle")
            movieManager = DataManagerPickle(MovieValidator, "movies.pickle")
            rentalManager = DataManagerPickle(RentalValidator, "rentals.pickle")
        elif dataManagerType == "text":
            # WITH SIMPLE TXT FILES:
            clientManager = DataManagerText(ClientValidator, "clients.text", Client)
            movieManager = DataManagerText(MovieValidator, "movies.text", Movie)
            rentalManager = DataManagerText(RentalValidator, "rentals.text", Rental)
        elif dataManagerType == "sql":
            # WITH SQL
            clientManager = DataManagerSql(ClientValidator, "moviestore", "clients", Client)
            movieManager = DataManagerSql(MovieValidator, "moviestore", "movies", Movie)
            rentalManager = DataManagerSql(RentalValidator, "moviestore", "rentals", Rental)
        elif dataManagerType == "json":
            # WITH JSON
            clientManager = DataManagerJson(ClientValidator, "clientsJSON", "clients", Client)
            movieManager = DataManagerJson(MovieValidator, "moviesJSON", "movies", Movie)
            rentalManager = DataManagerJson(RentalValidator, "rentalsJSON", "rentals", Rental)

        print("clientManager: ", type(clientManager))
        print("movieManager: ", type(movieManager))
        print("rentalManager: ", type(rentalManager))

        clientService = ClientService(clientManager)
        movieService = MovieService(movieManager)
        rentalService = RentalService(rentalManager)

        console = Console(clientService, movieService, rentalService, undoRedoHandler)
        console.startConsole()
    except Exception as ex:
        print("Exception: ", ex)
        traceback.print_exc()

run_application()
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 12:40
"""
import traceback

from data.data_manager import DataManager
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
from services.undo_redo_handler import UndoHandler
from ui.console import Console


def run_application():
    """
    The main method of the application
    :return: nothing
    """
    try:
        undoRedoHandler = UndoHandler()

        # IN MEMORY
        # clientManager = DataManager(ClientValidator)
        # movieManager = DataManager(MovieValidator)
        # rentalManager = DataManager(RentalValidator)

        # WITH PICKLE SERIALIZATION
        clientManager = DataManagerPickle(ClientValidator, "clients.pickle")
        movieManager = DataManagerPickle(MovieValidator, "movies.pickle")
        rentalManager = DataManagerPickle(RentalValidator, "rentals.pickle")

        # WITH SIMPLE TXT FILES
        # clientManager = DataManagerText(ClientValidator, "clients.text", Client)
        # movieManager = DataManagerText(MovieValidator, "movies.text", Movie)
        # rentalManager = DataManagerText(RentalValidator, "rentals.text", Rental)

        clientService = ClientService(clientManager)
        movieService = MovieService(movieManager)
        rentalService = RentalService(rentalManager)

        console = Console(clientService, movieService, rentalService, undoRedoHandler)
        console.startConsole()
    except Exception as ex:
        print("Exception: ", ex)
        traceback.print_exc()

run_application()
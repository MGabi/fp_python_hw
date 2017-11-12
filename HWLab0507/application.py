"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 12:40
"""
import traceback

from data.data_manager import DataManager
from domain.validators.client_validator import ClientValidator
from domain.validators.movie_validator import MovieValidator
from domain.validators.rental_validator import RentalValidator
from services.client_service import ClientService
from services.movie_service import MovieService
from services.rental_service import RentalService
from ui.console import Console


def run_application():
    """
    The main method of the application
    :return: nothing
    """
    try:
        clientManager = DataManager(ClientValidator)
        movieManager = DataManager(MovieValidator)
        rentalManager = DataManager(RentalValidator)

        clientService = ClientService(clientManager)
        movieService = MovieService(movieManager)
        rentalService = RentalService(rentalManager)

        console = Console(clientService, movieService, rentalService)
        console.startConsole()
    except Exception as ex:
        print("Exception: ", ex)
        traceback.print_exc()

run_application()
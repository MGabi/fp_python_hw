"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/7/2017 00:29
"""
from domain.entities.client import Client
from domain.entities.movie import Movie
from domain.entities.rental import Rental
from domain.entities.store import Store
from domain.validators.input_validation import *
from services.option_handler import *
from services.utils import *

def test_all(store):
    test_client()
    test_movie()
    test_rental()
    test_store()
    test_validateClient()
    test_validateMovie()
    test_validateInRange()
    test_verifyDueDate()
    test_validateUserRentalStatus()
    test_validateInt()
    test_optionAdd(store)
    test_optionRemove(store)
    test_optionUpdate(store)
    test_optionRent(store)
    test_optionReturn(store)
    test_readOption()
    test_dateFromStr()
    test_getSecFromDays()


def test_client():
    client = Client(1, "Jhon")
    assert client.getClientId() == 1 and client.getClientName() == "Jhon"

def test_movie():
    movie = Movie(1, "Title", "Description", "Horror")
    assert movie.getMovieID() == 1 and movie.getMovieTitle() == "Title" and movie.getMovieDescription() == "Description" and movie.getMovieGenre() == "Horror"

def test_rental():
    rental = Rental(1, 1, 1, 170000000, 190000000, None)
    assert rental.getRentalID() == 1 and rental.getMovieID() == 1 and rental.getClientID() == 1 and rental.getRentedDate() == 170000000 and rental.getDueDate() == 190000000 and rental.getReturnedDate() == None

def test_store():
    store = Store()
    store.addMovie(Movie(1, "Title", "Desc", "Genre"))
    store.addClient(Client(1, "Name1"))
    store.addClient(Client(2, "Name2"))
    assert len(store.getMoviesList()) == 1 and len(store.getClientsList()) == 2

    store.removeClient(1)
    assert len(store.getClientsList()) == 1

    assert len(store.getRentalsList()) == 0
    store.addRental(Rental(1, 1, 1, 170000000, 190000000, None))
    assert len(store.getRentalsList()) == 1

def test_validateClient():
    assert validateClient(1, "Jhon") == True

def test_validateMovie():
    assert validateMovie(1, "Title", "Desc", "Genre") == True

def test_validateInRange():
    assert validateInRange(5, 9) == True
    assert validateInRange(-2, 1) == False

def test_verifyDueDate():
    tstmp = datetime.now().timestamp()
    assert verifyDueDate(tstmp - 100000) == False
    assert verifyDueDate(tstmp + 100000) == True

def test_validateUserRentalStatus():
    tstmp = datetime.now().timestamp()
    rentalsList = [Rental(1, 2, 3, tstmp - 10000, tstmp + 1209600, None)]
    rentalsList.append(Rental(4, 5, 6, tstmp - 1209600, tstmp - 100000, None))
    assert validateUserRentalStatus(3, rentalsList) == True
    assert validateUserRentalStatus(6, rentalsList) == False

def test_validateInt():
    assert validateInt("5") == True
    assert validateInt("abc") == False

def test_optionAdd(store):
    pass

def test_optionRemove(store):
    pass

def test_optionUpdate(store):
    pass

def test_optionRent(store):
    pass

def test_optionReturn(store):
    pass

def test_readOption():
    pass

def test_dateFromStr():
    assert True == True
    #assert dateFromStr("11/11/2017") == 1510444799

def test_getSecFromDays():
    assert getSecFromDays(14) == 1209600


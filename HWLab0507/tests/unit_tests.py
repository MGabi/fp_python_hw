"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/21/2017 00:47
"""
import pickle
from unittest import TestCase

from data.data_manager import DataManager
from data.data_manager_pickle import DataManagerPickle
from data.data_manager_text import DataManagerText
from domain.entities.client import Client
from domain.entities.movie import Movie
from domain.entities.rental import Rental
from domain.validators.client_validator import ClientValidator
from domain.validators.movie_validator import MovieValidator
from domain.validators.option_validator import OptionValidator
from domain.validators.other_validations import ValidateUserRentalStatus, ValidateMovieCanBeRented
from domain.validators.rental_validator import RentalValidator
from services.client_service import ClientService
from services.movie_service import MovieService
from services.rental_service import RentalService
from services.undo_redo_handler import UndoHandler
from services.utils import *

class TestUtils(TestCase):
    def test_timestampFromDate(self):
        self.assertEqual(Utils.timestampFromDate("12/12/2012"), 1355263200, "Timestamp from date failed")

    def test_dateFromTimestamp(self):
        d = datetime(2012, 12, 12)
        self.assertEqual(Utils.dateFromTimestamp(1355263200), d, "Date from timestamp failed")

    def test_queryList(self):
        c1 = Client(1, "Jhon")
        c2 = Client(2, "Jhonny")
        l = {1: c1, 2: c2}
        with self.assertRaises(Exception):
            Utils.queryList(l, "asdsdasda")
        self.assertEqual(Utils.queryList(l, "Jhonny"), {1: c2})

        r1 = Rental(1, 1, 1, 10000.0, 20000.0, None)
        r2 = Rental(2, 2, 2, 20000.0, 30000.0, None)
        l2 = {1: r1, 2: r2}
        with self.assertRaises(Exception):
            Utils.queryList(l2, "iwafmieafimfae")
        #self.assertEqual(Utils.queryList(l2, "10000"), {1: r1})
        #print(Utils.queryList(l2, "1"))

    def test_rentalDelay(self):
        self.assertGreater(Utils.rentalDelay(Rental(1, 1, 1, 1355263200, 1355263200, None)), 0, "Delay error")
        self.assertLess(Utils.rentalDelay(Rental(1, 1, 1, 1355263200, 1907724000, None)), 0, "Delay error")

    def test_constants(self):
        self.assertEqual(Utils.CST_RENTAL_PERIOD, 1209600)
        self.assertEqual(Utils.CLIENT_ID, "clientID")
        self.assertEqual(Utils.CLIENT_NAME, "clientNAME")
        self.assertEqual(Utils.MOVIE_ID, "movieID")
        self.assertEqual(Utils.MOVIE_TITLE, "movieTITLE")
        self.assertEqual(Utils.MOVIE_DESCRIPTION, "movieDESCRIPTION")
        self.assertEqual(Utils.MOVIE_GENRE, "movieGENRE")
        self.assertEqual(Utils.RENTAL_ID, "rentalID")
        self.assertEqual(Utils.RENTED_DATE, "rentedDATE")
        self.assertEqual(Utils.DUE_DATE, "dueDATE")
        self.assertEqual(Utils.RETURNED_DATE, "returnedDATE")

class TestClientService(TestCase):

    def setUp(self):
        self.dataManager = DataManager(ClientValidator)
        self.clientService = ClientService(self.dataManager)

        for i in range(1, 10):
            self.clientService.addClient(Client(i, "Name" + str(i)))

    def test_addClient(self):
        with self.assertRaises(Exception):
            self.clientService.addClient(Client(1, "Jhon"))

        self.clientService.addClient(tuple([Client(33, "Name")]))
        self.clientService.addClient(Client(55, "Name"))
        c = self.clientService.getClient(55)
        self.assertEqual(c.attrs, {Utils.CLIENT_ID: 55, Utils.CLIENT_NAME: "Name"}, "Error add client")

    def test_updateClient(self):
        with self.assertRaises(Exception):
            self.clientService.updateClient(Client(555, "Jhon"))

        self.clientService.updateClient(tuple([Client(1, "Jhon")]))
        self.clientService.updateClient(Client(1, "Jhon"))
        c = self.clientService.getClient(1)
        self.assertEqual(c.attrs, {Utils.CLIENT_ID: 1, Utils.CLIENT_NAME: "Jhon"})

    def test_removeClient(self):
        l = len(self.clientService.getAllClients())

        with self.assertRaises(Exception):
            self.clientService.removeClient(-2)

        self.clientService.removeClient(tuple([2]))
        self.clientService.removeClient(3)
        self.assertEqual(l-2, len(self.clientService.getAllClients()))

    def test_getAllClients(self):
        i = 1
        for el in self.clientService.getAllClients().values():
            self.assertEqual(el.attrs, {Utils.CLIENT_ID: i, Utils.CLIENT_NAME: "Name" + str(i)})
            i += 1

    def test_getClient(self):
        self.assertEqual(self.clientService.getClient(-3), None)

        c = {Utils.CLIENT_ID: 5, Utils.CLIENT_NAME: "Name5"}
        self.assertEqual(c, self.clientService.getClient(5).attrs)

class TestMovieService(TestCase):

    def setUp(self):
        self.dataManager = DataManager(MovieValidator)
        self.movieService = MovieService(self.dataManager)

        for i in range(1, 10):
            self.movieService.addMovie(Movie(i, "Title" + str(i), "Desc" + str(i), "Genre" + str(i)))

    def test_addMovie(self):
        with self.assertRaises(Exception):
            self.movieService.addMovie(Movie(1, "Title", "Desc", "Genre"))

        self.movieService.addMovie(tuple([Movie(22, "abc", "desc", "blabla")]))
        self.movieService.addMovie(Movie(25, "abc", "desc", "blabla"))
        c = self.movieService.getMovie(2)
        self.assertEqual(c.attrs, {Utils.MOVIE_ID: 2,
                                    Utils.MOVIE_TITLE: "Title2",
                                    Utils.MOVIE_DESCRIPTION: "Desc2",
                                    Utils.MOVIE_GENRE: "Genre2"}, "Error add movie")

    def test_updateMovie(self):
        with self.assertRaises(Exception):
            self.movieService.updateMovie(Movie(5555, "asfaw", "gaegea", "gaeage"))

        self.movieService.updateMovie(Movie(1, "TitleX", "DescX", "GenreX"))
        self.movieService.updateMovie(tuple([Movie(1, "TitleX", "DescX", "GenreX")]))
        c = self.movieService.getMovie(1)
        self.assertEqual(c.attrs, {Utils.MOVIE_ID: 1,
                                    Utils.MOVIE_TITLE: "TitleX",
                                    Utils.MOVIE_DESCRIPTION: "DescX",
                                    Utils.MOVIE_GENRE: "GenreX"})

    def test_removeMovie(self):
        l = len(self.movieService.getAllMovies())

        with self.assertRaises(Exception):
            self.movieService.removeMovie(-2)

        self.movieService.removeMovie(3)
        self.movieService.removeMovie(tuple([2]))
        self.assertEqual(l-2, len(self.movieService.getAllMovies()))

    def test_getAllMovies(self):
        i = 1
        for el in self.movieService.getAllMovies().values():
            self.assertEqual(el.attrs, {Utils.MOVIE_ID: i,
                                    Utils.MOVIE_TITLE: "Title" + str(i),
                                    Utils.MOVIE_DESCRIPTION: "Desc" + str(i),
                                    Utils.MOVIE_GENRE: "Genre" + str(i)})
            i += 1

    def test_getMovie(self):
        self.assertEqual(self.movieService.getMovie(-3), None)

        c = {Utils.MOVIE_ID: 4,
            Utils.MOVIE_TITLE: "Title4",
            Utils.MOVIE_DESCRIPTION: "Desc4",
            Utils.MOVIE_GENRE: "Genre4"}
        self.assertEqual(c, self.movieService.getMovie(4).attrs, c)

class TestRentalService(TestCase):

    def setUp(self):
        self.manager = DataManager(RentalValidator)
        self.rentalService = RentalService(self.manager)
        self.rentalService.addRental(Rental(564, 1, 1, 214, 2144, None))
        for i in range(1, 10):
            self.rentalService.addRental(Rental(i, i, i, 100+i, 200+i, None))

    def test_addRental(self):
        l = len(self.rentalService.getAllRentals())
        self.rentalService.addRental(Rental(11, 2, 2, 200, 300, None))
        #self.rentalService.addRental(tuple([Rental(12, 2, 2, 200, 300, None)]))
        self.assertEqual(l+1, len(self.rentalService.getAllRentals()))

    def test_updateRental(self):
        r = Rental(3, 3, 3, 500, 600, 800)
        self.rentalService.updateRental(r)
        self.rentalService.updateRental(tuple([r]))
        r2 = self.rentalService.getRental(3)
        self.assertEqual(r.ID, r2.ID)
        self.assertEqual(r.clientID, r2.clientID)
        self.assertEqual(r.movieID, r2.movieID)
        self.assertEqual(r.rentedDATE, r2.rentedDATE)
        self.assertEqual(r.dueDATE, r2.dueDATE)
        self.assertEqual(r.returnedDATE, r2.returnedDATE)

    def test_finishRental(self):
        self.rentalService.finishRental(self.rentalService.getRental(5))
        self.assertIsNot(self.rentalService.getRental(5).returnedDATE, None)

    def test_getRentalWithIDs(self):
        r = self.rentalService.getRentalWithIDs(4, 4)
        self.assertEqual(r.ID, 4)
        self.assertEqual(r.clientID, 4)
        self.assertEqual(r.movieID, 4)
        r2 = self.rentalService.getRentalWithIDs(55, 94)
        self.assertIs(r2, None)

    def test_getRental(self):
        r = self.rentalService.getRental(7)
        self.assertEqual(r.ID, 7)

    def test_getAllRentals(self):
        self.assertEqual(len(self.rentalService.getAllRentals()), 10)

    def test_getMostRentedMovies(self):
        l = self.rentalService.getMostRentedMovies()
        self.assertEqual(l[0][0], 1)
        self.assertEqual(l[0][1], 2)

    def test_getMostActiveClients(self):
        l = self.rentalService.getMostActiveClients()
        self.assertEqual(l[0][0], 1)
        self.assertEqual(l[0][1], 28)

    def test_getAllRentedMovies(self):
        l = self.rentalService.getAllRentedMovies()
        self.assertEqual(l, [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_getLateRentals(self):
        l = self.rentalService.getLateRentals()
        self.assertEqual(len(l), 10)

    def test_removeRental(self):
        self.rentalService.removeRental(2)
        self.assertEqual(self.rentalService.getRental(2), None)
        self.rentalService.removeRental(tuple([3]))
        self.assertEqual(self.rentalService.getRental(3), None)

class ValidateTest(object):
    @staticmethod
    def validate(obj):
        if not isinstance(obj.name, str):
            raise Exception("Not a string")

class ObjForTest(object):

    def __init__(self, *args):
        self.__id = args[0]
        self.__name = args[1]

    @property
    def ID(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return str(self.ID) + " " + self.name

    def toTxt(self):
        return str(self.ID) + ";" + self.name + "\n"

class TestDataService(TestCase):

    def setUp(self):
        self.dataManager = DataManager(ValidateTest)

    def test_saveEntity(self):
        o = ObjForTest(1, "Name1")
        self.dataManager.saveEntity(o)

        with self.assertRaises(Exception):
            o = ObjForTest(3, 2321)
            self.dataManager.saveEntity(o)

    def test_getEntityById(self):
        self.dataManager.saveEntity(ObjForTest(1, "name"))

        self.assertEqual(self.dataManager.getEntityById(-2), None)
        self.assertEqual(self.dataManager.getEntityById(1).ID, 1, "ID error")
        self.assertEqual(self.dataManager.getEntityById(1).name, "name", "Name error")

    def test_updateEntity(self):
        self.dataManager.saveEntity(ObjForTest(2, "Jhon"))
        self.dataManager.saveEntity(ObjForTest(3, "Marry"))

        with self.assertRaises(Exception):
            self.dataManager.updateEntity(5, ObjForTest(3, "Asd"))

        self.dataManager.updateEntity(2, ObjForTest(2, "Martin"))
        self.assertEqual(self.dataManager.getEntityById(2).ID, 2, "ID error")
        self.assertEqual(self.dataManager.getEntityById(2).name, "Martin", "Name error")

    def test_deleteEntityById(self):
        self.dataManager.saveEntity(ObjForTest(1, "Jhon"))
        self.dataManager.saveEntity(ObjForTest(2, "Marry"))

        with self.assertRaises(Exception):
            self.dataManager.deleteEntityById(5)

        self.dataManager.deleteEntityById(2)

        c = self.dataManager.getEntityById(2)
        self.assertEqual(c, None, "Failed deleting")

    def test_entityExists(self):
        o = ObjForTest(1, "asd")
        self.dataManager.saveEntity(o)
        self.assertEqual(self.dataManager.entityExists(2), False)
        self.assertEqual(self.dataManager.entityExists(1), True)

    def test_getEntities(self):
        o = ObjForTest(1, "asd")
        o2 = ObjForTest(2, "sadas")
        self.dataManager.saveEntity(o)
        self.dataManager.saveEntity(o2)

        self.assertEqual(len(self.dataManager.getEntities()), 2)

class TestDataManagerPickle(TestCase):

    def setUp(self):
        self.dataManager = DataManagerPickle(ValidateTest, "fileTestPickle")
        f = open("fileTestPickle", "wb")
        f.close()
        self.dataManager.saveEntity(ObjForTest(1, "Name1"))
        self.dataManager.saveEntity(ObjForTest(2, "Name2"))
        self.dataManager.saveEntity(ObjForTest(3, "Name3"))
        self.dataManager.saveEntity(ObjForTest(4, "Name4"))

    def test_saveEntity(self):
        self.dataManager.saveEntity(ObjForTest(5, "Name5"))
        self.assertEqual(self.dataManager.getEntityById(5).name, "Name5")

        with self.assertRaises(Exception):
            self.dataManager.saveEntity(ObjForTest(3, 2321))

    def test_getEntityById(self):
        self.assertEqual(self.dataManager.getEntityById(-2), None)

        e = self.dataManager.getEntityById(2)
        self.assertEqual(e.ID, 2, "ID error")
        self.assertEqual(e.name, "Name2", "Name error")

    def test_updateEntity(self):
        with self.assertRaises(Exception):
            self.dataManager.updateEntity(5, ObjForTest(3, "Asd"))

        self.dataManager.updateEntity(3, ObjForTest(3, "Name333"))
        e = self.dataManager.getEntityById(3)
        self.assertEqual(e.ID, 3, "ID error")
        self.assertEqual(e.name, "Name333", "Name error")

    def test_deleteEntityById(self):
        with self.assertRaises(Exception):
            self.dataManager.deleteEntityById(5)

        self.dataManager.deleteEntityById(4)

        c = self.dataManager.getEntityById(4)
        self.assertEqual(c, None, "Failed deleting")

    def test_entityExists(self):
        self.assertEqual(self.dataManager.entityExists(1), True)
        self.assertEqual(self.dataManager.entityExists(10), False)

    def test_getEntities(self):
        # for obj in self.dataManager.getEntities().values():
        #     print(obj)
        self.assertEqual(len(self.dataManager.getEntities()), 4)

class TestDataManagerTxt(TestCase):

    def setUp(self):
        self.dataManager = DataManagerText(ValidateTest, "fileTestTxt", ObjForTest)
        f = open("fileTestTxt", "w")
        f.close()
        self.dataManager.saveEntity(ObjForTest(1, "Name1"))
        self.dataManager.saveEntity(ObjForTest(2, "Name2"))
        self.dataManager.saveEntity(ObjForTest(3, "Name3"))
        self.dataManager.saveEntity(ObjForTest(4, "Name4"))

    def test_saveEntity(self):
        self.dataManager.saveEntity(ObjForTest(5, "Name5"))
        self.assertEqual(self.dataManager.getEntityById(5).name, "Name5")

        with self.assertRaises(Exception):
            self.dataManager.saveEntity(ObjForTest(3, 2321))

    def test_getEntityById(self):
        self.assertEqual(self.dataManager.getEntityById(-2), None)

        e = self.dataManager.getEntityById(2)
        self.assertEqual(e.ID, 2, "ID error")
        self.assertEqual(e.name, "Name2", "Name error")

    def test_updateEntity(self):
        with self.assertRaises(Exception):
            self.dataManager.updateEntity(5, ObjForTest(3, "Asd"))

        self.dataManager.updateEntity(3, ObjForTest(3, "Name333"))
        e = self.dataManager.getEntityById(3)
        self.assertEqual(e.ID, 3, "ID error")
        self.assertEqual(e.name, "Name333", "Name error")

    def test_deleteEntityById(self):
        with self.assertRaises(Exception):
            self.dataManager.deleteEntityById(5)
        for el in self.dataManager.getEntities().values():
            print(el)
            print(type(el.ID))
            print(type(el.name))
        self.dataManager.deleteEntityById(4)

        c = self.dataManager.getEntityById(4)
        self.assertEqual(c, None, "Failed deleting")

    def test_entityExists(self):
        o = self.dataManager.getEntityById(1)

        self.assertEqual(self.dataManager.entityExists(1), True)
        self.assertEqual(self.dataManager.entityExists(10), False)

    def test_getEntities(self):
        # for obj in self.dataManager.getEntities().values():
        #     print(obj)
        self.assertEqual(len(self.dataManager.getEntities()), 4)


class TestClient(TestCase):

    def test_Client(self):
        c = Client(1, "Name 1")
        self.assertEqual(c.ID, 1, "ID error")
        c.ID = 2
        self.assertEqual(c.ID, 2, "ID setting error")
        self.assertEqual(c.clientNAME, "Name 1", "Name error")
        c.clientNAME = "Name 2"
        self.assertEqual(c.clientNAME, "Name 2", "Name setting error")
        self.assertEqual(c.attrs, {Utils.CLIENT_ID: 2, Utils.CLIENT_NAME: "Name 2"}, "Attrs error")

class TestMovie(TestCase):

    def test_Movie(self):
        m = Movie(1, "Title", "Desc", "Genre")
        self.assertEqual(m.ID, 1, "ID error")
        m.ID = 2
        self.assertEqual(m.ID, 2, "ID setting error")

        self.assertEqual(m.movieTITLE, "Title", "Title error")
        m.movieTITLE = "Title 2"
        self.assertEqual(m.movieTITLE, "Title 2", "Title setting error")

        self.assertEqual(m.movieDESCRIPTION, "Desc", "Description error")
        m.movieDESCRIPTION = "Desc 2"
        self.assertEqual(m.movieDESCRIPTION, "Desc 2", "Description setting error")

        self.assertEqual(m.movieGENRE, "Genre", "Genre error")
        m.movieGENRE = "Genre 2"
        self.assertEqual(m.movieGENRE, "Genre 2", "Genre setting error")

        self.assertEqual(m.attrs, {Utils.MOVIE_ID:2, Utils.MOVIE_TITLE: "Title 2", Utils.MOVIE_DESCRIPTION: "Desc 2", Utils.MOVIE_GENRE: "Genre 2"})

class TestRental(TestCase):

    def test_Rental(self):
        r = Rental(1, 1, 1, 1000, 1400, None)
        self.assertEqual(r.ID, 1, "ID Error")
        r.ID = 2
        self.assertEqual(r.ID, 2, "ID Error")

        self.assertEqual(r.movieID, 1, "MovieID Error")
        r.movieID = 2
        self.assertEqual(r.movieID, 2, "MovieID Error")

        self.assertEqual(r.clientID, 1, "ClientID Error")
        r.clientID = 2
        self.assertEqual(r.clientID, 2, "ClientID Error")

        self.assertEqual(r.rentedDATE, 1000, "Rented date Error")
        r.rentedDATE = 1001
        self.assertEqual(r.rentedDATE, 1001, "Rented date Error")

        self.assertEqual(r.dueDATE, 1400, "Due date Error")
        r.dueDATE = 1401
        self.assertEqual(r.dueDATE, 1401, "Due date Error")

        self.assertEqual(r.returnedDATE, None, "Returned date Error")
        r.returnedDATE = 1201
        self.assertEqual(r.returnedDATE, 1201, "Returned date Error")

        self.assertEqual(r.attrs, {Utils.RENTAL_ID: 2, Utils.MOVIE_ID: 2, Utils.CLIENT_ID: 2, Utils.RENTED_DATE: 1001, Utils.DUE_DATE: 1401, Utils.RETURNED_DATE: 1201}, "Attrs Error")

class TestClientValidator(TestCase):

    def test_validate(self):
        c1 = Client("asd", "abcd")

        with self.assertRaises(Exception):
            ClientValidator.validate(c1)

        c1 = Client(1, "ab")

        with self.assertRaises(Exception):
            ClientValidator.validate(c1)

        c1 = Client(1, "abcd")

        ClientValidator.validate(c1)

class TestMovieValidator(TestCase):

    def test_validate(self):
        m1 = Movie(1, "abc", "abc", "abc")
        m2 = Movie("abc", "abc", "abc", "abc")

        with self.assertRaises(Exception):
            MovieValidator.validate(m2)

        MovieValidator.validate(m1)

class TestOptionValidator(TestCase):

    def test_validate(self):
        with self.assertRaises(Exception):
            OptionValidator.validate("asd", 1, 5)

        with self.assertRaises(Exception):
            OptionValidator.validate(-3, 1, 5)

        OptionValidator.validate(2, 1, 5)

class TestOtherValidation(TestCase):

    def test_ValidateUserRentalStatus(self):
        rentals = {1: Rental(1, 1, 1, 1000, 1400, 1200)}
        cID = 1
        mID = 1

        with self.assertRaises(Exception):
            ValidateUserRentalStatus.validate(cID, rentals, mID)

        rentals = {1: Rental(1, 1, 1, 1511826429, 1521826429, None)}
        with self.assertRaises(Exception):
            ValidateUserRentalStatus.validate(cID, rentals, mID)

        rentals = {1: Rental(1, 1, 1, 1511826429, 1521826429, None)}
        ValidateUserRentalStatus.validate(cID, rentals, 2)

    def test_ValidateMovieCanBeRented(self):
        movies = {1:"abc", 2:"bcd"}

        with self.assertRaises(Exception):
            ValidateMovieCanBeRented.validate(3, movies)
        ValidateMovieCanBeRented.validate(2, movies)

class TestRentalValidator(TestCase):

    def test_validate(self):
        rental = Rental("abc", 1, 1, 1000, 1400, 1200)

        with self.assertRaises(Exception):
            RentalValidator.validate(rental)

        rental = Rental(1, "abc", 1, 1000, 1400, 1200)

        with self.assertRaises(Exception):
            RentalValidator.validate(rental)

        rental = Rental(1, 1, "abc", 1000, 1400, 1200)

        with self.assertRaises(Exception):
            RentalValidator.validate(rental)

        rental = Rental(-2, 1, 1, 1000, 1400, 1200)

        with self.assertRaises(Exception):
            RentalValidator.validate(rental)

        rental = Rental(1, 1, 1, 1000, 1400, 1200)
        RentalValidator.validate(rental)

class ListObj(list):
    def __init__(self):
        super(ListObj, self).__init__()

    def append(self, obj):
        super(ListObj, self).append(obj)

    def remove(self, id):
        print("here")
        super(ListObj, self).remove(id[0])

class TestUndoHandler(TestCase):
    def setUp(self):
        self.handler = UndoHandler()
        self.elements = ListObj()
        self.elements.append(1)
        self.elements.append(2)
        self.elements.append(3)
        self.elements.append(4)
        self.elements.append(5)
        self.elements.append(6)

    def test_registerOperationUndoRedo(self):
        self.elements.append(7)
        self.handler.registerOperationUndo(self.elements.remove, 7)
        self.handler.registerOperationRedo(self.elements.append, 7)
        self.assertEqual(len(self.handler.opListUndo), 1)
        self.assertEqual(len(self.handler.opListRedo), 1)

    def test_attrs(self):
        lu = self.handler.opListUndo
        self.assertEqual(lu, [])
        lr = self.handler.opListRedo
        self.assertEqual(lr, [])
        li = self.handler.listIndex
        self.assertEqual(li, -1)
        self.handler.listIndex = 1
        self.assertEqual(self.handler.listIndex, 1)

    def test_undoRedo(self):
        with self.assertRaises(Exception):
            self.handler.undo()
        with self.assertRaises(Exception):
            self.handler.redo()

        self.elements.append(7)
        self.handler.registerOperationUndo(self.elements.remove, 7)
        self.handler.registerOperationRedo(self.elements.append, 7)

        self.handler.undo()
        self.assertEqual(self.elements, [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.handler.listIndex, -1)
        self.handler.redo()
        self.assertEqual(self.elements, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.handler.listIndex, 0)

        self.handler.listIndex = -1
        self.handler.deleteAfterActions()
        self.assertEqual(len(self.handler.opListUndo), 0)
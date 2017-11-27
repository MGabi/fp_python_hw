"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/21/2017 00:47
"""
from unittest import TestCase

from data.data_manager import DataManager
from domain.entities.client import Client
from domain.entities.movie import Movie
from domain.entities.rental import Rental
from domain.validators.client_validator import ClientValidator
from domain.validators.movie_validator import MovieValidator
from domain.validators.rental_validator import RentalValidator
from services.client_service import ClientService
from services.movie_service import MovieService
from services.rental_service import RentalService
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
        try:
            Utils.queryList(l, "esdsdsds")
            assert False
        except Exception:
            pass

        self.assertEqual(Utils.queryList(l, "Jhonny"), {1: c2})

    def test_rentalDelay(self):
        self.assertGreater(Utils.rentalDelay(Rental(1, 1, 1, 1355263200, 1355263200, None)), 0, "Delay error")
        self.assertLess(Utils.rentalDelay(Rental(1, 1, 1, 1355263200, 1907724000, None)), 0, "Delay error")

class TestClientService(TestCase):

    def setUp(self):
        self.dataManager = DataManager(ClientValidator)
        self.clientService = ClientService(self.dataManager)

        for i in range(1, 10):
            # self.clientService.addClient({Utils.CLIENT_ID: i,
            #                                 Utils.CLIENT_NAME: "Name" + str(i)})
            self.clientService.addClient(Client(i, "Name" + str(i)))
    def test_addClient(self):
        try:
            # self.clientService.addClient({Utils.CLIENT_ID: 1, Utils.CLIENT_NAME: "Jhon"})
            self.clientService.addClient(Client(1, "Jhon"))
            assert False
        except Exception as ex:
            pass

        c = self.clientService.getClient(2)
        self.assertEqual(c.attrs, {Utils.CLIENT_ID: 2, Utils.CLIENT_NAME: "Name2"}, "Error add client")

    def test_updateClient(self):
        # self.clientService.updateClient(1, {Utils.CLIENT_NAME: "Jhon"})
        self.clientService.updateClient(Client(1, "Jhon"))
        c = self.clientService.getClient(1)
        self.assertEqual(c.attrs, {Utils.CLIENT_ID: 1, Utils.CLIENT_NAME: "Jhon"})

    def test_removeClient(self):
        l = len(self.clientService.getAllClients())
        try:
            self.clientService.removeClient(-2)
            assert False
        except Exception:
            pass

        self.clientService.removeClient(3)
        self.assertEqual(l-1, len(self.clientService.getAllClients()))

    def test_getAllClients(self):
        i = 1
        for el in self.clientService.getAllClients().values():
            self.assertEqual(el.attrs, {Utils.CLIENT_ID: i, Utils.CLIENT_NAME: "Name" + str(i)})
            i += 1

    def test_getClient(self):
        try:
            self.clientService.getClient(-3)
            assert False
        except Exception:
            pass

        c = {Utils.CLIENT_ID: 5, Utils.CLIENT_NAME: "Name5"}
        self.assertEqual(c, self.clientService.getClient(5).attrs)

class TestMovieService(TestCase):

    def setUp(self):
        self.dataManager = DataManager(MovieValidator)
        self.movieService = MovieService(self.dataManager)

        for i in range(1, 10):
            # self.movieService.addMovie({Utils.MOVIE_ID: i,
            #                               Utils.MOVIE_TITLE: "Title" + str(i),
            #                               Utils.MOVIE_DESCRIPTION: "Desc" + str(i),
            #                               Utils.MOVIE_GENRE: "Genre" + str(i)})
            self.movieService.addMovie(Movie(i, "Title" + str(i), "Desc" + str(i), "Genre" + str(i)))

    def test_addMovie(self):
        try:
            self.movieService.addMovie(Movie(1, "Title", "Desc", "Genre"))
            assert False
        except Exception as ex:
            pass

        c = self.movieService.getMovie(2)
        self.assertEqual(c.attrs, {Utils.MOVIE_ID: 2,
                                    Utils.MOVIE_TITLE: "Title2",
                                    Utils.MOVIE_DESCRIPTION: "Desc2",
                                    Utils.MOVIE_GENRE: "Genre2"}, "Error add movie")

    def test_updateMovie(self):
        # self.movieService.updateMovie(1, {Utils.MOVIE_TITLE: "TitleX",
        #                                 Utils.MOVIE_DESCRIPTION: "DescX",
        #                                 Utils.MOVIE_GENRE: "GenreX"})
        self.movieService.updateMovie(Movie(1, "TitleX", "DescX", "GenreX"))
        c = self.movieService.getMovie(1)
        self.assertEqual(c.attrs, {Utils.MOVIE_ID: 1,
                                    Utils.MOVIE_TITLE: "TitleX",
                                    Utils.MOVIE_DESCRIPTION: "DescX",
                                    Utils.MOVIE_GENRE: "GenreX"})

    def test_removeMovie(self):
        l = len(self.movieService.getAllMovies())
        try:
            self.movieService.removeMovie(-2)
            assert False
        except Exception:
            pass

        self.movieService.removeMovie(3)
        self.assertEqual(l-1, len(self.movieService.getAllMovies()))

    def test_getAllMovies(self):
        i = 1
        for el in self.movieService.getAllMovies().values():
            self.assertEqual(el.attrs, {Utils.MOVIE_ID: i,
                                    Utils.MOVIE_TITLE: "Title" + str(i),
                                    Utils.MOVIE_DESCRIPTION: "Desc" + str(i),
                                    Utils.MOVIE_GENRE: "Genre" + str(i)})
            i += 1

    def test_getMovie(self):
        try:
            self.movieService.getMovie(-3)
            assert False
        except Exception:
            pass

        c = {Utils.MOVIE_ID: 4,
            Utils.MOVIE_TITLE: "Title4",
            Utils.MOVIE_DESCRIPTION: "Desc4",
            Utils.MOVIE_GENRE: "Genre4"}
        self.assertEqual(c, self.movieService.getMovie(4).attrs, c)

# class TestRentalService(TestCase):
#
#     def setUp(self):
#         self.dataManager = DataManager(RentalValidator)
#         self.rentalService = RentalService(self.dataManager)
#
#         for i in range(1, 12):
#             rDate = Utils.timestampFromDate(str(randint(1, 12)) + "/" + str(randint(1, 12)) + "/" + str(randint(2015, 2019)))
#             #rDate = Utils.timestampFromDate(str(i%12) + "/" + str(i%12) + "/" + str(randint(2017, 2018)))
#
#             self.rentalService.addRental({Utils.RENTAL_ID: i,
#                                             Utils.MOVIE_ID: randint(1, 9),
#                                             Utils.CLIENT_ID: randint(1, 9),
#                                             Utils.RENTED_DATE: rDate,
#                                             Utils.DUE_DATE: rDate + Utils.CST_RENTAL_PERIOD,
#                                             Utils.RETURNED_DATE: None})
#
#     def test_addRental(self):
#         try:
#             self.rentalService.addRental({Utils.RENTAL_ID: 1,
#                                           Utils.MOVIE_ID: 1,
#                                           Utils.CLIENT_ID: 1,
#                                           Utils.RENTED_DATE: 12345315531,
#                                           Utils.DUE_DATE: 13231321321,
#                                           Utils.RETURNED_DATE: None})
#             assert False
#         except Exception as ex:
#             pass
#
#         c = self.rentalService.getRental(2)
#         self.assertEqual(c.attrs, {Utils.MOVIE_ID: 2,
#                                     Utils.MOVIE_TITLE: "Title2",
#                                     Utils.MOVIE_DESCRIPTION: "Desc2",
#                                     Utils.MOVIE_GENRE: "Genre2"}, "Error add movie")

class ValidateTest(object):
    @staticmethod
    def validate(obj):
        if not isinstance(obj.name, str):
            raise Exception("Not a string")

class ObjForTest(object):
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

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

class TestDataService(TestCase):

    def setUp(self):
        self.dataManager = DataManager(ValidateTest)

    def test_saveEntity(self):
        o = ObjForTest(1, "Name1")
        self.dataManager.saveEntity(o)

        try:
            o = ObjForTest(2, "NameX")
            self.dataManager.saveEntity(o)
            assert False, "Failed duplicate id validation"
        except Exception:
            pass

        try:
            o = ObjForTest(3, 2321)
            self.dataManager.saveEntity(o)
            assert False, "Failed name validation"
        except Exception:
            pass

    def test_getEntityById(self):
        self.dataManager.saveEntity(ObjForTest(1, "name"))

        self.assertEqual(self.dataManager.getEntityById(1).ID, 1, "ID error")
        self.assertEqual(self.dataManager.getEntityById(1).name, "name", "Name error")

    def test_updateEntity(self):
        self.dataManager.saveEntity(ObjForTest(2, "Jhon"))
        self.dataManager.saveEntity(ObjForTest(3, "Marry"))

        try:
            self.dataManager.updateEntity(5, ObjForTest(3, "Asd"))
            assert False, "Failed duplicate id validation before udpating"
        except Exception:
            pass

        self.dataManager.updateEntity(2, ObjForTest(2, "Martin"))
        self.assertEqual(self.dataManager.getEntityById(2).ID, 2, "ID error")
        self.assertEqual(self.dataManager.getEntityById(2).name, "Martin", "Name error")

    def test_deleteEntityById(self):
        self.dataManager.saveEntity(ObjForTest(1, "Jhon"))
        self.dataManager.saveEntity(ObjForTest(2, "Marry"))

        try:
            self.dataManager.deleteEntityById(5)
            assert False, "Failed checking unexisting ID"
        except Exception:
            pass

        self.dataManager.deleteEntityById(2)

        c = self.dataManager.getEntityById(2)
        self.assertEqual(c, None, "Failed deleting")

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
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 12:43
"""
from services.utils import Utils


class Movie(object):
    """
    This class holds data
    for a movie object
    """
    def __init__(self, *args):
        self.__movieID = args[0]
        self.__movieTITLE = args[1]
        self.__movieDESCRIPTION = args[2]
        self.__movieGENRE = args[3]


    @property
    def ID(self):
        return self.__movieID

    @ID.setter
    def ID(self, ID):
        self.__movieID = ID

    @property
    def movieTITLE(self):
        return self.__movieTITLE

    @movieTITLE.setter
    def movieTITLE(self, movieTITLE):
        self.__movieTITLE = movieTITLE

    @property
    def movieDESCRIPTION(self):
        return self.__movieDESCRIPTION

    @movieDESCRIPTION.setter
    def movieDESCRIPTION(self, movieDESCRIPTION):
        self.__movieDESCRIPTION = movieDESCRIPTION

    @property
    def movieGENRE(self):
        return self.__movieGENRE

    @movieGENRE.setter
    def movieGENRE(self, movieGENRE):
        self.__movieGENRE = movieGENRE

    @property
    def attrs(self):
        return {Utils.MOVIE_ID: self.ID, Utils.MOVIE_TITLE: self.movieTITLE, Utils.MOVIE_DESCRIPTION: self.movieDESCRIPTION, Utils.MOVIE_GENRE: self.movieGENRE}

    def toTxt(self):
        return str(self.ID) + ";" + self.movieTITLE + ";" + self.movieDESCRIPTION + ";" + self.movieGENRE + "\n"

    def toJson(self):
        return {"id": self.ID, Utils.MOVIE_TITLE: self.movieTITLE, Utils.MOVIE_DESCRIPTION: self.movieDESCRIPTION, Utils.MOVIE_GENRE: self.movieGENRE}

    @staticmethod
    def makeFromJson(dictData):
        return Movie(dictData["id"], dictData[Utils.MOVIE_TITLE], dictData[Utils.MOVIE_DESCRIPTION], dictData[Utils.MOVIE_DESCRIPTION], dictData[Utils.MOVIE_GENRE])

    @staticmethod
    def createTableQuery():
        return """CREATE TABLE IF NOT EXISTS movies
                    (id INTEGER PRIMARY KEY,
                    movieTitle VARCHAR(50),
                    movieDescription VARCHAR(200),
                    movieGenre VARCHAR (50))"""

    def getTuple(self):
        return tuple([self.ID, self.movieTITLE, self.movieDESCRIPTION, self.movieGENRE])

    def getUpdateQuery(self):
        return "UPDATE movies SET id=?, movieTitle='{0}', movieDescription='{1}', movieGenre='{2}' WHERE id=?".format(self.movieTITLE, self.movieDESCRIPTION, self.movieGENRE)
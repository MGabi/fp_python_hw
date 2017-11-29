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
    # def __init__(self, movieID, movieTITLE, movieDESCRIPTION, movieGENRE):
    #     self.__movieID = movieID
    #     self.__movieTITLE = movieTITLE
    #     self.__movieDESCRIPTION = movieDESCRIPTION
    #     self.__movieGENRE = movieGENRE

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
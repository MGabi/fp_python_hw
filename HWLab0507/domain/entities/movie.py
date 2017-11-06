"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:05
"""
import domain.entities.keywords as KEYWORDS
class Movie:
    """
    This class holds data for a certain movie from the store
    @__movieID : INT
    @__movieTitle : STRING
    @__movieDescription : STRING
    @__movieGenre : STRING
    """
    def __init__(self, movieId, movieTitle, movieDescription, movieGenre):
        self.__movieId = movieId
        self.__movieTitle = movieTitle
        self.__movieDescription = movieDescription
        self.__movieGenre = movieGenre

    def getMovieID(self):
        return self.__movieId

    def setMovieID(self, movieId):
        self.__movieId = movieId

    def getMovieTitle(self):
        return self.__movieTitle

    def setMovieTitle(self, movieTitle):
        self.__movieTitle = movieTitle


    def getMovieDescription(self):
        return self.__movieDescription

    def setMovieDescription(self, movieDescription):
        self.__movieDescription = movieDescription


    def getMovieGenre(self):
        return self.__movieGenre

    def setMovieGenre(self, movieGenre):
        self.__movieGenre = movieGenre


    def getAttrs(self):
        return {KEYWORDS.movie_id: self.getMovieID(),
                KEYWORDS.movie_title: self.getMovieTitle(),
                KEYWORDS.movie_description: self.getMovieDescription(),
                KEYWORDS.movie_genre: self.getMovieGenre()}
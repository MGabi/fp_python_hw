"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:05
"""
class Movie:

    def __init__(self, movieId, movieTitle, movieDescription, movieGenre):
        self.__movieId = movieId
        self.__movieTitle = movieTitle
        self.__movieDescription = movieDescription
        self.__movieGenre = movieGenre

    def getMovieId(self):
        return self.__movieId

    def setMovieId(self, movieId):
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
        attrs = []
        attrs.append(self.getMovieId())
        attrs.append(self.getMovieTitle())
        attrs.append(self.getMovieDescription())
        attrs.append(self.getMovieGenre())
        return attrs
"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:42
"""
class MovieException(Exception):
    pass

class MovieValidator(object):

    @staticmethod
    def validate(movie):
        if type(movie.ID) is not int:
            raise MovieException("ID {0} is not an int!".format(movie.ID))
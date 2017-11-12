"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 17:12
"""
from datetime import datetime


class Utils(object):

    """
    Some keywords used in the entire app
    """
    CLIENT_ID = "clientID"
    CLIENT_NAME = "clientNAME"
    MOVIE_ID = "movieID"
    MOVIE_TITLE = "movieTITLE"
    MOVIE_DESCRIPTION = "movieDESCRIPTION"
    MOVIE_GENRE = "movieGENRE"
    RENTAL_ID = "rentalID"
    RENTED_DATE = "rentedDATE"
    DUE_DATE = "dueDATE"
    RETURNED_DATE = "returnedDATE"
    keywords = {"client_id": CLIENT_ID,
                "client_name": CLIENT_NAME,
                "movie_id": MOVIE_ID,
                "movie_title": MOVIE_TITLE,
                "movie_description": MOVIE_DESCRIPTION,
                "movie_genre": MOVIE_GENRE,
                "rental_id": RENTAL_ID,
                "rented_date": RENTED_DATE,
                "returned_date": RETURNED_DATE}

    @staticmethod
    def dateFromStr(date):
        """
        Converts date from DD/MM/YYY format to timestamp
        :param date: a date in string format as DD/MM/YYY
        :return: float value of the date timestamp
        """
        return datetime.strptime(date, "%d/%m/%Y").timestamp()

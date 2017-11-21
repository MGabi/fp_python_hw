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
    CST_RENTAL_PERIOD = 1209600
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
    def timestampFromDate(date):
        """
        Converts date from DD/MM/YYY format to timestamp
        :param date: a date in string format as DD/MM/YYY
        :return: float value of the date timestamp
        """
        return datetime.strptime(date, "%d/%m/%Y").timestamp()

    @staticmethod
    def dateFromTimestamp(timestamp):
        """
        Converts timestamp (float) value to date
        formatted as DD/MM/YYYY
        :param timestamp: time in seconds as float
        :return: new date from timestamp ( DD/MM/YYY )
        """
        return datetime.fromtimestamp(timestamp)

    @staticmethod
    def queryList(wantedList, query):
        """
        Queries the dictionary for finding occurences of `query` in it's elements
        :param query: string for querying
        :return: a dictionary contaning elements with `query` in them
        """
        newList = {}
        query = query.lower()
        ctr = 1
        for el in wantedList.values():
            for k, v in el.attrs.items():
                if v is None:
                    break

                if isinstance(v, int):
                    v = str(v)

                if isinstance(v, float):
                    v = str(Utils.dateFromTimestamp(v))

                if query in v.lower():
                    newList[ctr] = el
                    ctr += 1
                    break
        if len(newList) == 0:
            raise Exception("No such elements in the list!")

        return newList

    @staticmethod
    def rentalDelay(rental):
        """
        Calculates the delay of a rental in seconds
        from the current time
        :param rental: rental object
        :return: the difference of currentTime - dueDate in seconds
        """
        return datetime.now().timestamp() - rental.dueDATE
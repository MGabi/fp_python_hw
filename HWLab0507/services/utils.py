"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/6/2017 23:40
"""
from _datetime import datetime

def dateFromStr(date):
    """
    Returns a timestamp from a given date
    :param date: date to create timestamp
    :return: timestamp as float
    """
    return datetime.strptime(date, "%d/%m/%Y").timestamp()

def getSecFromDays(days):
    """
    Returns the seconds contained in a number of days
    :param days: number of days
    :return: seconds in a given number of days
    """
    return days*24*60*60
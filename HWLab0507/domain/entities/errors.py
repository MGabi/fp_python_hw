"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/3/2017 13:53
"""
class OutOfRangeError(Exception):
    def __init__(self):
        Exception.__init__(self, "The index is out of range")
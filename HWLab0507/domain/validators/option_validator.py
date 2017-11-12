"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 15:49
"""
class OptionException(Exception):
    pass

class OptionValidator(object):

    @staticmethod
    def validate(option, min, max):
        try:
            option = int(option)
        except ValueError as ve:
            raise OptionException("The introduced option is not a digit!")

        if not option in range(min, max + 1):
            raise OptionException("The introduced option does not exist!")
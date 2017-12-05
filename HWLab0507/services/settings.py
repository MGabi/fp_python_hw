"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/5/2017 12:14
"""
class Settings(object):

    @staticmethod
    def getDataManagerType():
        type = ""
        with open("settings.properites", "a") as settings:
            pass
        with open("settings.properites", "r") as settings:
            type = settings.readline()

        return type.split()[2]
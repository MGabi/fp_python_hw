"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/12/2017 13:42
"""
class ClientException(Exception):
    pass

class ClientValidator(object):

    @staticmethod
    def validate(client):
        if type(client.ID) is not int:
            raise ClientException("ID {0} is not an int!".format(client.ID))
        if len(client.clientNAME) < 3:
            raise ClientException("NAME {0} is not valid. Should have a minimum of 3 characters".format(client.clientNAME))
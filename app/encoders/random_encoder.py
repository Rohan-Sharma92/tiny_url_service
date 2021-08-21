from app.encoders.encoding_strategy import EncodingStrategy
import random
import string


# get random string of letters and digits
class RandomEncoder(EncodingStrategy):

    '''
    Random Encoder which generates a random string consisting of digits, lowercase and uppercase characters
    By default, this will generate a six character string
    '''

    def generateEncodedString(self, lim=6) -> string:
        source = string.ascii_letters + string.digits
        encoded_str = ''.join((random.choice(source) for i in range(lim)))
        return encoded_str

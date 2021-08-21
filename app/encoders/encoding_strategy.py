from abc import abstractmethod


class EncodingStrategy(object):
    '''
    Abstract strategy for encoding process
    '''

    @abstractmethod
    def generateEncodedString(self):
        """Required Method"""

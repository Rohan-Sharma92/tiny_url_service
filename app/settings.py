from app.cache.url_cache import URLCache
from app.encoders.encoder import Encoder
from app.encoders import random_encoder
from app.decoders.decoder import Decoder
import logging, os


class LoggingConfig:
    '''
    Logging configuration defining style of logging and log levels.
    '''
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
    LOG_FILE_NAME = os.environ.get('LOG_FILE_NAME', 'short_link').upper()

    @staticmethod
    def init_logging():
        logging.basicConfig(filename=LoggingConfig.LOG_FILE_NAME + ".log",
                            format='%(asctime)s:%(thread)d - %(levelname)s - %(message)s',
                            level=LoggingConfig.LOG_LEVEL)


class Configuration:
    '''
    Configuration encapsulates common functionalities used across different modules of the application such as encoders and decoders.
    The prefix URL can be overridden by setting PREFIX_URL environment variable 
    '''
    cache = None
    encoder = None
    decoder = None

    def __init__(self):
        self.cache = URLCache()
        prefixURL = os.environ.get("PREFIXURL", "http://short.est/")
        self.encoder = Encoder(random_encoder.RandomEncoder(), self.cache, prefixURL)
        self.decoder = Decoder(self.cache)
        LoggingConfig.init_logging()

    
config = Configuration()

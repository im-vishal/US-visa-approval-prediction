from us_visa.logger import logger
from us_visa.exception import USvisaException
import sys

# logger.info("Welcome to our custom logger.")


try:
    a = 2 / 0
except Exception as e:
    raise USvisaException(e, sys)
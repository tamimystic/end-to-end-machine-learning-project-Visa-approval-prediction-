import sys
from us_visa.logger import logging
from us_visa.exception import CustomException

logging.info("Wellcome my ml projects")

try:
    r=10/0
    print(r)
except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)

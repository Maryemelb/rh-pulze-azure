import logging
logging.basicConfig(
    filename='data/backend.log',
    level= logging.WARNING,
    format="%(levelname)s :%(asctime)s :%(name)s :%(message)s"

)
logger= logging.getLogger('data_logs')
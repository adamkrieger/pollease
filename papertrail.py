import socket
from logging.handlers import logging, SysLogHandler
from config import PAPERTRAIL_PORT, PAPERTRAIL_SERVER

class Papertrail():
    def get_papertrail_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logging_filter = ContextFilter()
        logger.addFilter(logging_filter)

        syslog = SysLogHandler(address=(PAPERTRAIL_SERVER, PAPERTRAIL_PORT))
        formatter = logging.Formatter('%(asctime)s POLLEASE: %(message)s', \
         datefmt='%b %d %H:%M:%S')

        syslog.setFormatter(formatter)
        logger.addHandler(syslog)

        return logger

class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True

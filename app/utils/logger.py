import logging
from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter(
    "%(asctime)s [%(levelname).4s] [%(name)s] %(funcName)s() %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = TimedRotatingFileHandler(
    './logs/lmtool.log', when='d', interval=1, backupCount=5)
file_handler.setFormatter(formatter)
handlers = [console_handler, file_handler]
logging.basicConfig(handlers=handlers)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

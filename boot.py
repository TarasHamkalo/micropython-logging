from logging.appenders.console_appender import ConsoleAppender
from logging.appenders.plain_file_appender import PlainFileAppender
LOG_LEVEL = 'INFO'
LOG_NAME = 'run'

MAX_CONCURRENT_FILES = 10
MAX_FILE_SIZE_B = 0.5 * 1024

# TODO strange dependency
APPENDERS_DEST = [
  ConsoleAppender(),
  PlainFileAppender(LOG_NAME, 'log', MAX_CONCURRENT_FILES, MAX_FILE_SIZE_B)
]

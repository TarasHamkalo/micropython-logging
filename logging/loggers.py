from .logger import Logger
from .levels import Levels

from .appenders.appenders import Appenders

# TODO: move to config
from boot import LOG_LEVEL

class Loggers:
  loggers = {}
  appenders = Appenders()

  @classmethod
  def _initialize(cls):
    Loggers.with_name('MAIN')

  @classmethod
  def close(cls):
    cls.appenders.close()

  @classmethod
  def log(cls):
    return cls.loggers['MAIN']

  @classmethod
  def with_name(cls, name):
    if name in cls.loggers:
      return cls.loggers[name]

    log = Logger(cls.appenders, Levels.from_string(LOG_LEVEL), name)
    cls.loggers[name] = log
    return log

  @classmethod
  def class_logger(cls, clazz):
    # clazz.log = Loggers.with_name(clazz.__name__)
    clazz.log = Loggers.with_name(clazz.__module__ + '.' + clazz.__name__)
    return clazz

  @classmethod
  def main_logger(cls, clazz):
    clazz.log = cls.log()
    return clazz


Loggers._initialize()
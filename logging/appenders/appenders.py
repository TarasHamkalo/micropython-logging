from logging.appenders.appender import Appender

from boot import APPENDERS_DEST

class Appenders(Appender):

  # TODO: other ways for init (from props ?)
  def __init__(self):
    self.appenders = APPENDERS_DEST

  def append(self, **params):
    for appender in self.appenders:
      appender.append(**params)

  def close(self):
    for appender in self.appenders:
      appender.close()
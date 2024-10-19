from .appender import Appender

class ConsoleAppender(Appender):
  # LOG_FORMAT = '[{}:{}:{}] {} ({}) -- {}'
  LOG_FORMAT = '[{hh}:{mm}:{ss}] {level} ({marker}) -- {msg}'

  def append(self, **params):
    print(self.LOG_FORMAT.format(**params))

  def close(self):
    pass
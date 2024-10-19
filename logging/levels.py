class Level:
  def __init__(self, name, priority):
    self.name = name
    self.priority = priority

class Levels:
  TRACE = Level('TRACE', 1)
  DEBUG = Level('DEBUG', 2)
  INFO = Level('INFO', 3)
  WARN = Level('WARN', 4)
  ERROR = Level('ERROR', 5)

  LEVELS_MAP = {
    'TRACE': TRACE,
    'DEBUG': DEBUG,
    'INFO': INFO,
    'WARN': WARN,
    'ERROR': ERROR
  }

  @classmethod
  def from_string(cls, str_level):
    return cls.LEVELS_MAP[str_level.upper()]


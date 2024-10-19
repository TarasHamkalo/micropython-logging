from .levels import Levels
import time

class Logger:
  def __init__(self, appenders, log_level, name):
    self.appenders = appenders
    self.log_level = log_level
    self.name = name

  def trace(self, msg_format, **args):
    self._log(Levels.TRACE, msg_format, **args)

  def debug(self, msg_format, **args):
    self._log(Levels.DEBUG, msg_format, **args)

  def info(self, msg_format, **args):
    self._log(Levels.INFO, msg_format, **args)

  def warn(self, msg_format, **args):
    self._log(Levels.WARN, msg_format, **args)

  def error(self, msg_format, **args):
    self._log(Levels.ERROR, msg_format, **args)

  def _log(self, level, msg_format, **args):
    if self.log_level.priority > level.priority:
      return

    msg = msg_format.format(**args)
    hh, mm, ss = time.localtime()[3:6]
    self.appenders.append(**{
      'msg': msg,
      'marker': self.name,
      'level': level.name,
      'hh': hh,
      'mm': mm,
      'ss': ss
    })
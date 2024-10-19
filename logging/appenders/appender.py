class Appender:

  def append(self, msg, marker, level, hh, mm, ss):
    raise NotImplementedError('Abstract method')

  def close(self):
    raise NotImplementedError('Abstract method')

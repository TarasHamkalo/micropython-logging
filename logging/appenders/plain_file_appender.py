import os
import sys

from .appender import Appender

# TODO: extract the part with rolling
# TODO: prioritize ERRORS when removing older log?
# TODO: on rerun older log aren't used, even tho their size could be <= MAX_SIZE_B
class PlainFileAppender(Appender):

  LOG_NAME_FORMAT = 'run-{hh}:{mm}:{ss}.log'

  LOG_FORMAT = '[{hh}:{mm}:{ss}] {level} ({marker}) -- {msg}\n'

  def __init__(self, fname, fext, max_concurrent_files, max_file_size_b):
    self.file = None
    self.fname = fname
    self.fext = fext
    self.max_file_size_b = max_file_size_b
    self.max_concurrent_files = max_concurrent_files

  def append(self, **params):
    self._roll(params)
    self.file.write(self.LOG_FORMAT.format(**params))
    self.file.flush()

  def close(self):
    try:
      self.file.close()
    except:
      err_msg = 'PlainFileAppender: Was not able to close file, ' + \
                ' perhaps you have not logged anything.'
      print(err_msg, file=sys.stderr, flush=True)

  def _roll(self, params):
    if self.file is None or self.file.tell() >= self.max_file_size_b:
      self._fit_new_log()
      if self.file is not None:
        self.close()
      self.file = open(self.LOG_NAME_FORMAT.format(**params), 'w+')

  def _fit_new_log(self):
    old_logs = self._retrieve_old_logs()
    if len(old_logs) >= self.max_concurrent_files:
      # print(old_logs, file=sys.stderr, flush=True)
      for log in old_logs[:self.max_concurrent_files - 1]:
        os.remove(log)

  def _retrieve_old_logs(self):
    return sorted(
      [f for f in os.listdir('.') if f.startswith(self.fname) and f.endswith(self.fext)]
    )
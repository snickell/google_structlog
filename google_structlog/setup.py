import structlog

from .setup_stdout import setup_stdout_logger
from .setup_google import setup_google_logger

_INITIALIZED = False

def getLogger(*args, **kwargs):
  global _INITIALIZED
  if not _INITIALIZED:
    setup()
  
  return structlog.get_logger(*args, **kwargs)

def setup(namespace=None, setup_google=True, setup_stdout=True):
  if setup_google:
    # Stream structured logs to Google Cloud's Stackdriver
    setup_google_logger()

  if setup_stdout:
    # Stream unstructured logs to STDOUT
    if namespace:
      setup_stdout_logger(namespace)
    else:
      setup_stdout_logger('__main__')
      setup_stdout_logger()

  global _INITIALIZED
  _INITIALIZED = True

import logging
import structlog
import sys
from .setup_google import get_default_logging_namespace

def setup_stdout_logger(
      namespace=get_default_logging_namespace(), 
      loglevel=logging.DEBUG
    ):

  logger = logging.getLogger(namespace)
  logger.setLevel(loglevel)

  formatter = structlog.stdlib.ProcessorFormatter(
    processor=structlog.dev.ConsoleRenderer(
      colors=True
    ),
  )

  handler = logging.StreamHandler(sys.stdout)
  handler.setFormatter(formatter)
  logger.addHandler(handler)
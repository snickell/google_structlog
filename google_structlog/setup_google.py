from google.cloud.logging import Client
from google.cloud.logging import _helpers
from google.cloud.logging.handlers import CloudLoggingHandler
from google.cloud.logging.handlers.transports.background_thread import _Worker

from pythonjsonlogger import jsonlogger
import structlog

from functools import cache as only_run_once
import datetime
import json
import logging

def monkeypatch_google_enqueue():
  def decode_json_then_enqueue(self, record, message, resource=None, labels=None, trace=None, span_id=None):
    try:
      info = json.loads(message)
    except json.decoder.JSONDecodeError:
      info = { "message": message }
    finally:
      info["python_logger"] = record.name

    queue_entry = {
      "info": info,
      "severity": _helpers._normalize_severity(record.levelno),
      "resource": resource,
      "labels": labels,
      "trace": trace,
      "span_id": span_id,
      "timestamp": datetime.datetime.utcfromtimestamp(record.created),
    }

    self._queue.put_nowait(queue_entry)
  
  _Worker.enqueue = decode_json_then_enqueue

def configure_structlog():
  structlog.configure(
      processors=[
          structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
      ],
      logger_factory=structlog.stdlib.LoggerFactory(),
  )

def get_handler(logName):
  handler = CloudLoggingHandler(Client(), logName)
  handler.setFormatter(jsonlogger.JsonFormatter())
  return handler

def get_default_logging_namespace():
  try:
    import __main__
    return __main__.__loader__.name.split('.')[0]
  except:
    pass

@only_run_once
def setup_google_logger(log_name=get_default_logging_namespace()):
  configure_structlog()
  monkeypatch_google_enqueue()

  google_handler = get_handler(log_name)
  
  # Add google_structlog handler to the root logger
  root_logger = logging.getLogger()
  root_logger.addHandler(google_handler)

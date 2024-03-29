Out of the box setup for python apps to send structured logs to 
Google Cloud's Stackdriver, in a format that allows stackdriver queries
over the structure.

This package sets up structured logging with stackdriver that Just Works(TM):
no configuration required. There's no confurability, 
but virtually no API means its easy to leave behind if you outgrow it.

Usage
=====

```python
from google_structlog import getLogger

logger = getLogger()
logger.warn('Danger Will Robinson', source='Robot', target='Will Robinson', threat='Boredom')
```

The logger comes from [structlog](https://www.structlog.org/) and allows all the options you'd expect on a `structlog.get_logger()` logger, including binding of repeated attributes:
```python
from google_structlog import getLogger
logger = getLogger()
# Include source= and target= values in the output of all calls to sublogger
sublogger = logger.bind(source='Robot', target='Will Robinson')
sublogger.warn('Danger Will Robinson: impending maintenance', threat='Responsibility')
```

Releasing a new version to pypi
=====

- Bump version in `setup.py`, make sure we stay ahead of Chrome and Firefox
- `rm -rf ./dist/*` if needed to remove past versions
- `python3 setup.py sdist bdist_wheel`
- `twine upload dist/*`
- Login to pypi as `snickell` lol (but seriously, TODO: not sure how to share PyPi creds with @ceresimaging)
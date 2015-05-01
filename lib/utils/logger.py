#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Set default logging handler to avoid "No handler found" warnings.
import logging
"""try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger().addHandler(NullHandler())
"""

logger = logging.getLogger()
handler = logging.StreamHandler()
#handler = logging.FileHandler('log/pyster.log')
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)   
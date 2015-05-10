#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__author__ = 'Pablo Alvao'
__version__ = '0.0.52'
__license__ = 'free'

import os, sys
# Make sure our bundled libraries take precedence
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))

from bottle import run
from utils.config import settings

import logging
log = logging.getLogger(__name__)

if __name__ == "__main__":
    if settings['server']['reloader']:
        if 'BOTTLE_CHILD' not in os.environ:
            log.debug('Using reloader, spawning first child.')
        else:
            log.debug('Child spawned.')

    if not settings['server']['reloader'] or ('BOTTLE_CHILD' in os.environ):
        log.info("Setting up application.")
        import api, routes, controllers
        log.info("Serving requests.")

    run(port=settings['server']['port'],
        host=settings['server']['host'],
        debug=settings['server']['debug'],
        reloader=settings['server']['reloader'])

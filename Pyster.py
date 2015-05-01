#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
# Make sure our bundled libraries take precedence
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))

from bottle import run

import logging, utils.logger
log = logging.getLogger(__name__)

if __name__ == "__main__":
    log.info('Starting Pyster')
    import api, routes, controllers
    # run(reloader=True)
    run(port=8080, host='192.168.0.102')

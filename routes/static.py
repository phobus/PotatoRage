#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Static routes

Created by: Rui Carmo
License: MIT (see LICENSE for details)
"""

import os, sys, logging
from bottle import route, static_file

log = logging.getLogger()

from utils.config import settings

@route('/static/<path:path>')
def send_static(path):
    """Static file handler"""
    return static_file(path, root='static')

@route('/img/<path:path>')
def send_static(path):
    """Static file handler"""
    return static_file(path, root=settings['folders']['img'])

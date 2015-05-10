#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main routes

Created by: Rui Carmo
License: MIT (see LICENSE for details)
"""
import os, sys, logging
from bottle import view, route, static_file

log = logging.getLogger()

"""@route('/')
def index():
    return static_file('index.html', root='views')"""

@route('/')
@view('layout')
def index():
    return {}

# import all other routes
import static, debug, docs

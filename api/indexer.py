#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import os, sys, logging, json

log = logging.getLogger()

from bottle import route, get, put, post, delete, request, response, abort
import api

from controllers import IndexerAPIController

prefix = api.prefix + '/idx'  # + TODO: FILL THIS IN

# Collection URI - List
@get(prefix + '/<media>')
def list(media):
    return IndexerAPIController.query_media(media, request.query.query, request.query.page)
    
# Element URI - Retrieve element
@get(prefix + '/<media>/<id>')
def element(media, id):
    return IndexerAPIController.get_media(media, id)

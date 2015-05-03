#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import os, sys, logging, json

log = logging.getLogger()

from bottle import route, get, put, post, delete, request, response, abort
import api

from controllers import indexerAPIController

prefix = api.prefix + '/idx'  # + TODO: FILL THIS IN

# Collection URI - List
@get(prefix + '/<media>')
def list(media):
    return indexerAPIController.query_media(request.query.indexer,
                                            media,
                                            request.query.query,
                                            request.query.page)
    
# Element URI - Retrieve element
@get(prefix + '/<media>/<id>')
def element(media, id):
    return indexerAPIController.get_media(request.query.indexer,
                                          media,
                                          id)

# Collection URI - Add item to collection
@post(prefix + '/<media>')
def append(media):
    return indexerAPIController.append_media(request.forms.indexer,
                                             media,
                                             request.forms.id)

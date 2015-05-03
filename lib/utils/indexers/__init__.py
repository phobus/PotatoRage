#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)

def init_idx():
    global idx
    idx = {}
    
    from themoviedb import TheMovieDb
    tmdb = TheMovieDb()
    idx[tmdb.name] = tmdb
    log.debug('Init %s' % tmdb.name)
    
try:
    idx
except NameError:
    init_idx()

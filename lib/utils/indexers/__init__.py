#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from utils.config import settings, checkFolder
from models import DAO

import logging
log = logging.getLogger(__name__)


def init_idx():
    global idx
    idx = {}
    
    from themoviedb import TheMovieDb
    i = TheMovieDb()
    log.debug('Init %s' % i.name)
    print DAO['settings']
    print DAO['settings'].select_by_id('TheMovieDb.img')
    print DAO['settings'].select_all()
    i.server_img = 'http://image.tmdb.org/t/p/w154'
    i.local_img = os.path.join(settings['folders']['img'], i.name)
    checkFolder(i.local_img)
    idx[i.name] = i
    
try:
    idx
except NameError:
    init_idx()

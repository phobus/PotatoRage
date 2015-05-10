#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.indexers import idx
#from utils.indexers.themoviedb import TheMovieDb

def query_media(media, query, page):
    if not page:
        page = 1
    return idx[_current_indexer(media)].search(media, query, page)

def get_media(media, id):
    return idx[_current_indexer(media)].get_media(media, id)

def _current_indexer(media):
    return 'TheMovieDb'

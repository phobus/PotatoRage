#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.indexers import idx
#from utils.indexers.themoviedb import TheMovieDb

def query_media(indexer, media, query, page):
    if not page:
        page = 1
        
    if not indexer:
        indexer = _current_indexer(media)
        
    return idx[indexer].search(media, query, page)

def get_media(indexer, media, id):
    if not indexer:
        indexer = _current_indexer(media)
        
    return idx[indexer].get_media(media, id)

def append_media(media, id, indexer):
    if not indexer:
        indexer = _current_indexer(media)
        
    media = idx[indexer].get_media(media, id)
    
    return {}

def _current_indexer(media):
    return 'TheMovieDb'

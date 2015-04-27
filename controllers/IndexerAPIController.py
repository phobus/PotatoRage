#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.indexers import idx

from models.movieDAO import movieDAO
from models.tvDAO import tvDAO
from models.episodeDAO import episodeDAO

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

def append_media(indexer, media, id):
    if not indexer:
        indexer = _current_indexer(media)
        
    data = idx[indexer].get_media(media, id)
    
    if media == 'movie':
        print movieDAO().query_insert(data)
    elif media == 'tv':
        print tvDAO().query_insert(data)
        season = None
        for n_season in range(data['n_seasons']):
            season = idx[indexer].get_season(data['id'], n_season + 1)
            episodeDAO().insert_season(season)
    return {}

def _current_indexer(media):
    return 'TheMovieDb'
    

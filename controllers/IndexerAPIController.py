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
    
    if query:
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
        movieDAO().insert(data)
        pass
    elif media == 'tv':
        tvDAO().insert(data)
        eps = []
        for n_season in range(data['n_seasons']):
            eps.extend(idx[indexer].get_season(data['id'], n_season + 1, data['tv_id']))
        episodeDAO().insert_many(eps)
    episodeDAO().commit()
    return {}

def _current_indexer(media):
    return 'TheMovieDb'
    

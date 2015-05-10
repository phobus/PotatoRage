#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.indexers import idx

from models import DAO, commit

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
    idx[indexer].store_img(data['poster'])
    if media == 'movie':
        DAO['movie'].insert(data)
    elif media == 'tv':
        DAO['tv'].insert(data)
        eps = []
        for n_season in range(data['n_seasons']):
            eps.extend(idx[indexer].get_season(data['id'], n_season + 1, data['tv_id']))
        DAO['episode'].insert_many(eps)
    commit()
    return {}

def _current_indexer(media):
    if media == 'movie':
        return DAO['settings'].select_by_id('idx_movies')['value'];
    elif media == 'tv':
        return DAO['settings'].select_by_id('idx_tv')['value'];

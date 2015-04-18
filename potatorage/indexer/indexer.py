#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Indexer:
    def __init__(self, indexer_id, name, url, idx_tv, idx_movie):
        self.indexer_id = indexer_id;
        self.name = name;
        self.url = url;
        self.idx_tv = idx_tv;
        self.idx_movie = idx_movie;
        
    def info(self):
        return {'indexer_id' : self.indexer_id,
                'name' : self.name,
                'url' : self.url,
                'idx_tv' : self.idx_tv,
                'idx_movie' : self.idx_movie }
        
    def search_movies(self, query):
        pass
    
    def get_movie(self, movie_id):
        pass
    
    def search_tv(self, query):
        pass
    
    def get_tv(self, movie_id):
        pass

    def save_tv(self, media, id):
        """
        API save tv in DB
        """
        pass
    
    def save_movie(self, media, id):
        """
        API save movie in DB
        """
        pass
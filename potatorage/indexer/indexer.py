#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Indexer:
    def __init__(self, indexer_id, name, url, idx_tv, idx_movie):
        self.indexer_id = indexer_id;
        self.name = name;
        self.url = url;
        self.idx_tv = idx_tv;
        self.idx_movie = idx_movie; 

    def build_results(self, results):
        return {'indexer':self.info(), 'results': results}
        
    def info(self):
        # result = {}
        return {'id':self.indexer_id,
                'name': self.name,
                'url':self.url}
        
    def search_movies(self, query):
        pass
    
    def get_movie(self, movie_id):
        pass
    
    def search_show(self, query):
        pass
    
    def get_movie(self, movie_id):
        pass

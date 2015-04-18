#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json

from potatorage.indexer.indexer import Indexer

class TheMovieDb(Indexer):
    def __init__(self):
        Indexer.__init__(self, 0, 'TheMovieDb', 'https://www.themoviedb.org/', True, True)
        self.config = {}
        self.config['base_url'] = 'http://api.themoviedb.org/3'
        self.config['api_key'] = '28eeb03a21186cf0512bfd1d11ce829e'
        self.config['language'] = 'es'
        self.url_config = u'%(base_url)s/configuration?api_key=%(api_key)s' % self.config
        self.url_search = u'%(base_url)s/search/%%s?api_key=%(api_key)s&language=%(language)s&query=%%s' % self.config
        self.url_get = u'%(base_url)s/%%s/%%s?api_key=%(api_key)s&language=%(language)s' % self.config
        self.url_img = ''
        self.load_config()
        
    def load_config(self):
        response = urllib2.urlopen(self.url_config)
        data = response.read()
        dict = json.loads(data)
        self.url_img = dict['images']['base_url'] + dict['images']['poster_sizes'][1]
    
    def search_movies(self, query):
        query = urllib.quote(query.encode("utf-8"))
        url = self.url_search % ('movie', query)

        response = urllib2.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        results = []
        for r in dict['results']:
            results.append({'id': r['id'],
                            'title': r['title'],
                            'date': r['release_date'],
                            'vote_average': r['vote_average']})
        return {'results': results}
    
    def get_movie(self, movie_id):
        movie_id = urllib.quote(movie_id.encode("utf-8"))
        url = self.url_get % ('movie', movie_id)

        response = urllib2.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        print url
        results = {'id': dict['id'],
                   'imdb_id': dict['imdb_id'],
                   'title': dict['title'],
                   'date': dict['release_date'],
                   'vote_average': dict['vote_average'],
                   'status': dict['status'],
                   'overview': dict['overview'],
                   'url_poster': self.url_img + dict['poster_path'] if dict['poster_path'] else None
                   }
        return results

    def search_series(self, query):
        query = urllib.quote(query.encode("utf-8"))
        url = self.url_search % ('tv', query)

        response = urllib2.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        results = []
        for r in dict['results']:
            results.append({'id': r['id'],
                            'title': r['name'],
                            'date': r['first_air_date'],
                            'vote_average': r['vote_average']})
        return {'results': results}
    
    def get_serie(self, tv_id):
        tv_id = urllib.quote(tv_id.encode("utf-8"))
        url = self.url_get % ('tv', tv_id)

        response = urllib2.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        results = {'id': dict['id'],
                   'title': dict['name'],
                   # 'imdb_id': dict['imdb_id'],
                   'date': dict['first_air_date'],
                   'vote_average': dict['vote_average'],
                   'status': dict['status'],
                   'overview': dict['overview'],
                   'url_poster': self.url_img + dict['poster_path'],
                   #
                   'n_episodes': dict['number_of_episodes'],
                   'n_seasons': dict['number_of_seasons']}
        return results

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json

class TheMovieDb:
    def __init__(self):
        self.config = {}
        self.config['base_url'] = 'http://api.themoviedb.org/3'
        self.config['api_key'] = '28eeb03a21186cf0512bfd1d11ce829e'
        self.config['language'] = 'es'
        self.url_config = u'%(base_url)s/configuration?api_key=%(api_key)s' % self.config
        self.url_search_movies = u'%(base_url)s/search/movie?api_key=%(api_key)s&language=%(language)s&query=%%s' % self.config
        self.url_search_seres = u'%(base_url)s/search/tv?api_key=%(api_key)s&language=%(language)s&query=%%s' % self.config
        self.url_get_movie = u'%(base_url)s/movie/%%s?api_key=%(api_key)s&language=%(language)s' % self.config
        self.url_get_serie = u'%(base_url)s/tv/%%s?api_key=%(api_key)s&language=%(language)s' % self.config
        self.url_img = ''
        self.load_config()
        
    def load_config(self):
        response = urllib2.urlopen(self.url_config)
        data = response.read()
        dict = json.loads(data)
        self.url_img = dict['images']['base_url'] + dict['images']['poster_sizes'][1]
    
    def search_movies(self, query):
        query = urllib.quote(query.encode("utf-8"))
        url = self.url_search_movies % query

        response = urllib2.urlopen(url)
        json = response.read()
        return json
    
    def get_movie(self, id):
        id = urllib.quote(id.encode("utf-8"))
        url = self.url_get_movie % id

        response = urllib2.urlopen(url)
        json = response.read()
        return json

    def search_series(self, query):
        query = urllib.quote(query.encode("utf-8"))
        url = self.url_search_seres % query

        response = urllib2.urlopen(url)
        json = response.read()
        return json
    
    def get_serie(self, id):
        id = urllib.quote(id.encode("utf-8"))
        url = self.url_get_serie % id

        response = urllib2.urlopen(url)
        json = response.read()
        return json

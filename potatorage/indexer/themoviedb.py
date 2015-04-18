#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json

from potatorage.indexer.indexer import Indexer

class TheMovieDb(Indexer):
    def __init__(self):
        """
        TheMovieDb http API wrapper
        """
        Indexer.__init__(self, 0, 'TheMovieDb', 'https://www.themoviedb.org/', True, True)
        self.config = {}
        self.config['base_url'] = 'http://api.themoviedb.org/3'
        self.config['api_key'] = '28eeb03a21186cf0512bfd1d11ce829e'
        self.config['language'] = 'es'
        self.url_config = u'%(base_url)s/configuration?api_key=%(api_key)s' % self.config
        self.url_search = u'%(base_url)s/search/%%s?api_key=%(api_key)s&language=%(language)s&query=%%s' % self.config
        self.url_get = u'%(base_url)s/%%s/%%s?api_key=%(api_key)s&language=%(language)s' % self.config
        self.url_img = ''
        self._load_config()
        
    def _load_config(self):
        """
        load configuration from TheMovieDb
        """
        response = urllib2.urlopen(self.url_config)
        data = response.read()
        dict = json.loads(data)
        self.url_img = dict['images']['base_url'] + dict['images']['poster_sizes'][1]

    def _search(self, media, query):
        """
        search from TheMovieDb by query
        """
        query = urllib.quote(query.encode("utf-8"))
        if media in ('tv', 'movie'):
            url = self.url_search % (media, query)
            response = urllib2.urlopen(url)
            data = response.read()
            dict = json.loads(data)
            return dict
    
    def _get_media(self, media, id):
        """
        search from TheMovieDb by id
        """
        id = urllib.quote(id.encode("utf-8"))
        if media in ('tv', 'movie'):
            url = self.url_get % (media, id)
            response = urllib2.urlopen(url)
            data = response.read()
            dict = json.loads(data)
            return dict
    
    def _parse_movie(self, dict):
        return {'id': dict['id'],
                'imdb_id': dict['imdb_id'],
                'title': dict['title'],
                'date': dict['release_date'],
                'rating': dict['vote_average'],
                'status': dict['status'],
                'overview': dict['overview'],
                'poster': dict['poster_path']}
    
    def _parse_tv(self, dict):
        return {'id': dict['id'],
                'title': dict['name'],
                # 'imdb_id': dict['imdb_id'],
                'date': dict['first_air_date'],
                'rating': dict['vote_average'],
                'status': dict['status'],
                'overview': dict['overview'],
                'poster': dict['poster_path'],
                #
                'n_episodes': dict['number_of_episodes'],
                'n_seasons': dict['number_of_seasons']}
        
    def search_movies(self, query):
        """
        API search movies
        """
        dict = self._search('movie', query)
        results = []
        for r in dict['results']:
            results.append({'id': r['id'],
                            'title': r['title'],
                            'date': r['release_date'],
                            'rating': r['vote_average']})
        return {'results': results}
    
    def search_tv(self, query):
        """
        API search TV shows
        """
        dict = self._search('tv', query)
        results = []
        for r in dict['results']:
            results.append({'id': r['id'],
                            'title': r['name'],
                            'date': r['first_air_date'],
                            'rating': r['vote_average']})
        return {'results': results}
    
    def get_movie(self, movie_id):
        """
        API get movie by id
        """
        results = self._get_media('movie', movie_id)
        results = self._parse_movie(results)
        results['poster'] = self.url_img + results['poster'] if results['poster'] else None
        return results
    
    def get_tv(self, tv_id):
        """
        API get movie by id
        """
        results = self._get_media('tv', tv_id)
        results = self._parse_tv(results)
        results['poster'] = self.url_img + results['poster'] if results['poster'] else None
        return results

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
        pass
      

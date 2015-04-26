#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

from base_indexer import Indexer

class TheMovieDb(Indexer):
    def __init__(self, api_key='28eeb03a21186cf0512bfd1d11ce829e', version=3, language='es'):
        Indexer.__init__(self, 'TheMovieDb', 'https://www.themoviedb.org/', ('movie', 'tv'))
        self.config = {}
        
        self.config['api_key'] = api_key
        self.config['version'] = version
        self.config['language'] = language
        
        # URLs
        self.config['base_url'] = u'https://api.themoviedb.org/%(version)s' % self.config
        #
        self.config['url_config'] = u'%(base_url)s/configuration?api_key=%(api_key)s' % self.config
        self.config['url_search'] = u'%(base_url)s/search/%%s?api_key=%(api_key)s&language=%(language)s&query=%%s&page=%%s' % self.config
        self.config['url_get'] = u'%(base_url)s/%%s/%%s?api_key=%(api_key)s&language=%(language)s' % self.config
        self.config['url_get_season'] = u'%(base_url)s/tv/%%s/season/%%s?api_key=%(api_key)s&language=%(language)s' % self.config
        
        #
        self.url_img = None
        #self._load_config()

    def _load_config(self):
        """
        load configuration from TheMovieDb
        """
        dict = Indexer._requestJson(self, self.config['url_config'])
        self.url_img = dict['images']['base_url'] + dict['images']['poster_sizes'][1]

    def search(self, media, query, page=1):
        """
        search from TheMovieDb by query
        """
        query = urllib.quote(query.encode("utf-8"))
        if media in self.media:
            dict = Indexer._requestJson(self, self.config['url_search'] % (media, query, page))
            return dict
    
    def get_media(self, media, id):
        """
        search from TheMovieDb by id
        """
        id = urllib.quote(id.encode("utf-8"))
        if media in self.media:
            dict = Indexer._requestJson(self, self.config['url_get'] % (media, id))
            return dict
        
    def _get_season(self, id, season):
        id = urllib.quote(id.encode("utf-8"))
        dict = Indexer._requestJson(self, self.config['url_get_season'] % (id, season))
        return dict

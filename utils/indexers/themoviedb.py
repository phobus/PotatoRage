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
        self.config['url_get'] = u'%(base_url)s/%%s/%%s?api_key=%(api_key)s&language=%(language)s&append_to_response=external_ids' % self.config
        self.config['url_get_season'] = u'%(base_url)s/tv/%%s/season/%%s?api_key=%(api_key)s&language=%(language)s' % self.config
        
        #
        self.url_img = None
        # self._load_config()

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
            return {'indexer': self.name,
                    'results': self._parse_search(media, dict),
                    'page': dict['page'],
                    'total_pages': dict['total_pages'],
                    'total_results': dict['total_results']
                    }
            
    def get_media(self, media, id):
        """
        search from TheMovieDb by id
        """
        id = urllib.quote(id.encode("utf-8"))
        if media in self.media:
            dict = Indexer._requestJson(self, self.config['url_get'] % (media, id))
            return self._parse_media(media, dict)
        
    def get_season(self, id, season):
        # id = urllib.quote(id.encode("utf-8"))
        dict = Indexer._requestJson(self, self.config['url_get_season'] % (id, season))
        return self._parse_season(dict)
    
    def _parse_search(self, media, dict):
        results = []
        if media == 'movie':
            for r in dict['results']:
                results.append({'id': r['id'],
                                'title': r['title'],
                                'date': r['release_date'],
                                'rating': r['vote_average']})
        elif media == 'tv':
            for r in dict['results']:
                results.append({'id': r['id'],
                                'title': r['name'],
                                'date': r['first_air_date'],
                                'rating': r['vote_average']})
        return results
    
    def _parse_media(self, media, dict):
        if media == 'movie':
            return {'indexer': self.name,
                    'id': dict['id'],
                    'imdb_id': dict['imdb_id'],
                    'title': dict['title'],
                    'date': dict['release_date'],
                    'rating': dict['vote_average'],
                    'status': dict['status'],
                    'overview': dict['overview'],
                    'poster': dict['poster_path']}
            
        elif media == 'tv':
            return {'indexer': self.name,
                    'id': dict['id'],
                    'title': dict['name'],
                    'imdb_id': dict['external_ids']['imdb_id'],
                    'date': dict['first_air_date'],
                    'rating': dict['vote_average'],
                    'status': dict['status'],
                    'overview': dict['overview'],
                    'poster': dict['poster_path'],
                    #
                    'n_episodes': dict['number_of_episodes'],
                    'n_seasons': dict['number_of_seasons']}
    
    def _parse_season(self, dict):
        results = []
        for ep in dict['episodes']:
                results.append({'indexer': self.name,
                                'id': ep['id'],
                                'title': ep['name'],
                                'episode_number': ep['episode_number'],
                                'date': ep['air_date'],
                                'overview': ep['overview'],
                                #
                                'season_number': dict['season_number']})
        return {'episodes': results}
        """return {'indexer': self.name,
                'id': dict['id'],
                'title': dict['name'],
                'season_number': dict['season_number'],
                'date': dict['air_date'],
                'overview': dict['overview'],
                #'poster': dict['poster_path'],
                'episodes': results}"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json

import logging, utils.logger
log = logging.getLogger(__name__)

from tvdb_cache import CacheHandler

class Indexer:
    def __init__(self, name, url, media):
        self.name = name
        self.url = url
        self.media = media
        
    def _requestJson(self, url):
        log.info('Retrieving URL %s' % url)
        #response = urllib2.urlopen(url)

        opener = urllib2.build_opener(CacheHandler("/home/neganix/git/Pyster/data/cache/"))
        response = opener.open(url)
        #response.recache()

        """if recache:
            log().debug("Attempting to recache %s" % url)
            response.recache()"""
        data = response.read()
        return json.loads(data)
    
    def search(self, media, query):
        raise NotImplementedError( "Indexer not implements search" )
    
    def get_media(self, media, id):
        raise NotImplementedError( "Indexer not implements get_media" )
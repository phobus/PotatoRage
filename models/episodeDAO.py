#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base_DAO import DAO

class episodeDAO(DAO):
    def __init__(self):
        DAO.__init__(self, 'episode')
    
    def insert_season(self, dict):
        for ep in dict['episodes']:
            print self.query_insert(ep)
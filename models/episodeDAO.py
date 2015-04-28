#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base_DAO import DAO

class episodeDAO(DAO):
    def __init__(self):
        DAO.__init__(self, 'episode')
    
    def insert_seasons(self, seasons):
        #cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
        query = self.query_insert(seasons[0][0])
        print query
        for s in seasons:
            for ep in s:
                print ep
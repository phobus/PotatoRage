#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from setup import DATA_BASE

class Schema(object):
    def __init__(self):
        self.version = 1
    
    def createDataBase(self):
        queries = [
            'CREATE TABLE db_version (db_version INT);',
            "INSERT INTO db_version VALUES (%s);" % self.version,
            'CREATE TABLE indexer (indexer_id INT PRIMARY KEY, name TEXT, url TEXT, series INT, movies INT);', 
            "INSERT INTO indexer VALUES (0, 'TheTVDB','http://thetvdb.com/', 1, 0);",
            'CREATE TABLE series (serie_id INT PRIMARY KEY, indexer_id INT, name TEXT, network TEXT);'
            ]
        con = sqlite3.connect(DATA_BASE)
        #con = sqlite3.connect(':memory:')
        for query in queries:
            con.execute(query)
        con.commit()
        con.close()

        
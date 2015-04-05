#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class Database(object):
    def __init__(self):
        self.version = 1
    
    def createDataBase(self):
        queries = ['CREATE TABLE db_version (db_version INTEGER);',
                   "INSERT INTO db_version (db_version) VALUES (%s);" % s,
                   'CREATE TABLE imdb_info (indexer_id INTEGER PRIMARY KEY, imdb_id TEXT, title TEXT, year NUMERIC, akas TEXT, runtimes NUMERIC, genres TEXT, countries TEXT, country_codes TEXT, certificates TEXT, rating TEXT, votes INTEGER, last_update NUMERIC)',
                    ]

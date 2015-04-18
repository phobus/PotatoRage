#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3
from setup import DATA_BASE, SQL_FOLDER

DB_VERSION = 2

class Schema(object):
    def __init__(self):
        pass
        
    def createDataBase(self):
        queries = open(os.path.join(SQL_FOLDER, 'schema.sql'), 'r').read()
        conn = sqlite3.connect(DATA_BASE)
        c = conn.cursor()
        c.executescript(queries)
        conn.commit()
        c.close()
        conn.close()
        
    def createDataBase2(self):
        queries = [
            'CREATE TABLE db_version (db_version INT);',
            "INSERT INTO db_version VALUES (%s);" % self.version,
            'CREATE TABLE indexer (indexer_id INT PRIMARY KEY, name TEXT, url TEXT, series INT, movies INT);',
            "INSERT INTO indexer VALUES (0, 'TheTVDB','http://thetvdb.com/', 1, 0);",
            'CREATE TABLE media (media_id INT PRIMARY KEY AUTOINCREMENT, type TEXT, indexer_id INT, imdb_id TEXT, title TEXT, date DATE, overview TEXT, status TEXT, rating REAL, status TEXT, poster TEXT);',
            ]
        con = sqlite3.connect(DATA_BASE)
        # con = sqlite3.connect(':memory:')
        for query in queries:
            con.execute(query)
        con.commit()
        con.close()

        'INSERT INTO media VALUES (?,?,?,?,?,?,?,?,?,?)'

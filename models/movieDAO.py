#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base_DAO import DataAccess

class movieDAO(DataAccess):
    def __init__(self, con):
        DataAccess.__init__(self, 'movie', con)
        self.query['check_by_imdb'] = self.query['count'] + ' WHERE imdb_id = ?'
        self.query['check_idx_id'] = self.query['count'] + ' WHERE indexer = ? AND id = ?'
        
    def check_by_imdb(self, imdb_id):
        cur = self.con.cursor()
        cur.execute(self.query['check_by_imdb'], (imdb_id,))
        result = cur.fetchone()
        cur.close()
        return result
    
    def check_idx_id(self, idx, id):
        cur = self.con.cursor()
        cur.execute(self.query['check_idx_id'], (idx, id))
        result = cur.fetchone()
        cur.close()
        return result
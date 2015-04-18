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

    def insert(self, table, values):
        cols = values.keys()
        # generate insert statementx    
        stmt = 'INSERT INTO %s (%s) VALUES (%s)' %(table,
                                                   ', '.join(cols),
                                                   ', '.join([":%s" % col for col in cols]))
        print stmt
        return stmt
#https://excelicious.wordpress.com/2010/04/23/python-data-access-patterns-part-1/


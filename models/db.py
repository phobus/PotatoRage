#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from utils.config import settings

import logging
log = logging.getLogger(__name__)

def _dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_con():
    log.debug('Create connection %s' % settings['files']['db'])
    con = sqlite3.connect(settings['files']['db'], check_same_thread=False)
    con.row_factory = _dict_factory 
    return con

def exec_script(file_name):
    try:
        from models import connection

        cur = connection.cursor()
        log.debug('Execute script %s' % file_name)
        cur.executescript(open(file_name, 'r').read())
        
        cur.close()
        connection.commit()
    
    except lite.Error, e:
        if connection:
            connection.rollback()
        
        log.error("Error %s:" % e.args[0])
        sys.exit(1)
        
    finally:
        if cur:
            cur.close() 

def create_db():
    log.debug('Creating DB')
    import os
    exec_script(os.path.join(settings['folders']['sql_dir'], 'schema.sql'))
    
    from models import DAO, commit 
    from utils.indexers import idx
    url_img = idx['TheMovieDb'].load_config()
    DAO['settings'].insert({'name':'TheMovieDb.img', 'value':url_img})
    commit()
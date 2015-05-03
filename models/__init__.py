#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)
  
def init_dao():
    global connection, DAO
    from db import create_con
    connection = create_con()
    DAO = {}
    
    from base_DAO import DataAccess
    from movieDAO import movieDAO
    from tvDAO import tvDAO
    
    o = movieDAO(connection)
    DAO[o.table_name] = o
    
    o = tvDAO(connection)
    DAO[o.table_name] = o
    
    o = DataAccess('episode', connection)
    DAO[o.table_name] = o
    
    o = DataAccess('settings', connection)
    DAO[o.table_name] = o
    
    return DAO

def commit():
    connection.commit()
    
try:
    connection
except NameError:
    log.debug('Init database')
    
    init_dao()
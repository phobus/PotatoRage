#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_con():
    con = sqlite3.connect('/home/neganix/git/Pyster/data/todo.db')
    # con.row_factory = sqlite3.Row
    con.row_factory = dict_factory 
    return con

def exec_script(file_name):
    try:
        con = create_con()
        cur = con.cursor()
        
        cur.executescript(open(file_name, 'r').read())
        
        con.commit()
        
        # cur.close()
        # con.close()
    
    except lite.Error, e:
        if con:
            con.rollback()
            
        print "Error %s:" % e.args[0]
        sys.exit(1)
        
    finally:
        if con:
            con.close() 

        

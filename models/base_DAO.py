#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Veeeery basic DAO. 
Based on INTEGER PRIMARY KEY AUTOINCREMENT for all tables
AUTOINCREMENT field is: table name + '_id'

don't try it at home, better take ORM
"""

# from models import db
from db import create_con
db = create_con()

class DAO:
    def __init__(self, table_name, con=db):
        self.table_name = table_name
        self.table_id = table_name + '_id'
        self.con = con
        
        self.query = {}
        
        self.query['count'] = 'SELECT count(*) total_results FROM %s' % self.table_name
        self.query['select_all'] = 'SELECT * FROM %s %%s%%s%%s' % self.table_name
        self.query['select_by_id'] = 'SELECT * FROM %s WHERE %s = ?' % (self.table_name, self.table_id)
        self.query['delete'] = 'DELETE FROM %s WHERE %s = ?' % (self.table_name, self.table_id)
        self.query['insert'] = 'INSERT INTO %s (%%s) VALUES (%%s)' % self.table_name
        self.query['update'] = 'UPDATE %s SET %%s WHERE %s = :%s' % (self.table_name,
                                                                     self.table_id,
                                                                     self.table_id)
        
    def count(self):
        cur = self.con.cursor()
        cur.execute(self.query['count'])
        result = cur.fetchone()
        cur.close()
        return result
    
    def select_all(self, order_by=None, limit_ini=None, limit_end=None):
        cur = self.con.cursor()
        stmt = self.query['select_all'] % (' ORDER BY %s' % order_by if order_by else '',
                                           ' LIMIT %s' % limit_ini if limit_ini else '',
                                           ', %s' % limit_end if limit_end else '')
        cur.execute(stmt)
        result = cur.fetchall()
        cur.close()
        return result

    def select_by_id(self, id_autonumeric):
        cur = self.con.cursor()
        cur.execute(self.query['select_by_id'], (id_autonumeric,))
        result = cur.fetchone()
        cur.close()
        return result
        
    def delete(self, id_autonumeric):
        cur = self.con.cursor()
        cur.execute(self.query['delete'], (id_autonumeric,))
        result = cur.rowcount
        cur.close()
        return result
        
    def insert(self, dict):
        id = dict.pop(self.table_id, None)
        if not id:
            cols = dict.keys()
            stmt = self.query['insert'] % (', '.join(cols),
                                           ', '.join([":%s" % col for col in cols]))
            cur = self.con.cursor()
            cur.execute(stmt, dict)
            result = cur.rowcount
            dict[self.table_id] = cur.lastrowid
            cur.close()
            return result
        
    def insert_many(self, dict):
        #id = dict.pop(self.table_id, None)
        #if not id:
        cols = dict[0].keys()
        stmt = self.query['insert'] % (', '.join(cols),
                                       ', '.join([":%s" % col for col in cols]))
        cur = self.con.cursor()
        cur.executemany(stmt, dict)
        result = cur.rowcount
        #dict[self.table_id] = cur.lastrowid
        cur.close()
        return result
        
    def update(self, dict):
        id = dict.pop(self.table_id, None)
        if id:
            cols = dict.keys()  
            stmt = self.query['update'] % ', '.join(["%s = :%s" % (col, col)  for col in cols])
            dict[self.table_id] = id
            cur = self.con.cursor()
            cur.execute(stmt, dict)
            result = cur.rowcount
            cur.close()
            return result

    def commit(self):
        db.commit()   

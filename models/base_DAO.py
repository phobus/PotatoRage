#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Veeeery basic DAO. 
Based on INTEGER PRIMARY KEY AUTOINCREMENT for all tables
AUTOINCREMENT field is: table name + '_id'

don't try it at home, better take ORM
"""

from models import db

class DAO:
    def __init__(self, table_name, con=db):
        self.table_name = table_name
        self.table_id = table_name + '_id'
        self.con = con
        
    def count(self):
        # with sqlite3.connect(db_filename) as conn:
        cur = self.con.cursor()
        cur.execute('SELECT count(*) total_results FROM %s' % self.table_name)
        result = cur.fetchone()
        cur.close()
        return result
    
    def select_all(self, order_by=None, limit_ini=None, limit_end=None):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM %s%s%s%s' % (self.table_name,
                                           ' ORDER BY %s' % order_by if order_by else '',
                                           ' LIMIT %s' % limit_ini if limit_ini else '',
                                           ', %s' % limit_end if limit_end else ''))
        result = cur.fetchall()
        cur.close()
        return result

    def select_by_id(self, id_autonumeric):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM %s WHERE %s = :%s' % (self.table_name,
                                                    self.table_id,
                                                    self.table_id))
        result = cur.fetchone()
        cur.close()
        return result
        
    def delete(self, id_autonumeric):
        cur = self.con.cursor()
        cur.execute('DELETE FROM %s WHERE %s = :%s' % (self.table_name,
                                                  self.table_id,
                                                  self.table_id))
        result = cur.fetchone()
        cur.close()
        return result
        
    def query_insert(self, dict):
        # cur.lastrowid
        id = dict.pop(self.table_id, None)
        if not id:
            cols = dict.keys()  
            stmt = 'INSERT INTO %s (%s) VALUES (%s)' % (self.table_name,
                                                       ', '.join(cols),
                                                       ', '.join([":%s" % col for col in cols]))
            return stmt
    
    def query_update(self, dict):
        id = dict.pop(self.table_id, None)
        if id:
            cols = dict.keys()  
            stmt = 'UPDATE %s SET %s WHERE %s = :%s' % (self.table_name,
                                         ', '.join(["%s = :%s" % (col, col)  for col in cols]),
                                         self.table_id,
                                         self.table_id)
            dict[self.table_id] = id
            return stmt

        
if __name__ == "__main__":
    testDAO = DAO('tv')
    row = {'color':'red', 'number': 2}
    print testDAO.count()
    print testDAO.select_all()
    print testDAO.select_all(limit_ini=20)
    print testDAO.select_all('tv_id', 30, 50)
    print testDAO.query_select_by_id(4)
    print testDAO.query_insert(row)
    row[testDAO.table_id] = 2
    print testDAO.query_update(row)
    print testDAO.query_delete(4)
    print row

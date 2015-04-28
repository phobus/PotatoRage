#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Veeeery basic DAO. 
Based on INTEGER PRIMARY KEY AUTOINCREMENT for all tables
AUTOINCREMENT field is: table name + '_id'

don't try it at home, better take ORM
"""

import db

class DAO:
    def __init__(self, table_name):
        self.table_name = table_name
        self.table_id = table_name + '_id'
    
    def query_count(self):
        # with sqlite3.connect(db_filename) as conn:
        con = db.create_con()
        cur = con.cursor()
        
        cur.execute('SELECT count(*) total_results FROM %s' % self.table_name)
        
        result = cur.fetchall()
        return result[0]['total_results']
    
    def query_select_all(self, order_by=None, limit_ini=None, limit_end=None):
        return 'SELECT * FROM %s%s%s%s' % (self.table_name,
                                           ' ORDER BY %s' % order_by if order_by else '',
                                           ' LIMIT %s' % limit_ini if limit_ini else '',
                                           ', %s' % limit_end if limit_end else '')


    def query_select_by_id(self, id_autonumeric):
        return 'SELECT * FROM %s WHERE %s = :%s' % (self.table_name,
                                                    self.table_id,
                                                    self.table_id)
        
    def query_delete(self, id_autonumeric):
        return 'DELETE FROM %s WHERE %s = :%s' % (self.table_name,
                                                  self.table_id,
                                                  self.table_id)
        
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
    print testDAO.query_count()
    print testDAO.query_select_all()
    print testDAO.query_select_all(limit_ini=20)
    print testDAO.query_select_all('my_column', 30, 50)
    print testDAO.query_select_by_id(4)
    print testDAO.query_insert(row)
    row[testDAO.table_id] = 2
    print testDAO.query_update(row)
    print testDAO.query_delete(4)
    print row

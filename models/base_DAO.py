#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Veeeery basic DAO. 
Based on INTEGER PRIMARY KEY AUTOINCREMENT for all tables
AUTOINCREMENT field is: table name + '_id'

don't try it at home, better take ORM
"""
    
class DAO:
    def __init__(self, table_name):
        self.table_name = table_name
        self.table_id = table_name + '_id'
        
    def query_select_all(self):
        return 'SELECT * FROM %s' % self.table_name

    def query_select_by_id(self, id_autonumeric):
        return 'SELECT * FROM %s WHERE %s = :%s' % (self.table_name,
                                                    self.table_id,
                                                    self.table_id)
        
    def query_delete(self, id_autonumeric):
        return 'DELETE FROM %s WHERE %s = :%s' % (self.table_name,
                                                  self.table_id,
                                                  self.table_id)
        
    def query_insert(self, dict):
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
            stmt = 'UPDATE %s SET %s' % (self.table_name,
                                         ', '.join(["%s = :%s" % (col, col)  for col in cols]))
            dict[self.table_id] = id
            return stmt

        
if __name__ == "__main__":
    testDAO = DAO('test')
    print testDAO.query_select_all()
    print testDAO.query_select_by_id(4)
    print testDAO.query_insert({'color':'red', 'number': 2})
    print testDAO.query_delete(4)
    d = {testDAO.table_id:2, 'color':'red', 'number': 2}
    print testDAO.query_update(d)
    print d

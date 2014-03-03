#!/usr/bin/python2
# Filename: libsqlwrap.py
# coding=utf-8

import sqlite3

class sqlWrap():
    
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.conn.text_factory = str
        self.cursor = self.conn.cursor()
        self._database = database
        
    def insert(self, table, predata):
        # [predata]'s data-type: tuple
        sqlCommand = "INSERT INTO {0} VALUES {1};".format(table, str(predata))
        self.cursor.execute(sqlCommand)
        self.conn.commit()
        
    def update(self, table, column, predata, redata):
        sqlCommand = "UPDATE {0} SET {1} = '{3}' WHERE {1} = '{2}';".format(table, column, predata, redata)
        self.cursor.execute(sqlCommand)
        self.conn.commit()
        
    def delete(self, table, column, predata):
        sqlCommand = "DELETE FROM {0} WHERE {1} = '{2}';".format(table, column, predata)
        self.cursor.execute(sqlCommand)
        self.conn.commit()

    def query(self, table, column, predata):
        sqlCommand = "SELECT * FROM {0} WHERE {1} = '{2}';".format(table,column,predata)
        self.cursor.execute(sqlCommand)
        return self.cursor.fetchall()
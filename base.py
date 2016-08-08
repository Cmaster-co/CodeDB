#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Captain
# date: 2016-07-29

import json
import MySQLdb
import logging

from conf import mysql

class Base():
	db = None
	sql_where = ""
	sql_select = "*"
	def __init__(self):
		try:
			conn=MySQLdb.connect(host=mysql['host'],\
								user=mysql['user'],\
								passwd=mysql['passwd'],\
								db=mysql['db'],\
								port=mysql['port'])
		except Exception as e:
			print "ERROR: ",e
		
		print "conn database succeed!"
		self.db = conn


	def insert(self, table, data):
		try:
			cur = self.db.cursor()
			sql = "INSERT INTO " + str(table) + " ("
			values = ")VALUES("
			val = col = u''
			for k,v in data.items():
				col += k + ', '
				if type(v) == type(''):
					val += "'"+ str(v) + "', "
				else:
					val += v + ', '

			sql = sql + col[:-2] + values + val[:-2] + ")"

			print 'insert sql = ',str(sql)

			cur.execute(sql)
			self.db.commit()
			return True
		except Exception as e:
			print "ERROR: " + str(e)
			return False


	def update(self, table, data):
		try:
			cur = self.db.cursor()
			sql = "UPDATE " + str(table) + " SET"
			for k,v in data.items():
				if type(v) == type(''):
					sql += " %s = '%s'"%(k,v)
				else:
					sql += " %s = %s" %(k,v)
				sql += ","
			sql = sql[:-1]
			sql += str(self.sql_where)

			print 'update sql = ',sql

			cur.execute(sql)
			self.db.commit()
			return True
		except Exception as e:
			print "ERROR: " + str(e)
			return False
		finally:
			self.flush()



	def delete(self, table):
		try:
			cur = self.db.cursor()
			sql = "DELETE FROM " + table
			sql += self.sql_where

			print 'delete sql = ',sql

			cur.execute(sql)
			self.db.commit()
			return True
		except Exception as e:
			print "ERROR: " + str(e)
			return False
		finally:
			self.flush()


	def get_column(self,table):
		try:
			columns = []
			cur = self.db.cursor()
			if  self.sql_select == '*':
				sql = "SHOW COLUMNS FROM " + str(table)
				cur.execute(sql)
				col = cur.fetchall()
				for i in col:
					columns.append(i[0])
			else:
				columns = self.sql_select
				columns = columns.replace(' ','')
				columns = columns.split(',')
			
		except Exception as e:
			print "ERROR: ",e

		finally:
			return columns


	def get(self, table):
		try:
			result = []
			cur = self.db.cursor()
			
			print 'get db cursor succeed!'

			sql = "SELECT " + str(self.sql_select) + " FROM " + str(table) + str(self.sql_where)

			print 'select sql = ',str(sql)

			cur.execute(sql)
			self.db.commit()
			columns = self.get_column(table)

			for row in cur.fetchall():
				result.append(dict(zip(columns, row)))

		except Exception as e:
			print "ERROR: " + str(e)

		finally:
			self.flush()
			return result


	def select(self, column):
		self.sql_select = column


	def where(self, column, data):
		sql = " WHERE"
		if type(data) == type(''):
			sql += " %s = '%s'"%(column, data)
		else:
			sql += " %s = %s"%(column, data)
		self.sql_where = sql


	def flush(self):
		self.sql_where = ""
		self.sql_select = "*"


	def and_where(self, columns, data):
		pass


	def or_where(self, columns, data):
		pass


	def in_where(self, columns, data):
		pass


	def join():
		pass


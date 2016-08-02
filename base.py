#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Captain
# date: 2016-07-29

import json
import MySQLdb

from conf import host,user,passwd,db,port

class Base():
	database = None
	sql_where = ""
	sql_select = "*"

	def getdb():
		#get connection from MySQLdb
		conn=MySQLdb.connect(host=host,\
							user=user,\
							passwd=passwd,\
							db=db,\
							port=port)
		return conn


	def insert(self, table, data):
		try:
			cur = database.cursor()
			sql = "INSERT INTO " + table + " ("
			values = ")VAULES("
			val = col = u''
			for k,v in data.items():
				col += k + ', '
				if type(v) == type(''):
					val += "'"v + "', "
				else:
					val += v + ', '

			sql = sql + col[:-2] + values + val[:-2] + ")"
			cur.execute(sql)
			return True
		except e:
			print "ERROR: " + str(e)
			return False


	def update(self, table, data):
		try:
			cur = database.cursor()
			sql = "UPDATE " + table + " SET"
			for k,v in data.items():
				if type(v) == type(''):
					sql += " %s = '%s'"%(k,v)
				else:
					sql += " %s = %s" %(k,v)
				sql += ","
			sql = sql[:-1]
			sql += self.sql_where
			cur.execute(sql)
			return True
		except e:
			print "ERROR: " + str(e)
			return False
		finally:
			self.flush()



	def delete(self, table):
		try:
			cur = database.cursor()
			sql = "DELETE FROM " + table
			sql += self.sql_where
			cur.execute(sql)
			return True
		except e:
			print "ERROR: " + str(e)
			return False
		finally:
			self.flush()


	def get_column(table):
		try:
			columns = []
			cur = database.cursor()
			if  self.select == '*':
				sql = "SHOW COLUMNS FROM " + table
				cur.execute(sql)
				columns = cur.fetchone()
			else:
				columns = self.select
				columns = columns.replace(' ','')
				columns = columns.split(',')
		except:
			print "ERROR: "

		finally:
			return columns


	def get(self, table):
		try:
			cur = database.cursor()
			
			sql = "SELECT " + self.select + " FROM " + table + self.sql_where
			result = cur.execute(sql)

		except e:
			print "ERROR: " + str(e)

		finally:
			self.flush()



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


	def and_where():
		pass


	def or_where():
		pass


	def in_where():
		pass


	def join():
		pass


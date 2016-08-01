#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Captain
# date: 2016-07-29

import json
import MySQLdb

from conf import host,user,passwd,db,port

class Base():
	database = None

	def getdb():
		#get connection from MySQLdb
		conn=MySQLdb.connect(host=host,\
							user=user,\
							passwd=passwd,\
							db=db,\
							port=port)
		return conn


	def insert(table, data):
		try:
			cur=database.cursor()
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


	def update(table, data):
		pass

	def delete(table, data):
		pass

	def get(table):
		pass

	def select(column, data):
		pass

	def where(column, data):
		pass

	def flush():
		pass



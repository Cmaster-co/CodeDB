#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Captain
# date: 2016-07-29

import json
import MySQLdb

try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test',port=3306)
	cur=conn.cursor()
	cur.execute('select * from user')
	
	result=cur.fetchone()
	print result
	print 'ID: %s info %s' % result
 
	results=cur.fetchmany(5)
	for r in results:
 		print r
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
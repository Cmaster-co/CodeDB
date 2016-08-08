#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Captain
# date: 2016-07-29

import base

c = base.Base()

d = c.get('test')

for i in d:
	print i

e = {'name':'Mike', 'phone':'12345', 'address':'Canada'}

c.insert('test',e)

d = c.get('test')

for i in d:
	print i
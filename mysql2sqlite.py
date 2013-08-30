#!/bin/env python
#coding:utf-8

import os,time,stat
import web

mysqldb = web.database(dbn='mysql', db='asset', user='root', pw='xxxxxxxxx',host='10.10.99.214')
sqlitedb = web.database(dbn='sqlite', db='/home/liujianhei/codes/python/django/deploy-platform/mydata.db')

data = mysqldb.select('hostip', what="hostip.hostip, hostip.hostname, hostip.rack, hostip.mac, hostip.description, 'CentOS 6.3', hostip.hid, hostip.sn")
items = list(data)
dict = []
for item in items:
    dict += [{"ip": item['hostip'], "hostname": item['hostname'], "mac": item['mac'], "sn": item['sn'], "os": 'CentOS 6.3', "rack": item['rack'], "details": item['description']}]

sqlitedb.multiple_insert('itam_item', values=dict)

#! /usr/bin/python
# -*-coding:utf-8-*-

f = open(u'address.txt').readlines()
print len(f)
for i in range (0,len(f)):
    print f[i]


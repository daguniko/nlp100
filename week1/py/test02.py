#! /usr/bin/python
# -*-coding:utf-8-*-
#(2) タブ１文字につきスペース１文字に置換したもの．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

f = open(u'../data/address.txt').readlines()

for line in f:
    print line.expandtabs(1)

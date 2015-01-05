#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(31) このファイルを読み込み，単語をキーとして，品詞，活用形，基本形のタプルのリストを値とするマッピング型に格納せよ．プログラムの動作を確認するため，標準入力から読み込んだ単語の語彙項目を閲覧するプログラムを実装せよ．

f = open(u"../data/inflection_head.table.txt").readlines()

map = {"":"()"}

for line in f:
    line = line.split("|")
    map[line[0]] = (line[1],line[3],line[6])


print "辞書のKeyは以下のようになっています。"
print map.keys()
print "\n調べたいKeyを入力してください。"
input_line = raw_input()
print map[input_line]

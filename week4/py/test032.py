#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(32) (31)で読み込んだマッピング型オブジェクトを，marshalモジュールを使ってファイルに書き出せ．書き出したファイルを今後「辞書」と呼ぶ．
import marshal

f1 = open(u"../data/inflection_head.table.txt").readlines()
f2 = open(u"../data/mapfile","w")

map = {"":"()"}

for line in f1:
    line = line.split("|")
    map[line[0]] = (line[1],line[3],line[6])

marshal.dump(map,f2)





# print "辞書のKeyは以下のようになっています。"
# print map.keys()
# print "\n調べたいKeyを入力してください。"
# input_line = raw_input()
# print map[input_line]


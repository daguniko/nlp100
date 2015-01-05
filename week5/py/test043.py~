#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(42) 文章中に出現するすべての動詞を抜き出せ．

import MeCab
m = MeCab.Tagger("-Ochasen")
f = open(u"../data/japanese.txt").readlines()
dict = {}
sent = [[] for i in range(len(f))]

i = 0
verblist = []
print "ここまで"

for line in f:

    node = m.parseToNode(line)
    while node:
        print node.surface,node.feature
        spl = node.feature.split(",")
        dict = {"surface":node.surface, "base":spl[6],"pos":spl[0],"pos1":spl[1]}
        sent[i].append(dict)
        if spl[0] == "動詞":
            verblist.append(node.surface)
        node = node.next

    i = i + 1
    print line

for i in range(len(verblist)):
    print verblist[i]



#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(45) 文章中の「ＡのＢ」という表現（ＡとＢは名詞の１形態素）をすべて抜き出せ

import MeCab
m = MeCab.Tagger("-Ochasen")
f = open(u"../data/japanese.txt").readlines()
dict = {}
sent = [[] for i in range(len(f))]

i = 0
sverblist = []
print "ここまで"

for line in f:

    node = m.parseToNode(line)
    while node:
        print node.surface,node.feature
        spl = node.feature.split(",")
        dict = {"surface":node.surface, "base":spl[6],"pos":spl[0],"pos1":spl[1]}
        sent[i].append(dict)
        if spl[0] == "名詞":
            node2 = node.next
            spl2 = node2.feature.split(",")
            dict = {"surface":node2.surface, "base":spl2[6],"pos":spl2[0],"pos1":spl2[1]}

            if node2.surface == "の":
                node3 = node2.next
                spl3 = node3.feature.split(",")
                dict = {"surface":node3.surface, "base":spl3[6],"pos":spl3[0],"pos1":spl3[1]}
                if spl3[0] == "名詞":
                    sverblist.append(node.surface + node2.surface + node3.surface)

        node = node.next

    i = i + 1
    print line

for i in range(len(sverblist)):
    print sverblist[i]




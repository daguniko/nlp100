#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(65) 64のリストに含まれる名詞句に対し，その名詞句に係る文節・その名詞句が係る文節の単語（周辺単語と呼ぶ）を出力するプログラムを実装せよ．周辺単語は名詞，動詞，形容詞の基本形とせよ．出力形式は，"(名詞句)\t(方向) (周辺単語)"とし，名詞句に係る文節では「方向」を"<-"とし，名詞句が係る文節では「方向」を"->"とせよ．以降，「方向」と「周辺単語」を組み合わせたものを，名詞句の「文脈」と呼ぶ．
#regular expression part
import CaboCha
import os
import re
from collections import defaultdict

#set cabocha
c = CaboCha.Parser("-f1")
files = os.listdir("../data/cabocha/");
readfile = []
for file in files:
    if ".n" in file:
        continue
    elif "log.txt" in file:
        continue
    else:
        readfile.append(file)

import re

for file in readfile:
    f = open(u"../data/cabocha/" + file).readlines()
    for line in f:



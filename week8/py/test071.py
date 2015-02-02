#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(71) ５つのファイル（英語のテキスト）にGENIA taggerを適用せよ．GENIA taggerは１文１行形式の入力を受け取るので，22のプログラムを再利用せよ．また，入力ファイルはgzipで圧縮されていることに注意せよ．

import os,re
import sys
from collections import defaultdict

def read():
    files = os.listdir("../data/corpus")
    print files
    print sys.path
    sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/geniatagger_python-0.1-py2.7.egg")

def main():
    import geniatagger
    tagger = geniatagger.GeniaTagger("/Users/sudo/Tool/geniatagger")
    print "main"
    print tagger.parse("This is a pen")

# c = CaboCha.Parser("-f1")
# files = os.listdir("../data/cabocha/");
# readfile = []
# for file in files:
#     if ".n" in file:
#         continue
#     elif "log.txt" in file:
#         continue
#     else:
#         readfile.append(file)

# import re

# for file in readfile:
#     f = open(u"../data/cabocha/" + file).readlines()
#     for line in f:





if __name__ == "__main__":
    read()
    main()

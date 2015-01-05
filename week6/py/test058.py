#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(58) 係り元が２つ以上ある文節に対し，その文節とすべての係り元を表示せよ．

from test054 import *

def test58_morph(all_sent_list):
    print all_sent_list
    for one_sent_list in all_sent_list:
        for one_chunk in one_sent_list:
            for another_chunk in one_sent_list:
                if one_chunk.num == another_chunk.dst:
                    print another_chunk.morphs_add + "\t" + one_chunk.morphs_add


if __name__ == '__main__':
	all_sent_list=test54_morph("../data/cabocha_japanese.txt")
	test58_morph(all_sent_list)

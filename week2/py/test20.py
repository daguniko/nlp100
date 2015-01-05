#! /usr/bin/python
# -*-coding:utf-8-*-
#(20) ツイートから絵文字らしき文字列を抽出せよ．

import re

f = open(u"../data/tweet.txt").readlines()
#for emoji
emoji = re.compile(ur"[\uE000-\uF8FF]")
 
#for kaomoji
kaomoji = re.compile(r"\([^一-龠 ぁ-ん ァ-ヴ 1-9]{2,5}\)")


for line in f:
    match = emoji.search(line)
    if match:
        print match.group()
    match = kaomoji.search(line)
    if match:
        print match.group()

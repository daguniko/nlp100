#! /usr/bin/python
# -*-coding:utf-8-*-
#(15) ツイッターのユーザー名（例えば@xxxxxxx）を，そのユーザーのページへのリンク（<a href="https://twitter.com/#!/xxxxxxx">@xxxxxxx</a>で囲まれたHTML断片）に置換せよ．

import re

f = open(u"../data/tweet.txt").readlines()

for line in f:
    match = re.search("@.{1,15}[:|\s]",line)
    if match:
        a = match.group()
        if a.find(":") >= 0:
            a = a.replace(":","")
        a = a.split()
        print '<a href="https://twitter.com/#!/%s">' %(str(a[0])) + str(a[0]) + "</a>"


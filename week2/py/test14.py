#! /usr/bin/python
# -*-coding:utf-8-*-
#(14) ツイッターのユーザー名（@で始まる文字列）を抽出せよ．

f = open('../data/tweet.txt').readlines()

# implementation by using regular expression
import re
sr = re.compile("@.{1,15}(:|\s)")

for line in f:
    match = sr.search(line)
    if match:
        a = match.group()
        if a.find(":") >= 0:
            a = a.replace(":","")
        a = a.split()
        print a[0]


# #improve problem
# namelist = []
# for line in f:
#     match = re.search("@.{1,15}[:|\s]",line)
#     if match:
#         a = match.group()
#         if a.find(":") >= 0:
#             a = a.replace(":","")
#         a = a.split()
#         namelist.append(a[0])

# #from collections import Counter
# print namelist
# from collections import Counter

# counter = Counter(namelist)
# for word, cnt in counter.most_common():
#     if cnt > 1 :
#         aiu = word + "\t" + str(cnt)
#         print aiu


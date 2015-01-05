#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-

from collections import Counter
s1 = u"すもももももももものうち"

# countしたい情報をCounterの引数に入れる
count = Counter(s1)

# countの中にはカウンターの情報のリストがオブジェクトで入ってる
print count

# itemsの中にはkeyと値が入ってる
for k,v in count.items():
    print k,v

# keysの中にはkeyが入ってる
for i in count.keys():
    print i

# valuesの中にはcountしたvalueが入ってる
for i in count.values():
    print i

# most_commonの中にはValueの多い順番から入ってる
z = count.most_common()
print z

# most_common(1)に入ってる情報
print z[1][0],
print z[1][1]

# lambda関数の使い方
print sorted(z,key = lambda x:x[1],reverse = True)


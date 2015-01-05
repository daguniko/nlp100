#!/bin/bash
# (1) 行数をカウントしたもの．確認にはwcコマンドを用いよ．

a=`cat ../data/address.txt | wc -l`
echo ${a}

#!/bin/bash

echo "3回目の小テストの点数(0から20までの数字)を入れてください。"
read num

if [ "$num" -ge 0 -a "$num" -lt 7 ]
then
    echo "もっと勉強しましょう"
elif [ "$num" -ge 7 -a "$num" -lt 15 ]
then
    echo "まずまずです"
elif [ "$num" -ge 15 -a "$num" -le 20 ]
then
    echo "よくがんばりました"
else
    echo "入力した数字は0から20までの数字ではありません"
fi

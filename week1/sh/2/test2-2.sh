#!/bin/bash

echo "好きな整数を入れてください"
read num

if [ "$num" -lt 100 ]
then
    echo "$numは100未満です"
elif [ "$num" -lt 1000 ]
then
    echo "$numは100以上1000未満です"
else
    echo "$numは1000以上です"
fi
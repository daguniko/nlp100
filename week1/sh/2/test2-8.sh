#!/bin/bash

num=$RANDOM

echo "隠された値を当ててください"

while true
do
    echo "0から32767までの値を入力してください"
    read x
    if [ $x -gt $num ]
    then
	echo "もっと小さいです"
    elif [ $x -lt $num ]
    then
	echo "もっと大きいです"
    else
	echo "ずばりあたりです"
	break

    fi
done

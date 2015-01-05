#!/bin/bash

num=3
while [ "$num" -lt 10 ]
do
    echo '${num}'"の値は$num"
    num=`expr $num + 1`
done
#!/bin/bash

year1=`date +%Y`

year2=`expr ${year1} + 10`

echo -e "現在${year1}年です。\n10年後は${year2}年です。"
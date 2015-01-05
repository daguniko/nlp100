#!/bin/bash

echo "リテラシーの先生の名前をローマ字で入力してください"
read name

if [ "$name" = "suzuki" -o "$name" = "doi" ]
then
    echo "あなたはAクラスの学生です"
elif [ "$name" = "susaki" -o "$name" = "oshiro" -o "$name" = "oshiro" ]
then
    echo "あなたはBクラスの学生です"
elif [ "$name" = "yamaga" -o "$name" = "shinoara" ]
then
    echo "あなたはCクラスの学生です"
else
    echo "入力ミスか、入力した名前の先生はいません。"
fi


#!/bin/bash

echo "リテラシーの先生の名前をローマ字で入力してください"
if [ "$1" = "" ]
then
    echo "先生の名前を引数として入力してください"
elif [ "$1" = "suzuki" -o "$1" = "doi" ]
then
    echo "あなたはAクラスの学生です"
elif [ "$1" = "susaki" -o "$1" = "oshiro" -o "$1" = "oshiro" ]
then
    echo "あなたはBクラスの学生です"
elif [ "$1" = "yamaga" -o "$1" = "shinoara" ]
then
    echo "あなたはCクラスの学生です"
else
    echo "入力ミスか、入力した名前の先生はいません。"
fi


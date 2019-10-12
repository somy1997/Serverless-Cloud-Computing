#!/bin/bash -xe

python3 oracle.py $1 $2 -pp statsServerMumbai/$3_post.csv cwlogsServerMumbai/$3_post.txt
python3 oracle.py $1 $2 -pg statsServerMumbai/$3_get.csv cwlogsServerMumbai/$3_get.txt
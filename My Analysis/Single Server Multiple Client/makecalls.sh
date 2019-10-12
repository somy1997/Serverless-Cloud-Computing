#!/bin/bash -xe

python3 oracle.py $1 $2 -mp $4_post.csv https://7yx9o87rrh.execute-api.ap-south-1.amazonaws.com/test/postcustomerdetails -v -g $3
python3 oracle.py $1 $2 -mg $4_get.csv https://7yx9o87rrh.execute-api.ap-south-1.amazonaws.com/test/getcustomerdetails -v
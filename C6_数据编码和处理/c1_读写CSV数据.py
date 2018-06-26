# 问题: 想读写一个csv格式的文件

import csv
with open('002494.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    i = 0
    for row in f_csv:
        print(row)
        i += 1
        if i >= 3:
            break

# 一种用
from collections import namedtuple
with open('002494.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        
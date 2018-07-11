# 问题: 有一个字典或者实例的序列, 想根据某个特定的字段来分组迭代访问
# 解决方案: itertools.groupby()

rows = [
    {'address':'5412 N CLARK', 'date':'07/01/2012'},
    {'address':'5418 N CLARK', 'date':'07/04/2012'},
    {'address':'5800 N CLARK', 'date':'07/02/2012'},
    {'address':'2122 N CLARK', 'date':'07/03/2012'},
    {'address':'5645 N CLARK', 'date':'07/02/2012'},
    {'address':'1060 N CLARK', 'date':'07/01/2012'},
    {'address':'1039 N CLARK', 'date':'07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

# 先用itemgetter进行排序
rows.sort(key=itemgetter('date')) 
# 要用groupby一定要事先排序, 否则无法准确分组
# 分组迭代, groupby返回一个值和一个迭代器对象
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

print('-'*100)
# 如果仅仅想根据date字段将数据分组, 那么还可以使用defaultdict()构建多值字典
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

# print(rows_by_date)
for key, value in rows_by_date.items():
    print(key)
    print(value)
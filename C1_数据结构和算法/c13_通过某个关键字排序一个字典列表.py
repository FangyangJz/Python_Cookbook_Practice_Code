# 问题: 有一个字典列表, 想根据某个或某几个字典字段来排序这个列表
# 解决方案: operator模块的itemgetter函数

rows = [
    {'fname':'Brian', 'lname':'Jones', 'uid':1003},
    {'fname':'David', 'lname':'Beazley', 'uid':1002},
    {'fname':'John', 'lname':'Cleese', 'uid':1001},
    {'fname':'Big', 'lname':'Jones', 'uid':1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

print('-' *100)
# itemgetter 也支持多个keys
# 参数 key 也可以是lambda表达式,
# 比如: key=lambda r: r['fname'] 或者 key=lambda r: (r['lname'], r['fname'])
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

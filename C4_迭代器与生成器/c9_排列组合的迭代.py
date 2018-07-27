# 问题: 想迭代遍历一个集合中元素的所有可能的排列或组合
# 解决方案: 1. itertools.permutations 得到排列
#           2. itertools.combinations 单次得到组合 
#           3. itertools.combinations_with_replacement 允许同一个元素被选择多次

from itertools import permutations, combinations, combinations_with_replacement

items = ['a','b','c']
for p in permutations(items):
    print(p)

# 如果想指定长度的所有排列
for p in permutations(items, 2):
    print(p)

print('='*50)
for c in combinations(items,1):
    print(c)
for c in combinations(items,3):
    print(c)

print('-'*50)
for c in combinations_with_replacement(items, 3):
    print(c)

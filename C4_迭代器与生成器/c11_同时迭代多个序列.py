# 问题: 想同时迭代多个序列, 每次分别从一个序列中取出一个元素
# 解决方案: zip, zip_longest

from itertools import zip_longest

a = [1 ,5, 4, 2]
b = [11,22,33,44,55,66]

for x, y in zip(a, b):  # zip返回的是个迭代器
    print(x, y)

for i in zip(a, b):
    print(i)

for i in zip_longest(a, b):
    print(i)
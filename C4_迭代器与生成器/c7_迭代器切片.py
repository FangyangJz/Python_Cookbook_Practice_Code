# 问题: 想得到一个由迭代器生成的切片对象
# 解决方案: itertools.islice()

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
# c[10:20]  # TypeError: 'generator' object is not subscriptable
from itertools import islice
for x in islice(c, 10, 20, 2):
    print(x)

# 需要认识到 迭代器 是不可逆的
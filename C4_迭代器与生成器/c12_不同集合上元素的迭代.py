# 问题: 想在多个对象执行相同操作, 但是这些对象在不同的容器中
# 解决方案: itertools.chain

from itertools import chain

a = [1,2,3]
b = ['a','n','c']
# chain不会创建新的序列, 所以非常省内存
for x in chain(a,b):
    print(x)
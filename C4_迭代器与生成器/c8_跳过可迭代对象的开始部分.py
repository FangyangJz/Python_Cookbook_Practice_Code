# 问题: 想遍历一个可迭代对象, 但是开始的一些元素想跳过去
# 解决方案: itertools.dropwhile

from itertools import dropwhile

# 使用dropwhile没有达到预期效果?????????????
# with open('skip.txt', encoding='utf-8') as f:
# with open('skip.txt') as f:
#     # for line in f:
#     #     print(line, type(line))

#     for line in dropwhile(lambda line: line.startswith('#'), f):
#         print(line, end='')

# 如果知道要跳过的元素个数, 可以用itertools.islice
from itertools import islice

items = [x for x in 'abc1405']
print(items)
for x in islice(items, 3, None): # None 表示3到最后相当于 -1
    print(x)
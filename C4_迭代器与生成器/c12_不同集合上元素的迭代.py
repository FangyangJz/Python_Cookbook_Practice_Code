# 问题: 想在多个对象执行相同操作, 但是这些对象在不同的容器中
# 解决方案: itertools.chain

from itertools import chain

a = [1,2,3]
b = ['a','n','c']
# chain不会创建新的序列, 所以非常省内存
for x in chain(a,b):  # 这个会保留原来的顺序
    print(x)

# with open('file1','rt') as file1,\
#     open('file2','rt') as file2,\
#     open('file3','rt') as file3:

#     for line in heapq.merge(file1, file2):
#         file3.write(line)


# heapq.merge()需要所有输入序列必须是排序过的,
# 它仅仅是检查所有序列的开始部分并返回最小的那个
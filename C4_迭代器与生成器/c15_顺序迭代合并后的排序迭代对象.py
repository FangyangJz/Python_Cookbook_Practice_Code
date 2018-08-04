# 问题: 有一些列排序序列, 想将它们合并后得到一个序列并在上面迭代遍历
# 解决方案: heapq.merge

import heapq

a = [1,4,5,10]
b = [2,6,11,12]
for c in heapq.merge(a,b): # 这个会混合排序
    print(c)
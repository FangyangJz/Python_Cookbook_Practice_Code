# 问题 : 实现一个按优先级排序的队列, pop操作总是返回优先级最高的元素
# 解决方案 : heapq模块. heap堆()的数据结构有点像栈, push进去的, pop出来
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, )

    
# 问题 : 实现一个按优先级排序的队列, pop操作总是返回优先级最高的元素
# 解决方案 : heapq模块. heap堆()的数据结构有点像栈, push进去的, pop出来
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

pq = PriorityQueue()
pq.push(Item('foo'), 1)
pq.push(Item('Bar'), 5)
pq.push(Item('spam'), 4)
pq.push(Item('grok'), 1)

print(pq.pop())
print(pq.pop())
print(pq.pop())   # 优先级相同的按照插入顺序返回
print(pq.pop())

# 还可以比较大小
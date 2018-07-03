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

pq = PriorityQueue()
pq.push(2, 10)
pq.push(3, 11)
pq.push(0, 8)
pq.push(-1, 7)
pq.push(4, -5)
print(pq._queue, pq._index)
print(pq.pop())   # 把[(-11,1,3),....] 弹出来, 然后返回(-11,1,3)[-1]的元素
print(pq._queue, pq._index)

# 延伸
# 堆作为数据结构在内存和二级缓存中充当了重要的角色。优先队列中也会经常使用堆，
# 这也就给堆数据结构提出了很多挑战。例如内存中存放了数多个计划任务的时候,
# 我们可以定义一个数列list（priority,task）来保存在堆结构中。但是这样就出现了很多问题 
# 1.排序的稳定性:当任务加入到堆中时，如果两个任务有同等的优先级，两个任务实际上在列表里是没什么区别的，那我怎么得到返回值？ 
# 2.在Python3以后的版本中，如果元组(priority,task)priority是一样的，
#   而且task没有一个默认的比较参照值，那这样我们其实是没有办法来比较的。 
# 3.如果一个任务的优先级发生了改变，那么我们如何来处理该任务在相应堆中优先级的变化，堆中位置肯定会改变。 
# 4.如果一个任务因为要等待其他的任务(最简单的比方，等待父进程)而照成悬挂状态，
#   我们如何在堆中去找到它并且做相应的操作(降低优先级或者删除该任务)

# 解决前两个问题的方法我们可以采用三元数组的方法。设置一个优先级，一个条目值，一个任务值。
# 即使当两个任务有相同优先级的时候，因为条目值不一样可以帮助cpu来裁决它们被加载的顺序。 
# 剩下需要解决的问题是如何找到被悬挂而推迟的任务，然后尝试去修改优先级或者永久删除这个任务。
# 我们可以使用字典，来指向堆中某个任务的条目值。 
# 最后就是删除操作，删除会改变堆的结构。为了保证堆结构的特性，
# 我们可以标记已有将被删除的任务的条目值，然后将该任务重新打标加入到堆中。

# pq = []                         # list of entries arranged in a heap
# entry_finder = {}               # mapping of tasks to entries
# REMOVED = '<removed-task>'      # placeholder for a removed task
# counter = itertools.count()     # unique sequence count

# def add_task(task, priority=0):
#     'Add a new task or update the priority of an existing task'
#     if task in entry_finder:
#         remove_task(task)
#     count = next(counter)
#     entry = [priority, count, task]
#     entry_finder[task] = entry
#     heappush(pq, entry)

# def remove_task(task):
#     'Mark an existing task as REMOVED.  Raise KeyError if not found.'
#     entry = entry_finder.pop(task)
#     entry[-1] = REMOVED

# def pop_task():
#     'Remove and return the lowest priority task. Raise KeyError if empty.'
#     while pq:
#         priority, count, task = heappop(pq)
#         if task is not REMOVED:
#             del entry_finder[task]
#             return task
#     raise KeyError('pop from an empty priority queue') 
# 问题 : 怎样从一个集合中获得最大或者最小的N个元素列表?
# 解决方案: heapq模块的两个函数 nlargest() 和 nsmallest()
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(5, nums))

portfolio = [
    {'name':'IBM', 'shares':100, 'price':91.1},
    {'name':'AAPL', 'shares':50, 'price':532.1},
    {'name':'FB', 'shares':200, 'price':21.1},
    {'name':'HPQ', 'shares':35, 'price':31.1},
    {'name':'YHOO', 'shares':45, 'price':16.1},
    {'name':'ACME', 'shares':75, 'price':115.1},
]
print('---------------------------------------')
# 以 price 作为比较对象
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)
print('---------------------------------------')

# 性能好, 底层的堆排序
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heapq.heapify(nums)
print(nums)
# heappop 弹出来的是 heapq[0] 最小值
print(heapq.heappop(nums))
heapq.heappush(nums,-10)
print(nums)

#######################################3
# 1. 查找元素个数比较小用 heapq.nlargest() 比较好
# 2. 查找1个元素的时候, min() 和 max() 好
# 3. 查找元素个数 N 接近整个序列长度时, 
#    先排序, sorted(items)[:N] 或 sorted(items)[-N:]

# 让原本不兼容的代码可以一起工作
# 计算两点间的距离
import math
from functools import partial

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)

# 假设现在有个基点, 根据点与基点之间的距离来排序所有的这些点
# sort()只可以接受一个关键字参数, 通过partial来解决这个问题
pt = (4, 3)

# points.sort(key=partial(distance, pt)) # 这行和下面效果一样
r = sorted(points, key=partial(distance, pt))
print(r)

print(points)

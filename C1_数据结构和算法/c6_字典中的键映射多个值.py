# 问题 : 怎么实现一个键对应多个值的 dict? multidict
# 解决方案:
# 1. 将多个值放在其他容器中, 比如 [], {}
#    列表可以保证插入顺序, 集合可以去重
# 2. collections.defaultdict

from collections import defaultdict
d1 = defaultdict(list)
d1['a'].append(1)
d1['a'].append(2)
d1['b'].append(4)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)      # 注意set用add , list 用append
d2['a'].add(2)
d2['b'].add(5)

print(d1, d2)

#########################################
# defaultdict 会自动创建key,即使没有指定
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', {1,}).add(5)   # 集合{}不能为空,会报错
d.setdefault('b', {}).add(6)
d.setdefault('b', {}).add(6)
print(d)

########################################
# defaultdict 在初始化值的时候代码非常简单
pairs = [(1,2), (3,4), (5,6)]
dd = defaultdict(list)
for key, value in pairs:
    dd[key].append(value)
print(dd)
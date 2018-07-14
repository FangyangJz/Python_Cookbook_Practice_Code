# 问题: 现在有多个字典或映射, 想将它们从逻辑上合并为一个单一的映射后执行某些操作,
#       比如查找值或检查某些键是否存在
# 解决方案: collections 模块中的 ChainMap

from collections import ChainMap

a = {'x':1, 'z':3}
b = {'y':1, 'z':4}
c = ChainMap(a, b)
print(c)
print(c['z'])
# ChainMap类只是在内部创建了一个容纳这些字典的列表
# 并重新定义了一些常见的字典操作来遍历这个列表, 
# 大部分字典操作可用
print('len(c) is ', len(c))
print(list(c.keys()))
print(list(c.values()))
# 如果出现重复的键, 那么只会出现第一次出现的映射值

##############################################################
print('#'*100)
# ChainMap 的 new_child() 和 parents
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
print('-'*100)
#############################  左子, 右父
# Discard last mapping
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
###############################
# ChainMap对象 在原字典数据修改后, 数据也变化了, 
# dict.update的数据相当于copy出一个新字典, 原数据变化, 新字典不变
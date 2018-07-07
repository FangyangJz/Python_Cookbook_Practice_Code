# 问题: 想创建一个字典, 并且在迭代或序列化这个字典的时候能够控制元素顺序
# 解决方案: collections 模块中的 Orderdict 类
# 注意: Orderdict 是一个双向链表结构, 大小是普通字典的2倍, 数据量过大的时候要考虑内存开销

from collections import OrderedDict
import json

def ordered_dict():
    d = OrderedDict()
    # 按照插入元素的顺序来排序字典
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])
    return d

if __name__ == '__main__':
    d = ordered_dict()
    x = json.dumps(d)
    print(x, type(x))
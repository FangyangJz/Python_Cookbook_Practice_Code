# 问题: 想构建一个能支持迭代操作的自定义对象, 并希望找到一个能实现迭代协议的简单方法
# 解决方案: 

class Node:
    '''实现一个以深度优先方式遍历树形节点的生成器'''
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    
    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
    # python的迭代协议要求一个__iter__()方法返回一个特殊的迭代器对象
    # 这个迭代器对象实现了__next__()方法并通过StopIteration异常标识迭代的完成
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
    # yield from iterable本质上等于for item in iterable: yield item的缩写版
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
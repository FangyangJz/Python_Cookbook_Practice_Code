# 问题: 你构建了一个自定义的容器对象,你想直接在你的这个新容器上执行迭代操作
# 解决方案: __iter__()方法

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    
    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
        # iter(s) 等效于 s.__iter__()
        # 和 len(s) 等效于 s.__len__() 一样
        return iter(self._children)  # 函数里面是个list, iter([list])返回一个生成器

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)
# 问题: 你想改变对象实例的打印或显示输出, 让它们更具可读性
# 解决方案: 重构__str__(self) 和 __repr__(self)方法

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):   # 决定 ipython 交互式返回的结果
        return 'Pair({0.x!r}, {0.y!r})'.format(self)  # !r指明输出使用__repr__()来代替默认的__str__()
        # return 'Pair(%r, %r)' % (self.x, self.y) 上面的代码等价于这句

    def __str__(self):   # 决定 返回的结果, 转成一个字符串, 和print结果一样
        return '({0.x!s}, {0.y!s})'.format(self)  # {0.x} 代表第一个参数的x属性

p = Pair(3, 4)
print(p)
print(p.__str__())
print(p.__repr__())
# 问题: 有一个被其他python代码使用的callable对象, 可能是一个回调函数或处理器
#       但是参数太多了, 导致调用时出错
# 解决方案: functools.partial() 固定函数的某些参数, 然后返回一个新的callable对象,
#          新的callable接受未赋值的参数, 然后和之前固定的参数合并起来, 
#          将所有参数传递给原始函数

from functools import partial

def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam, 1)
s1(2,3,4)

s2 = partial(spam, d=43)
s2(1,2,3)

s3 = partial(spam, 1, 2, d=42)
s3(10)

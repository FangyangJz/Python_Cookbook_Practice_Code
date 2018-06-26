# 问题: 你写了一个装饰器作用在某个函数上, 
#      但是这个函数的重要的元信息比如:名字\文档字符串\注解和参数签名都丢失了
# 解决方案: functools 库中的 @wraps(func)
import time
from functools import wraps

def timethis(func):
    @wraps(func)   # 就这个!!!!!!
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):   # 参数:类型 , 是 Python 3.5 增加的，用于描述参数的类型
    '''Function description doc'''
    print('I am countdown func')
    while n > 0:
        n -= 1

countdown(100000)
print(countdown.__name__)  # 有functools里的 @wraps(func)挡着, 结果是countdown
# 注释掉 @wraps(func)后, 结果变成 wrapper
print(countdown.__annotations__) # 这些都是函数的元信息
print(countdown.__doc__)

################################################
# @wraps 还有一个重要的功能, 它可以让你通过属性 __wrapped__直接访问被包装的函数
countdown.__wrapped__(10000)
################################################
# __wrapped__ 属性还能让被装饰函数正确暴露底层的参数签名信息
from inspect import signature
print(signature(countdown))


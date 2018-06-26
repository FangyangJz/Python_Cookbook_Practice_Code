# 问题: 想在函数上添加一个包装器, 增加额外的操作处理(比如日志, 计时等)
# 解决方案: 如果想使用额外的代码包装一个函数, 可以定义一个装饰器函数
import time
from functools import wraps

'''
Python 中使用装饰器对在运行期对函数进行一些外部功能的扩展。
但是在使用过程中，由于装饰器的加入导致解释器认为函数本身发生了改变，
在某些情况下——比如测试时——会导致一些问题。
Python 通过 functool.wraps 为我们解决了这个问题：
在编写装饰器时，在实现前加入 @functools.wraps(func) 可以保证装饰器不会对被装饰函数造成影响。
'''
# 下节详细讲 functools 里面的 warps(func)

def timethis(func):
    '''Decorator that reports the execution time'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis  # 相当于 countdown = timethis(countdown)
def countdown(n):
    while n > 0:
        n -= 1

countdown(10000000)

#######################################################
class A:
    @classmethod
    def method(cls):
        pass
# ============================
# 下面这种内置方法(@classmethod, @property, @staticmethod)
# 和上面等价
class B:
    def method(cls):
        pass
    method = classmethod(method)
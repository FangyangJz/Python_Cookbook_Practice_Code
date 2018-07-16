# 问题: 想定义一个函数或者方法, 他的一个或多个参数是可选的并且有一个默认值
# 解决方案: 参数默认值就 param=10 这样指定就可以了,
#          可修改的容器就 param=None 就行了

# 如果并不想提供一个默认值, 仅想测试下某个默认参数是否有传递进来
_no_value = object()
def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    return '------'
# 不传和传None是有区别的
print(spam(1,2))
print(spam(1,None))
print(spam(1))

print('='*100)
# 默认参数的值仅仅在函数定义的时候赋值一次
x = 42
def spam(a, b=x):
    return a, b

print(spam(1))
x = 23
print(spam(1))

# ! 注意 ! 默认参数一定是不可变对象, 比如None, True, False,数字或字符串
# def spam(a, b=[]):   这种写法是错误的

# 再一个注意! None 和 False 不一样, 
# 判断None 要用 if xxx is None:
# 判断False 用 if not xxx:  
# None 和 空列表\字符串\元组\字典等都相当于 False

# 问题: 用lambda定义了一个匿名函数, 想在定义时捕获到某些变量的值
# 解决方案:

# 注意! lambda 和 函数参数默认值的区别
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
# 1. 函数的参数默认值 def add(aa, bb=x) 在第一次定义函数的时候就固定了,
#    后面即使改变了x, bb依旧是原来的值
# 2. 而lambda表达式不同, x发生变化, 调用代表着lambda表达式的函数看到x是啥, 就用啥
print(a(10), b(10))

# 如果希望lambda表达式定义的匿名函数在定义时就捕获到值, 可以将参数定义成默认参数
x = 10 
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10), b(10))

######################################################################
# 上面所说的还可以通过一个例子来看下
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0), end=' ')  # 因为没有指定默认参数赋值, 最后lambda里的n都是4

print('\n-----------------')
# 正确写法
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0), end=' ')
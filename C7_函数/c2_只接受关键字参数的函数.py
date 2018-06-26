# 问题 : 希望函数的某些参数强制使用关键字参数传递
# 解决方式: 将强制关键字参数放到某个*参数
def recv(max, *, block):  # 如果block没有block=参数赋值, 就会报错
    pass

# recv(1024, True)
recv(1024, block=True)

# 利用这种技术, 我们还能在接收任意多个位置参数的函数中, 指定关键字参数
def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m
print(mininum(1,5,2,-5,10))
print(mininum(1,5,2,-5,10, clip=0))
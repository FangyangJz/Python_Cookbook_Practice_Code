# 问题: 想从一个序列中随机抽取若干元素, 或者想生成几个随机数
# 解决方案: 
#   random.seed()  初始化种子
#   random.choice() 抽1个
#   random.sample(values, 3) 抽3个
#   random.shuffle(values) 打乱顺序
#   random.randint(start, stop)  随机生成1个int
#   random.random()   随机生成0~1范围内均匀分布的1个浮点数
#   random.getrandbits(10)  获取10位(二进制, 十进制1024)随机整数
#   random.uniform()  计算均匀分布随机数
#   random.gauss()   计算正态分布随机数

#  注意! random模块的函数不应该用在和密码学相关的程序中, 
#  如果需要, 使用ssl模块中的相应函数, ssl.RAND_bytes()可以生成1个安全的随机字节序列

import random
import ssl

values = [1,2,3,4,5,6]
print(random.choice(values))
print(random.sample(values, 3))

random.shuffle(values)
print(values)
print(random.randint(0, 10))
print(random.random())
print(random.getrandbits(10))
print(ssl.RAND_bytes(4))
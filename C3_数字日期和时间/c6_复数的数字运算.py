# 问题: 需要用复数
# 解决方案: complex(real, image) 或者 带有后缀j的浮点数

a = complex(2, 4)
b = 3 - 5j

print(a, b, type(a), type(b))
print(a.imag, b.imag, a.real, b.real)
print(a.conjugate())
print(abs(a))

print('-'*100)
# 用 cmath 进行数学计算
import cmath
print(cmath.sin(a))
print(cmath.exp(a))

print('='*100)
# 用 numpy 也可以处理复数
import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a+2)
print(np.sin(a))

# python 的 math 模块无法产生复数值
# import math
# math.sqrt(-1)   # 报错
#
# cmath模块可以
import cmath
print(cmath.sqrt(-1)) 

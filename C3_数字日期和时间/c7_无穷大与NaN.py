# 问题: 想创建或测试正无穷, 负无穷 或 NaN(非数字) 的浮点数
# 解决方案: float()
# sign           ::=  "+" | "-"
# infinity       ::=  "Infinity" | "inf"
# nan            ::=  "nan"

import math

a = float('inf')
b = float('-inf')
c = float('nan')
# 用math.isinf() 和 math.isnan()来测试这些值确实存在
print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))

print('-'*100)
# 关于inf的传播
print('inf + 45 : ', a + 45)
print('inf * 45 : ', a * 45)
print('10 / inf : ', 10 / a)
print('inf - inf :', a + b)
print('inf / inf :', a / a)

print('='*100)
# 关于nan的传播
print('nan + 23 : ', c + 23)
print('nan / 2 : ', c / 2)
print('nan * 2 : ', c * 2)
print('math.sqrt(nan) : ', math.sqrt(c))
d = float('nan')
print('nan == nan : ', c == d)
print('nan is nan : ', c is d)
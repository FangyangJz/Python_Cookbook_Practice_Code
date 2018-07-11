# 问题: 需要用分数计算
# 解决方案: fractions模块

from fractions import Fraction
a = Fraction(8, 6)
b = Fraction(7, 16)
c = Fraction(1, 2)
print(a + b)
print(a * b)
print(4 ** c)
print(b.numerator, b.denominator)
# convert to float
print(c, float(c))
x = b.limit_denominator(18) # 找到c最接近的分数
print(x)
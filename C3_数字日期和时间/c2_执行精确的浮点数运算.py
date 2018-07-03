# 问题: 需要对浮点数执行精确的计算操作, 不希望出现任何小误差
# 解决方案: decimal模块
from decimal import Decimal

a = 4.2
b = 2.1
print(a+b)

a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)

# 控制计算结果, 可以用decimal模块中的localcontext
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3  # 可以指定任意长度,比如100位小数
    print(a/b)

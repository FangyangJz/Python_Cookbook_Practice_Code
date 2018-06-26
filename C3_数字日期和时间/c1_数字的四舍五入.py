a = 3.141592653
x = round(a, 2)
print(x)

# 边界值1.5 , round返回离他最近的偶数
a = 1.5
print(round(a))

# round() 参数为负数, 舍入作用在十位百位千位
a = 16843
print(round(a, -1))
print(round(a, -3))

# 注意区分 format(限) 和 round(舍)
x = 1.23456
print(format(x, '0.2f'))
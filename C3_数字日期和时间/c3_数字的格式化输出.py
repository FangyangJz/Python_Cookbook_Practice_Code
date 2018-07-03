# 问题: 需要将数字格式化后输出
# 解决方案: format

x = 1234.56789
print(format(x, '0.2f'))   # 不固定长度, 2位小数浮点数
print(format(x, '>10.1f')) # 固定10位chars, 右对齐, 1位小数浮点数
print(format(x, '<10.1f')) # 左对齐
print(format(x, '^10.1f')) # 居中对齐
print(format(x, ','))      # 千分位用,
print(format(x, '0,.1f'))
print(format(x, 'e'))
print(format(x, '0.2E'))

print('The value is {:0,.2f}'.format(x))  # 这个和line 10 代码有不同, 不加:会报错
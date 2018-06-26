# 包含N个元素的元组或序列,怎样解压后同时赋值给N个变量?
# 不报错的前提 : 变量数和元素数一致
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)
name, shares, price, (year, mon, day) = data
print(name, shares, price, year, mon, day)

# 只想解压一部分的, 可以用占位符来代替要丢弃的值
_, shares, price, _ = data
print(shares, price)

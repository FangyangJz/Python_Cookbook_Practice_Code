
print("ACME", 50, 91.5)
print("ACME", 50, 91.5, sep=',')
print("ACME", 50, 91.5, sep='', end='!!\n')
print('-'*50)

# 用end参数禁止换行
for i in range(5):
    print(i)
for i in range(5):
    print(i, end=' ')

# 除了用sep参数指定分割符号, 还可以用 '指定符号str'.join()
# 缺点是 只能适用于 字符串
print(','.join(('ACME', '50', '91.5')))
# 其他类型的要想办法转换成str类型
row = ('ACME', 50, 91.5)
print(type(str(x) for x in row))
# join() 里面放 生成器也可以啊
print(','.join(str(x) for x in row))

print('='*50)
print(row, sep=',')
print(*row, sep=',')
# 问题 : 转换或者输出使用二八十六进制表示的整数
# 解决方案: bin() , oct(), hex()

x = 1234

print(bin(x))
print('{:b}'.format(x))
print('-------------------------')
print(oct(x))
print('{:o}'.format(x))
print('-------------------------')
print(hex(x))
print('{:x}'.format(x))
print('-------------------------')

x = -1234
# print('{:b}'.format(x))
print(format(x, 'b'))
print('{:b}'.format(2**32))
print(format(2**32 + x, 'b'))
print('-------------------------')
print(int('4d2', 16))
print(int('10011010010', 2))

# 注意八进制转换
# import os
# os.chmod('script.py', 0o755) 
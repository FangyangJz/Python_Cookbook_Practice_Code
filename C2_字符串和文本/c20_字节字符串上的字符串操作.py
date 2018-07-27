# 问题: 想在字节字符串上执行普通的文本操作
data = bytearray(b'hello world')
print(data[:5])
print(data.startswith(b'hell'))
print(data.split())
print(data.replace(b'hello', b'yep'))

# 文本字符串和字节字符串的区别
text_string = 'Hello world'
byte_string = b'Hello world'
print(text_string[0], byte_string[0])

# 字节字符串如果被打印的话
print(byte_string)
print(byte_string.decode('ascii'))

# 字节字符串对 format % 等格式化操作不适用
# 如果想适用, 需要先将字节字符串转成文本字符串
# print(b'{}'.format(b'ACME'))  # 报错

# 虽然字节字符串处理效率快, 但是容易出错, 还是用文本字符串安全!
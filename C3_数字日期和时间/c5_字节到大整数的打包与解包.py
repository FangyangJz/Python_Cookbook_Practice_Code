# 问题: 有一个字节字符串, 想将其解压成一个整数, 或者需要将一个大整数转换成一个字节字符串
# 解决方案: int.from_bytes() 或 int.to_bytes()

# 将bytes解析成int
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

# 将int解析成bytes
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))
print('-'*100)

# 这个转换在平时并不常见, 在一些应用领域会出现, 比如密码学或网络
# 比如 128位整数的IPv6
# 也可以考虑用后面6.11节的struct模块来解压字节, 但是struct模块解压对于整数大小是有限制的
# 用下面这种字符串合并的方式, 可以突破限制
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
import struct
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

print('='*100)
# 用个例子展示下 big 和 little 的区别
x = 0x01020304
print('%x' % x)
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

# 有些整数太大,如果用int.to_bytes会报错 
x = 521**22
# print(x.to_bytes(16, 'little'))  # 报错
# 这个时候用 int.bit_length() 确定需要多少字节位来存储这个int
print(x.bit_length())
nbytes, rem = divmod(x.bit_length(), 8)
print(nbytes, rem)
if rem:  # 如果余数存在, 加一个字节
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))

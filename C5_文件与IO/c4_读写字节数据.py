# 问题: 想读写二进制文件, 比如图片\声音文件等
# 解决方案: 使用rb或wb模式的open()

with open('file.bin', 'wb') as f:
    f.write(b'hello world')

with open('file.bin','rb') as f:
    data = f.read()
    print(data)

t = 'Hello world'
b = b'Hello world'
for c in t:
    print(c, end=' ')
print(' ')
for c in b:
    print(c, end=' ')
print('\n'+ '-'*50)

# 想从二进制的文件中读取或写入数据, 必须确保要进行编解码操作
with open('file.bin', 'rb') as f:
    data = f.read(4)
    text = data.decode('utf-8')
    print(data)
    print(text)

with open('file.bin', 'wb') as f:
    text = 'HHHa World!'
    f.write(text.encode('utf-8'))

# 二进制I/O还有一个特性, 数组和C结构体类型能直接被写入, 而不需要中间转换
import array
nums = array.array('i', [1,2,3,4])
with open('data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0,0,0,0, 0,0,0,0])
with open('data.bin', 'rb') as f:
    f.readinto(a)  # 直接把二进制数据读到底层的内存中去
print(a)
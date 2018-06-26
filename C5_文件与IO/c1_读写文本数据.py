# 问题: 需要读写各种不同编码的文本数据, 比如ASCII, UTF-8, UTF-16等
# 解决方案: 使用带有rt模式的open()函数读取文本文件

'''
w,r,wt,rt都是python里面文件操作的模式。
w是写模式，r是读模式。
t是windows平台特有的所谓text mode(文本模式）,区别在于会自动识别windows平台的换行符。
类Unix平台的换行符是\n，而windows平台用的是\r\n两个ASCII字符来表示换行，python内部采用的是\n来表示换行符。
rt模式下，python在读取文本时会自动把\r\n转换成\n.
wt模式下，Python写文件时会用\r\n来表示换行。
'''

# Read the entire file as a single string
with open('data.txt', 'rt') as f:
    data = f.read()
    print(data)

# Iterate over the lines of the file
with open('data.txt', 'rt') as f: 
    for line in f:
        print(line)


# open() 函数有个参数 encoding='utf-8' 
# 编码格式可以用sys模块的函数获得
import sys
r = sys.getdefaultencoding()
print(r)

# open()函数还有个参数 newline='' ,有这个参数的时候, linux机器读换行是\n, window读换行是\r\n

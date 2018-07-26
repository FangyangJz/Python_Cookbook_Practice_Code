# 问题: 想将几个小的字符串合并为一个大的字符串
# 解决方案: join()

parts = ['Is', 'Chicago','Not','Chicago?']
print(' '.join(parts))
print(','.join(parts))
a = 'Is dsafdsa'
b = 'Not SADFDSAF'
print('{} {}'.format(a,b))

# join比用 + 字符串方法,速度快
# 生成器的join效率更高
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

c = 'sadfs'
# print的优雅方式
print(a+':'+b+':'+c)   # Ugly
print(':'.join([a,b,c]))  # Ugly
print(a,b,c, sep=':')  # Better

# 这里有个方案, 可以限制写IO的数量
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)
# 结合文件操作
with open('file.txt','w') as f:
    for part in combine(sample(), 32768):
        f.write(part)
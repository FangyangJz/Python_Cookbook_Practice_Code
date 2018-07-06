# 问题: 想反向迭代一个序列
# 解决方案: 使用内置的reversed() 生成器

a = [1,2,3,4,5]
for x in reversed(a):
    print(x)
print('-'*50)
# 反向迭代仅仅当对象的大小可预先确定
# 或者 实现了__reversed__()的特殊方法是才能生效
# 如果不符合, 需要先将对象转换为一个列表才行

# 下面演示在自定义类上实现 __reversed__()方法来实现反向迭代
class Countdown:
    def __init__(self, start):
        self.start = start
    
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    
    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == '__main__':
    for rr in reversed(Countdown(5)):
        print(rr)

    print('='*50)
    
    for rr in Countdown(5):
        print(rr)
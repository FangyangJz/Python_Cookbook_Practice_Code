# 问题 : 想实现一个自定义迭代模式, 跟普通的内置函数range(),reversed()不一样
# 解决方案: yield 返回

def custom_range(start, stop, increment):
    x = start
    while x < stop:
        yield x   # 这里将函数转为了生成器, 生成器和普通函数不同在, 它只能用于迭代操作
        x += increment

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

def main():
    for n in custom_range(0, 4, 0.5):
        print(n)

    # 测试countdown生成器
    c = countdown(3)
    print(c)
    print(next(c))
    print(next(c))

if __name__ == '__main__':
    main()
# 问题: 你的程序已经出现一大堆无法直视的硬编码切片下标, 你想清理下代码
# 解决方案: slice(start, stop)

def name_slice():
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)
    print(SHARES.start)
    print(SHARES.stop)
    print(SHARES.step)  # None

    a = slice(5, 50, 2)
    s = 'HelloWorld'
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])


if __name__ == '__main__':
    name_slice()
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    print(items)
    del items[a]
    print(items)


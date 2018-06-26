# 问题, 想遍历一个可迭代对象中的所有元素, 但是不想用for循环
# 解决方案: 使用next(), 并在代码中捕获stopiteration异常

def manual_iter_1():
    with open('data.txt') as f:
        try:
            while True:
                line = next(f)    # 多行文本的一行相当于迭代对象中的一次迭代
                print(line, end='')
        except StopIteration:
            pass

# 另外一种写法
def manual_iter_2():
    with open('data.txt') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='') # end='' 表示不换行

if __name__ == '__main__':
    manual_iter_1()
    print('-------------')
    manual_iter_2()
    print('==========')
    items = [1,2,3]
    # list类型不是一个可迭代类型, 用iter转成可迭代类型
    it = iter(items)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
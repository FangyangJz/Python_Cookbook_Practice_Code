# 问题: 有一个数据序列, 想利用一些规则 从中提取出需要的值 或 缩短序列
# 解决方案: 使用列表推导式

my_list = [1,4,-5,10,-7,2,3,-1]
# 使用列表推导式, 缺点是如果结果大, 占用大量内存
print([n for n in my_list if n>0])
print([n for n in my_list if n<0])

# 占用大量内存的缺点 可以用生成器来改进
pos = (n for n in my_list if n>0)
print(pos)
for x in pos:
    print(x, end=' ')

print('\n' + '='*100)
# 当过滤规则比较复杂, 那么无法放到if中, 
# 可以将过滤规则放进一个函数, 然后用filter()函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(value):
    try:
        x = int(value)
        return True
    except ValueError:
        return False
# filter创建了一个迭代器, 所以要用list转换
ivals = list(filter(is_int, values))
print(ivals)

# 过滤操作的一个变种就是将不符合条件的值用新的值代替
clip_neg = [n if n>0 else 0 for n in my_list]
print(clip_neg)

# 另外一个值得关注的过滤工具就是itertool.compress()
# 以一个iterable对象和一个相应的Boolean选择器序列作为输入参数, 输出选择器为True的元素
from itertools import compress
string_list = ['dd','aa','cc','de','kk','jj','yy','zz']
counts = [0,3,10,4, 1,7,6,1]
more5 = [n>5 for n in counts]  # 创建Boolean序列
l = list(compress(string_list, more5)) 
print(l)
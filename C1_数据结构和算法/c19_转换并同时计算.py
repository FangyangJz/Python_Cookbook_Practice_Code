# 问题: 需要在数据序列上执行聚集函数(比如sum(), min(), max()), 首先需要转换或者过滤数据
# 解决方案: 使用生成器表达式参数

nums = [1,2,3,4,5]
s = sum(x*x for x in nums)
# s = sum([x*x for x in nums]) 这么创建临时列表没有生成器优雅,
# 当元素数量非常大的时候, 生成器更省内存
print(s)

# Determine if any.py file exist in a directory
import os

files = os.listdir()
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print("Sorry, no python.")

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio =[
    {'name':'GOOG', 'shares':50},
    {'name':'YHOO', 'shares':75},
    {'name':'AOL', 'shares':20}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# min, sum , max这些函数还有参数key回调函数, 结果的形式和上面不太一样
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)

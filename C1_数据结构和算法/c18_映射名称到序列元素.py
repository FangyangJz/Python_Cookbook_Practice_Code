# 问题: 用下标数访问列表或元组中的元素, 这么做代码不易读,希望通过名称来访问元素
# 解决方案: collections.namedtuple()

from collections import namedtuple

Subcriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subcriber('jonss@example.com', '2012-10-19')
print(sub)
print(sub.addr, sub.joined)
# namedtuple()的实例对象和元组类型极其接近, 支持元组操作
print(len(sub))
addr, joined = sub
print(addr, joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

ss = [('a', 100, 2.34), ('a', 200, 4.87), ('a', 100, 2.34)]
ss_total = compute_cost(ss)
print(ss_total) 

print('-'*100)
# 命名元组的目的是代替字典, 因为字典的存储需要更多的内存空间
# 如果你需要构建一个非常大的包含字典的数据结构, 那么使用命名元组会更加高效
# 需要注意的是, tuple不能随便改值 tuple.field_name = 75 这么赋值修改会报错
# 非要修改的话, new = tuple._replace(field_name=75) , 创建一个全新的命名元组
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
new = s._replace(shares=75)
print(s)
print(new)

print('='*100)
# _replace()方法还有一个很有用的特性: 
# 当你的命名元组有可选或缺失字段时, 可以方便的填充数据
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name':'ACME', 'shares':100, 'price':123.45}
print(dict_to_stock(a))
b = {'name':'ACME', 'shares':100, 'price':123.45, 'date':'12/17/2012'}
print(dict_to_stock(b))

# 最后, 如果目标是定义一个需要更新很多实例属性的高效数据结构, 那么命名元组不是最佳选择
# 考虑定义一个__slot__方法的类参考后面8.4
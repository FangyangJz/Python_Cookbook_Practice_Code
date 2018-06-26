# 问题:你想构造一个可接收任意数量参数的参数
# 解决方案: 用*参数

# rest是由其他位置参数组成的元组
def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))

print(avg(1, 2))
print(avg(1,2,3,4))
print('-----------------------------------')
# 接收任意数量的关键字参数, 用**开头
import html

def make_element(name, value, **attrs):
    keyvals = ['%s="%s" ' % item for item in attrs.items()]
    print(keyvals)
    print(attrs.items())
    print(attrs)
    print('=============================')
    attr_str = ''.join(keyvals)
    element = '<{name} {attrs}>{value}</{name}>'.format(name=name, attrs=attr_str,value=html.escape(value))
    return element

print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))  # 这里的输出, html.escape起到了数据脱敏的作用

def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):  # **kwargs只能出现在最后一个参数
    pass
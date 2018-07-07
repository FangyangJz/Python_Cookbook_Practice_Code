# 问题: 怎样在一个序列上保持元素顺序的同时,消除重复的值?
# 解决方案: 

# 1. 如果序列上的值都是hashable类型(不可变的), 那么可以用集合或者生成器
#  注意! 如果只是将list转set去掉重复值, 结果是没有顺序的, 原来的顺序会被打乱
#  这里介绍的函数避免了上面的问题  
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
# 这里 list 的元素是 int 类型的(hashable)
a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))

# 2. 如果想消除的元素是字典类型, 可变的, not hashable
# 将1中的函数稍作修改
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

b = [
    {'x':1, 'y':2}, 
    {'x':1, 'y':3}, 
    {'x':1, 'y':2}, 
    {'x':2, 'y':4}
    ]
print(list(dedupe(b, key=lambda d:(d['x'], d['y']))))
print(list(dedupe(b, key=lambda d: d['x'])))
# 修改后的函数兼容了以前的版本, 既可以处理hashable元素, 也可以处理非hashable元素
# 处理非hashable元素的时候, 要指定key参数
print(list(dedupe(a)))

# 同样, 如果想去掉一个文件重复的行, 也可以用上面的函数
with open('data.txt', 'r') as f:
    for line in dedupe(f):
        print(line, end='')
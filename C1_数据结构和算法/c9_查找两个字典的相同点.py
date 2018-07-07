# 问题: 怎样在两个字典中寻找相同点?(比如相同的键, 值等)
# 解决方案: 利用键视图(keys()) 或 元素视图(item()的key-value)的集合操作
#          因为值可能存在相同的情况, 所以值视图(.values())不支持这里的集合操作,你可以手动转set

a = {'x':1, 'y':2, 'z':3}
b = {'w':10, 'x':11, 'y':2}

print(a.keys() & b.keys(), type(a.keys()))
print(a.keys() - b.keys(), type(a.keys() - b.keys()))
print(b.keys() - a.keys())
print(a.items() & b.items(), type(a.items()), type(a.items() & b.items()))

# 也可以用于 修改 或 过滤 字典元素.
# 以现有的字典, 获得排除几个指定键的新字典
c = {key : a[key] for key in a.keys() - {'z','w'}}
print(c)
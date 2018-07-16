# 问题: 想为sort()操作创建一个很短的回调函数, 但又不想用def去写一个单行函数
#       而是希望通过某个快捷方式以内联方式来创建这个函数
# 解决方案: lambda表达式

names = ['David Beazley', 'Brian Jones', 'Raymond Hett', 'Ned Bat']

print(lambda names:names.split()[-1])
expression = lambda name:name.split()[-1].lower()
print(expression(names[0]))

print('-'*100)
# 这里可以看出 sorted 的 key 是将names参数逐一迭代进回调函数
result = sorted(names, key=lambda name: name.split()[-1].lower())
print(result)
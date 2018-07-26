# 问题: 想创建一个内嵌变量的字符串, 变量被它的值所表示的字符串替换掉
# 解决方案: format(), format_map(), vars()

s = '{name} has {n} messages.'
print(s.format(name='GG', n=37))
name = 'sss'
n = 25
print(s.format_map(vars()))

# vars() 应用于实例对象的例子
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('CC', 20)
print(s.format_map(vars(a)))

# format format_map 指定了几个位置(key), 就要赋几个变量值
# 少了就会报错, 可以在类中封装 
# def __missing__(self, key):
    #  return '{' + key + '}'

# 还有一些高级用法, 这里不做深究
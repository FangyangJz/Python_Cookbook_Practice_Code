# 问题: 想通过指定的文本模式区检查字符串的开头或结尾
# 解决方案: str.startwith() 或 str.endwith()
filename = 'spam.txt'
print(filename.endswith('txt'))
print(filename.startswith('file'))

import os
print(os.listdir('.'))  # 参数path为 '.' ,表示当前目录下
filenames = os.listdir('.')

name_list = [name for name in filenames if name.endswith(('.c', '.h'))]
print(name_list)

name_list = [name for name in filenames if name.startswith('c')]
print(name_list)

print(any(name.endswith('.py') for name in filenames))
print('--------------------------------------------------')

choices = ['http:', 'https:']
url = 'http://www.python.org'
bool_value = url.startswith(tuple(choices))   # 参数是元组类型
print(bool_value)

# 其他字符串方法还可以用字符串切片(不够优雅)
# 也可以用re.match, 适用于复杂情况
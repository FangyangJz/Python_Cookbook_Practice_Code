# 问题: 一些长字符串, 想用指定的列宽将其格式化
# 解决方案: textwrap模块
import textwrap
import os

s = '''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
'''
print(len(s))
print(textwrap.fill(s,20))
print(textwrap.fill(s,40, initial_indent='    '))
print(textwrap.fill(s,40, subsequent_indent='    '))

# 获取终端尺寸
r = os.get_terminal_size()
print(r)
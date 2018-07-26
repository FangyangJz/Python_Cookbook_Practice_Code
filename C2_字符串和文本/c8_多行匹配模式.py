# 问题: 使用正则匹配文本, 想跨越多行去匹配
# 解决方案: 1. 在匹配模式中把.替换成(?:.|\n)对换行符的匹配
#          2. compile()中加参数 re.DOTALL

import re
# (.)不能匹配换行符
text1 = '/*this is one line comment */'
text2 = '''/* this is a 
multiline comment*/
'''
comment_patt = re.compile(r'/\*(.*?)\*/')
r = re.findall(comment_patt, text1)
print(r)
r = re.findall(comment_patt, text2)
print(r)

# 在匹配模式中把.替换成(?:.|\n)对换行符的匹配
comment_patt = re.compile(r'/\*((?:.|\n)*?)\*/')
r = re.findall(comment_patt, text2)
print(r)

# compile()参数设置 re.DOTALL, 和上面一样效果
comment_patt = re.compile(r'/\*(.*?)\*/', re.DOTALL)
r = re.findall(comment_patt, text2)
print(r)
# 问题: 想匹配或搜索特定模式的文本
# 解决方案: 
#   1. 简单的字符串str.find(), str.endswith(), str.startswith()
#   2. 复杂的匹配用正则表达式和re模块. re.compile(r'\d+') 确定模式
#      re.match返回boolean, re.findall返回匹配到的字符串, re.finditer返回迭代器
#      匹配模式用原始字符串,这样有\不用写成\\
#      如果是大量的匹配和搜索操作, 最好不要省去re.compile过程

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

import re

date = '11/27/2012ssss,,, 12/22/2018.....11/22/8909'
r = re.findall(r'\d+', date)
print(r)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
r = datepat.match(date)
print(r.group(1), r.group(2), r.group(3))

print('-'*50)
# re.finditer()返回的是个迭代器
for m in datepat.finditer(date):
    print(m, m.group(), m.groups())
# 问题: 如题
# 解决方案: 简单的用 str.replace(), 复杂用re.sub()

text = 'yeah, but no, but yeah, but no, but yeah'
new = text.replace('yeah','yep')
print(new)

import re

text = 'Today is 11/28/2012.Pycon starts 3/13/2013'
# sub第一参数是匹配模式, 第二个参数是替换模式, \3指向前面模式的捕获信号
r = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(r)

# re.sub() 还有一种回调函数的写法, 这里不做详解
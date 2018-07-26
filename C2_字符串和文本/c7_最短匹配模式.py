# 问题: .*是贪婪匹配,会找最长的
# 解决方案: .*? 非贪婪匹配, 找短的

import re

str_pat1 = re.compile(r'"(.*)"')
text1 = 'Computer says "no."...'
text2 = 'Computer says "no." Phone says "yes."....'
print(re.findall(str_pat1, text1))
print(re.findall(str_pat1, text2))
print('-'*50)
str_pat2 = re.compile(r'"(.*?)"')
print(re.findall(str_pat2, text1))
print(re.findall(str_pat2, text2))
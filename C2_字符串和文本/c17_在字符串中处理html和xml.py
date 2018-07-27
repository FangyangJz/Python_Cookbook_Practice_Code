# 问题: 想将html或xml实体如&entity或&#code替换为对应的文本, 或者需要转换文本中的特定字符
# 解决方案: html.escape()

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

# s = 'Spicy &quot;Jalape&#241;o&quot.'
s = '&quot;&lt;tag&gt;text&lt;/tag&gt;&quot;'
from html import unescape
print(unescape(s))

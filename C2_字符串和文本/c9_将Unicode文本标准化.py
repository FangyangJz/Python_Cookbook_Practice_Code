# 问题: 需要确保所有字符串在底层有相同的表示
# 解决方案: unicodedata模块

import unicodedata
# 在linux上面可以成功执行
s1 = u'Spicy Jalape\u00f1o'
s2 = u'Spicy Jalapen\u0303o'
print(s1, s2)
print(s1==s2)
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3, t4)
print(t3 == t4)

# 清理n上面的~, 需要上面是NFD模式,表示字符应该分解为多个组合字符表示
r = ''.join(c for c in t3 if not unicodedata.combining(c))
print(r)
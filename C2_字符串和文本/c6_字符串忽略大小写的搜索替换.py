# 问题: 需要以忽略大小写的方式搜索和替换文本字符串
# 解决方案: re.IGNORECASE 标志参数
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
r = re.findall('python', text, flags=re.IGNORECASE)
print(r)
r = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(r)

# 回调函数写法
def matchcase(word):  # 这里对应传入的snake
    def replace(m):  # 这里对应传入的python
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

r = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(r)
# 问题: 想去掉文本字符串开头，结尾，中间不想要的字符, 比如空白
# 解决方案: strip()

# 去除操作不会对文本中间产生影响
s = '  hello  world \n'
print(s.strip())
print(s.lstrip())
print(s.rsplit())
t = '------hello======'
print(t.lstrip('-'))
print(t.strip('-='))

print('-'*50)
with open('file.txt', 'rt', encoding='utf-8') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
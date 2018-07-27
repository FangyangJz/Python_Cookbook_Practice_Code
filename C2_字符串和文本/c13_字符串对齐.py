# 问题: 想通过某种对齐方式来格式化字符串
# 解决方案: ljust(), rjust(), center()

text = 'Hello World'
print(text.ljust(20,'*'))
print(text.rjust(20))
print(text.center(20, '='))

print(format(text,'>20'))
print(format(text,'^20'))

print(format(text,'=>20'))
print(format(text,'*^20'))
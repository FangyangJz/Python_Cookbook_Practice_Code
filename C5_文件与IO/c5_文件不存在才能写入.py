# 问题: 想写一个文件, 但是前提必须这个文件不存在, 即不允许覆盖已存在的文件
# 解决方案: open()的模式 由'wt' 改用 'xt', 如果是二进制的用 'xb'

with open('data.txt','xt') as f:
    f.write('hello\n')

# Traceback (most recent call last):
#   File "c5_文件不存在才能写入.py", line 4, in <module>
#     with open('data.txt','xt') as f:
# FileExistsError: [Errno 17] File exists: 'data.txt'
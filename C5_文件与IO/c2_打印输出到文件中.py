# 问题: 想将print()函数的输出重定向到一个文件中去
# 解决方案: 在print()函数中指定file关键字参数

with open('test.txt', 'wt') as f:
    # 注意,文件要是以二进制打开, 打印就会报错
    print('Hello world', file=f)
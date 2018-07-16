# 问题: 写好一个函数, 想为这个函数增加一些额外的信息,帮助使用者清楚如何使用该函数
# 解决方案: 使用函数参数注解, python本身没有类型声明, 所以注解就是文档的意思
#          一般注解使用 类 或 字符串 比较好, 尽管数字,对象实例也可以
#         ->int 注解函数输出为int类型
#         参数: int 注解参数类型为int类型

def add(x:int, y:int) ->int:
    return x + y

print(help(add))
# 函数注解只存储在函数的__annotations__属性中
print(add.__annotations__)
print(add(5,2))
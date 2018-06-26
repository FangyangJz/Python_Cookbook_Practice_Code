想用 from module import * 精确控制导入的内容
可以用 __all__ 来指定

def spam():
    pass

def grok():
    pass

blah = 42
# 通过*只能导出 spam 和 blah
__all__ = ['spam', 'blah']
# 如果没有 __all__ 限定, from module import * 会导入所有没有_开头的
# __all__ 为空列表, 没有东西导出
# __all__ 包含未被定义的名字, 导入时报错, AttributeError

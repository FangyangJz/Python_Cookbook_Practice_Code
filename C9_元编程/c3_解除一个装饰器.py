# 问题: 一个装饰器已经作用在一个函数上, 想撤销它, 直接访问原始的未包装的那个函数
# 解决方案: 通过上节中的 functools 库中的 @wraps(func) 装饰, 直接可以访问__wrapped__属性

# 上节有例子了

# 注意! @staticmethod 和 @classmethod 不遵循这个约定(他们把原始函数都存储在属性__func__中)
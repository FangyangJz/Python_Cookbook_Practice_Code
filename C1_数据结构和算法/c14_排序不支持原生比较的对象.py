# 问题: 想排序类型相同的对象, 但是他们并不支持原生的比较操作
# 解决方案: 
# 1. sorted(key=callable) 
# 2. operator 模块中的 attrgetter 函数

# 方法 1
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print('users : ', users)
print(sorted(users, key=lambda u: u.user_id))

# 方法 2
from operator import attrgetter
# attrgetter('last_name', 'first_name') 支持多个key
print(sorted(users, key=attrgetter('user_id')))
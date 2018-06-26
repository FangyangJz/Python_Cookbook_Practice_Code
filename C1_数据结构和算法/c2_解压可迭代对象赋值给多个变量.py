# 和上一问题一样, 如果可迭代对象的元素超过变量个数时, 会报错

# 解决办法用 *变量名 
records = (60, 65, 75, 80, 83, 90)
def drop_first_last(records):
    first, *middle, last = records
    return sum(middle)/len(middle)

r = drop_first_last(records)
print(r)

# 小案例 
records = ('Dave', 'dave@email.com', '773-123-121', '857-123-1111')
name, email, *phone_number = records
print(phone_number)

# 看前最近一个月数据 与 前7个月均值的 对比
*pre7data, current = [10,8,9,8,2,3,1, 5]
pre7data_mean = sum(pre7data)/len(pre7data)
print(pre7data_mean, current)

# *号 舍弃小案例
records = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = records
print(name, year)

# 字符串分割
line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
uname, *fields, homedir, sh = line.split(":")
print(uname, homedir, sh, fields)

# *号分割实现的递归算法演示(python有递归次数限制,不推荐)
def summ(items):
    head, *tail = items
    return head + summ(tail) if tail else head   #   (cond为true执行) if cond else (cond为false执行)
print(summ([9,8,7,6,5,4]))
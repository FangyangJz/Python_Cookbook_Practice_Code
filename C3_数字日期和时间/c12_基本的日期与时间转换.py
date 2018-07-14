# 问题: 需要执行简单的时间转换, 比如天到秒, 小时到分钟等
# 解决方案: datetime模块的timedelta

from datetime import timedelta,datetime

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds/3600)
print(c.total_seconds()/3600)

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
print(b - a, (b-a).days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

# 计算时, datetime会自动处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)

# 更复杂的时间计算, 可以使用dateutil.relativedelta()函数代替
from dateutil.relativedelta import relativedelta
a = datetime(2012, 9, 23)
b = datetime(2012, 12, 21)
print(a + relativedelta(months= +1))
print(a + relativedelta(months= 4))

d = relativedelta(b, a)
print(d, '\n', d.months, d.days)
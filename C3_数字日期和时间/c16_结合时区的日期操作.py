# 问题: 有一个安排在2012年12月21日早上9:30在芝加哥的电话会议, 
#       那么印度班加罗尔那边应该在当地时间几点参加会议呢?
# 解决方案: pytz模块 (有点落后, python现在貌似有更先进的, 参考 PEP431 +)

from datetime import datetime, timedelta
from pytz import timezone

d = datetime(2012,12,21,9,30,0)
print(d)

# 让chicago为本地时间
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
# 结果为 2012-12-21 09:30:00-06:00  西六区

# convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)
# 2012-12-21 21:00:00+05:30   东5.5区??

# 考虑美国夏时令时间的细节转换,需要用函数normalize
d = datetime(2013,3,10, 1,45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print("Doesn't care about 夏时令 :", later)
later = central.normalize(loc_d + timedelta(minutes=30))
print("Yes, Care about 夏时令 :   ", later)

#####################################################################
print('#'*100)
# 为了不被夏时令搞乱, 最好处理本地化时间的策略是转成UTC时间
print(loc_d)
from pytz import utc
utc_d = loc_d.astimezone(utc)
print(utc_d)
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))
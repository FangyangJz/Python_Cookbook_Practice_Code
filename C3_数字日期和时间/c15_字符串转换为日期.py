# 问题: 接收字符串输入, 想将其转换成datetime对象
# 解决方案: datetime.strptime()

from datetime import datetime

text = '2012-09-20'
# strptime  字符串转datetime
# %Y 代表4位年份, %m代表两位月份
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
# datetime 表现形式转换 , strftime
nice_z = datetime.strftime(z, "%A %B %d, %Y")
print(nice_z)

# ! 注意 ! strptime 效率不高, 高效做法如下(比上面快7倍):
def parse_ymd(s):     # 已知日期格式为YYYY-MM-DD
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
# 问题: 需要在当前月份中循环每一天, 想找到一个计算这个日期范围的高效方法
# 解决方案: 

from datetime import datetime,date,timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)  # 将日期比如(2018,7,13)替换成(2018,7,1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

if __name__ == '__main__':
    a_day = timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day
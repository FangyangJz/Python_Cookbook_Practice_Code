# 问题: 需要查找星期中某一天最后出现的日期, 比如星期五
# 解决方案： datetime模块

from datetime import datetime, timedelta

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()   # 星期五 返回 4
    day_num_target = weekdays.index(dayname)   # weekdays.index('Monday') 返回 0
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

if __name__ == '__main__':
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thurday',
            'Friday', 'Saturday', 'Sunday']
    m = get_previous_byday('Monday')
    print(m)

    # 执行大量的日期计算, 最好用deteutil模块
    from dateutil.relativedelta import relativedelta
    from dateutil.rrule import *
    d = datetime.now()
    print(d)
    print(d + relativedelta(weekday=FR))
    print(d + relativedelta(weekday=FR(-1)))  # 这个函数用法改了
# 问题: 你想通过format()函数和字符串方法使得一个对象能支持自定义的格式化
# 解决方案: 在类里定义__format__()方法
_formats = {
    'ymd':'{d.year}-{d.month}-{d.day}',
    'mdy':'{d.month}/{d.day}/{d.year}',
    'dmy':'{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2018, 6, 22)
print(format(d))
print(format(d, 'mdy'))

print('------------------------------------')
from datetime import date
d = date(2018,6,21)
print(format(d))
print(format(d, '%A, %B, %d, %Y'))
print('The end is {:%d %b %Y}.Goodbye'.format(d))
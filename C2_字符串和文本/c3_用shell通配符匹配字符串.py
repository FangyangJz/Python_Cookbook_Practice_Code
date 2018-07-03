# 问题: 想用unix shell常用的通配符区匹配文本字符串
# 解决方案: fnmatch模块的函数 fnmatch() 和 fnmatchcase()

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.TXT'))   # 不同操作系统对大小写有别, win不分大小写
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
filter_names = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(filter_names)

print('#'*100)
#########################################
# fnmatchcase() 完全匹配, 区分大小写
print(fnmatch('foo.txt', '*.TXT'))
print(fnmatchcase('foo.txt', '*.TXT'))
print('#'*100)
#########################################

addresses = ['5412 N CLARK ST', '1060 W ADDISON ST',
             '1039 W GRANVILLE AVE', '2122 N CLARK ST',
             '4802 N BROADWAY' ]
addr1 = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(addr1)
addr2 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(addr2)
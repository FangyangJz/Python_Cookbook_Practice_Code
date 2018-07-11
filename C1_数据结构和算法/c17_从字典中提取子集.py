# 问题: 想构造一个字典, 它是另外一个字典的子集
# 解决方案: 使用字典推导

prices = {
    'ACME':45.23, 'AAPL':612.78,
    'IBM':206.55, 'HPQ':37.20,
    'FB':10.75
    }
# make a dict of all prices over 200
p1 = {key:value for key, value in prices.items() if value>200}
print(p1)

# make a dict of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p2)
# p2 还可以这么写, 但是这么写比上面那种慢
p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)
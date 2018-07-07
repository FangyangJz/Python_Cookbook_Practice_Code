# 问题: 怎样在字典中执行一些计算(比如求最大值,最小值,排序等)
# 解决方案: zip() 先将key 和value对调成tuple类, 然后先比较前面的value,后比较key

prices = {
    'ACME':45.23, 'AAPL':612.78,
    'IBM':206.55, 'HPQ':37.20,
    'FB':10.75
    }

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(min_price, max_price)
print(prices_sorted)

# 注意zip()返回的是一个只能访问一次的迭代器
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
print(max(prices_and_names))  # 执行第二次, 报错
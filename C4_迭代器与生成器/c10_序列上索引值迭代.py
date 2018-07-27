# 问题: 想在迭代一个序列的同时, 跟踪索引
# 解决方案: enumerate

from collections import defaultdict

my_list = ['a','b','c']
for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list,10): # 设定启始索引值
    print(idx, val)

word_summary = defaultdict(list)
with open('data.txt','r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
print(word_summary)

# data = [(1,2), (3,4), (5,6)]
# for n, (x, y) in enumerate(data):  # Correct!
# for n, x, y in enumerate(data):  # Wrong!
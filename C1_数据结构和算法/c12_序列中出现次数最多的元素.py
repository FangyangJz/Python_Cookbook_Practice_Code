# 问题: 怎样找出一个序列中出现次数最多的元素呢?
# 解决方案: collections.Counter类 most.common()方法

from collections import Counter

words = ['look', 'into', 'my', 'eyes' ,
'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes',
'not', 'around', 'the', 'eyes', "don't", 'look', 'around',
'the', 'eyes', 'look', 'into', 'my', 'eyes', 'you', 'are','under'
]

words_counts = Counter(words)  # Counter可以接收任何hashable序列对象
top_three = words_counts.most_common(3)
print(top_three)
print(words_counts['eyes'])

# 增加额外的词
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
words_counts.update(morewords)
print(words_counts.most_common())

print('-'*100)
# 还可以做加减法
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
print(a - b)
# 问题: 在迭代操作或其他操作的时候, 怎样只保留最后有限个元素的历史记录?
# 解决方法: collections.deque
from collections import deque

def search(lines, pattern, history=5):
    # deque 构造了一个deque类型的队列, 参数固定长度为5
    # deque 的队列用append入队
    # 如果不设置 maxlen 队列长度, 默认为无限大小的队列, appendleft(value)/appendright
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

if __name__ == '__main__':
    with open('.\\data.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
    
    q = deque()
    print(q)
    q.append(1)
    q.append(2)
    print('append 1 2: ', q)
    q.append([3,4])
    print('append [3,4]: ', q)
    q.appendleft(10)
    print('appendleft 10: ', q)
    q.pop()
    print('pop() : ', q)
    q.popleft()
    print('popleft(): ', q)
    # 注意!!!!!!!!!!!1 
    # 在 队列 两端插入或删除元素时间复杂度都是 O(1)
    # 在 列表 的开头插入或删除元素的时间复杂度是 O(N)
# 问题: 想定义一个生成器函数, 然后暴露给用户使用
# 解决方案: 把生成器函数放到 类中的__iter__()方法中去

from collections import deque

class linehistory(object):
    
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
        
    def clear(self):
        self.history.clear()


if __name__ == "__main__":
    with open('data.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')
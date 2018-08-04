import os

if not os.path.exists('data.txt'):
    with open('data.txt') as f:
        f.write('hello')
else:
    print('File already exists!')
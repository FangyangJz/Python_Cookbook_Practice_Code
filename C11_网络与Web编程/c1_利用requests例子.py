# 利用requests库发起一个head请求, 并从响应中提取一些http头数据的字段

import requests

resp = requests.head('http://www.python.ort/index.html')

status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content_type']
content_length = resp.headers['content-length']

# requests.get 例子
resp = requests.get('http://pypi.python.org/pypi?:action=login', auth=('user', 'password'))

# 用requests库 pass http cookies from one request to the next:
# first request
resp1 = requests.get(url)
# second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)

# 用requests upload content
url = 'http://httpbin.org/post'
files = {'file':('data.csv', open('data.csv', 'rb'))}
r = requests.post(url, files=files)
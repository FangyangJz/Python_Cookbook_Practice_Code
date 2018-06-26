# 问题 : 需要使用http协议以客户端的方式访问多种服务,例如:下载数据或者与基于REST的API进行交互

# 发送一个简单的http post 请求到远程的服务上
from urllib import request, parse

url = 'http://httpbin.org/post'

parms = {
    'name1':'value1',
    'name2':'value2'
}

# encode the query string
querystring = parse.urlencode(parms)

# make a Get request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()
print(resp, type(resp))
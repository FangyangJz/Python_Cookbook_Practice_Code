# 基于urllib封装, 适合复杂业务
import requests

url = 'http://httpbin.org/post'
parms = {
    'name1':'value1',
    'name2':'value2'
}

headers = {
    'User-agent':'none/ofyourbusiness',
    'Spam':'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)
text = resp.text  # resp.text 返回的是unicode解码的响应文本
print(text, type(text))
content = resp.content  # 返回的是原始的二进制数据
print(content, type(content))